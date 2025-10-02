# n개 중 n/2개 가져갈 수 있음
# 같은 종류 == 같은 번호
# n/2마리 선택하는 방법 중, 가장 많은 종류 가져가는 방법 -> 종류 번호 개수 return

# set(nums) 개수, n/2 개수 중 작은 거 고르면 될 듯
def solution(nums):
    answer = min(len(set(nums)), len(nums)//2)
    return answer