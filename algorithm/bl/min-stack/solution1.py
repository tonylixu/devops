class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        # Time complexity is O(n)
        self.nums.insert(0,x)

    def pop(self):
        """
        :rtype: void
        """
        # Time complexity is O(1)
        self.nums.pop(0)

    def top(self):
        """
        :rtype: int
        """
        # Time complexity is O(1)
        return self.nums[0]

    def getMin(self):
        """
        :rtype: int
        """
        # Time complexity is O(n)
        return min(self.nums)


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(2)
obj.push(3)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print param_3
