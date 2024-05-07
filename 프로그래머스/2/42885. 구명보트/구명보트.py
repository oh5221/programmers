from collections import deque
def solution(people, limit):
    people = deque(sorted(people, reverse=True))
    print(people)
    # [8, 7, 5, 5], 10 / [8, 7, 5], 10
    
    num = 0
    
    while people:
        if len(people) > 1 and people[0] + people[-1] <= limit:
            num += 1
            people.popleft()
            people.pop()
        else:
            num += 1
            people.popleft()
        
    
    return num