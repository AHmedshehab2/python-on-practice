def is_plaindorme(x :str)-> bool:
  cleaned = "".join(char.lower() for char in x if char.isalnum())
    
  return cleaned == cleaned[::-1]

x = input()
if is_plaindorme(x) == True:
  print("yes")
else :
  print("no")