import jieba
def getText():
    txt = open("hamlet.txt","r").read()
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        txt.replace(ch," ")
    return txt

hamlettxt = getText()
words = hamlettxt.split()
counts = {}
for word in words:
    counts[word] = counts.get(word,0) + 1
items = list(counts.items())
items.sort(key = lambda x:x[1],reverse= True)
for i in range(10):
    word,count = items[i]
    print("{0:<10}{1:>5}".format(word,count))

txt2 = open("threekingdoms.txt","r",encoding="utf-8").read()
words2 = jieba.lcut(txt2)
counts2 = {}
for word2 in words2:
    if len(word2) == 1:
        continue
    else:
        counts2[word2] = counts2.get(word2,0) + 1
items2 = list(counts2.items())
items2.sort(key = lambda x:x[1],reverse=True)
for i in range(20):
    word2,count2 = items2[i]
    print("{0:<10}{1:>5}".format(word2,count2))