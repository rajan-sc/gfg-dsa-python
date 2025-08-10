# Palindrome number are those weather we read from left to right or vice versa they are same 
# Example 78987 and 7 Palindrome 
# not palindrome 21 and 43

def palindrome(n):
    rev = 0
    temp = n # Performing operation on this 

    while temp != 0:
        last_digit = temp % 10  #(mod of 10 to get last digit)
        rev = rev * 10 + last_digit 
        temp //= 10
    if rev == n:
        print("Yeah Palindrome hehe.")
    else:
        print("Not a palindrome.")

palindrome(212)
palindrome(21)

