string_1, string_2=[str(x) for x in input('Enter two strings: ').split(', ')]
output = ""

if len(string_1)>len(string_2):
  for i in range(len(string_2)):
    output+=string_1[i]
    output+=string_2[i]
    if len(string_2)*2==len(output):
      break
  print(output+string_1[len(string_2):])
elif len(string_1)<len(string_2):
  for i in range(len(string_1)):
    output+=string_1[i]
    output+=string_2[i]
    if len(string_1)*2==len(output):
      break
  print(output+string_2[len(string_1):])