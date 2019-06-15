si=input()
letter_flag = False
number_flag = False
for b in si:
  if b.isalpha():
      letter_flag = True
  if b.isdigit():
      number_flag = True
if letter_flag and number_flag:
      print('Yes')
else:
  print('No')
