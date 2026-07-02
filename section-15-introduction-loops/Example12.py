# Understanding The Break Keyword
from importlib.util import source_hash

while True:
    print("Statement-1")
    print("Statement-2")
    print("Statement-3")
    break

# We Can Terminate The Infinite Loop Using 
i = 0

while True:
    print("i = ", i)
    if i > 5:
        break

num = 0
while num < 10:
    print("Iteration : " + num)

    if num == 3:
        break

    num += 1