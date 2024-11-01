from collections import deque
class TextEditor:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def addText(self, text: str) -> None:
        for ch in text:
            self.stack1.append(ch)

    def deleteText(self, k: int) -> int:
        i = 0

        while self.stack1 and i < k:
            self.stack1.pop()
            i += 1

        return i

    def cursorLeft(self, k: int) -> str:
        i = 0

        while self.stack1 and i < k:
           self.stack2.append(self.stack1.pop())

           i += 1

        return ''.join(self.stack1[-10:]) if len(self.stack1) >= 10 else ''.join(self.stack1)

    def cursorRight(self, k: int) -> str:
        i = 0
        while self.stack2 and i < k:
            self.stack1.append(self.stack2.pop())
            i += 1

        return ''.join(self.stack1[-10:]) if len(self.stack1) >= 10 else ''.join(self.stack1)

editor = TextEditor()
editor.addText('leetcode')
print(editor.deleteText(4))
editor.addText('practice')
# print(editor.stack1)
print(editor.cursorRight(3))
print(editor.cursorLeft(8))
print(editor.deleteText(10))
print(editor.cursorLeft(2))
print(editor.cursorRight(6))


test = [1, 3, 4, 5, 6, 6, 6, 7, 70]

print(test[-8:])