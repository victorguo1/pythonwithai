    # crypto/dataservice.py 
import requests
import pandas as pd

# Crypto Currency
def get_cypto_data(cypto_currency, market,API_KEY):
    # Get Crypto Currency
    
    if market == "USD":
        urlkey = "CAD"
    else:
        urlkey = market
    url = 'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_WEEKLY&interval=5min&symbol=' + cypto_currency + '&market=' + urlkey + '&apikey=' + API_KEY
    print(url)
    r = requests.get(url)
    dataIntraday = r.json()
    #print(dataIntraday)

    return dataIntraday['Time Series (Digital Currency Weekly)']

def convert_to_df_crypto(data,market):
    print(f"convert_to_df_crypto {market}")
    """Convert the result JSON in pandas dataframe"""
    df = pd.DataFrame.from_dict(data, orient='index')
    df = df.reset_index()

    #Rename columns
    if market == "USD":
        colums = {
            "index": "date", 
            "1b. open (USD)": "open",
            "2b. high (USD)": "high", 
            "3b. low (USD)": "low", 
            "4b. close (USD)": "close"
        }
    else:
        colums = {
            "index": "date", 
            f"1a. open ({market})": "open",
            f"2a. high ({market})": "high", 
            f"3a. low ({market})": "low", 
            f"4a. close ({market})": "close"
        }

    df = df.rename(index=str, columns=colums)
    #Checks
    df.head()
    df.info()

    #Change to datetime
    df['date'] = pd.to_datetime(df['date'])

    #Sort data according to date
    df = df.sort_values(by=['date'])

    #Change the datatype
    df.open = df.open.astype(float)
    df.high = df.high.astype(float)
    df.low = df.low.astype(float)
    df.close = df.close.astype(float)

    #Checks
    df.head()
    df.info()

    return df