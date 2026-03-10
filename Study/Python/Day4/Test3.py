# 3. [파일 처리 & 예외 방지]
# 문제: memo.txt라는 파일을 쓰기 모드(w)로 열어 본인의 다짐 세 줄을 적으세요.
# 반드시 with 구문을 사용해야 합니다.
# 그 후, 다시 파일을 읽기 모드(r)로 열어 각 줄 앞에 번호를 붙여 출력하세요. (예: 1. 첫 번째 줄 ...)

with open("memo.txt", "w", encoding="utf-8") as file:
    file.write("1. 운동 꾸준히 가고 건강 챙기기\n")
    file.write("2. 공부 열심히 하고 취업준비 열심해서 취업하기\n")
    file.write("3. 일본어 공부하기\n")

print("--- 나의 다짐 목록 ---") 

try:
    with open("memo.txt", "r") as file:
        lines = file.readlines() 
        for line in lines :
            print(line)
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
