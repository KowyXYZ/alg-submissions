class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        daysPassed = []

        for i in range(len(temperatures)):
            j = i + 1

            while j < len(temperatures):
                if temperatures[j] > temperatures[i]:
                    break

                j += 1

            if j == len(temperatures):
                daysPassed.append(0)
            else:
                daysPassed.append(j - i)

        return daysPassed