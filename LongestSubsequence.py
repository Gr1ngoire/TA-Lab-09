class LongestSubsequence:

    def __init__(self):
        pass

    def doTask(self, arr1, arr2):
        return self.findAscending(self.findCommon(arr1, arr2))

    def findCommon(self, arr1, arr2):
        n = len(arr1)
        m = len(arr2)
        dpmatrix = [[0 for i in range(n + 1)] for i in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if j == 0 or i == 0:
                    continue
                elif arr1[j - 1] == arr2[i - 1]:
                    dpmatrix[i][j] = dpmatrix[i - 1][j - 1] + 1
                else:
                    dpmatrix[i][j] = max(dpmatrix[i][j - 1], dpmatrix[i - 1][j])
        seqLen = dpmatrix[m][n]
        longestSequence = [0] * (seqLen)
        while m > 0 and n > 0:
            if arr1[n - 1] == arr2[m - 1]:
                longestSequence[seqLen - 1] = arr1[n - 1]
                n -= 1
                m -= 1
                seqLen -= 1
            elif dpmatrix[m][n - 1] < dpmatrix[m - 1][n]:
                m -= 1
            else:
                n -= 1
        return longestSequence

    def findAscendingLen(self, arr):
        n = len(arr)
        lengthAtIndex = [1] * n
        for i in range(1, n):
            prevSmallerLengths = []
            for j in range(0, i):
                if arr[i] > arr[j]:
                    prevSmallerLengths.append(lengthAtIndex[j])
            lengthAtIndex[i] = 1 + max(prevSmallerLengths, default=0)
        return max(lengthAtIndex, default=0)

    def findAscending(self, arr):
        n = len(arr)
        lengthAtIndex = [1] * n
        prevIndex = [-1] * n
        for i in range(1, n):
            prevSmallerLengths = []
            prevSmallerIndexes = []
            for j in range(0, i):
                if arr[i] > arr[j]:
                    prevSmallerLengths.append(lengthAtIndex[j])
                    prevSmallerIndexes.append(j)
            maxIndex = 0
            if len(prevSmallerLengths) != 0:
                for k in range(1, len(prevSmallerLengths)):
                    if prevSmallerLengths[maxIndex] < prevSmallerLengths[k]:
                        maxIndex = k
                lengthAtIndex[i] = 1 + prevSmallerLengths[maxIndex]
                prevIndex[i] = prevSmallerIndexes[maxIndex]
        biggestSequenceEnd = 0
        for i in range(1, n):
            if lengthAtIndex[biggestSequenceEnd] < lengthAtIndex[i]:
                biggestSequenceEnd = i
        longestSequence = []
        while biggestSequenceEnd != -1:
            longestSequence.append(arr[biggestSequenceEnd])
            biggestSequenceEnd = prevIndex[biggestSequenceEnd]
        return longestSequence[::-1]