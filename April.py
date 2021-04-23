import unittest
import sqlite3
import json
import re
import os
import requests
import datetime

#
# Name: April Tsai
# Who did you work with: Morgan Bo
#

API_KEY = "4M1NX09GXDYK7C0S"

def read_cache(CACHE_FILE):
    """
    This function reads from the JSON cache file and returns a dictionary from the cache data.
    If the file doesn’t exist, it returns an empty dictionary.
    """

    dir_path = os.path.dirname(os.path.realpath(__file__))
    CACHE_FILE = dir_path + '/' + "cache_stocks.json"
    try:
        cache_file = open(CACHE_FILE, 'r', encoding="utf-8") 
        cache_contents = cache_file.read()  
        CACHE_DICTIONARY = json.loads(cache_contents) 
        cache_file.close() 
        return CACHE_DICTIONARY
    except:
        CACHE_DICTIONARY = {}
        return CACHE_DICTIONARY

def write_cache(CACHE_FILE, CACHE_DICTIONARY):
    """
    This function encodes the cache dictionary (CACHE_DICT) into JSON format and
    writes the JSON to the cache file (CACHE_FNAME) to save the search results.
    """

    with open(CACHE_FILE, "w") as outfile:
        json.dump(CACHE_DICTIONARY, outfile)    

def create_request_url(symbol):
    """
    This function prepares and returns the request url for the API call.

    The documentation of the API parameters is at https://www.alphavantage.co/documentation/ 

    """

    base_url = "https://www.alphavantage.co/"
    url = base_url + f"query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=full&apikey={API_KEY}"

    return url

def get_data_from_cache(symbol, CACHE_FILE):

    url = create_request_url(symbol)
    dictionary = read_cache(CACHE_FILE)

    if url in dictionary:
        print("Using cache for {}".format(symbol))
        return dictionary[url]
    else:
        print("Fetching data for {}".format(symbol))
        try:
            response = requests.get(url)
            stocks_data = response.text

            if response.status_code == 200:
                dictionary[url] = json.loads(stocks_data)
                write_cache(CACHE_FILE, dictionary)
                return dictionary[url]
            else:
                print("Stock Data Not Found")
                return None
        except:
            print("Exception")
            return None   
    
def read_data_from_file(filename):
    full_path = os.path.join(os.path.dirname(__file__), filename)
    f = open(full_path)
    file_data = f.read()
    f.close()
    json_data = json.loads(file_data)
    return json_data

def set_up_database(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

def set_up_tesla_stocks_table(data, cur, conn):
    cur.execute("CREATE TABLE IF NOT EXISTS Tesla_Stock (date TEXT PRIMARY KEY, open REAL, high REAL, low REAL, close REAL, volume REAL)")
    conn.commit()

    tsla_url = create_request_url("TSLA")

    keys = data[tsla_url]["Time Series (Daily)"].keys()
    time_frame = []

    regex = r"^2020|^2021"
    
    for key in keys:
        if re.findall(regex, key):
            time_frame.append(key)
    
    time_frame.reverse()

    remove_time = []

    cur.execute("SELECT COUNT(*) FROM Tesla_Stock")
    row_count = int(cur.fetchone()[0])
    print(row_count)

    stop_program = 0

    for index in range(25):
        
        if row_count == 0:
            open_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["1. open"]
            high_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["2. high"]
            low_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["3. low"]
            close_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["4. close"]
            volume = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["5. volume"]
            
            cur.execute("INSERT OR IGNORE INTO Tesla_Stock (date, open, high, low, close, volume) VALUES(?, ?, ?, ?, ?, ?)", (time_frame[index], open_price, high_price, low_price, close_price, volume))

            conn.commit()
        
        if row_count == 25:
            index = index + 25
            open_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["1. open"]
            high_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["2. high"]
            low_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["3. low"]
            close_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["4. close"]
            volume = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["5. volume"]
            
            cur.execute("INSERT OR IGNORE INTO Tesla_Stock (date, open, high, low, close, volume) VALUES(?, ?, ?, ?, ?, ?)", (time_frame[index], open_price, high_price, low_price, close_price, volume))

            conn.commit()

        if row_count == 50:
            index = index + 50
            open_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["1. open"]
            high_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["2. high"]
            low_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["3. low"]
            close_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["4. close"]
            volume = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["5. volume"]
            
            cur.execute("INSERT OR IGNORE INTO Tesla_Stock (date, open, high, low, close, volume) VALUES(?, ?, ?, ?, ?, ?)", (time_frame[index], open_price, high_price, low_price, close_price, volume))

            conn.commit()
        
        if row_count == 75:
            index = index + 75
            open_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["1. open"]
            high_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["2. high"]
            low_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["3. low"]
            close_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["4. close"]
            volume = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["5. volume"]
            
            cur.execute("INSERT OR IGNORE INTO Tesla_Stock (date, open, high, low, close, volume) VALUES(?, ?, ?, ?, ?, ?)", (time_frame[index], open_price, high_price, low_price, close_price, volume))

            conn.commit()
        
        if row_count == 100:
            index = index + 100
            open_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["1. open"]
            high_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["2. high"]
            low_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["3. low"]
            close_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["4. close"]
            volume = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["5. volume"]
            
            cur.execute("INSERT OR IGNORE INTO Tesla_Stock (date, open, high, low, close, volume) VALUES(?, ?, ?, ?, ?, ?)", (time_frame[index], open_price, high_price, low_price, close_price, volume))

            conn.commit()
        
        if row_count == 125:
            index = index + 125
            open_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["1. open"]
            high_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["2. high"]
            low_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["3. low"]
            close_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["4. close"]
            volume = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["5. volume"]
            
            cur.execute("INSERT OR IGNORE INTO Tesla_Stock (date, open, high, low, close, volume) VALUES(?, ?, ?, ?, ?, ?)", (time_frame[index], open_price, high_price, low_price, close_price, volume))

            conn.commit()
        
        if row_count == 150:
            index = index + 150
            open_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["1. open"]
            high_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["2. high"]
            low_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["3. low"]
            close_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["4. close"]
            volume = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["5. volume"]
            
            cur.execute("INSERT OR IGNORE INTO Tesla_Stock (date, open, high, low, close, volume) VALUES(?, ?, ?, ?, ?, ?)", (time_frame[index], open_price, high_price, low_price, close_price, volume))

            conn.commit()
        
        if row_count == 175:
            index = index + 175
            open_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["1. open"]
            high_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["2. high"]
            low_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["3. low"]
            close_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["4. close"]
            volume = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["5. volume"]
            
            cur.execute("INSERT OR IGNORE INTO Tesla_Stock (date, open, high, low, close, volume) VALUES(?, ?, ?, ?, ?, ?)", (time_frame[index], open_price, high_price, low_price, close_price, volume))

            conn.commit()
        
        if row_count == 200:
            index = index + 200
            open_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["1. open"]
            high_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["2. high"]
            low_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["3. low"]
            close_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["4. close"]
            volume = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["5. volume"]
            
            cur.execute("INSERT OR IGNORE INTO Tesla_Stock (date, open, high, low, close, volume) VALUES(?, ?, ?, ?, ?, ?)", (time_frame[index], open_price, high_price, low_price, close_price, volume))

            conn.commit()
        
        if row_count == 225:
            index = index + 225
            open_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["1. open"]
            high_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["2. high"]
            low_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["3. low"]
            close_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["4. close"]
            volume = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["5. volume"]
            
            cur.execute("INSERT OR IGNORE INTO Tesla_Stock (date, open, high, low, close, volume) VALUES(?, ?, ?, ?, ?, ?)", (time_frame[index], open_price, high_price, low_price, close_price, volume))

            conn.commit()
        
        if row_count == 250:
            index = index + 250
            open_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["1. open"]
            high_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["2. high"]
            low_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["3. low"]
            close_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["4. close"]
            volume = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["5. volume"]
            
            cur.execute("INSERT OR IGNORE INTO Tesla_Stock (date, open, high, low, close, volume) VALUES(?, ?, ?, ?, ?, ?)", (time_frame[index], open_price, high_price, low_price, close_price, volume))

            conn.commit()
        
        if row_count == 275:
            index = index + 275
            open_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["1. open"]
            high_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["2. high"]
            low_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["3. low"]
            close_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["4. close"]
            volume = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["5. volume"]
            
            cur.execute("INSERT OR IGNORE INTO Tesla_Stock (date, open, high, low, close, volume) VALUES(?, ?, ?, ?, ?, ?)", (time_frame[index], open_price, high_price, low_price, close_price, volume))

            conn.commit()
        
        if row_count == 300:
            index = index + 300
            open_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["1. open"]
            high_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["2. high"]
            low_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["3. low"]
            close_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["4. close"]
            volume = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["5. volume"]
            
            cur.execute("INSERT OR IGNORE INTO Tesla_Stock (date, open, high, low, close, volume) VALUES(?, ?, ?, ?, ?, ?)", (time_frame[index], open_price, high_price, low_price, close_price, volume))

            conn.commit()
        
        if row_count == 325:
            index = index + 325
            open_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["1. open"]
            high_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["2. high"]
            low_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["3. low"]
            close_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["4. close"]
            volume = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["5. volume"]
            
            cur.execute("INSERT OR IGNORE INTO Tesla_Stock (date, open, high, low, close, volume) VALUES(?, ?, ?, ?, ?, ?)", (time_frame[index], open_price, high_price, low_price, close_price, volume))

            conn.commit()
            stop_program += 1

            if stop_program == 3:
                break

def set_up_gamestop_stocks_table(data, cur, conn):
    cur.execute("CREATE TABLE IF NOT EXISTS Gamestop_Stock (date TEXT PRIMARY KEY, open REAL, high REAL, low REAL, close REAL, volume REAL)")
    conn.commit()

    gme_url = create_request_url("GME")

    keys = data[gme_url]["Time Series (Daily)"].keys()
    time_frame = []

    regex = r"^2020|^2021"
    
    for key in keys:
        if re.findall(regex, key):
            time_frame.append(key)
    
    time_frame.reverse()

    remove_time = []

    cur.execute("SELECT COUNT(*) FROM Gamestop_Stock")
    row_count = int(cur.fetchone()[0])
    print(row_count)

    stop_program = 0

    for index in range(25):
        
        if row_count == 0:
            open_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["1. open"]
            high_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["2. high"]
            low_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["3. low"]
            close_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["4. close"]
            volume = data[gme_url]["Time Series (Daily)"][time_frame[index]]["5. volume"]
            
            cur.execute("INSERT OR IGNORE INTO Gamestop_Stock (date, open, high, low, close, volume) VALUES(?, ?, ?, ?, ?, ?)", (time_frame[index], open_price, high_price, low_price, close_price, volume))

            conn.commit()
        
        if row_count == 25:
            index = index + 25
            open_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["1. open"]
            high_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["2. high"]
            low_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["3. low"]
            close_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["4. close"]
            volume = data[gme_url]["Time Series (Daily)"][time_frame[index]]["5. volume"]
            
            cur.execute("INSERT OR IGNORE INTO Gamestop_Stock (date, open, high, low, close, volume) VALUES(?, ?, ?, ?, ?, ?)", (time_frame[index], open_price, high_price, low_price, close_price, volume))

            conn.commit()

        if row_count == 50:
            index = index + 50
            open_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["1. open"]
            high_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["2. high"]
            low_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["3. low"]
            close_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["4. close"]
            volume = data[gme_url]["Time Series (Daily)"][time_frame[index]]["5. volume"]
            
            cur.execute("INSERT OR IGNORE INTO Gamestop_Stock (date, open, high, low, close, volume) VALUES(?, ?, ?, ?, ?, ?)", (time_frame[index], open_price, high_price, low_price, close_price, volume))

            conn.commit()
        
        if row_count == 75:
            index = index + 75
            open_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["1. open"]
            high_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["2. high"]
            low_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["3. low"]
            close_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["4. close"]
            volume = data[gme_url]["Time Series (Daily)"][time_frame[index]]["5. volume"]
            
            cur.execute("INSERT OR IGNORE INTO Gamestop_Stock (date, open, high, low, close, volume) VALUES(?, ?, ?, ?, ?, ?)", (time_frame[index], open_price, high_price, low_price, close_price, volume))

            conn.commit()
        
        if row_count == 100:
            index = index + 100
            open_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["1. open"]
            high_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["2. high"]
            low_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["3. low"]
            close_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["4. close"]
            volume = data[gme_url]["Time Series (Daily)"][time_frame[index]]["5. volume"]
            
            cur.execute("INSERT OR IGNORE INTO Gamestop_Stock (date, open, high, low, close, volume) VALUES(?, ?, ?, ?, ?, ?)", (time_frame[index], open_price, high_price, low_price, close_price, volume))

            conn.commit()
        
        if row_count == 125:
            index = index + 125
            open_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["1. open"]
            high_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["2. high"]
            low_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["3. low"]
            close_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["4. close"]
            volume = data[gme_url]["Time Series (Daily)"][time_frame[index]]["5. volume"]
            
            cur.execute("INSERT OR IGNORE INTO Gamestop_Stock (date, open, high, low, close, volume) VALUES(?, ?, ?, ?, ?, ?)", (time_frame[index], open_price, high_price, low_price, close_price, volume))

            conn.commit()
        
        if row_count == 150:
            index = index + 150
            open_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["1. open"]
            high_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["2. high"]
            low_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["3. low"]
            close_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["4. close"]
            volume = data[gme_url]["Time Series (Daily)"][time_frame[index]]["5. volume"]
            
            cur.execute("INSERT OR IGNORE INTO Gamestop_Stock (date, open, high, low, close, volume) VALUES(?, ?, ?, ?, ?, ?)", (time_frame[index], open_price, high_price, low_price, close_price, volume))

            conn.commit()
        
        if row_count == 175:
            index = index + 175
            open_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["1. open"]
            high_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["2. high"]
            low_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["3. low"]
            close_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["4. close"]
            volume = data[gme_url]["Time Series (Daily)"][time_frame[index]]["5. volume"]
            
            cur.execute("INSERT OR IGNORE INTO Gamestop_Stock (date, open, high, low, close, volume) VALUES(?, ?, ?, ?, ?, ?)", (time_frame[index], open_price, high_price, low_price, close_price, volume))

            conn.commit()
        
        if row_count == 200:
            index = index + 200
            open_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["1. open"]
            high_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["2. high"]
            low_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["3. low"]
            close_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["4. close"]
            volume = data[gme_url]["Time Series (Daily)"][time_frame[index]]["5. volume"]
            
            cur.execute("INSERT OR IGNORE INTO Gamestop_Stock (date, open, high, low, close, volume) VALUES(?, ?, ?, ?, ?, ?)", (time_frame[index], open_price, high_price, low_price, close_price, volume))

            conn.commit()
        
        if row_count == 225:
            index = index + 225
            open_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["1. open"]
            high_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["2. high"]
            low_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["3. low"]
            close_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["4. close"]
            volume = data[gme_url]["Time Series (Daily)"][time_frame[index]]["5. volume"]
            
            cur.execute("INSERT OR IGNORE INTO Gamestop_Stock (date, open, high, low, close, volume) VALUES(?, ?, ?, ?, ?, ?)", (time_frame[index], open_price, high_price, low_price, close_price, volume))

            conn.commit()
        
        if row_count == 250:
            index = index + 250
            open_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["1. open"]
            high_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["2. high"]
            low_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["3. low"]
            close_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["4. close"]
            volume = data[gme_url]["Time Series (Daily)"][time_frame[index]]["5. volume"]
            
            cur.execute("INSERT OR IGNORE INTO Gamestop_Stock (date, open, high, low, close, volume) VALUES(?, ?, ?, ?, ?, ?)", (time_frame[index], open_price, high_price, low_price, close_price, volume))

            conn.commit()
        
        if row_count == 275:
            index = index + 275
            open_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["1. open"]
            high_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["2. high"]
            low_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["3. low"]
            close_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["4. close"]
            volume = data[gme_url]["Time Series (Daily)"][time_frame[index]]["5. volume"]
            
            cur.execute("INSERT OR IGNORE INTO Gamestop_Stock (date, open, high, low, close, volume) VALUES(?, ?, ?, ?, ?, ?)", (time_frame[index], open_price, high_price, low_price, close_price, volume))

            conn.commit()
        
        if row_count == 300:
            index = index + 300
            open_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["1. open"]
            high_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["2. high"]
            low_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["3. low"]
            close_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["4. close"]
            volume = data[gme_url]["Time Series (Daily)"][time_frame[index]]["5. volume"]
            
            cur.execute("INSERT OR IGNORE INTO Gamestop_Stock (date, open, high, low, close, volume) VALUES(?, ?, ?, ?, ?, ?)", (time_frame[index], open_price, high_price, low_price, close_price, volume))

            conn.commit()
        
        if row_count == 325:
            index = index + 325
            open_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["1. open"]
            high_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["2. high"]
            low_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["3. low"]
            close_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["4. close"]
            volume = data[gme_url]["Time Series (Daily)"][time_frame[index]]["5. volume"]
            
            cur.execute("INSERT OR IGNORE INTO Gamestop_Stock (date, open, high, low, close, volume) VALUES(?, ?, ?, ?, ?, ?)", (time_frame[index], open_price, high_price, low_price, close_price, volume))

            conn.commit()
            stop_program += 1

            if stop_program == 3:
                break

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    CACHE_FILE = dir_path + '/' + "cache_stocks.json"
    stocks = ["TSLA", "GME"]
    [get_data_from_cache(stock, CACHE_FILE) for stock in stocks]
    json_data = read_data_from_file("cache_stocks.json")
    cur, conn = set_up_database('stocks.db')
    # set_up_tesla_stocks_table(json_data, cur, conn)
    set_up_gamestop_stocks_table(json_data, cur, conn)



if __name__ == "__main__":
    main()
    

