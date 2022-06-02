from Corruption import CorruptionSolving

PERCENT = 0.12
ACCOUNTS = 10
RANGE = 10000

corruption_solving = CorruptionSolving(PERCENT, ACCOUNTS, RANGE)
print(corruption_solving.count_profit_merging_sum())