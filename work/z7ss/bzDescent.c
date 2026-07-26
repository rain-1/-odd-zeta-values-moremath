/* Brown-Zudilin's DESCENT template, applied one level up.
 *
 * BZ (CellZeta.tex lines 691-725) obtain the weight-5 leading coefficient from the
 * weight-3 one by ONE extra summation:
 *
 *   Q(p;q) = sum_{k} (-1)^{k+p4+p5+p6} C(k,p6) C(q4,k-p4) C(q5,k-p5)
 *                    * A( p0,p1,p2,p3-k ; q1,q2,q3-p6+k )
 *   A(P;Q) = (-1)^{P0+P1+P2+P3} sum_j C(j,P0) C(j+Q3-P0, P3+Q3-P0) C(Q1,j-P1) C(Q2,j-P2)
 *
 * (verified in this file: the totally symmetric specialisation reproduces 1,21,2989,714549.)
 *
 * The weight-7 analogue should then be  q_n = sum_k <3 binomials> * Q(<shifted weight-5 params>).
 * This program scans that template for a match with q_n = 1, 61, 52921, 94357501.
 */
#include <stdio.h>
#include <stdlib.h>

typedef __int128 i128;

static i128 gbin(long long x, long long m)
{
    if (m < 0) return 0;
    if (m == 0) return 1;
    if (x >= 0 && x < m) return 0;
    i128 num = 1, den = 1;
    for (long long i = 0; i < m; i++) { num *= (i128)(x - i); den *= (i128)(i + 1); }
    return num / den;
}

/* weight-3 leading coefficient A(P0,P1,P2,P3;Q1,Q2,Q3) */
static i128 Aw3(long long P0,long long P1,long long P2,long long P3,
                long long Q1,long long Q2,long long Q3)
{
    long long lo = P1>P2?P1:P2, hi = (P1+Q1<P2+Q2)?P1+Q1:P2+Q2;
    if (hi-lo > 400) return 0;
    i128 S=0;
    for (long long j=lo;j<=hi;j++){
        i128 c = gbin(j,P0); if(!c) continue;
        c *= gbin(Q1,j-P1); if(!c) continue;
        c *= gbin(Q2,j-P2); if(!c) continue;
        c *= gbin(j+Q3-P0, P3+Q3-P0); if(!c) continue;
        S += c;
    }
    if ((P0+P1+P2+P3)&1) S=-S;
    return S;
}

/* weight-5 leading coefficient via the descent (equivalent to BZ eq. sumQ) */
static i128 Qw5(const long long*p,const long long*q)
{
    long long lo=p[4]>p[5]?p[4]:p[5], hi=(p[4]+q[4]<p[5]+q[5])?p[4]+q[4]:p[5]+q[5];
    if (hi-lo>400) return 0;
    i128 S=0;
    for(long long k=lo;k<=hi;k++){
        i128 c=gbin(k,p[6]); if(!c)continue;
        c*=gbin(q[4],k-p[4]); if(!c)continue;
        c*=gbin(q[5],k-p[5]); if(!c)continue;
        i128 a=Aw3(p[0],p[1],p[2],p[3]-k, q[1],q[2],q[3]-p[6]+k);
        if(k&1) S-=c*a; else S+=c*a;
    }
    if((p[4]+p[5]+p[6])&1) S=-S;
    return S;
}

int main(int argc,char**argv)
{
    /* sanity: BZ totally symmetric weight-5 */
    for(long long n=0;n<=4;n++){
        long long p[7]={n,n,n,2*n,n,n,n}, q[6]={0,n,n,n,n,n};
        i128 v=Qw5(p,q);
        printf("descent weight-5 check n=%lld : %lld\n",n,(long long)v);
    }
    printf("(expect 1, 21, 2989, 714549, 217515501)\n\n");

    long long T[4]={1,61,52921,94357501};
    int R = argc>1?atoi(argv[1])+1:4;          /* inner parameter values 0..R-1 */
    int RO = argc>2?atoi(argv[2])+1:3;         /* outer parameter values 0..RO-1 */
    long long scanned=0, hit2=0, hit3=0;
    /* inner weight-5 parameters, tied by the dihedral symmetry of the BZ cell:
       p = (a,a,a,b,a,a,a) n , q = (c,c,d,c,c) n           */
    for(int a=0;a<R;a++)for(int b=0;b<R;b++)for(int c=0;c<R;c++)for(int d=0;d<R;d++)
    /* outer layer parameters  P4,P5,P6,Q4,Q5  (all multiples of n) */
    for(int P4=0;P4<RO;P4++)for(int P5=0;P5<RO;P5++)for(int P6=0;P6<RO;P6++)
    for(int Q4=0;Q4<RO;Q4++)for(int Q5=0;Q5<RO;Q5++)
    /* which inner slot absorbs -k, and which absorbs +k */
    for(int sm=0;sm<7;sm++)for(int sp=0;sp<5;sp++)
    for(int sgn=0;sgn<2;sgn++)
    {
        scanned++;
        i128 v[4];
        int bad=0;
        for(int n=0;n<4 && !bad;n++){
            long long L=n;
            long long lo=P4*L>P5*L?P4*L:P5*L;
            long long hi=(P4*L+Q4*L<P5*L+Q5*L)?P4*L+Q4*L:P5*L+Q5*L;
            if(hi-lo>200){bad=1;break;}
            i128 S=0;
            for(long long k=lo;k<=hi;k++){
                i128 cc=gbin(k,P6*L); if(!cc)continue;
                cc*=gbin(Q4*L,k-P4*L); if(!cc)continue;
                cc*=gbin(Q5*L,k-P5*L); if(!cc)continue;
                long long p[7]={a*L,a*L,a*L,b*L,a*L,a*L,a*L};
                long long q[6]={0,c*L,c*L,d*L,c*L,c*L};
                p[sm]-=k;
                q[sp+1]+=k;
                i128 w=Qw5(p,q);
                if(sgn && (k&1)) S-=cc*w; else S+=cc*w;
            }
            v[n]=S;
        }
        if(bad) continue;
        if(v[0]==0) continue;
        if(v[1]!=(i128)T[1]*v[0] && v[1]!=-(i128)T[1]*v[0]) continue;
        if(v[2]!=(i128)T[2]*v[0] && v[2]!=-(i128)T[2]*v[0]) continue;
        hit2++;
        if(v[3]!=(i128)T[3]*v[0] && v[3]!=-(i128)T[3]*v[0]) continue;
        hit3++;
        printf("HIT inner p=(%d..,%d) q=(%d..,%d) outer(P4,P5,P6,Q4,Q5)=(%d,%d,%d,%d,%d) "
               "shift -k in p[%d], +k in q[%d], altsign=%d\n",
               a,b,c,d,P4,P5,P6,Q4,Q5,sm,sp+1,sgn);
    }
    printf("descent-template scan: %lld configurations, matched q0,q1,q2: %lld, also q3: %lld\n",
           scanned,hit2,hit3);
    return 0;
}
