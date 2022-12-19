# coding: utf8
import math
from ascii_codes import ascii_dict
from random import choice

with open('opentext.txt', "r", encoding="utf-8") as f:
    opentext = f.read()
    opentext = opentext.replace('ё', 'е')


p = int(input("Simple number\n"))
q = int(input("Simple number\n"))
#opentext = input("Your Opentext\n")
binr = list(opentext)


def found_exp():
    global f
    all_exps = []
    for e in range(2, f)[:1000]:
        if math.gcd(f, e) == 1:
            all_exps.append(e)
            # print(all_exps)
    return choice(all_exps)


def pow(x, pow, mod):
    res = 1
    powRes = 0
    while powRes < pow:
        powRes1 = 2
        res1 = x
        while powRes + powRes1 <= pow:
            res1 = (res1 * res1) % mod
            powRes1 *= 2
        powRes1 //= 2
        res = (res * res1) % mod
        powRes += powRes1
    return res % mod


# алгоритм евклида
def evklidv(a, b):
    global f
    i = 1
    y2 = 0
    y1 = 1
    while (a != 0) & (b != 0):
        q = a // b
        r = a % b
        y = y2 - (q * y1)
        a = b
        b = r
        y2 = y1
        y1 = y
        i += 1
    if y2 < 0:
        y2 += f
    return y2, i


# математические операции
n = p * q
print('Your n\n', n)
f = (p - 1) * (q - 1)
e = found_exp()
print('Your e\n', e)
d, m = evklidv(f, e)
print("d\n", d)

# перевод в двоичный код
bits = []
for letter in list(opentext):
    bits.append(ascii_dict[letter])
    print(''.join(bits))
binarystring = ''.join(bits)

# считаем длину блока
lenblock = math.floor(math.log(n, 2))

# подгоняем под размер кратное длине блока
i = 0
while len(binarystring) % lenblock != 0:
    binarystring = binarystring.zfill(i)
    i += 1
print(binarystring)

# Разбиваем на блоки
ssplit = list(map(''.join, zip(*[iter(binarystring)] * lenblock)))
print(ssplit)

# переводим в десятичную СС
ssplit = [int(block, 2) for block in ssplit]
print(ssplit)

# считаем М и переводим в двоичную СС
ssplit = [bin((num ** e) % n)[2:].zfill(lenblock + 1) for num in ssplit]
print(ssplit)

# Разбиваем на 8 блоков
ssplit = ''.join(ssplit)
print(ssplit)
k = 0
while len(ssplit) % 8 != 0:
    ssplit = ssplit.zfill(k)
    k += 1
print(ssplit)

encodenum = list(map(''.join, zip(*[iter(ssplit)] * 8)))
print(encodenum)

# переопределяем значения
print([list(ascii_dict.keys())[list(ascii_dict.values()).index(i)] for i in encodenum])
encode_text = ''.join([list(ascii_dict.keys())[list(ascii_dict.values()).index(i)] for i in encodenum])
print(encode_text)

with open('encoded_text.txt', "w", encoding="utf-8") as f:
    f.write(encode_text.encode("utf-8").decode('utf-8'))
