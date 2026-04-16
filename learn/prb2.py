def equal_chars(x: str, y: str) -> str:
  return "YES" if sorted(x) == sorted(y) else "NO"


if __name__ == "__main__":
  n = int(input())
  for _ in range(n):
    input()
    x, y = input().split(" ")
    print(equal_chars(x, y))
