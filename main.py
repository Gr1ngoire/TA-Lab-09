from CorruptionGreedyAlgorithm import CorruptionGreedyAlgorithm
from LongestSubsequence import LongestSubsequence

PERCENT = 0.12
ACCOUNTS = 10
RANGE = 10000

corruption_solve = CorruptionGreedyAlgorithm(PERCENT, ACCOUNTS, RANGE)
print(corruption_solve.get_optimal_money_account())


longest_subs = LongestSubsequence()
testarr1 = [1, 2, 7, 2, 3, 8, 1, 2]
testarr2 = [9, 1, 8, 4, 2, 6, 3]

print(longest_subs.doTask(testarr1, testarr2))