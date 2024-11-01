class Balance_Parentheseis:
    left_brackets = ['(', '{', '[', '<']
    right_brackets = [')', '}', ']', '>']

    def is_rght_bracket(self, ch):
        return ch in self.right_brackets

    def is_left_bracket(self, ch):
        return ch in self.left_brackets
    
    def is_matched(self, left, right):
        return self.left_brackets.index(left) == self.right_brackets.index(right)

    def is_balanced(self, str):
        stack = []
        count = []
        c = 0
        for ch in str:
            if self.is_left_bracket(ch):
                c += 1
                stack.append(ch)

            if self.is_rght_bracket(ch):
                count.append(c)
                c = 0
                if len(stack) == 0:
                    return False
                left = stack.pop()

                if not self.is_matched(left, ch):
                    return False

        return max(count)


balance = Balance_Parentheseis()

result = balance.is_balanced("(1+(2*3)+((8)/4))+1")

print(result)

