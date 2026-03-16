# Q2) 두 조건 중 하나라도 참이면 통과, or 사용금지, 중첩 if문으로 해결할 것
# 3의 배수이거나 5의 배수이면 "OK" 아니면 "NO"를 출력하라.

num = int(input("숫자 입력 : "))

if num % 3 == 0 :
    print("OK")
elif num % 5 == 0 :
    print("OK")
else :
    print("NO")
