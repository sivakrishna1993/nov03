# def centuryFromYear(year):
#     return year // 100 + 1
# print(centuryFromYear(2010))


# def allLongestStrings(inputArray):
#     m = max(len(s) for s in inputArray)
#     mm = [s for s in inputArray if len(s) == m]
#     return mm
# print(allLongestStrings(["aba", "aa", "ad", "vcd", "aba"]))

# def commonCharacterCount(s1, s2):
#     com = [min(s1.count(i),s2.count(i)) for i in set(s1)]
#     return sum(com)
# print(commonCharacterCount(s1 = "aabcc",s2 = "adcaa"))

# def isLucky(n):
#     d = list(map(int,str(n)))
#     print(d)
#     m = int(len(d) / 2)
#     return sum(d[:m]) == sum(d[m:])
# print(isLucky('1230'))

# n = '1230'
# s=t=0
# d = list(n)
# print(d)
# print(len(d))
# for i in range(int(len(d)/2)):
#     s =s+ int(d[i])
# print(s)
# for j in range(int(len(d)/2),len(d)):
#     t = t+int(d[j])
# print(t)
# if s == t:
#     print("is lucky")
# else:
#     print("not lucky")


# s1 = 'siva'
# s2 = 'krishna'
# l =[]
# for i in range(int(s1,s2)):
#     a = s1.count(i)
#     b = s2.count(i)
#     c = min(a,b)
#     l.append(c)
#
# print(sum(l))


# def sortByHeight(a):
#     l = sorted([i for i in a if i > 0])
#     for n,i in enumerate(a):
#         if i == -1:
#             l.insert(n,i)
#     return l
# print(sortByHeight([-1, 150, 190, 170, -1, -1, 160, 180]))


# n = 1230
# print(type(n))
# a = str(n)
# print(type(a))
#
# print(list(map(int,str(a))))
# b = int(len(a)/2)
# print(b)
# if (sum(a[:b]) == sum(a[b:])):
#     print("True")
# else:
#     print("False")


# l =[(1,'one'),(2,'two'),(3,'three')]
# a = dict(l)
# print(a)
#
# s1= 'siva'
# s2= 'visa'
# if sorted(s1)==sorted(s2):
#     print("yes")
# else:
#     print("no")
#
# l1 = [1,2,3,4]
# b =tuple(l1)
# print(b)
#
# d = {1:'one',2:'two',3:'three'}
# print(d)


# import pandas as pd
# df = pd.read_csv("/home/krish/Desktop/TTTsiva.csv")
# # df1 = pd.DataFrame(df)
# print(df.dtypes)
# print(type(df))






# s = 'human'
# print(list(s))
#
# l=[]
# for i in 'human':
#     l.append(i)
# print(l)
#
# a = [i for i in 'human']
# print(a)
#
# letters = list(map(lambda x: x, 'human'))
# print(letters)
from tokenize import String

a = [1,2,3,4,5]
# a.pop(3)
# del a[0]
# print(a)
#
# x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# a1 = sorted(x)
# print(a1.items)
# b = iter(a)
# print(next(b))
#
#
# def fun():
#     n=1
#     while n <=10:
#         sq= n*n
#         yield sq
#         n+=1
# print(list(fun()))


# def add1(a,b):
#     return a*10+b*10
# print(add1(2,3))
import re
# l = 'hello world'
# print(re.sub(r'\s+',"",l))
# print(l.replace("",""))
# a =""
# for i in l:
#     if i in " ":
#         pass
#     else:
#         a=a+i
# print(len(a))
#
# aa=float("-11.24e8")
# print(aa)
#
# bb= round(15.56,2)
# print(bb)
#
# def cube(n):
#     print(n**3)
# a = cube(3)
# print(a)

# """print a string untill the condition is satisfied"""
#
# num = 1
# while num < 10:
#     print("Hello siva")
#     num += 1
#
#
# import timeit
#
# def for_loop():
#     for number in range(10):
#         sum = 1+2
#         print(sum)
# timeit.timeit(for_loop)


# a = 10
# b=repr(a)
# print(type(b))
#
# import datetime
# date = datetime.datetime.now()
# print(str(date))
# print(repr(date))

# a = set(['one',2,3,1,2,3,'two',4,5])
# print(a)
#
# b = ['toto','12','pswd']
# c ='::'.join(b)
# print(c)


from collections import Counter
# a = 'hello world'
# print(len(a))
# print(a.count('o'))
# b =Counter(a)
# print(b)
# a = Counter("geeksforgeeks")
# for i in a.elements():
#     print ( i, end = " ")
# print()
# k=""
# for i in a:
#     if i in " ":
#         pass
#     else:
#         k+=i
# print(len(k))


# a = ('1','-29','-56','726')
# b = [int(x) for x in a]
# print(b)
# print(a[-4:-1:2])


# a =[1,2,3,4,5,6,7]
# del a[0]
# a[0]=8
# a.remove(4)
# a.pop()
# print(a)

# x = abs(-11.33)
# print(x)
# y = abs(19+23j)
# print(y)
# z = abs(22.33)
# print(z)

# s = 0
# i = 1
# while i<=100:
#     s += i**2
#     i +=1
# print(s)

# s = 'siva krishna'
# b = 0
# for i in s:
#     if i == 'a':
#         b += 1
# print(b)

# lst = [11,18,9,12,23,4,17]
# cnt = []
# for i in range(len(lst)):
#     v = lst[i]
#     # print(v)
#     if v > 15:
#         cnt.append(v)
# print(cnt)


# d1 = {1:'one',2:'two',3:'three'}
# # d1.update(4='four')
# d1.update(a = 'for')
# print(d1)

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
#
# x = car.get("price",15000)
# print(x)

# def main():
#     f = open("C:/Users/SIVAKRISHNA/Desktop/siva.txt","w+")
#     for i in range(10):
#         f.write("this is line %d\r\n"%(i+1))
#     f.close()
#     print(f)
# if __name__=="__main__":
#     main()


# f = open("C:/Users/SIVAKRISHNA/Desktop/siva1.txt","w+")
# for i in range(10):
#     f.write("this is line %d\r\n"%(i+1))
# f.close()
# print(f)

# d = {1:1,2:2,3:3}
# print(d.update())
# d[4]=4
# print(d)
# d1={6:5}
# d.update(a=6)
# print(d)


# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern triangle
# def triangle(n):
#     k = 2 * n - 2
#     for i in range(0, n):
#         for j in range(0, k):
#             print(end=" ")
#         k = k - 1
#         for j in range(0, i + 1):
#             print("* ", end="")
#         print("\r")
# n = 5
# triangle(n)



# def alphabeticShift(inputString):
#     y = chr(ord(inputString)+1)
#     return y
# print(alphabeticShift('s'))

import requests

import requests

req = requests.get('http://www.edureka.co/')

# req.encoding  # returns 'utf-8'
# print(req.json())
# req.status_code  # returns 200
# req.elapsed  # returns datetime.timedelta(0, 1, 666890)
# print(req.json())
# req.url  # returns 'https://edureka.co/'
# print(req.json())
# req.history
# # returns [&lt;Response [301]&gt;, &lt;Response [301]&gt;]
#
# req.headers['Content-Type']
# # returns 'text/html; charset=utf-8'
# print(req.json())


req = requests.post('https://en.wikipedia.org/w/index.php', data = {'search':'Nanotechnology'})
req.raise_for_status()
with open('Nanotechnology.html', 'wb') as fd:
    for chunk in req.iter_content(chunk_size=50000):
        fd.write(chunk)
