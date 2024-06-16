a_math, a_eng = map(int, input().split())
b_math, b_eng = map(int, input().split())

if (b_math > a_math) or (b_math == a_math and b_eng > a_eng):
    print("B")
else:
    print("A")