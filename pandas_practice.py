# #載入 Pandas 模組
# import pandas as pd
# # 建立 單維 Series
# data=pd.Series([20,10,15])
# # 基本 Series 操作
# print(data)
# print("Max", data.max())
# print("Median", data.median())
# data=data*2
# print(data)

# data=data==20
# print(data)


# #建立 雙維 DataFrame
# data=pd.DataFrame({
#     "name":["Amy", "John", "Bob"],
#     "salary":[30000, 50000, 40000]
# })
# #基本 DataFrame 操作
# # print(data)
# #取得特定欄位
# # print(data["salary"])
# #取得特定的列
# print(data)
# print("================")
# print(data.iloc[1]) # 印出第二列


# # 載入pandas模組
# import pandas as pd
# #定義 data 資料，建立 單唯資料 Series
# data1=pd.Series([5,4,-2,3,7], index=["a","b","c","d","e"])

# data2=pd.Series(["您好", "Python", "Pandas"])

# # 觀察資料
# print(data1)
# print("資料型態", data1.dtype)
# print("資料數量", data1.size)
# print("資料索引", data1.index)

# # 取得資料: 根據訊續、根據索引
# print(data1[2], data1[0])
# print(data1["e"], data1["d"])

# #數字運算: 基本、統計、順序
# print("最大值", data1.max())
# print("總和", data1.sum())
# print("標準差", data1.std())
# print("中位數", data1.median())
# print("最大的三個數", data1.nlargest(3)) # data1.nsmallest(2) 最小兩個數

# #字串運算: 基本、串接、搜尋、取代

# print(data2.str.lower()) # 全部變小寫
# print(data2.str.len()) # 算出每個字串的長度
# print(data2.str.cat(sep="-")) # 串接字串，可以自訂串接的符號
# print(data2.str.contains("好")) #判斷每個字串是否包含特定的字元
# print(data2.str.replace("您好", "Hello")) #字串取代

#註解
#篩選資料 condition
#引入pandas模組
import pandas as pd
# #篩選練習 - Series
# data = pd.Series([30,15,20])
# condition = data>18
# # print(condition)
# filteredData=data[condition]
# print(filteredData)

# data = pd.Series(["您好","Python","Pandas"])
# condition=data.str.contains("P")
# print(condition)
# filteredData=data[condition]
# print(filteredData)

#篩選練習 - DataFrame
data=pd.DataFrame({
    "name":["Amy", "Bob", "Charles"],
    "salary":[30000, 50000, 40000]
})
# print(data)
# condition=data["salary"]>=40000
condition=data["name"]=="Amy"
print(condition)
filteredData=data[condition]
print(filteredData)
