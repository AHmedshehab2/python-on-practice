set1 = set(map(int , input().split()))
set2 = set(map(int , input().split()))
intersection= set1 & set2

print(" ".join(map(str, intersection)))