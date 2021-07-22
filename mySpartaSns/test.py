import sys
sys.setrecursionlimit(10**5)

n = int(input())
arr = [0 for _ in range(n+1)]
arr[1] = 1

if n == 1:
  arr.append(2)
  arr.append(4)
elif n == 2:
  arr[2] = 2
  arr.append(4)
else:
  arr[2] = 2
  arr[3] = 4

def case(n):
  result = 0
  if n <= 3:
    result = arr[n]
  else:
    if arr[n-1] !=0 and arr[n-2] !=0 and arr[n-3] !=0:
      result = arr[n-1] + arr[n-2] + arr[n-3]
    else:
      result = case(n-1) + case(n-2) + case(n-3)
      arr[n] = result
  return result%1000007

print(case(n))