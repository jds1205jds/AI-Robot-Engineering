# 2차원 리스트의 원소의 합계를 구하세요. 단, for 이중반복 구문을 꼭 사용하세요.

array = [[1,2,3],[4,5,6],[7,8,9]]
sum=0

for i in array:
    for j in i:
        sum+=j


print(sum)
