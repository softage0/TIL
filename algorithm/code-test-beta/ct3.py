import math

def solution(b):
    for a in range(1, 500001):
        result = math.sqrt(pow(a, 2) + pow(b, 2))
        if result.is_integer():
            return int(result)

    return -1
    