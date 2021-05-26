# idea is to balance out the para numbers i.e. +1 and -1 for opening and closing brackets
# so, to balance out, we can maintain a st to store the indexes of opening brackets and as soon as a closing bracket is 
# found, we pop out the top from stack, this way only extra opening bracket's indexes will be there on stack
# also, the extra closing brackets are the ones with not "(" for them i.e. stack is empty when we found that 
# closing bracket
# so, whenever we have ")" and stack is empty, we can store the index of that ")" to a stack/set
# now, we have all the indexes to be removed from the string, just iterate over the string and generate a new one

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # to store the indexes of the opening brackets
        st = []
        
        # to store the indexes to remove
        idx_to_remove = set()
        
        out = ""
        
        for i,each in enumerate(s):
            # if alpha, continue
            if each not in ("(",")"):
                continue
            # if opening bracket, append th index to stack
            if each == "(":
                st.append(i)
                
            # if closing bracket and stack is empty i.e. -ve balance
            elif not st:
                idx_to_remove.add(i)
            
            # if closing bracket and stack is not empty, pop top
            else:
                st.pop()
                
        # all the indexes to remove (indexes of extra opening brackets and indexes of extra closing brackets)
        idx_to_remove = idx_to_remove.union(set(st))
        
        for i,each in enumerate(s):
            if i not in idx_to_remove:
                out += each
        return out

# time: O(N) - to traverse the letters in string
# space: O(N) ~ to store the indexes of extra brackets