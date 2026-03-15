def 나누기(a, b):
    if b == 0:
        raise ZeroDivisionError("0으로 나눌 수 없습니다.")
    return a / b

try:
    나누기(10, 0)
except ZeroDivisionError as e:
    print(f"경고: {e}")
