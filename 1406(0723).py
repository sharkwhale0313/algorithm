from sys import stdin

left = list(stdin.readline().strip())
right = list()
n = int(input())

for _ in range(n):
    command = stdin.readline()
    if command[0] == 'L':
        if left:
            right.append(left.pop())
    elif command[0] == 'D':
        if right:
            left.append(right.pop())
    elif command[0] == 'B':
        if left:
            left.pop()
    elif command[0] == 'P':
        left.append(command[2])

print(''.join(left + list(reversed(right))))