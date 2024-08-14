import random
import subprocess
import math

b = []
with open("breakdown.txt",'r',encoding='utf-8') as gets:
    b = gets.read().splitlines()


def swap(i1,i2):
    b[i1], b[i2] = b[i2], b[i1]


def heapify():
    index1 = random.randint(0,len(b) - 1)
    parentindex = math.floor((index1 - 1) / 2)
    parentindex = max(0,parentindex)
    print("child: ", b[index1])
    print("parent: ", b[parentindex])
    res = input("type 1 to swap parent with child: ")
    if res == "1":
       swap(index1,parentindex)
    if res == "output":
        with open("breakdown.txt",'w',encoding='utf-8') as put:
                put.write("\n".join(b))
                put.close()
    if res == "tierify":
         c = []
         for index, value in enumerate(b):
              layer = math.floor(math.log2(index + 1))
              c.append([layer,value])
         with open("output.txt",'w',encoding='utf-8') as put:
                put.write("\n".join(c))
                put.close()


while True:
    heapify()