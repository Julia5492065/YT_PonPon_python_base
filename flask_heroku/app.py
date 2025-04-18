from flask import Flask
app=Flask(__name__) #__name__代表目前執行模組

@app.route("/") #函式的裝飾 (Decorator): 已函是為基礎，提供附加的功能
def home():
    return "Hello Flask2"

@app.route("/test") #代表我們要處理的網站路徑
def test():
    return "This is test"

if __name__=="__main__": #如果以主程式執行
    app.run() #立刻啟動伺服器