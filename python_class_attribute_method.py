#定義類別、與類別屬性(封裝在類別中的變數和函式)
#定義一個類別IO，有兩個屬性 supportedSrcs 和 read
class IO:
    supportedSrcs=["console", "file"]
    def read(src):
        if src not in IO.supportedSrcs:
            print("Not Supported")
        else:
            print("Read from", src)
# #使用類別
print(IO.supportedSrcs)
IO.read("file")
IO.read("internet")


# #Point 實體物件的設計: 平面座標上的點
class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y
# #建立實體物件
# #建立時，可直接傳入參數資料
# #建立實體物件，並取得實體屬性資料
# #建立第一個實體物件
p1=Point(3,4)
print(p1.x, p1.y)
# #建立第二個實體物件
p2=Point(5,6)
print(p2.x, p2.y)


# #FullName 實體物件的設計: 分開紀錄姓、明資料的全名
class FullName:
    def __init__(self, first, last):
        self.first=first
        self.last=last
name1=FullName("C.W.", "Peng")
print(name1.first, name1.last)
name2=FullName("T.Y", "Lin")
print(name2.first, name2.last)


class Point:
#     #定義初始化函式
    def __init__(self, x, y):
        self.x=x
        self.y=y
#     #建立第一個實體方法
    def show(self):
        print(self.x, self.y)
#     #建立第二個實體方法
    def distance(self, targetX, targetY):
        return(((self.x-targetX)**2)+((self.y-targetY)**2))**0.5

# #建立實體物件
p1=Point(3,4)
p1.show()#呼叫實體方法/函式

# #呈現第二個實體方法/函式
result=p1.distance(0,0)#計算座標3,4和座標0,0之間的距離
print(result)

#File 實體物件的設計: 包裝檔案讀取的程式
class File:
    #定義初始化函式
    def __init__(self, name):
        self.name=name
        self.file=None #尚未開啟檔案:初期式None
    #建立第一個實體方法
    def open(self):
        self.file=open(self.name, mode="r", encoding="utf-8")
    #建立第二個實體方法
    def read(self):
        return self.file.read()

#讀取第一個檔案
f1=File("data1.txt")
f1.open()#呼叫實體方法/函式
data=f1.read()
print(data)

#讀取第二個檔案
f2=File("data2.txt")
f2.open()#呼叫實體方法/函式
data=f2.read()
print(data)
