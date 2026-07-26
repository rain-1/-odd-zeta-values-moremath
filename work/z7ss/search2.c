/* Exhaustive search for a single-sum hypergeometric (factorial-ratio) representation
 * of the weight-7 leading coefficients q_n = 1, 61, 52921, 94357501, ...
 *
 *   F(n,k) = z^k * prod_{(a,b) in S} ((a n + b k)!)^{e_{a,b}}
 *   S = { (a,b) : 0<=a<=A, -B<=b<=B, (a,b)!=(0,0), not(a==0 && b<0) }
 *   sum e a = 0, sum e b = 0 (balanced),  sum |e| <= W,  1<=|z|<=ZMAX
 *
 * Prunes
 *   (i)  balance reachability,
 *   (ii) growth: max_t [ sum_j e_j L_j log L_j + t log|z| ] must be >= log(mu),
 *        mu = 6329.2605 the dominant characteristic root of the (verified) order-4
 *        recurrence.  f is linear in e, so a partial assignment admits the upper
 *        bound  f_cur(t) + budget * max_{i>=j} |g(L_i(t))|.
 * Then exact rational tests q_1 = 61, q_2 = 52921 (prime-exponent-vector arithmetic).
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define NPRIME 18
static const int PR[NPRIME] = {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61};
#define MAXARG 64
static signed char fpv[MAXARG+1][NPRIME];

#define NT 160                     /* t-grid for the growth prune */
static double TG[NT], GJ[64][NT], HREM[65][NT];
static double LOGMU = 8.75293868604;

static int A,B,W,ZMAX,SHARD=0,NSHARD=1;
static long long T1=61, T2=52921;
static int NF, fa[64], fb[64], ev[64];
static double fcur[NT];
static long long nleaf=0,nvalid=0,nhit1=0,nhit2=0,nprune=0;
static FILE*out;

static void initfact(void){
    for(int p=0;p<NPRIME;p++) fpv[0][p]=0;
    for(int m=1;m<=MAXARG;m++){
        for(int p=0;p<NPRIME;p++) fpv[m][p]=fpv[m-1][p];
        int x=m;
        for(int p=0;p<NPRIME;p++) while(x%PR[p]==0){x/=PR[p];fpv[m][p]++;}
        if(x!=1){fprintf(stderr,"prime table small at %d\n",m);exit(1);}
    }
}
static double g(double L){ return (L<=1e-12)?0.0:L*log(L); }

static void initgrid(void){
    double TMAX = A + 1.0;
    for(int i=0;i<NT;i++) TG[i] = TMAX*(i+0.5)/NT;
    for(int j=0;j<NF;j++)
        for(int i=0;i<NT;i++){
            double L = fa[j] + fb[j]*TG[i];
            GJ[j][i] = (L < -1e-12) ? 0.0 : g(L);   /* conservative */
        }
    for(int i=0;i<NT;i++) HREM[NF][i]=0.0;
    for(int j=NF-1;j>=0;j--)
        for(int i=0;i<NT;i++){
            double v = fabs(GJ[j][i]);
            HREM[j][i] = (v>HREM[j+1][i])?v:HREM[j+1][i];
        }
}

static int evalsum(int n,int z,__int128*pnum,__int128*pden)
{
    int KLO=-4*n-6,KHI=4*n+6;
    int Ek[48][NPRIME],kk[48],nt=0;
    for(int k=KLO;k<=KHI;k++){
        int zero=0,bad=0;
        for(int j=0;j<NF && !zero && !bad;j++){
            if(!ev[j])continue;
            int L=fa[j]*n+fb[j]*k;
            if(L<0){ if(ev[j]<0) zero=1; else bad=1; }
            else if(L>MAXARG) return 1;
        }
        if(zero)continue;
        if(bad)return 1;
        if(nt>=48)return 1;
        int E[NPRIME]; for(int p=0;p<NPRIME;p++)E[p]=0;
        for(int j=0;j<NF;j++){
            if(!ev[j])continue;
            int L=fa[j]*n+fb[j]*k;
            for(int p=0;p<NPRIME;p++)E[p]+=ev[j]*fpv[L][p];
        }
        kk[nt]=k; memcpy(Ek[nt],E,sizeof(E)); nt++;
    }
    if(nt==0)return 1;
    int Em[NPRIME];
    for(int p=0;p<NPRIME;p++){Em[p]=Ek[0][p];for(int i=1;i<nt;i++)if(Ek[i][p]<Em[p])Em[p]=Ek[i][p];}
    const __int128 CAP=((__int128)1)<<100;
    __int128 S=0;
    for(int i=0;i<nt;i++){
        __int128 T=1;
        for(int p=0;p<NPRIME;p++){
            int e=Ek[i][p]-Em[p];
            for(int t=0;t<e;t++){T*=PR[p]; if(T>CAP)return 1;}
        }
        int k=kk[i];
        if(z!=1){ if(k<0)return 1; for(int t=0;t<k;t++){T*=z; if(T>CAP||T<-CAP)return 1;} }
        S+=T;
    }
    __int128 num=S,den=1;
    for(int p=0;p<NPRIME;p++){
        int e=Em[p];
        if(e>0)for(int t=0;t<e;t++){num*=PR[p]; if(num>CAP||num<-CAP)return 1;}
        else for(int t=0;t<-e;t++){den*=PR[p]; if(den>CAP)return 1;}
    }
    *pnum=num;*pden=den;return 0;
}
static int matches(int n,long long tgt,int z){
    __int128 num,den; if(evalsum(n,z,&num,&den))return 0;
    return num==(__int128)tgt*den;
}
static void report(int z){
    fprintf(out,"z=%d ",z);
    for(int j=0;j<NF;j++) if(ev[j]) fprintf(out,"(%d,%d)^%d ",fa[j],fb[j],ev[j]);
    fprintf(out,"\n"); fflush(out);
}

static void dfs(int j,int budget,int sa,int sb)
{
    if(j==NF){
        if(sa||sb)return;
        nleaf++;
        int lo=0,hi=0,any=0;
        for(int i=0;i<NF;i++){ if(ev[i]<0){ if(fb[i]>0)lo=1; if(fb[i]<0)hi=1;} if(ev[i])any=1; }
        if(!any||!lo||!hi)return;
        nvalid++;
        for(int az=1;az<=ZMAX;az++) for(int s=0;s<2;s++){
            int z = s?-az:az;
            if(matches(1,T1,z)){ nhit1++; if(matches(2,T2,z)){ nhit2++; report(z);} }
        }
        return;
    }
    if(abs(sa)>budget*A||abs(sb)>budget*B) return;
    /* growth prune */
    if(j>0){
        double best=-1e300;
        double lz = log((double)ZMAX);
        for(int i=0;i<NT;i++){
            double u = fcur[i] + budget*HREM[j][i] + TG[i]*lz;
            if(u>best)best=u;
        }
        if(best < LOGMU - 0.20){ nprune++; return; }
    }
    int elo=-budget, ehi=budget;
    for(int e=elo;e<=ehi;e++){
        if(j==0 && NSHARD>1 && ((e+64)%NSHARD)!=SHARD) continue;
        int c=e<0?-e:e;
        ev[j]=e;
        if(e){ for(int i=0;i<NT;i++) fcur[i]+=e*GJ[j][i]; }
        dfs(j+1,budget-c,sa+e*fa[j],sb+e*fb[j]);
        if(e){ for(int i=0;i<NT;i++) fcur[i]-=e*GJ[j][i]; }
    }
    ev[j]=0;
}

int main(int argc,char**argv){
    A=argc>1?atoi(argv[1]):3;
    B=argc>2?atoi(argv[2]):3;
    W=argc>3?atoi(argv[3]):10;
    ZMAX=argc>4?atoi(argv[4]):1;
    const char*fn=argc>5?argv[5]:"hits.txt";
    SHARD=argc>6?atoi(argv[6]):0;
    NSHARD=argc>7?atoi(argv[7]):1;
    if(argc>8) LOGMU=atof(argv[8]);
    if(argc>9) T1=atoll(argv[9]);
    if(argc>10) T2=atoll(argv[10]);
    initfact();
    NF=0;
    for(int a=0;a<=A;a++)for(int b=-B;b<=B;b++){ if(a==0&&b<=0)continue; fa[NF]=a;fb[NF]=b;NF++; }
    initgrid();
    for(int i=0;i<NT;i++)fcur[i]=0;
    out=fopen(fn,"w");
    dfs(0,W,0,0);
    fclose(out);
    fprintf(stderr,"A=%d B=%d W=%d Z=%d shard %d/%d: leaves=%lld valid=%lld pruned=%lld q1hits=%lld q1q2hits=%lld\n",
            A,B,W,ZMAX,SHARD,NSHARD,nleaf,nvalid,nprune,nhit1,nhit2);
    return 0;
}
