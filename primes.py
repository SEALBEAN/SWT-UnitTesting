import math


def primes(aFloat: float, bFloat: float):
    assert aFloat <= 1000000, "a must <= 1000000"
    assert bFloat <= 1000000, "b must <= 1000000"
    #   swap a,b if a > b
    # Round a,b to integer

    cFloat: float
    if (aFloat > bFloat):
        cFloat = aFloat
        aFloat = bFloat
        bFloat = cFloat

    a = int(math.ceil(aFloat))
    b = int(math.floor(bFloat))
    if (b < 2):
        return "Không có số nguyên tố nào nằm trong đoạn [" + str(aFloat) + ", " + str(bFloat) + "]"

#   if a < 0 => the number of primes [a,b] = [0,b]
    if (a < 0):
        a = 0

#     -----Using sieve of Eratosthenes (sàng nguyên tố) to find all primes between a and b-----
#     Step 1: Create p array with (b + 1) elements, mark 0, 1 isn't a prime
    mark = [True] * (b + 1)
    mark[0] = mark[1] = False

#     Step 2: remove all multiples by making p[<multiples>] = False
    for i in range(2, round(math.sqrt(b + 1)) + 1):
        for j in range(i*i, b + 1, i):
            mark[j] = False

#     Step 3: Check and return primes
    count = 0
    for i in range(a, b + 1):
        if mark[i]:
            count = count + 1

#     (Count == 0): doesn't have primes
    if count == 0:
        return "Không có số nguyên tố nào nằm trong đoạn [" + str(aFloat) + ", " + str(bFloat) + "]"
#      Else: have primes
    else:
        result = str("")
        for i in range(a, b + 1, 1):
            if mark[i] == True:
                result = result + str(i) + ", "
        return result.rstrip(", ")


#     -------------------MAIN FUNCTION--------------------------
if __name__ == "__main__":
    aFloat = float(input("input a: "))
    bFloat = float(input("input b: "))
    print(primes(aFloat, bFloat))
