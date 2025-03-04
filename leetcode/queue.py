from collections import deque

if __name__ == '__main__':
    queue = deque()

    queue.append('a')
    queue.append('b')
    queue.append('c')

    stack = deque()
    stack.append(1)
    stack.append(2)
    stack.append(3)

    print(queue.pop())
    print(queue.popleft())

    print(stack.pop())