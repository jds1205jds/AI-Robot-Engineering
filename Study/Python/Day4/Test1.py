# 1. [리스트 내포 & 문자열 처리]
# 문제: 학생들의 이름이 담긴 리스트 names = ["  kim", "lee  ", "  park  ", "choi"]가 있습니다.
# 리스트 내포를 사용하여 각 이름의 앞뒤 공백을 제거하고 이름의 길이가 3글자 이상인 사람만 대문자로 변환하여 새로운 리스트를 만드세요.

names = ["  kim", "lee  ", "  park  ", "choi"]
n1 = [name.strip().upper() for name in names if len(name.strip()) >= 3]
print(n1)
