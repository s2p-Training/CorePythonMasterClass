n = 1257
num = n

m = 0
r = 0

isPalindrome = None

while (n >0):
    r = n % 10
    n = n // 10
    m = m * 10 + r

if n == num:
    isPalindrome = True
else:
    isPalindrome = False

print(isPalindrome)