def get_best_point(arr, point):
    test_arr = arr[:]
    pos = 0
    left = 0
    right = 0
    while len(test_arr):
        if left <= right:
            left += test_arr.pop(0)
            pos += 1
        else:
            right += test_arr.pop()
    if left == right:
        point_left = get_best_point(arr[pos:], point)
        point_right = get_best_point(arr[:pos], point)
        if point_left >= point_right:
            point += point_left
        else:
            point += point_right
        point += 1
    return point

T = int(input())

for _ in range(T):
    N = int(input())
    A = [int(value) for value in input().split() if value != '0']
    if len(A):
        print(get_best_point(A, 0))
    else:
        print(N-1)
