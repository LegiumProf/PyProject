from functools import reduce
with open("news.txt", "r") as f:
    news = []
    for line in f.readlines():
        count = line.split()[0]
        new = []
        for i in range(1, len(line.split())):
            new.append(line.split()[i])
        news.append([int(count), new])
    print(news)
    def reduce_prov(pred, this):
        if pred[0] < this[0]:
            print(this[0], " ".join(this[1]))
            return this
        else:
            return pred
    reduce(reduce_prov, news)