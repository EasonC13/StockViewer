# StockViewer 
![StockViewer](https://stockviewer.tsraise.com/featureImg.png)
> This is a Mid-Term Project of DataVisualization class at NTNU.

This Project's WebSite is avaliable on https://easonc13.github.io/StockViewer

You can also [Check the presentation's slide to get more information about this (clickable)](https://drive.google.com/file/d/129v98gWWVDxhEzZvBOJRJzP4a1oDUWDU/view?usp=sharing)

---

因為身邊有很多朋友都有在看盤，而且 Tony 有在做關於股票漲跌預測模型。

因此我們想做一個資料視覺化的網頁，讓使用者一目瞭然指定的股票的漲跌趨勢。

## 於是 StockViewer 就誕生了！

採用前後端分離的模式進行開發，後端主要由 Tony 負責建設，使用 Python 搭配 FastAPI，經過 [Alpaca API](https://pypi.org/project/alpaca-trade-api/) 抓取即時的股票資料，並作運算處理，計算出股票的漲跌幅度後，傳送至前端伺服器進行顯示。

前端主要由怡升負責建置，圓圈的大小，代表今天該股票漲跌的幅度。圓圈內的顏色，紅色代表漲，綠色代表跌（目前版本是這樣，未來考慮新增自訂顏色功能）。

使用者可以在下面新增/刪除股票，使用者指定的股票，會被記錄在 cookies 中，未來會顯示同樣的股票，也可以使用 Default 選項，清除 cookies。

目前只支援美國一些主流交易所的股票，台灣的股票還不支持。未來會考慮推出無後端版本，由前端網頁的 JavaScript 直接抓取 Alpaca API 的即時股票資料並進行運算後呈現資料。（要發PR可以發這個嗷嗷）
