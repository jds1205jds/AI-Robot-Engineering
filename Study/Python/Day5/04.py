def test() :
  print("첫줄입니다")
  try :
    print("try구문입니다")
    return
    print("try구문 뒤입니다")
  except :
    print("except구문입니다")
  else :
    print("else 구문입니다")
  finally :
    print("finally구문입니다")

  print("test()마지막줄입니다")

test()

#출력
# 첫줄입니다
# try구문입니다
# fianlly구문입니다

# return을 사용하면 중간에 탈출가능 하지만 파이널리 구문은 무조건 출력
