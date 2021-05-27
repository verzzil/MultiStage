import random

products = ['vodka', 'bread', 'fat', 'potato', 'apple', 'mamba', 'water']
baskets = 10
arr = []
support = 3
countarr = [0] * len(products)
hash_buckets = []
hash_buckets2 = []
del1 = []
del2 = []


def hash1(hash_buck):
    for i in range(len(products)):
        a = []
        for j in buckets:
            for k in j:
                if ((k[0] + k[1]) % len(products)) == i:
                    if not a.__contains__(k):
                        a.append(k)
        hash_buck.append(a)


def hash2(hash_buck):
    for i in range(len(products)):
        a = []
        for j in buckets:
            for k in j:
                if ((k[0] + 2 * k[1]) % len(products)) == i:
                    if not a.__contains__(k):
                        a.append(k)
        hash_buck.append(a)


def del_hash(mas, hash_buckets):
    for i in mas:
        for j in hash_buckets:
            for k in j:
                if k == i:
                    j.remove(i)


def hash_bucketsf(hash_buckets, result):
    for i in hash_buckets:
        for j in i:
            for k in j:
                if not result.__contains__(products[k]):
                    result.append(products[k])
            if not result.__contains__([products[j[0]], products[j[1]]]):
                result.append([products[j[0]], products[j[1]]])


for i in range(baskets):
    a = random.sample(range(len(products)), random.randint(2, 5))
    a.sort()
    arr.append(a)
    for j in a:
        countarr[j] += 1

buckets = []
for i in arr:
    bucket = []
    for j in range(len(i) - 1):
        for k in range(j + 1, len(i)):
            bucket.append([i[j], i[k]])
    buckets.append(bucket)

hash1(hash_buckets)
hash2(hash_buckets2)
for i in hash_buckets:
    count = 0
    for j in i:
        for k in buckets:
            for p in k:
                if p == j:
                    count += 1
    if count < support:
        for j in i:
            del2.append(j)
            del1.append(j)
del_hash(del1, hash_buckets)
del_hash(del2, hash_buckets2)
del2 = []

for i in hash_buckets2:
    count = 0
    for j in i:
        for k in buckets:
            for p in k:
                if p == j:
                    count += 1
    if count < support:
        for j in i:
            del2.append(j)
del_hash(del2, hash_buckets2)
del1 = []
del2 = []

for i in range(len(countarr)):
    if countarr[i] < support:
        for j in hash_buckets:
            for k in j:
                if k[0] == i or k[1] == i:
                    del1.append(k)
        for j in hash_buckets2:
            for k in j:
                if k[0] == i or k[1] == i:
                    del2.append(k)
del_hash(del1, hash_buckets)
del_hash(del2, hash_buckets2)

result = []
hash_bucketsf(hash_buckets, result)
hash_bucketsf(hash_buckets2, result)

for i in products:
    print(i)
print()
for i in result:
    print(i)
