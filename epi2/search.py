"""Search problems."""
import math
import random

def find_first(a, k):
  """Find the first occurrence of `k` in array `a`."""

  L, U = 0, len(a) - 1
  while L <= U:
    M = (L + U) // 2
    if ((M > 0 and a[M] == k and a[M - 1] < k) or
        (M == 0 and a[M] == k)):
      return M
    elif a[M] >= k:
      U = M - 1
    else:
      L = M + 1
  return None

def bisect_sqrt(n):
  """Find the sqrt of float `n` using bisection."""

  L, U = (0, n) if n > 1 else (0, 1)
  tol = 1e-8
  
  while abs(L - U) > tol:
    guess = (L + U) / float(2)
    if guess * guess > n:
      U = guess
    else:
      L = guess
  
  return guess


def pivot_array(a, L, U):
  """Pivot array a[L : (U + 1)] around Uth entry.

  Time: O(n)
  Space: O(1)
  
  Returns:
    Final position of pivot.
  """

  pivot, comp = U, L
  while pivot > comp:
    if a[pivot] > a[comp]:
      comp += 1
    else:
      # Move current comp after pivot and put item before pivot in `comp` spot
      a[pivot - 1], a[comp] = a[comp], a[pivot - 1]
      a[pivot], a[pivot - 1] = a[pivot - 1], a[pivot]
      pivot -= 1
  return pivot


def quickselect(a, k):
  """Find kth largest value in array `a`.

  Time: O(n) almost surely using randomization
  Space: O(1)
  """

  random.shuffle(a)
  L, U = 0, len(a) - 1
  pos = -1
  while not pos == k:
    pos = pivot_array(a, L, U)
    if pos > k:
      U = pos - 1
    elif pos < k:
      L = pos + 1
  return a[pos]

