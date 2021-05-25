# idea is to while appending to the stack, aalong wth the the curr val append the min till now as well inclusive of the curr val,
# so at any given point you will have the min till now

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.st = []
        

    def push(self, val: int) -> None:
        if not self.st:
            self.st.append((val,val))
        else:
            self.st.append((val, min(self.st[-1][1], val)))

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        return self.st[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# time: O(1) - for all the operations
# space : O(1) if we dont consider the stack we are working on else O(N)