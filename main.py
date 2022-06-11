from Corruption import CorruptionSolving
from LongestSubsequence import LongestSubsequence

PERCENT = 0.12
ACCOUNTS = 10
RANGE = 10000

corruption_solving = CorruptionSolving(PERCENT, ACCOUNTS, RANGE)
print(corruption_solving.count_profit_merging_sum())



longest_subs = LongestSubsequence()
testarr1 = [1, 2, 7, 2, 3, 8, 1, 2]
testarr2 = [9, 1, 8, 4, 2, 6, 3]

print(longest_subs.doTask(testarr1, testarr2))