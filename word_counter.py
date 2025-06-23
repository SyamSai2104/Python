file = input("Enter a file name: ")
wordcount = dict()
with open(file, 'r') as f:
    for line in f:
        line = line.rstrip()
        words = line.split()
        for word in words:
            wordcount[word] = wordcount.get(word, 0) + 1
temp = list()
for k, v in wordcount.items():
    newt = (v,k)
    temp.append(newt)
    temp.sort(reverse=True)
for k,v in temp[:5]:
    print(v, k)