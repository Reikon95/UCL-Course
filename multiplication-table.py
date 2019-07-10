numbers = []
def fill_numbers(max_val):
  for val in range(1, (max_val + 1)):
    numbers.append(val)

fill_numbers(10)

print(numbers)
#generates the list of numbers

def multiples():
  for elem in numbers:
    i = 0
    while i < numbers[-1]:
      i += 1
      print((elem * i), end=' ') #end makes it horizontal


multiples()
#nested loop to do the actual maths
