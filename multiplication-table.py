#we start but creating an empty list and a loop to fill it with numbers desired, in this case 1 - 10

numbers = []

def fill_numbers(max_val):
  for val in range(1, (max_val + 1)):
    numbers.append(val)

fill_numbers(10)

print(numbers)

#now we have the numbers desired in a neat list

def multiples():
  for elem in numbers:
    i = 0
    while i < numbers[-1]:
      i += 1
      print(elem * i)


multiples()

#this second function is a nested loop, generates the multiplications of the number up to the last element of numbers, the desired max value
