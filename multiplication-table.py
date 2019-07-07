def multiplication(max_num, num):
  while num < (max_num + 1):
    print(num * max_num)
    num += 1

multiplication(10, 1)

def multitable(max_num, num):
  while max_num > (num - 1):
    multiplication(max_num, num)
    max_num -= 1

multitable(10, 1)

#generates the values correctly (function within function), need to sort into a table somehow
