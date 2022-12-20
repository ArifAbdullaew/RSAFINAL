# coding: utf8
import math
from ascii_codes import ascii_dict


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


def splitToBlocks(textBitted, blockLength):
    # массив разбитыми по блокам текстами
    binblocksText = []
    # разворачиваем битовую строку, чтобы начать делить блоки с младших битов
    textBitted = textBitted[::-1]
    # делим битовую строку на блоки с длиной блока @blockLength
    for i in range(0, len(textBitted), blockLength):
        block = textBitted[i:i + blockLength][::-1].zfill(blockLength)
        binblocksText.append(block)

    return binblocksText


def clearArray(bin_string, null_string):
    clear_arr = []
    for val in bin_string:
        if val != null_string:
            clear_arr.append(val)

    return clear_arr


with open('encode.txt.txt', "r", encoding="utf-8") as f:
    text = f.read()
    text = text.replace('ё', 'е')

d = int(input("Your d\n"))
n = int(input("Your n\n"))
blockLength = math.floor(math.log(n, 2))

# текст в битовую последовательность
bits = []
for letter in list(text):
    bits.append(ascii_dict[letter])
binarystring = ''.join(bits)

# длина блока будет меняться в обратном порядке
blockLength += 1
# делим на блоки двоичную строку и переводим блоки в 10СС
blockSplitted = list(map(lambda x: int(x, 2), splitToBlocks(binarystring, blockLength)))[::-1]
# меняем длину блока
blockLength -= 1
# возводим в степень каждый элемент массива в степень d и переводим в двоичную СС
blocksJoined = list(map(lambda x: bin(pow(x, d, n))[2:].zfill(blockLength), blockSplitted))
blocksJoined = list(map(lambda x: bin(pow(x, d, n))[2:].zfill(blockLength), blockSplitted))
blocksJoined = ''.join(blocksJoined)


blockLength = 8
end = "".join([list(ascii_dict.keys())[list(ascii_dict.values()).index(block)] for block in
               clearArray(splitToBlocks(blocksJoined, blockLength), "00000000")])

print(end[::-1])

with open('decoded.txt', "w", encoding="utf-8") as f:
    f.write(end[::-1].encode("utf-8").decode('utf-8'))
