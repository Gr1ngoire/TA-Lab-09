import random


class CorruptionGreedyAlgorithm:

    def __init__(self, percent, count_of_accounts, money_range):
        self.__percent = percent
        self.__count_of_accounts = count_of_accounts
        # self.__accounts = [5854, 6966, 2165, 7664, 8134, 9146, 2222, 5882, 1275, 8745]
        self.__accounts = []

        for i in range(self.__count_of_accounts):
            self.__accounts.append(random.randrange(0, money_range))

        print(self.__accounts)

    def get_optimal_money_account(self):
        data = {
            "minMoneyLoss": None,
            "first": None,
            "second": None,
        }

        while len(self.__accounts) > 1:
            for i in range(1, len(self.__accounts)):
                if (data["minMoneyLoss"] is None) or (
                        (self.__accounts[0] + self.__accounts[i]) * self.__percent < data["minMoneyLoss"]):
                    data["minMoneyLoss"] = (self.__accounts[0] + self.__accounts[i]) * self.__percent
                    data["first"] = self.__accounts[0]
                    data["second"] = self.__accounts[i]

            toAdd = (data["first"] + data["second"]) * (1 - self.__percent)
            print(self.__accounts)
            self.__accounts.remove(data["first"])
            self.__accounts.remove(data["second"])
            self.__accounts.append(toAdd)
            data["minMoneyLoss"] = None
            data["first"] = None
            data["second"] = None

        return self.__accounts[0]
