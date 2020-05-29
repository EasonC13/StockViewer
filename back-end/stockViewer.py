import configparser

config = configparser.ConfigParser()
config.read('./security.ini')

import alpaca_trade_api as tradeapi
from fastapi import FastAPI, Depends, HTTPException, status, File, UploadFile, HTTPException, Query, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import uvicorn
import time

api_key = config["DEFAULT"]['api_key']
api_secret = config["DEFAULT"]['api_secret']
base_url = config["DEFAULT"]['base_url']

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Stocks = {}
class Stock:
    def __init__(self, info, time = None):
        self.info = info
        if time:
            self.time = time
        else:
            import time
            self.time = time.time()
    def onTime(self):
        if time.time() - self.time > 600:
            return False
        return True

@app.get("/alpaca/{stock_id_list}/{timeframe}")
async def barrs(stock_id_list,timeframe,limit = 20):#token: str = Depends(oauth2_scheme)):
    if timeframe not in ['minute','1Min','5Min','15Min','day','1D']:
        timeframe = "day"
        
    api = tradeapi.REST(api_key,api_secret,base_url,api_version='v2')
    account = api.get_account()

    stock_id_list = stock_id_list.replace(">","").split("<")
    stock_id_list = [i.upper() for i in stock_id_list]

    if len(stock_id_list[1:]) > int(limit):
        return {"Query_Limit":"Exceeded Query Limit"}

    data = dict()
    for stock in stock_id_list[1:]: 
        try:
            if stock in Stocks and Stocks[stock].onTime():
                data[stock] = Stocks[stock].info
            else:
                print("Updating stock: %s"%stock)
                bar = api.get_barset(stock,timeframe,limit=2)
                STD = (bar[stock][1].c - bar[stock][0].c)/ bar[stock][1].c
                data[stock] = dict()
                data[stock]["ID"] = stock
                data[stock]["SDT"] = STD
                data[stock]["Price_Now"] = bar[stock][-1].c
                Stocks[stock] = Stock(data[stock])
        except IndexError as e:
            return {"Query Error":"one of your queried stocks does not exist"}
        except Exception as e:
            print(e)
            return e
            #return {"Timeframe Error":{"please choose":{'minute','1Min','5Min','15Min','day','1D'}}}
            
        

    return data

