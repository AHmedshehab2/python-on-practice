def is_plaindorme(x :str)-> bool:
    left, right = 0, len(s) - 1

    while left < right:
        # Move pointers inward if non-alphanumeric
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True
            


x = input()
if is_plaindorme == True:
  print("yes")
else :
  print("no")