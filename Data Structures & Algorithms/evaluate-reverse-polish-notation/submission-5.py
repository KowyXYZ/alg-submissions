class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0 

        ops = ['+', '-', '*',  '/']


        temp = []

        for i in tokens:
            if i not in ops:
                temp.append(int(i))

            if i in ops:
                b = temp.pop()
                a = temp.pop()

                if i == '+':
                    temp.append(a + b)
                if i == '-':
                    temp.append(a - b)
                if i == '*':
                    temp.append(a * b)
                if i == '/':
                    temp.append(int(a / b))
        return temp[0]
