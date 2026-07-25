class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]

            if total == target:
                return [left +1, right+1 ]
            elif total < target:
                left +=1
            else:
                right -= 1
        

        numbers.insert(0, None)

        for i in range(1, len(numbers), 1):
            for j in range(1, len(numbers), 2):
                
                if (numbers[i] + numbers[j]) == target:
                    arr_to_send = [i, j]
                    arr_to_send.sort()

                    print("current index", i)
                    print("current index", j)
                    
                    return arr_to_send

        return []

        # print(numbers)

        numbers.insert(0, None)

        for i in range(1, len(numbers), 1):
            for j in range(1, len(numbers), 2):
                
                if (numbers[i] + numbers[j]) == target:
                    arr_to_send = [i, j]
                    arr_to_send.sort()

                    print("current index", i)
                    print("current index", j)
                    
                    return arr_to_send

        # return [0,0]