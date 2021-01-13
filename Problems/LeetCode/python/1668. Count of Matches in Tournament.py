# 1668. Count of Matches in Tournament
class Solution:
    """
    Given an integer n, number of teams in a tournament is:
    1. If curr number of teams is even, each team gets paired with another team.
    n / 2 matches are played, n /2 advance.
    2. If curr number of teams is odd, one team randomly advances and rest gets paired.
    (n - 1)/2 matches played, 1+(n-1)/2 teams advance to the next round
    Return num of matches played (1 team remains).
    """
    def number_of_matches(self, n: int) -> int:
        """
        n: number of teams.
        Assuming  1 <= n <= 200.
        Complexity:
        Time: O(log n). Gets halved each iteration.
        Space: O(1). No extra data structures are used except a counter int.
        LeetCode results
        Runtime: 28ms (85%)
        Memory: 14.3MB (7%)
        """
        matches: int = 0
        while n > 1:
            if n % 2 == 0:
                matches += n/2
                n = n/2
            elif n % 2 == 1:
                matches += (n-1)/2
                n = 1 + (n-1)/2
        # make sure to cast to int since division converts to float.
        return int(matches)
