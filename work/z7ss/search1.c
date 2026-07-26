/* Exhaustive search for a single-sum hypergeometric representation of the weight-7
 * coefficient sequence q_n = 1, 61, 52921, 94357501, ...
 *
 * Class searched:
 *     F(n,k) = z^k * prod_{(a,b) in S} ( (a*n + b*k)! )^{e_{a,b}}
 *     S = { (a,b) : 0 <= a <= A, -B <= b <= B, (a,b) != (0,0), not (a==0 && b<0) }
 *     sum |e| <= W ,   sum e*a = 0 ,   sum e*b = 0     (scale-balanced)
 *     z in {-ZMAX..ZMAX} \ {0}
 *     q_n^cand = sum_k F(n,k) over the natural (finite) support.
 *
 * This class contains every product of binomial coefficients C(an+bk, cn+dk) with
 * |coefficients| <= A,B raised to integer powers, and more (arbitrary factorial ratios).
 *
 * Filter: exact match of q_1 = 61 (rational arithmetic via prime exponent vectors),
 * then q_2 = 52921.  Survivors are printed for exact re-check in Python.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define NPRIME 18
static const int PR[NPRIME] = {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61};
#define MAXARG 64
static signed char fpv[MAXARG+1][NPRIME];   /* prime exponent vector of m! */

static int A, B, W, ZMAX;
static long long T1=61, T2=52921;
static int NF;                    /* number of forms */
static int fa[64], fb[64];        /* forms */
static int ev[64];                /* current exponents */

static long long nvec = 0, nvalid = 0, nhit1 = 0, nhit2 = 0;
static FILE *out;

static void initfact(void){
    for(int p=0;p<NPRIME;p++) fpv[0][p]=0;
    for(int m=1;m<=MAXARG;m++){
        for(int p=0;p<NPRIME;p++) fpv[m][p]=fpv[m-1][p];
        int x=m;
        for(int p=0;p<NPRIME;p++){
            while(x%PR[p]==0){ x/=PR[p]; fpv[m][p]++; }
        }
        if(x!=1){ /* prime factor beyond table */
            fprintf(stderr,"prime table too small at m=%d residue %d\n",m,x); exit(1);
        }
    }
}

/* ---- exact evaluation of sum_k z^k F(n,k) as a rational num/den (128 bit) ---- */
/* returns 0 = ok, 1 = reject (ill-defined / overflow) */
static int evalsum(int n, int z, __int128 *pnum, __int128 *pden)
{
    int KLO=-4*n-6, KHI=4*n+6;
    int Ek[64][NPRIME];      /* exponent vectors of the terms */
    int kk[64]; int nt=0;
    for(int k=KLO;k<=KHI;k++){
        int zero=0, bad=0;
        int E[NPRIME]; for(int p=0;p<NPRIME;p++) E[p]=0;
        for(int j=0;j<NF;j++){
            if(!ev[j]) continue;
            int L = fa[j]*n + fb[j]*k;
            if(L<0){
                if(ev[j]<0) zero=1; else bad=1;
            } else {
                if(L>MAXARG) return 1;
                for(int p=0;p<NPRIME;p++) E[p]+=ev[j]*fpv[L][p];
            }
        }
        if(zero) continue;      /* denominator factorial of negative arg -> term 0 */
        if(bad)  return 1;      /* numerator factorial of negative arg -> ill-defined */
        if(nt>=64) return 1;
        kk[nt]=k; memcpy(Ek[nt],E,sizeof(E)); nt++;
    }
    if(nt==0) return 1;
    /* common factor: componentwise min */
    int Em[NPRIME];
    for(int p=0;p<NPRIME;p++){ Em[p]=Ek[0][p]; for(int i=1;i<nt;i++) if(Ek[i][p]<Em[p]) Em[p]=Ek[i][p]; }
    __int128 S=0;
    for(int i=0;i<nt;i++){
        __int128 T=1;
        for(int p=0;p<NPRIME;p++){
            int e=Ek[i][p]-Em[p];
            for(int t=0;t<e;t++){ T*=PR[p]; if(T> (__int128)1<<100) return 1; }
        }
        /* z^k factor */
        int k=kk[i];
        if(z!=1){
            if(k<0) return 1;   /* negative powers of z: skip (k>=0 supports only) */
            for(int t=0;t<k;t++){ T*=z; if(T>((__int128)1<<100)||T<-((__int128)1<<100)) return 1; }
        }
        S+=T;
    }
    __int128 num=S, den=1;
    for(int p=0;p<NPRIME;p++){
        int e=Em[p];
        if(e>0){ for(int t=0;t<e;t++){ num*=PR[p]; if(num>((__int128)1<<110)||num<-((__int128)1<<110)) return 1; } }
        else   { for(int t=0;t<-e;t++){ den*=PR[p]; if(den>((__int128)1<<110)) return 1; } }
    }
    *pnum=num; *pden=den; return 0;
}

static int matches(int n, long long target, int z)
{
    __int128 num,den;
    if(evalsum(n,z,&num,&den)) return 0;
    return (num == (__int128)target*den);
}

static void report(int z){
    fprintf(out,"z=%d ",z);
    for(int j=0;j<NF;j++) if(ev[j]) fprintf(out,"(%d,%d)^%d ",fa[j],fb[j],ev[j]);
    fprintf(out,"\n");
}

/* DFS over exponent vectors */
static void dfs(int j, int budget, int sa, int sb)
{
    if(j==NF){
        if(sa||sb) return;
        nvec++;
        /* need at least one negative-exponent form with b>0 and one with b<0 (finite support) */
        int lo=0,hi=0,any=0;
        for(int i=0;i<NF;i++){ if(ev[i]<0){ if(fb[i]>0) lo=1; if(fb[i]<0) hi=1; } if(ev[i]) any=1; }
        if(!any||!lo||!hi) return;
        nvalid++;
        for(int z=1;z<=ZMAX;z++){
            for(int s=0;s<2;s++){
                int zz = s? -z : z;
                if(s && z==0) continue;
                if(matches(1,T1,zz)){
                    nhit1++;
                    if(matches(2,T2,zz)){ nhit2++; report(zz); }
                }
            }
        }
        return;
    }
    /* prune: remaining forms can change sa by at most budget*A, sb by budget*B */
    if(abs(sa) > budget*A || abs(sb) > budget*B) return;
    for(int e=-budget;e<=budget;e++){
        int c = (e<0)?-e:e;
        if(c>budget) continue;
        ev[j]=e;
        dfs(j+1, budget-c, sa+e*fa[j], sb+e*fb[j]);
    }
    ev[j]=0;
}

int main(int argc,char**argv)
{
    A = argc>1?atoi(argv[1]):3;
    B = argc>2?atoi(argv[2]):3;
    W = argc>3?atoi(argv[3]):8;
    ZMAX = argc>4?atoi(argv[4]):1;
    const char*fn = argc>5?argv[5]:"hits1.txt";
    if(argc>6) T1=atoll(argv[6]);
    if(argc>7) T2=atoll(argv[7]);
    initfact();
    NF=0;
    for(int a=0;a<=A;a++) for(int b=-B;b<=B;b++){
        if(a==0&&b<=0) continue;
        fa[NF]=a; fb[NF]=b; NF++;
    }
    fprintf(stderr,"A=%d B=%d W=%d ZMAX=%d forms=%d\n",A,B,W,ZMAX,NF);
    out=fopen(fn,"w");
    dfs(0,W,0,0);
    fclose(out);
    fprintf(stderr,"balanced vectors=%lld  finite-support=%lld  match q1=%lld  match q1&q2=%lld\n",
            nvec,nvalid,nhit1,nhit2);
    return 0;
}
