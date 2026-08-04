# DENSITY_PROBE — do companion denominators cancel at positive prime density?

**Fork report, 2026-08-05.**  Scripts: `work/z5eps/eps60_density.py`
(+ `eps60_results.json`).  Exact `Fraction` arithmetic; every recurrence
validated against its binomial sum (n <= 8, all six families PASS) before
use.  Families: A (Franel), C, D, E, gamma (Apery zeta(3)), zeta.
Ranges: n <= 300, primes p <= 200.  Deficiency convention:
`needed_p(n) = max(0, -v_p(B(n)))`, `allowed_p(n) = r*floor(log_p n)`.

## Verdict — the negative, stated cleanly

**Cancellation is confined to the single structural (ramified) prime per
family; at every other prime the classical denominator `d_n^r` is attained
EXACTLY.  There is no positive-density cancellation class.  The modular
denominator theory yields polynomial savings only.**

Evidence:

1. **Totally-cancelling primes in [5, 200]: zero, for all six families**
   (44 primes tested each; density 0.000).  The eps58 ramified-prime law is
   confirmed and is the *whole* story: A and E are 2-integral (worst needed
   exponent 0 at p=2 through n=300), C and zeta are 3-integral; every other
   prime appears in denominators.
2. **No partial savings either.**  At p = 5, 7, 11, 13 the observed worst
   denominator exponent equals the allowed `r*floor(log_p 300)` exactly
   (deficiency 0) in ALL six families — e.g. gamma at p=5: allowed 9,
   observed 9.  Away from the ramified prime the Eichler-formula bound
   `d_n^r` is sharp, not merely an upper bound.
3. Structural-prime table (worst needed exponent, n <= 300):
   A: (p2, p3) = (0, 10); C: (16, 0); D: (16, 10); E: (0, 10);
   gamma: (24, 15); zeta: (24, 0).

## The Catalan question (family E), brutally

`B_E(n)/A_E(n) -> G/2` — confirmed numerically to high precision
(`ell/(G/2) = 1.0`).  But the characteristic roots of E's recurrence are
4 and 8, **both > 1**: the linear form `A(n)(G/2) - B(n)` *grows* at
measured rate 1.3767 per n (= log 4 up to finite-n correction).  For
irrationality one needs the form to decay faster than the denominators
grow; here it does not decay at all.  Consequently:

* **even total cancellation of every denominator at every prime would
  yield nothing for Catalan from this pair** — the obstruction is
  analytic (root separation), not arithmetic;
* the shortfall is >= log 4 ~ 1.386 nats per n *before* any denominator
  is even considered (compare Apery's zeta(3) margin: -3.525 + 3 < 0).

## What survives as arithmetic content

The ramified-prime integrality (eps58's law, here re-confirmed to n=300
and sharpened by the exhaustive negative around it) is a clean, isolated,
theorem-shaped fact — a *structural* statement about the uniformization,
not a lever on irrationality.  The split-prime phenomena of the
half-Apery world (eps56) live in *Lucas congruences*, not in denominator
cancellation: the two should not be conflated, and this probe shows the
denominator side is rigid.

## Honest limits

n <= 300, p <= 200, six of fifteen families (the two chi_-3, the chi_-4
Catalan family, level-5 and level-6 controls, and the Apery control);
"totally cancelling" tested on the live window [p, 300].  Nothing here
excludes cancellation phenomena in numerators, in other normalizations
of B, or for the zeta(5) rows (out of scope; their rectification fails).
