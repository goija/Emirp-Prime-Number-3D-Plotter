import matplotlib.pyplot as plt
import math
import concurrent.futures


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def is_emirp(n):
    if not is_prime(n):
        return False
    rev_n = int(str(n)[::-1])
    if n == rev_n:
        return False
    return is_prime(rev_n)

def find_emirps(min_num, max_num):
    emirps = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_num = {executor.submit(
            is_emirp, num): num for num in range(min_num, max_num + 1)}
        for future in concurrent.futures.as_completed(future_to_num):
            num = future_to_num[future]
            if future.result():
                emirps.append(num)
    return emirps

while True:
    emirps = []
    for n in range(min_num, max_num+1):
        if is_emirp(n):
            emirps.append(n)
            print("Emirps:", emirps)

        x, y = [], []
        for n in emirps:
            x.append(n)
            y.append(int(str(n)[::-1]))

            plt.scatter(x, y, s=10, c='blue')
            plt.xlabel('Emirp Numbers')
            plt.ylabel('Emirp Reversed Numbers')
            plt.title('Emirp Numbers Plot')
            plt.show()
        
            go = input(f"Want another go? Y/N").lower()
        if go == 'y':
            while True:
            # your code here
                min_num = int(input("Enter the minimum number: "))
                max_num = int(input("Enter the maximum number: "))
                find_emirps(min_num, max_num)
        emirps = []
        for n in range(min_num, max_num+1):
            if is_emirp(n):
                emirps.append(n)
                print("Emirps:", emirps)

        x, y = [], []
        for n in emirps:
            x.append(n)
            y.append(int(str(n)[::-1]))

            plt.scatter(x, y, s=10, c='blue')
            plt.xlabel('Emirp Numbers')
            plt.ylabel('Emirp Reversed Numbers')
            plt.title('Emirp Numbers Plot')
            plt.show()
else: 
    exit()

