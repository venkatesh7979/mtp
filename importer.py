# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 12:43:25 2022

@author: Venkatesh Surampally

Use this to get financial data.
"""




class import_data:
    def __init__(self,start_date="2018-01-02",end_date="2022-07-01"):

        self.start_date = start_date
        self.end_date = end_date
        
    def financial_closing_data(self):
        import pandas as pd
        import yfinance as yf
        
        start = self.start_date
        end = self.end_date
        
        currency_tickers = ['INR=X','JPY=X','EUR=X','NZD=X','RUB=X','CNY=X']
        crypto = ['BTC-USD','ETH-USD','DOGE-USD','BNB-USD']
        us_treasury_bonds = ['^IRX','^FVX','^TNX','^TYX']
        futures = ['GC=F','SI=F','CL=F','BZ=F','NQ=F','^BSESN','^NSEI','^NYA','^GSPC','^DJI','^IXIC','000001.SS','399001.SZ']
        
        #Filling the null_values
        df_value = pd.DataFrame()
        df_value['Date'] = yf.Ticker('BTC-USD').history(start=start, end=end).index
        df_change = pd.DataFrame()
        df_change['Date'] = yf.Ticker('BTC-USD').history(start=start, end=end).index
        df_value.set_index('Date',inplace=True)
        df_change.set_index('Date',inplace=True)
        #print('Variable','Number of Records',sep='\t\t\t')
        #print('Expected',df_value.shape[0],sep='\t\t\t')
        for ticker in (currency_tickers+crypto+us_treasury_bonds+futures):
            data=yf.Ticker(ticker).history(start=start, end=end)
            #print(ticker,data.shape[0],sep='\t\t\t')
            for i,index in enumerate(df_value.index.tolist()):
                if index not in data.index.tolist():
                    data.loc[index] = data.loc[df_value.index.tolist()[i-1]]
            data.sort_index(axis=0,inplace=True)
            df_value[ticker] = data['Close']
            
        return df_value