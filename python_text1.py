# pr=[12,60,15,70,90]
# ppr=(3,4,5)
# ppr[0]=5
# print(ppr)

data=[0,1,2,3,4,5,6,7,8,9,10]
#集合
s1={3,4,5}
s2={4,5,6,7}
# s3=s1&s2#交集
# s3=s1|s2#聯集
# s3=s1-s2#差集
# s3=s2-s1#差集
# s3=s1^s2#反交集
# print(s3)
# s=set("hello")#把字串拆解成集合
# print("H" in s)

#字典運算
# dic={"apple":"蘋果","bug":"蟲蟲"}
# dic["apple"]="小蘋果"
# print(dic["apple"])
# print("bb" not in dic)
# print(dic)
# del dic["apple"]
# print(dic)

# dic={x:x*2 for x in [3,4,5]}#從列表的資料產生字典
# print(dic)

#判斷式
# a=1
# while a<=3:
#     x=input("請輸入數字: ")
#     x=int(x)
#     if x>200:
#         print("大於100")
#     elif x>100:
#         print("大於100，小於等於200")
#     else:
#         print("小於等於100")
#     a+=1

# n1=int(input("請輸入數字一: "))
# n2=int(input("請輸入數字二: "))
# op=input("請輸入運算(+, -, *, /): ")

# if op=="+":
#     print(n1+n2)
# elif op=="-":
#     print(n1-n2)
# elif op=="*":
#     print(n1*n2)
# elif op=="/":
#     print(n1/n2)
# else:
#     print("不支援的運算")

#迴圈
# a=1
# while a<5:
#     print("蘋果"+str(a)+"號")
#     print("香蕉{}串".format(a))
#     a+=1

# for a in data:
#     print("逐一取得字串中的字元",a)

# for a in range(3,6):
#     print(a)

# sum=0
# for a in range(11):
#     if a == 5:
#         break
#     sum=sum+a
# print(sum,a)

# n=0
# for x in[0,1,2,3]:
#     if x%2==0:
#         continue
#     print(x)
#     n+=1
# print(n)

# sum=0
# for n in data:
#     sum+=n
# else:
#     print(sum)

#統整練習
#輸入數字算出整數平方根
# k=True
# while k == True:
#     n = input("輸入數字找出整數平方根: ")
#     n=int(n)
#     if (n**0.5)% 1 ==0 :
#         print(int(n**0.5))
#         k= not k
#     else:
#         print("此數字沒有整數平方根",n**0.5)
#         continue


# #定義函式
# def sayHello(n1, n2):
#     return n1*n2   
# #呼叫函式
# value=sayHello(3,4)+sayHello(5,10)
# print(value)

#程式的包裝
# def calclate(max):
#     sum=0
#     for n in range(1,max+1):
#         sum=sum+n
#     print(sum)

# calclate(10)
# calclate(20)

#參數的預設資料
# def power(base,exp=0):
#     print(base**exp)
# power(3,2)
# power(4)

#使用參數名稱對應
# def divide(n1, n2):
#     print(n1/n2)
# divide(2,4)
# divide(n2=2,n1=4)

#無限/不定參數資料
# def avg(*ns):
#     sum=0
#     for n in ns:
#         sum=sum+n
#     print(sum/len(ns))

# avg(3,4)
# avg(3,5,10)
# avg(1,4,-1,-8)

#載入內件的sys模組並取得資訊
# import sys as system
# print(system.platform)
# print(system.maxsize)

#建立 geometry 模組. 載入使用
# import geometry
# result = geometry.distance(1,1,5,5)
# print(result)
# result = geometry.slope(1,2,5,6)
# print(result)

#調整搜尋模組的路徑
# import sys
# sys.path.append("modules")#在模組的搜尋路徑列表中【新增路徑】
# print(sys.path)#印出模組的搜尋路徑列表
# print("----------------------------------")

# import geometry
# print(geometry.distance(1,1,5,5))





#隨機模組
import random
#隨機選取
# data=random.choice([1,3,5,7,10])
# data=random.sample([1,2,3],2)
#隨機調換順序(洗牌)
# data=[1,5,8,20]
# random.shuffle(data)
# print(data)
#隨機取得亂數
# data=random.random()#0~1之間的隨機亂數
# print(data)
# data=random.uniform(0.0, 1.0)
# print(data)
#取得常態分配亂數
#平均數100, 標準差10，得到的資料多數在90~110之間
# data=random.normalvariate(100,10)
# print(data)

#統計模組
import statistics as stat
#平均數、中位數、標準數、常態分配
# data=stat.mean([1,4,5,8])
# data=stat.median([1,2,3,4,5,8,100])
# data=stat.stdev([1,2,3,4,5,8,10])
# print(data)