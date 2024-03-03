import re
def solution(new_id):
    print("1. 대문자를 소문자로 치환")
    new_id = new_id.lower()
    print(new_id)
    
    print("2. 알파벳 소문자, 숫자, -, _, . 제외한 모든 문자 제거")
    new_id = re.sub('[^0-9a-z-_.]', '', new_id)
    print(new_id)
    
    print("3. 마침표가 2번 이상 연속되면 한 개로 치환")
    new_id = re.sub(r'[.]{2,}', '.', new_id)
    print(new_id)
    
    print("4. 마침표가 처음이나 끝에 위치하면 제거")
    new_id = new_id.strip('.')
    print(new_id)
    
    print("5. 빈 문자열이면 a 대입")
    if new_id == '':
        new_id += "a"
    print(new_id)
    
    print("6. 길이 16자 이상이면 15자까지만")
    if len(new_id) >= 16:
        for i in range(15):
            new_id = new_id[:15]
        print(new_id)
        
        print("6-1. 마침표가 끝에 있으면 제거")
        if new_id[-1] == '.':
            new_id = new_id[:-1]
        print(new_id)
        
    
    print("7. 2글자 이하면 문자수 3 될 때까지 반복")
    while len(new_id) <= 2:
        new_id += new_id[-1]      
    print(new_id)
    
    return new_id