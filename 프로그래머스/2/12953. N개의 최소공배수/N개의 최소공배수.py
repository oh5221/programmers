from math import gcd
def solution(arr):
    num = arr[0]
    for a in arr[1:]:
        num = num * a // gcd(num, a)
    return num