from collections import deque

if __name__ == '__main__':

     L = [1,2,3,4,5]

     # Using Deque As Stack
     
     stack = deque(L)
     print(stack)

     stack.appendleft(11)
     stack.appendleft(12)
     stack.appendleft(13)

     print(stack)

     ele = stack.popleft()
     print(ele)

     ele = stack.popleft()
     print(ele)

