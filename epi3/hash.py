"""Hash problems."""
from collections import Counter

def is_perm_palindrome(s):
    """
    Check whether string s can be permuted to form a palindrome.

    E.g., "edified" -> "deified"
    
    Idea: Order of the original word unimportant. All we need for a palindrome
    is that all the letters are in pairs (if even count) or all except one.
    Therefore put the individual chars as keys in a counter and then check if
    all (or all but one) pairs.
    Time: O(N), Space: O(N)
    """
    
    count = Counter()
    for char in s:
        count[char] += 1
    odd_counts = 0
    for char in count:
        if count[char] % 2 > 0:
            odd_counts += 1
    if odd_counts > 1:
        return False
    return True


def top_student(records):
    """
    Scans a CSV of student records to find the student with the top average
    test score in the highest scoring 2-3 tests.

    Args:
        records: A list of parsed file lines with a student id and test score
                 between 0 and 100. For example, "1234,98"
    Returns:
        Int. Student id with the highest average score over at least three 
        tests.

    Brute force: Create a map keyed on student id and store a heap as value with
    the top 3 test scores. Then iterate through keys and compute the average 
    score for each student, keeping track of the max score and student id seen 
    so far and return that.
    Time: O(N), Space: O(M), where N is the number of scores and M is the number
    of unique students. 

    Actually it's hard to imagine doing much better because have to read through
    all the scores and accumulate averages. Therefore the time and space are
    closely tied to N and M.

    This one is a bit too easy to bother coding up. We pass.
    """
    
    pass


def smallest_subarray_with_words(text, words):
    """
    Find the smallest contiguous subarray in a text contains all the words in a
    set.

    Args:
        text: An array of words
        words: A set of words to look for.

    Brute force: Examine every subarray, storing the smallest so far containing
    all the words. 
    Time: O(N^2K), Space: O(K), where N is the length of the text and K is the
    number of words in the set (which all must be checked using an intermediate
    set). Note that I'm not including the return value in the space cost.

    Idea: Use two pointers to traverse array. Advance the upper pointer until
    all the words are covered, then advance the lower pointer until hit another 
    one of the words. Record the smallest subarray seen so far while traversing.
    Time: O(N), Space: O(K)
    => This one seems hard to beat.

    Example text:
     0         1      2       3      4        5     6         7       8
    ["should", "not", "save", "the", "union", "or", "should", "save", "the", 
    9
    "best"]
    words = set("save", "the", "union")
    lower, upper, best_lower, best_upper, curr_words
    0, 0, -Inf, 0, []
    0, 2, -Inf, 0, ["save": 1]
    0, 3, -Inf, 0, ["save": 1, "the": 1]
    0, 4, -Inf, 0, ["save": 1, "the": 1, "union": 1]
    2, 4, 2, 4, ["save": 1, "the": 1, "union": 1]
    3, 4, 2, 4, ["the": 1, "union": 1]
    3, 7, 2, 4, ["the": 1, "union": 1, "save": 1] => not optimal
    4, 7, 2, 4, ["union": 1, "save": 1]
    4, 8, 2, 4, ["union": 1, "save": 1, "the": 1] => not optimal
    5, 8, 2, 4, ["save": 1, "the": 1]
    5, 9, 2, 4, ["save": 1, "the": 1]
    break
    return (2, 4)
    """

    lower, upper = 0, 0
    curr_words = Counter()
    best_lower, best_upper= -float("inf"), 0
    remaining_words = len(words)
    while lower <= upper and upper < len(text) - 1:
        if remaining_words > 0:
            upper += 1
            if text[upper] in words:
                curr_words[text[upper]] += 1
                if curr_words[text[upper]] == 1:
                    remaining_words -= 1
        else:
            # Valid subarray
            # Advance lower pointer until hit a word
            # Makes sure array isn't suboptimally long
            while text[lower] not in words:
                lower += 1 
            if best_upper - best_lower > upper - lower:
                best_upper, best_lower = upper, lower
            # Get rid of lowest word
            curr_words[text[lower]] -= 1
            if curr_words[text[lower]] == 0:
                remaining_words += 1
            lower += 1

    return best_lower, best_upper

