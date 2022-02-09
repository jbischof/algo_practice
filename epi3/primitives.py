""" 
Playing with bits 

Useful operators:
    bin(x): binary representation
    x >> y: shift x y bits left (divide by 2**y)
    x << y: shift x y bits right (multiply by 2**y)
    &: bitwise and
    |: bitwise or
    ^: bitwise xor (1 if one bit active, 0 if both active or neither active)
       ^1 also can be used to flip bits in another integer using masks
    ~: bitwise complement (swap all the bits)

Compound operators:
    x & (x - 1): sets the lowest bit to zero
    x & ~(x - 1): extracts the lowest set bit
"""

def count_bits(x):
    """Count the number of positive bits in a binary representation.
    Args:
        x: Int

    Returns:
        Number of positive bits
    """

    num_bits = 0
    while x:
        # Check rightmost bit
        num_bits += x & 1
        # Divide by 2
        x = x >> 1
    return num_bits


def parity(x):
    """Checks whether the number of positive bits is even or odd.

    Time complexity: O(n), where n is the integer width.

    Returns:
        Int. Zero if parity is even and one if parity is odd.
    """

    parity = 0
    while x:
        # XOR parity with rightmost bit. If already even it stays even if 0
        # if already odd it stays odd with 0
        parity ^= x & 1
        # Divide by 2
        x = x >> 1
    return parity


def parity2(x):
    """Checks whether the number of positive bits is even or odd.

    This is a faster version of parity.

    Time complexity: O(k), where k is the number of positive bits.

    Returns:
        Int. Zero if parity is even and one if parity is odd.
    """

    parity = 0
    while x:
        # XOR parity with rightmost bit. If already even it stays even if 0
        # if already odd it stays odd with 0
        parity ^= x & 1
        # Divide by 2
        x = x >> 1
    return parity


def swap_bits(x, i, j):
    """Swap the bits in positions i and j of integer x"""
    bit_i, bit_j = (x >> i) & 1, (x >> j) & 1
    # Only swap if bits are not the same
    if bit_i ^ bit_j: 
        # If the bits differ than we just need to flip both of them
        mask = (1 << i) | (1 << j)
        x ^= mask
    return x


def reverse_bits(x, int_width=32):
    """Reverse the bits of an binary representation and return the resulting
    integer.

    Brute force: Extract the bits and record all the active positions in an 
    array. Then write out a new int with the positions reversed.
    Time: O(N), Space: O(N)

    In place: swap the bits in the first half of the int width with the second,
    just like we would do for an array
    Time: O(N), Space: O(1)
    """

    for i in range(0, int_width // 2):
        x = swap_bits(x, i, int_width - (i + 1))
    return x
