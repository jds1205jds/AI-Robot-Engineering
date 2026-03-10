# 2. [가변 매개변수 & 딕셔너리]
# 문제: make_profile이라는 함수를 만드세요.
# 첫 번째 매개변수로 이름을 받습니다.
# 그 뒤로 몇 개가 올지 모르는 취미들을 가변 매개변수로 받습니다.
# 최종적으로 {"name": "이름", "hobbies": ["취미1", "취미2", ...], 
# \"count": 취미갯수} 형태의 딕셔너리를 반환(return)해야 합니다.

def make_profile(name, *hobbies) :
    profile = {
        'name' : name,
        'hobbies' : list(hobbies),  # 오답 : hobbies는 튜플이므로 리스트로 변환
        'count' : len(hobbies)
    }
    return profile 
print(make_profile("daeseok", "reading", "swimming", "coding"))
