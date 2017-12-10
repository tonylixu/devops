import sys

class Solution:
    # Write your code here
    def __init__(self):
        # Queue definition
        self.q = []
        # Stack definition
        self.s = []
        
    def pushCharacter(self, c):
        # Push the character into the stack
        self.s.insert(0, c)
    
    def enqueueCharacter(self, c):
        self.q.insert(0, c)
        
    def popCharacter(self):
        return self.s.pop(0)
    
    def dequeueCharacter(self):
        return self.q.pop(-1)

if __name__ == '__main__':
    # read the string s
    s=raw_input()
    #Create the Solution class object
    obj=Solution()   

    l=len(s)
    # push/enqueue all the characters of string s to stack
    for i in range(l):
        obj.pushCharacter(s[i])
        obj.enqueueCharacter(s[i])

    isPalindrome=True
    '''
    pop the top character from stack
    dequeue the first character from queue
    compare both the characters
    ''' 
    for i in range(l / 2):
        if obj.popCharacter()!=obj.dequeueCharacter():
            isPalindrome=False
            break
    #finally print whether string s is palindrome or not.
    if isPalindrome:
        sys.stdout.write ("The word, "+s+", is a palindrome.")
    else:
        sys.stdout.write ("The word, "+s+", is not a palindrome.")    