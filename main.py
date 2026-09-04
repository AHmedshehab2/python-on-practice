set1 = set(map(int , input().split()))
set2 = set(map(int , input().split()))
intersection= set1 & set2
for i in intersection:
    print(i)