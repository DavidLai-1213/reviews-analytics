data = []
count = 0
with open("reviews.txt", 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        # if count % 1000 == 0:
        #     print(len(data))
print('檔案讀取完了，總共有', len(data), '筆資料')

print(data[0])


num = 0
for i in data:
    num += len(i)
print("資料的平均長度是", num/len(data))

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有', len(new), '比留言長度小於100')
print(new[0])

good = []
for d in data:
    if 'good' in d:
        good.append(d)
print("一共有", len(good), "比留言中提到good")
print(good[0])

bad =["bad" in d for d in data]
new = [d for d in data if len(d) < 100]


wc = {}
for d in data:
    words = d.split()
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1
for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])

while True:
    word = input('請問你想查甚麼字:')
    if word == 'q':
        break
    if word in wc:
        print(word, '出現過的次數:', wc[word])
    else:
        print('沒有喔')
print('感謝使用')














