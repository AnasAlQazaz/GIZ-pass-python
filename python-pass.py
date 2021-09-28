class Solution:

    @staticmethod
    def longest_palindromic(s: str) -> str:
        resultString = s[0]
        resultStringLen = 0
        inputStringLen = len(s)

        for i in range(inputStringLen):
            #checking whether the input string length is even or odd
            if inputStringLen % 2 != 0:
                #if the length is odd then we'll start from s[i] and then check the left and right of the element...
                left, right = i, i
            else:
                #if the length is even and then we'll start from from s[i:i+1] and then check the left and right of the 2elements...
                left, right = i, i + 1

                #if the right and left o are inside the string boundaries and they're equal, then we'll go further left and write
            while left >= 0 and right < inputStringLen and s[left] == s[right]:
                #if the current palindrom is larger than the stored one, we swap them 
                if (right - left + 1) > resultStringLen:
                    resultString = s[left:right+1]
                    resultStringLen = right - left + 1
                left -= 1
                right += 1

        print(resultString)
