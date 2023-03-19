"""

"""

def main():
    N = int(input())
    array = list(map(int, input().split()))
    result = []

    for num in array:
        if num % 2 == 0:
            result.append(num)
    
    print(*result)



main()