/* Is q_n = 1, 61, 52921, 94357501 (weight-7 M_{0,10} leading coefficient) equal to
 * Brown-Zudilin's WEIGHT-5 leading-coefficient double sum (their eq. sumQ)
 *
 *   Q(p;q) = (-1)^{p0+...+p6} sum_{k1,k2 in Z}
 *              C(k1,p0) C(k2,p6) C(k1+k2+q3-p0-p6, p3+q3-p0-p6)
 *              C(q1,k1-p1) C(q2,k1-p2) C(q4,k2-p4) C(q5,k2-p5)
 *
 * at parameters proportional to n:  p_j = A_j n  (j=0..6),  q_j = G_j n (j=1..5)?
 *
 * Motivation: BZ's own decomposition has  I_n = I'_n + I''_n zeta(2)  with I''_n a linear
 * form in 1, zeta(3), zeta(5) -- i.e. a WEIGHT-5 object -- and  I''_n = -9 q_n zeta5 + ...
 * So q_n is (up to a constant) the zeta(5)-coefficient of a weight-5 linear form, which for
 * the whole BZ J(p;q) family equals 2 Q(p;q).  If I''_n lies in that family, q_n = c Q(p;q).
 *
 * Test: match the RATIOS  Q(1)/Q(0) = 61  and  Q(2)/Q(0) = 52921  (scale invariant),
 * then Q(3)/Q(0) = 94357501.
 * Sanity check: A = (1,1,1,2,1,1,1), G = (1,1,1,1,1) must reproduce 1, 21, 2989 (weight 5).
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef __int128 i128;
static int AMAX = 3;

/* generalised binomial C(x,m), integer x (may be negative), integer m; 0 if m<0 */
static i128 gbin(long long x, long long m)
{
    if (m < 0) return 0;
    if (m == 0) return 1;
    if (x >= 0 && x < m) return 0;
    i128 num = 1, den = 1;
    for (long long i = 0; i < m; i++) { num *= (i128)(x - i); den *= (i128)(i + 1); }
    return num / den;   /* exact */
}

/* Q(p;q) with p[0..6], q[1..5] (q[0],q[3] used: q3 is q[3]) */
static int Qval(const long long *p, const long long *q, i128 *out)
{
    long long k1lo = p[1] > p[2] ? p[1] : p[2];
    long long k1hi = (p[1] + q[1] < p[2] + q[2]) ? p[1] + q[1] : p[2] + q[2];
    long long k2lo = p[4] > p[5] ? p[4] : p[5];
    long long k2hi = (p[4] + q[4] < p[5] + q[5]) ? p[4] + q[4] : p[5] + q[5];
    if (k1hi - k1lo > 400 || k2hi - k2lo > 400) return 1;
    i128 S = 0;
    long long M = p[3] + q[3] - p[0] - p[6];
    for (long long k1 = k1lo; k1 <= k1hi; k1++) {
        i128 c1 = gbin(k1, p[0]);
        if (c1 == 0) continue;
        c1 *= gbin(q[1], k1 - p[1]);
        if (c1 == 0) continue;
        c1 *= gbin(q[2], k1 - p[2]);
        if (c1 == 0) continue;
        for (long long k2 = k2lo; k2 <= k2hi; k2++) {
            i128 c2 = gbin(k2, p[6]);
            if (c2 == 0) continue;
            c2 *= gbin(q[4], k2 - p[4]);
            if (c2 == 0) continue;
            c2 *= gbin(q[5], k2 - p[5]);
            if (c2 == 0) continue;
            i128 c3 = gbin(k1 + k2 + q[3] - p[0] - p[6], M);
            if (c3 == 0) continue;
            S += c1 * c2 * c3;
        }
    }
    long long sg = 0; for (int j = 0; j <= 6; j++) sg += p[j];
    if (sg & 1) S = -S;
    *out = S;
    return 0;
}

static int evalAt(const int *A, const int *G, long long n, i128 *out)
{
    long long p[7], q[6];
    for (int j = 0; j < 7; j++) p[j] = (long long)A[j] * n;
    for (int j = 1; j <= 5; j++) q[j] = (long long)G[j - 1] * n;
    q[0] = 0;
    return Qval(p, q, out);
}

int main(int argc, char **argv)
{
    if (argc > 1) AMAX = atoi(argv[1]);
    /* sanity check: BZ totally symmetric weight-5 */
    {
        int A[7] = {1,1,1,2,1,1,1}, G[5] = {1,1,1,1,1};
        for (long long n = 0; n <= 4; n++) {
            i128 v; evalAt(A, G, n, &v);
            long long lo = (long long)v;
            printf("BZ weight-5 check n=%lld : %lld\n", n, lo);
        }
        printf("(expect 1, 21, 2989, 714549, 217515501)\n\n");
    }
    long long T[4] = {1, 61, 52921, 94357501};
    int A[7], G[5];
    long long tried = 0, hits = 0;
    int R = AMAX + 1;
    for (int i = 0; i < 7; i++) A[i] = 0;
    long long total = 1; for (int i = 0; i < 12; i++) total *= R;
    for (long long code = 0; code < total; code++) {
        long long c = code;
        for (int i = 0; i < 7; i++) { A[i] = c % R; c /= R; }
        for (int i = 0; i < 5; i++) { G[i] = c % R; c /= R; }
        i128 v0, v1, v2, v3;
        if (evalAt(A, G, 0, &v0)) continue;
        if (v0 == 0) continue;
        if (evalAt(A, G, 1, &v1)) continue;
        if (v1 != (i128)T[1] * v0 && -v1 != (i128)T[1] * v0) continue;
        if (evalAt(A, G, 2, &v2)) continue;
        if (v2 != (i128)T[2] * v0 && v2 != -(i128)T[2] * v0) continue;
        tried++;
        if (evalAt(A, G, 3, &v3)) continue;
        if (v3 != (i128)T[3] * v0 && v3 != -(i128)T[3] * v0) continue;
        hits++;
        printf("HIT  A=(%d,%d,%d,%d,%d,%d,%d) G=(%d,%d,%d,%d,%d)\n",
               A[0],A[1],A[2],A[3],A[4],A[5],A[6],G[0],G[1],G[2],G[3],G[4]);
    }
    printf("AMAX=%d  scanned %lld parameter vectors, matched q0,q1,q2: %lld, matched q3 too: %lld\n",
           AMAX, total, tried, hits);
    return 0;
}
