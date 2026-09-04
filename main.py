def is_plaindorme(x :str)-> bool:
    return x == x[::-1]


x = input()
if is_plaindorme == True:
  print("yes")
else :
  print("no")