def is_plaindorme(x :str)-> bool:
    return x == x[::-1]


x = input().split()
if is_plaindorme(x) == True:
  print("yes")
else :
  print("no")