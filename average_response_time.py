with open('response_time.txt') as lines_doc:
  lines = lines_doc.readlines()
  a = []
  b = []
  i = 0
  for time in lines:
    if i % 2 == 0:
      a.append(time)
    else:
      b.append(time)
    i += 1  
def average(lst):
  counter = 0
  total = 0
  for time in lst:
    counter += float(time)
    total += 1
  print(counter)
  print(total)
  mean = (counter/total)
  print(mean)

average(a)
average(b)
