n = int(input())


def solution():
    for i in range(1, 10):
        for j in range(1, 10):
            if i * j == n:
                print("Yes") 
                return
    print("No")


solution()
