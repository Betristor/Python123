import jieba
txt = open("names.txt","r",encoding="utf-8").read()
words = jieba.lcut(txt)
count = {}
for word in words:
    if word == " " or word == "," or word == "\n":
        continue
    else:
        count[word] = count.get(word,0) + 1
items = list(count.items())
items.sort(key = lambda x:x[1] ,reverse = True)
print(items[0])