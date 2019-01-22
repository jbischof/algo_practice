"""Array problems."""
import random
import math

def two_part(a, value, start_pos=0):
  """Partitions array based on value starting from `start_pos`.

  Time complexity: O(N)
  Space complexity: O(1)

  Returns:
    Beginning position of upper half of array
  """

  lte, gt = start_pos, len(a) 
  while lte < gt:
    if a[lte] <= value:
      lte += 1
    else:
      gt -= 1
      a[lte], a[gt] = a[gt], a[lte]
  return lte 


def dnf(a, pivot_pos):
  """Partition array into values less than, equal to, and greater than pivot.

  Time complexity: O(N)
  Space complexity: O(1)
  """

  pivot = a[pivot_pos]
  # Sort array into less than pivot and greater than pivot
  new_start = two_part(a, pivot - 1)
  two_part(a, pivot, new_start)
  

def array_game(a):
  """Check if game specified by array can be won.

  Each entry of array specifies how far can advance from each spot.

  Time complexity: O(N)
  Space complexity: O(1)
  
  Returns:
    True if game can be won, False otherwise.
  """

  pos = len(a)
  while pos > 0:
    # Check if can reach back to earlier position
    for next in range(pos - 1, -1, -1):
      if a[next] >= pos - next:
        pos = next
        break
      elif next == 0:
        return False
  return True


def del_dups(a):
  """Delete duplicates in sorted array.

  Time complexity: O(N)
  Space complexity: O(1)
  
  Returns:
    Length of deduped array.
  """

  idx = 1
  for i in xrange(1, len(a)):
    if a[i] != a[i - 1]:
      a[idx] = a[i]
      idx += 1
  return idx


class Sale(object):
  def __init__(self, a, buy, sale):
    self.buy = buy
    self.sale = sale
    self.gain = a[sale] - a[buy] 

def best_stock_sale(a):
  """Determine the best time to buy/sell a stock given an array of prices.
  
  Time complexity: O(N)
  Space complexity: O(1)
  """

  best_sale = Sale(a, 0, 1)
  best_buy = 0
  for i in range(1, len(a)):
    new_sale = Sale(a, best_buy, i)
    if new_sale.gain > best_sale.gain:
      best_sale = new_sale
    # If gain negative, have found a better low price
    if new_sale.gain < 0:
      best_buy = i
  return best_sale.buy, best_sale.sale


def sample_offline_data(a, k):
  """Same k data points from array `a`.

  Time complexity: O(N)
  Space complexity: O(1)
  """
  
  # Iterate through sampled positions
  for i in range(k):
    # Get index from one of remaining positions
    samp = int(math.floor(k + (len(a) - k) * random.random()))
    # Move into next sampled position
    a[i], a[samp] = a[samp], a[i]
  return a[:k]
    




