# idea is to have map of opening and closing brackets
# maintain a stack, append if opening bracket
# else check with the top of stack. if not match return False
class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        dic = {"{":"}", "(":")", "[": "]"}
        
        for each in s:
            if each in dic:
                st.append(each)
            else:
                if st:
                    temp = st.pop()
                    if not each == dic[temp]:
                        return False
                else:
                    return False
        return not st
    
# time: O(N) - to traverse the given string
# space : O(N) - for stack