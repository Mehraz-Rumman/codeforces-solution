for i in range(5):
  a = input().split()
  if '1' in a:
      x, y = i, a.index('1')
      print(abs(x - 2) + abs(y - 2))

