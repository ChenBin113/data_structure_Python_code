import time


def cock_one():
    start_time = time.time()

    for m in range(0, 101):
        for n in range(0, 101):
            for k in range(0, 301):
                if m + n + k == 100 and 5*m + 3*n + k/3 == 100:
                    print("{0} - {1} - {2}".format(m, n, k))
    end_time = time.time()
    print("CostTimes: {0}".format(end_time - start_time))


def cock_two():
    start_time = time.time()
    for m in range(0, 21):
        for n in range(0, 34):
            for k in range(0, 101):
                if m + n + k == 100 and 5*m + 3*n + k/3 == 100:
                    print("{0} - {1} - {2}".format(m, n, k))
    end_time = time.time()
    print( "CostTimes: {0}".format(end_time - start_time))


def cock_three():
    start_time = time.time()
    for m in range(0, 201):
        for n in range(0, 334):
            for k in range(0, 1001):
                if m + n + k == 1000 and 5*m + 3*n + k/3 == 1000:
                    print("{0} - {1} - {2}".format(m, n, k))
    end_time = time.time()
    print( "CostTimes: {0}".format(end_time - start_time))


if __name__ == "__main__":
    cock_one()
    cock_two()
    cock_three()
