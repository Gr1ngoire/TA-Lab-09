import math
import random


class CorruptionSolving:

    def __init__(self, percent, bank_accounts, user_range):
        self.__PERCENT = percent
        self.__BANK_ACCOUNTS = bank_accounts
        # self.__ACCOUNTS = [5854, 6966, 2165, 7664, 8134, 9146, 2222, 5882, 1275, 8745]
        self.__ACCOUNTS = []

        for i in range(self.__BANK_ACCOUNTS):
            self.__ACCOUNTS.append(random.randrange(0, user_range))

    # Main problem is merging the accounts, the best soultion is doing merging in a way of tree(from leaves to root),
    # not sequentially

    def __get_mid_index(self, arr):
        return math.floor(len(arr) / 2)

    def __get_percented_sum(self, two_elem_arr):
        return (two_elem_arr[0] + two_elem_arr[1]) * (1 - self.__PERCENT)

    def __splitter(self, arr, buff):
        # print(arr)
        if len(arr) == 2:
            buff.append(self.__get_percented_sum(arr))

        elif len(arr) % 2 == 0:
            self.__splitter(arr[0: self.__get_mid_index(arr)], buff)
            self.__splitter(arr[self.__get_mid_index(arr):], buff)

        elif len(arr) % 2 == 1 and len(arr) > 1:
            temp = arr[-1]
            new_arr = arr[0: -1].copy()
            new_arr[-1] = (new_arr[-1] + temp) * (1 - self.__PERCENT)
            self.__splitter(new_arr, buff)

    def count_profit_merging_sum(self):
        buffer = []
        while len(self.__ACCOUNTS) != 1:
            self.__splitter(self.__ACCOUNTS, buffer)
            self.__ACCOUNTS = buffer
            buffer = []

        return self.__ACCOUNTS[0]
