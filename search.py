import time


def ss(number_list, n):
    found = False
    start = time.time()
    for i in number_list:
        if i == n:
            found = True
            break
    end = time.time()
    result = end - start
    print("{} \n {} \n \n".format(found, result))

numbers = range(0, 10000000000000000)
ss(numbers, 2)
ss(numbers, 211100000)

