def isPalindrome(x):
    if x==0:
        return True

    elif x>0:
        length = 0
        check = 1
        while check>0:
            check = int(x/(10**length))
            length += 1
        length -= 1

        for i in range(int((length+1)/2)):
            if int((x%10**(i+1) - x%10**i)/10**i) != x//10**(length-i-1) - 10*(x//10**(length-i)):
                return False
        return True

    else:
        return False

print("Check whether your integer is a palindrome")
if isPalindrome(int(input("Enter an integer : "))):
    print("Your number is a palindrome")
else:
    print("Your number is NOT a palindrome")
