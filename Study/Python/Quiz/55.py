# python if ~ elif ~else 구문을 이용해 성적입력 프로그램을 python으로 작성해 보세요. [ input(), int(), and(&&), or(||) ]
# ex) 91 A / 83 B / 77 C / 63 D / 40 F

score = int(input("성적을 입력하세요 : "))

if score > 90 and score <= 100 :
    print("A")
elif score > 80 and score <= 90 :
    print("B")
elif score > 70 and score <= 80 :           
    print("C")  
elif score > 60 and score <= 70 :
    print("D")
elif score >= 0 and score <= 60 :
    print("F")
