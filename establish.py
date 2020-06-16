#生成word2index，index2word，文本列表，文本索引列表
def preprocess(lis):
    lis = [elem.strip().split('\t') for elem in lis]
    text = []
    sentence = []
    wordlis = []
    word2index = {'<BOS>':0, '<EOS>':1}
    for e in lis:
        if e == ['']:
            text.append(['<BOS>']+sentence+['<EOS>'])
            sentence = []
        else:
            sentence.append(e[1])
            wordlis.append(e[1])
    wordset = set(wordlis)
    tag = 2
    for word in wordset:
        if word2index.get(word, -1)==-1:
            word2index[word] = tag
            tag+=1
    index2word = dict()
    for k, v in word2index.items():
        index2word[v] = k
    return word2index, index2word, text, [[word2index[word] for word in sent] for sent in text]

#统计二元词频,采用+1平滑
def statistic(indextext, V):
    #将indextext分割成二元组
    bigramindex = []
    for sent in indextext:
        for i in range(len(sent)-1):
            bigramindex.append(sent[i:i+2])

    #统计二元组得到共现矩阵,最后一个词表示未登录词
    coexist = [[0 for i in range(V+1)] for _ in range(V+1)]
    for elem in bigramindex:
        coexist[elem[0]][elem[1]] += 1

    #将共现矩阵转化为概率转移矩阵，并引入+1平滑
    transfer = []
    for i in range(V+1):
        s = sum(coexist[i])+V+1
        transfer.append([(num+1)/s for num in coexist[i]])
    return transfer

if __name__ == "__main__":
    with open('data/train.conll', 'r', encoding='UTF-8') as f1:
        lis = f1.readlines()
    word2index, index2word, text, indextext = preprocess(lis)
    transfer = statistic(indextext, len(word2index))
    #存储一下word2index，与transfer
    with open('data/transfermatrix', 'w', encoding = 'UTF-8') as f2:
        for i in transfer:
            for j in i:
                f2.write(str(j))
                f2.write(' ')
            f2.write('\n')
    with open('data/worddict', 'w', encoding='UTF-8') as f3:
        for key, val in word2index.items():
            f3.write(key)
            f3.write(' ')
            f3.write(str(val))
            f3.write('\n')

