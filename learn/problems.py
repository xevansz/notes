def daily_temperatures(x: list) -> list:
  result = []
  for i in range(len(x)):
    step = 0
    found = False
    for j in range(i + 1, len(x)):
      step += 1
      if x[j] > x[i]:
        result.append(step)
        found = True
        break
    if not found:
      result.append(0)
  return result


def daily(x: list[int]) -> list:
  n = len(x)
  result = [0] * n
  stack = []  # stores indices

  for i in range(n):
    print(f"Day {i}, Temp {x[i]}, Stack {stack}" + "Iteration start")
    while stack and x[i] > x[stack[-1]]:
      print(f"Day {i}, Temp {x[i]}, Stack {stack}" + "In the loop")
      prev = stack.pop()
      result[prev] = i - prev
    stack.append(i)
    print(f"Day {i}, Temp {x[i]}, Stack {stack}" + "End of itertaion")

  print(result)


if __name__ == "__main__":
  # raw = input("Give input: ")
  # x = list(map(int, raw.split(",")))
  # 30,38,30,36,35,40,28

  daily([30, 38, 30, 36, 35, 40, 28])
  # result = daily(x)
  # print(result)
