# We are learning DSA
# What is Array? - A basic data structure which stores elements sequentially. It has indices so elements can be accessed randomly.
# Arrays can have 1 or more dimensions

import random

if __name__ == "__main__":
  a = [random.randint(0, 10) for _ in range(6)]
  # print(len(a))
  # 6
  print(*a)
