from math import log
#计算文本困惑度
def perplexity(bitext, transfer):
    w = 0
    p = 0
    for sent in bitext:
        for bigram in sent:
            w += 1
            p += log(transfer[bigram[0]][bigram[1]], 2)
    H = -p/w
    return 2**H

if __name__ == "__main__":
    with open('data/transfermatrix', 'r', encoding='UTF-8') as f1:
        transfer = [[float(num) for num in elem.strip().split()] for elem in f1.readlines()]
    with open('data/worddict', 'r', encoding='UTF-8') as f2:
        worddict = [elem.strip().split(' ') for elem in f2.readlines()]
    word2index = dict()
    for elem in worddict:
        word2index[elem[0]] = int(elem[1])
    with open('data/dev.conll', 'r', encoding='UTF-8') as f3:
        lis = f3.readlines()
    lis = [elem.strip().split('\t') for elem in lis]
    text = []
    sent = []
    for elem in lis:
        if elem == ['']:
            text.append(sent)
            sent = []
        else:
            sent.append(elem[1])
    indextext = [[word2index.get(word, -1) for word in sent] for sent in text]
    # 将indextext分解为二元组
    bigramtext = []
    for indexsent in indextext:
        bisent = [[0, indexsent[0]]]
        for i in range(len(indexsent)-1):
            bisent.append(indexsent[i:i+2])
        bisent.append([indexsent[-1], 1])
        bigramtext.append(bisent)

    print(perplexity(bigramtext, transfer))