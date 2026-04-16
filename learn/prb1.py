# Codeforces Round 1062 (Div 4)


def sq2(x: list) -> str:
  return "Yes" if len(set(x)) == 1 and x[0] > 0 else "No"


if __name__ == "__main__":
  n = int(input())

  if n > 0:
    for _ in range(n):
      x = list(map(int, input().split()))
      print(sq2(x))
