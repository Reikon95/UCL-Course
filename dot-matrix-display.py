message = 'This is a completely relevant exercise'
display_width = 16

message_length = len(message)
curr_start = 0
print(message_length)

final = display_width
first = 0
while True:
  print(message[first:final])
  first += 1
  final += 1
  i += 1

   '''
  
  INFINITE SCROLL REPEAT
  
  '''
    
max_display = 20
beg = 0
end = max_display
display = list(message[0:max_display])
storage = list(message[(max_display + 1):len(message)])

while True:
  result = ''.join(display)
  print(result)
  # print(storage)
  storage.append(display[0])
  del display[0]
  display.append(storage[0])
  del storage[0]

    
