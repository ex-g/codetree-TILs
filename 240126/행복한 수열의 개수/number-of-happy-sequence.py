n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
result = 0

# 가로부터 한 줄씩 꺼내오기
# 첫 숫자랑 둘째 숫자랑 같으면 cnt+1, 아니면 cnt 1로 초기화
# cnt가 m이상이면 result += 1

for i in range(n):
    cnt = 1
    for j in range(n-1):
        if arr[i][j] == arr[i][j+1]:
            cnt += 1
        else:
            cnt = 1
        if cnt >= m:
            result += 1
            break

# 세로도 똑같이 진행

for i in range(n):
    cnt = 1
    for j in range(n-1):
        if arr[j][i] == arr[j+1][i]:
            cnt += 1
        else:
            cnt = 1
        
        if cnt >= m:
            result += 1
            break

if n == 1 and m == 1:
    print(2)
else:
    print(result)