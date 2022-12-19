import math
from ascii_codes import ascii_dict



d = 1637  # int(input("Your d\n")) дефолт параметры с лекции
n = 21583  # int(input("Your n\n"))
#тут я почти везде принты ставлю чтобы понять че за суета
lenblockdefault = math.floor(math.log(n, 2))

#лог + 1
lenblock = lenblockdefault + 1
opentext = "↕:♂♣2š"  # input("Your Opentext\n")
binr = list(opentext)
print(binr)
# тут я перевожу символы из аскии
bits = []
for letter in list(opentext):
    bits.append(ascii_dict[letter])
    print(''.join(bits))
binarystring = ''.join(bits)
print(binarystring)

#разбиваю на 8 блоков
ssplit = list(map(''.join, zip(*[iter(binarystring)] * 8)))
print(ssplit)

#
lenstr = (math.floor((len(binarystring) / lenblock)) * lenblock) # тут я пытался сделать так, чтобы размер блока делился на логарифм
binarystring = binarystring[len(binarystring) - lenstr:]
print(binarystring)

#разбиваю на блоки
ssplit = list(map(''.join, zip(*[iter(binarystring)] * lenblock)))
print(ssplit)

#перевожу блоки в десятичную сс
ssplit = [int(block, 2) for block in ssplit]
print(ssplit)

# считаем С
ssplit = [bin((num ** d) % n)[2:].zfill(lenblockdefault) for num in ssplit]
print(ssplit)

ssplit = ''.join(ssplit)
print(ssplit)

#разбиваю на блоки
ssplit = list(map(''.join, zip(*[iter(ssplit)] * 8)))
print(ssplit)

#финалочка
print([list(ascii_dict.keys())[list(ascii_dict.values()).index(i)] for i in ssplit])
decode_text = ''.join([list(ascii_dict.keys())[list(ascii_dict.values()).index(i)] for i in ssplit])
print(decode_text)

# i = 0
# while len(binarystring) % lenblock != 0:
#     binarystring[i:]
#     i+=1
