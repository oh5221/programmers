# n마리 중 n/2마리를 가져갈 수 있음. 같은 종류의 포켓몬은 같은 번호
# 최대한 많은 종류를 포함한 n/2가 되어야 함. 그럴 때의 폰켓몬 종류 번호의 개수 return

# ponketmons = len(nums) // 2를 저장해 두고
# set(nums)를 해서 len(set(nums))가 ponketmons랑 동일하거나 크면 return ponketmons
# 더 작으면 return len(set(nums))
def solution(nums):
    ponketmons = len(nums) // 2
    set_nums = set(nums)
    
    if len(set_nums) >= ponketmons :
        return ponketmons
    else:
        return len(set_nums)