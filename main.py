text = input()
# Count word frequencies and print each in first-seen order
count = {}
for word in text.split():
  count[word] = count.get(word,0) + 1
for k,y in count.items():
  print(f"{k} {y}")