# ideas is to use three pointers, two pointers to traverse the array and check the count of each consecutive same characters (i, j ) and one pointer to write into the list in place
# start with i, j = 0 and increment j until char[i] == char[j], as soon as this condition fails, we can say that the count of that character is j - i. Now, write the current char char[i] on the posiiton of 3rd pointer and increment it
# Now convert the count into string and iterarte over the string count and write each digit at the 3rd pointer and increment it and make i = j
# return 3rd pointer as it will be the last point of writing on to the list

class Solution:
    def compress(self, chars: List[str]) -> int:
        idx, i = 0,0 
        while i < len(chars):
            j = i
            while j < len(chars) and chars[i] == chars[j]:
                j+=1
            chars[idx] = chars[i]
            idx+=1
            count = j - i 
            if count > 1:
                for digit in str(count):
                    chars[idx] = digit
                    idx+=1
            i = j
        return idx
    
# time : O(N) - iterating over the char list
# space : O(1) - constant space used