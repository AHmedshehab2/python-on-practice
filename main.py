n = int(input())
students = {}
for i in range(n):
    name,grade = input().split()
    students[name]=grade
    
from collections import defaultdict

group = defaultdict(list)

for name , grade in students.items():
    group[grade].append(name)

for key ,val in dict(group).items():
    print(f"{key}: {', '.join(val)}")