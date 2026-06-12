# Reverse A Number
n = 1257
m = 0
r = 0

while (n >0):
    r = n % 10
    n = n // 10
    m = m * 10 + r

print(m)