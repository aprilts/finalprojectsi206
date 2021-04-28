import unittest
import sqlite3
import requests
import json
import re
import os
import matplotlib.pyplot as plt

#The following functions retrieve data from APIs

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

def get_stocks_data_from_cache(symbol, CACHE_FILE):

    url = create_request_url(symbol)
    dictionary = read_cache(CACHE_FILE)

    if url in dictionary:
        return dictionary[url]
    else:
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

def get_covid_data(group_in, state_in, sex_in):
    base_url = "https://data.cdc.gov/resource/9bhg-hcku.json?$where=`group`={}&state={}&sex={}"

    group = group_in
    state = state_in
    sex = sex_in

    request_url = base_url.format(group, state, sex)
   
    r = requests.get(request_url)
    data = r.text
    dict_list = json.loads(data)
    
    return dict_list

def read_data_from_file(filename):
    full_path = os.path.join(os.path.dirname(__file__), filename)
    f = open(full_path)
    file_data = f.read()
    f.close()
    json_data = json.loads(file_data)
    return json_data

# The following functions sets up the database and inserts data
def set_up_database(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

def get_stock_dates(symbol, data):
    url = create_request_url(symbol)
    keys = data[url]["Time Series (Daily)"].keys()
    
    time_frame = []

    regex = r"^2020|^2021"
    
    for key in keys:
        if re.findall(regex, key):
            time_frame.append(key)
    
    time_frame.reverse()

    return time_frame

def set_up_tesla_stocks_table(data, cur, conn, time_frame):
    cur.execute("CREATE TABLE IF NOT EXISTS Tesla_Stock (date TEXT PRIMARY KEY, open REAL, high REAL, low REAL, close REAL, volume REAL)")
    conn.commit()

    tsla_url = create_request_url("TSLA")

    cur.execute("SELECT COUNT(*) FROM Tesla_Stock")
    row_count = int(cur.fetchone()[0])

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
        
        elif row_count == 25:
            index = index + 25
            open_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["1. open"]
            high_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["2. high"]
            low_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["3. low"]
            close_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["4. close"]
            volume = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["5. volume"]
            
            cur.execute("INSERT OR IGNORE INTO Tesla_Stock (date, open, high, low, close, volume) VALUES(?, ?, ?, ?, ?, ?)", (time_frame[index], open_price, high_price, low_price, close_price, volume))

            conn.commit()

        elif row_count == 50:
            index = index + 50
            open_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["1. open"]
            high_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["2. high"]
            low_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["3. low"]
            close_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["4. close"]
            volume = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["5. volume"]
            
            cur.execute("INSERT OR IGNORE INTO Tesla_Stock (date, open, high, low, close, volume) VALUES(?, ?, ?, ?, ?, ?)", (time_frame[index], open_price, high_price, low_price, close_price, volume))

            conn.commit()
        
        elif row_count == 75:
            index = index + 75
            open_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["1. open"]
            high_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["2. high"]
            low_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["3. low"]
            close_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["4. close"]
            volume = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["5. volume"]
            
            cur.execute("INSERT OR IGNORE INTO Tesla_Stock (date, open, high, low, close, volume) VALUES(?, ?, ?, ?, ?, ?)", (time_frame[index], open_price, high_price, low_price, close_price, volume))

            conn.commit()
        
        elif row_count == 100:
            index = index + 100
            open_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["1. open"]
            high_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["2. high"]
            low_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["3. low"]
            close_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["4. close"]
            volume = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["5. volume"]
            
            cur.execute("INSERT OR IGNORE INTO Tesla_Stock (date, open, high, low, close, volume) VALUES(?, ?, ?, ?, ?, ?)", (time_frame[index], open_price, high_price, low_price, close_price, volume))

            conn.commit()
        
        elif row_count == 125:
            index = index + 125
            open_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["1. open"]
            high_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["2. high"]
            low_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["3. low"]
            close_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["4. close"]
            volume = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["5. volume"]
            
            cur.execute("INSERT OR IGNORE INTO Tesla_Stock (date, open, high, low, close, volume) VALUES(?, ?, ?, ?, ?, ?)", (time_frame[index], open_price, high_price, low_price, close_price, volume))

            conn.commit()
        
        elif row_count == 150:
            index = index + 150
            open_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["1. open"]
            high_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["2. high"]
            low_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["3. low"]
            close_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["4. close"]
            volume = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["5. volume"]
            
            cur.execute("INSERT OR IGNORE INTO Tesla_Stock (date, open, high, low, close, volume) VALUES(?, ?, ?, ?, ?, ?)", (time_frame[index], open_price, high_price, low_price, close_price, volume))

            conn.commit()
        
        elif row_count == 175:
            index = index + 175
            open_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["1. open"]
            high_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["2. high"]
            low_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["3. low"]
            close_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["4. close"]
            volume = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["5. volume"]
            
            cur.execute("INSERT OR IGNORE INTO Tesla_Stock (date, open, high, low, close, volume) VALUES(?, ?, ?, ?, ?, ?)", (time_frame[index], open_price, high_price, low_price, close_price, volume))

            conn.commit()
        
        elif row_count == 200:
            index = index + 200
            open_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["1. open"]
            high_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["2. high"]
            low_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["3. low"]
            close_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["4. close"]
            volume = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["5. volume"]
            
            cur.execute("INSERT OR IGNORE INTO Tesla_Stock (date, open, high, low, close, volume) VALUES(?, ?, ?, ?, ?, ?)", (time_frame[index], open_price, high_price, low_price, close_price, volume))

            conn.commit()
        
        elif row_count == 225:
            index = index + 225
            open_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["1. open"]
            high_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["2. high"]
            low_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["3. low"]
            close_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["4. close"]
            volume = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["5. volume"]
            
            cur.execute("INSERT OR IGNORE INTO Tesla_Stock (date, open, high, low, close, volume) VALUES(?, ?, ?, ?, ?, ?)", (time_frame[index], open_price, high_price, low_price, close_price, volume))

            conn.commit()
        
        elif row_count == 250:
            index = index + 250
            open_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["1. open"]
            high_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["2. high"]
            low_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["3. low"]
            close_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["4. close"]
            volume = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["5. volume"]
            
            cur.execute("INSERT OR IGNORE INTO Tesla_Stock (date, open, high, low, close, volume) VALUES(?, ?, ?, ?, ?, ?)", (time_frame[index], open_price, high_price, low_price, close_price, volume))

            conn.commit()
        
        elif row_count == 275:
            index = index + 275
            open_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["1. open"]
            high_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["2. high"]
            low_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["3. low"]
            close_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["4. close"]
            volume = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["5. volume"]
            
            cur.execute("INSERT OR IGNORE INTO Tesla_Stock (date, open, high, low, close, volume) VALUES(?, ?, ?, ?, ?, ?)", (time_frame[index], open_price, high_price, low_price, close_price, volume))

            conn.commit()
        
        elif row_count == 300:
            index = index + 300
            open_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["1. open"]
            high_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["2. high"]
            low_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["3. low"]
            close_price = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["4. close"]
            volume = data[tsla_url]["Time Series (Daily)"][time_frame[index]]["5. volume"]
            
            cur.execute("INSERT OR IGNORE INTO Tesla_Stock (date, open, high, low, close, volume) VALUES(?, ?, ?, ?, ?, ?)", (time_frame[index], open_price, high_price, low_price, close_price, volume))

            conn.commit()
        
        elif row_count == 325:
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
        else: 
            print("DONE RUNNING TESLA DATA") 
            break

def set_up_gamestop_stocks_table(data, cur, conn, time_frame):
    cur.execute("CREATE TABLE IF NOT EXISTS Gamestop_Stock (date TEXT PRIMARY KEY, open REAL, high REAL, low REAL, close REAL, volume REAL)")
    conn.commit()

    gme_url = create_request_url("GME")

    cur.execute("SELECT COUNT(*) FROM Gamestop_Stock")
    row_count = int(cur.fetchone()[0])

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
        
        elif row_count == 25:
            index = index + 25
            open_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["1. open"]
            high_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["2. high"]
            low_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["3. low"]
            close_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["4. close"]
            volume = data[gme_url]["Time Series (Daily)"][time_frame[index]]["5. volume"]
            
            cur.execute("INSERT OR IGNORE INTO Gamestop_Stock (date, open, high, low, close, volume) VALUES(?, ?, ?, ?, ?, ?)", (time_frame[index], open_price, high_price, low_price, close_price, volume))

            conn.commit()

        elif row_count == 50:
            index = index + 50
            open_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["1. open"]
            high_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["2. high"]
            low_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["3. low"]
            close_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["4. close"]
            volume = data[gme_url]["Time Series (Daily)"][time_frame[index]]["5. volume"]
            
            cur.execute("INSERT OR IGNORE INTO Gamestop_Stock (date, open, high, low, close, volume) VALUES(?, ?, ?, ?, ?, ?)", (time_frame[index], open_price, high_price, low_price, close_price, volume))

            conn.commit()
        
        elif row_count == 75:
            index = index + 75
            open_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["1. open"]
            high_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["2. high"]
            low_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["3. low"]
            close_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["4. close"]
            volume = data[gme_url]["Time Series (Daily)"][time_frame[index]]["5. volume"]
            
            cur.execute("INSERT OR IGNORE INTO Gamestop_Stock (date, open, high, low, close, volume) VALUES(?, ?, ?, ?, ?, ?)", (time_frame[index], open_price, high_price, low_price, close_price, volume))

            conn.commit()
        
        elif row_count == 100:
            index = index + 100
            open_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["1. open"]
            high_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["2. high"]
            low_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["3. low"]
            close_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["4. close"]
            volume = data[gme_url]["Time Series (Daily)"][time_frame[index]]["5. volume"]
            
            cur.execute("INSERT OR IGNORE INTO Gamestop_Stock (date, open, high, low, close, volume) VALUES(?, ?, ?, ?, ?, ?)", (time_frame[index], open_price, high_price, low_price, close_price, volume))

            conn.commit()
        
        elif row_count == 125:
            index = index + 125
            open_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["1. open"]
            high_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["2. high"]
            low_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["3. low"]
            close_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["4. close"]
            volume = data[gme_url]["Time Series (Daily)"][time_frame[index]]["5. volume"]
            
            cur.execute("INSERT OR IGNORE INTO Gamestop_Stock (date, open, high, low, close, volume) VALUES(?, ?, ?, ?, ?, ?)", (time_frame[index], open_price, high_price, low_price, close_price, volume))

            conn.commit()
        
        elif row_count == 150:
            index = index + 150
            open_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["1. open"]
            high_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["2. high"]
            low_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["3. low"]
            close_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["4. close"]
            volume = data[gme_url]["Time Series (Daily)"][time_frame[index]]["5. volume"]
            
            cur.execute("INSERT OR IGNORE INTO Gamestop_Stock (date, open, high, low, close, volume) VALUES(?, ?, ?, ?, ?, ?)", (time_frame[index], open_price, high_price, low_price, close_price, volume))

            conn.commit()
        
        elif row_count == 175:
            index = index + 175
            open_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["1. open"]
            high_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["2. high"]
            low_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["3. low"]
            close_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["4. close"]
            volume = data[gme_url]["Time Series (Daily)"][time_frame[index]]["5. volume"]
            
            cur.execute("INSERT OR IGNORE INTO Gamestop_Stock (date, open, high, low, close, volume) VALUES(?, ?, ?, ?, ?, ?)", (time_frame[index], open_price, high_price, low_price, close_price, volume))

            conn.commit()
        
        elif row_count == 200:
            index = index + 200
            open_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["1. open"]
            high_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["2. high"]
            low_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["3. low"]
            close_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["4. close"]
            volume = data[gme_url]["Time Series (Daily)"][time_frame[index]]["5. volume"]
            
            cur.execute("INSERT OR IGNORE INTO Gamestop_Stock (date, open, high, low, close, volume) VALUES(?, ?, ?, ?, ?, ?)", (time_frame[index], open_price, high_price, low_price, close_price, volume))

            conn.commit()
        
        elif row_count == 225:
            index = index + 225
            open_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["1. open"]
            high_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["2. high"]
            low_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["3. low"]
            close_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["4. close"]
            volume = data[gme_url]["Time Series (Daily)"][time_frame[index]]["5. volume"]
            
            cur.execute("INSERT OR IGNORE INTO Gamestop_Stock (date, open, high, low, close, volume) VALUES(?, ?, ?, ?, ?, ?)", (time_frame[index], open_price, high_price, low_price, close_price, volume))

            conn.commit()
        
        elif row_count == 250:
            index = index + 250
            open_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["1. open"]
            high_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["2. high"]
            low_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["3. low"]
            close_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["4. close"]
            volume = data[gme_url]["Time Series (Daily)"][time_frame[index]]["5. volume"]
            
            cur.execute("INSERT OR IGNORE INTO Gamestop_Stock (date, open, high, low, close, volume) VALUES(?, ?, ?, ?, ?, ?)", (time_frame[index], open_price, high_price, low_price, close_price, volume))

            conn.commit()
        
        elif row_count == 275:
            index = index + 275
            open_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["1. open"]
            high_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["2. high"]
            low_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["3. low"]
            close_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["4. close"]
            volume = data[gme_url]["Time Series (Daily)"][time_frame[index]]["5. volume"]
            
            cur.execute("INSERT OR IGNORE INTO Gamestop_Stock (date, open, high, low, close, volume) VALUES(?, ?, ?, ?, ?, ?)", (time_frame[index], open_price, high_price, low_price, close_price, volume))

            conn.commit()
        
        elif row_count == 300:
            index = index + 300
            open_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["1. open"]
            high_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["2. high"]
            low_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["3. low"]
            close_price = data[gme_url]["Time Series (Daily)"][time_frame[index]]["4. close"]
            volume = data[gme_url]["Time Series (Daily)"][time_frame[index]]["5. volume"]
            
            cur.execute("INSERT OR IGNORE INTO Gamestop_Stock (date, open, high, low, close, volume) VALUES(?, ?, ?, ?, ?, ?)", (time_frame[index], open_price, high_price, low_price, close_price, volume))

            conn.commit()
        
        elif row_count == 325:
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
        else:
            print("DONE RUNNING GAMESTOP DATA") 
            break

def set_up_time_table(data, cur, conn):
    cur.execute("CREATE TABLE IF NOT EXISTS Time_Table (time_id INT, year_month TEXT UNIQUE)")

    id = 0
    for month in data:
        if (month["age_group"] == "All Ages"):
            id += 1
            regex = r".+start_date':\s'([0-9]+-[0-9]+)"
            yrmm = re.findall(regex, str(month))
            cur.execute('INSERT OR IGNORE INTO Time_Table (time_id, year_month) VALUES (?, ?)', (id, yrmm[0]))
    conn.commit()

def get_selected_age_group(data):
    age_groups = []
    selected_age_groups = []
    for month in data:
        if month["age_group"] not in age_groups:
            age_groups.append(month["age_group"])
    #Only want selected age groups: 5-14, 15-24, 25-34, 35-44, 45-54, 55-64, 65-74 (7 Groups)
    selected_age_groups.append(age_groups[4])
    selected_age_groups.append(age_groups[5])
    selected_age_groups.append(age_groups[7])
    selected_age_groups.append(age_groups[9])
    selected_age_groups.append(age_groups[11])
    selected_age_groups.append(age_groups[13])
    selected_age_groups.append(age_groups[14])
    return selected_age_groups

def set_up_age_group_table(data, cur, conn):
    cur.execute("CREATE TABLE IF NOT EXISTS Age_Group_Table (id INT , age_group TEXT UNIQUE)")
    age_groups = get_selected_age_group(data)
    
    for i in range(7):
        cur.execute('INSERT OR IGNORE INTO Age_Group_Table  (id, age_group) VALUES (?, ?)', (i + 1, age_groups[i]))
    conn.commit()

def set_up_covid_deaths_table(data, cur, conn, age_groups):
    cur.execute("CREATE TABLE IF NOT EXISTS COVID_Deaths (year_month_id INT, age_group_id INT, num_deaths INT)")

    cur.execute('SELECT COUNT(year_month_id) FROM COVID_Deaths')
    row_value = cur.fetchone()[0]

    if row_value == 0:  
        for month in data: 
            index = 0    
            if (month["age_group"] == age_groups[index]): 
                regex = r".+start_date':\s'([0-9]+-[0-9]+)"  
                yrmm = re.findall(regex, str(month))  
                cur.execute('SELECT time_id FROM Time_Table WHERE year_month = ?', (yrmm[0], ))  
                timeID = cur.fetchone()[0]    
                regex = r".+age_group':\s'([A-Za-z0-9]+\s?\-?[A-Za-z0-9]+\syears)" 
                age_range = re.findall(regex, str(month))
                cur.execute('SELECT id FROM Age_Group_Table  WHERE age_group = ?', (age_range[0], ))   
                ages = cur.fetchone()[0]   
                cur.execute('INSERT OR IGNORE INTO COVID_Deaths (year_month_id, age_group_id, num_deaths) VALUES (?, ?, ?)' , (timeID, ages,  month["covid_19_deaths"]))
                conn.commit()  

    elif row_value == 16:
          for month in data: 
            index = 1    
            if (month["age_group"] == age_groups[index]): 
                regex = r".+start_date':\s'([0-9]+-[0-9]+)"  
                yrmm = re.findall(regex, str(month))  
                cur.execute('SELECT time_id FROM Time_Table WHERE year_month = ?', (yrmm[0], ))  
                timeID = cur.fetchone()[0]    
                regex = r".+age_group':\s'([A-Za-z0-9]+\s?\-?[A-Za-z0-9]+\syears)" 
                age_range = re.findall(regex, str(month))
                cur.execute('SELECT id FROM Age_Group_Table  WHERE age_group = ?', (age_range[0], ))   
                ages = cur.fetchone()[0]   
                cur.execute('INSERT OR IGNORE INTO COVID_Deaths (year_month_id, age_group_id, num_deaths) VALUES (?, ?, ?)' , (timeID, ages,  month["covid_19_deaths"]))
                conn.commit() 

    elif row_value == 32:
          for month in data: 
            index = 2    
            if (month["age_group"] == age_groups[index]): 
                regex = r".+start_date':\s'([0-9]+-[0-9]+)"  
                yrmm = re.findall(regex, str(month))  
                cur.execute('SELECT time_id FROM Time_Table WHERE year_month = ?', (yrmm[0], ))  
                timeID = cur.fetchone()[0]    
                regex = r".+age_group':\s'([A-Za-z0-9]+\s?\-?[A-Za-z0-9]+\syears)" 
                age_range = re.findall(regex, str(month))
                cur.execute('SELECT id FROM Age_Group_Table  WHERE age_group = ?', (age_range[0], ))   
                ages = cur.fetchone()[0]   
                cur.execute('INSERT OR IGNORE INTO COVID_Deaths (year_month_id, age_group_id, num_deaths) VALUES (?, ?, ?)' , (timeID, ages,  month["covid_19_deaths"]))
                conn.commit()  

    elif row_value == 48:
          for month in data: 
            index = 3   
            if (month["age_group"] == age_groups[index]): 
                regex = r".+start_date':\s'([0-9]+-[0-9]+)"  
                yrmm = re.findall(regex, str(month))  
                cur.execute('SELECT time_id FROM Time_Table WHERE year_month = ?', (yrmm[0], ))  
                timeID = cur.fetchone()[0]    
                regex = r".+age_group':\s'([A-Za-z0-9]+\s?\-?[A-Za-z0-9]+\syears)" 
                age_range = re.findall(regex, str(month))
                cur.execute('SELECT id FROM Age_Group_Table  WHERE age_group = ?', (age_range[0], ))   
                ages = cur.fetchone()[0]   
                cur.execute('INSERT OR IGNORE INTO COVID_Deaths (year_month_id, age_group_id, num_deaths) VALUES (?, ?, ?)' , (timeID, ages,  month["covid_19_deaths"]))
                conn.commit() 

    elif row_value == 64:
          for month in data: 
            index = 4    
            if (month["age_group"] == age_groups[index]): 
                regex = r".+start_date':\s'([0-9]+-[0-9]+)"  
                yrmm = re.findall(regex, str(month))  
                cur.execute('SELECT time_id FROM Time_Table WHERE year_month = ?', (yrmm[0], ))  
                timeID = cur.fetchone()[0]    
                regex = r".+age_group':\s'([A-Za-z0-9]+\s?\-?[A-Za-z0-9]+\syears)" 
                age_range = re.findall(regex, str(month))
                cur.execute('SELECT id FROM Age_Group_Table  WHERE age_group = ?', (age_range[0], ))   
                ages = cur.fetchone()[0]   
                cur.execute('INSERT OR IGNORE INTO COVID_Deaths (year_month_id, age_group_id, num_deaths) VALUES (?, ?, ?)' , (timeID, ages,  month["covid_19_deaths"]))
                conn.commit() 
    elif row_value == 80:
          for month in data: 
            index = 5    
            if (month["age_group"] == age_groups[index]): 
                regex = r".+start_date':\s'([0-9]+-[0-9]+)"  
                yrmm = re.findall(regex, str(month))  
                cur.execute('SELECT time_id FROM Time_Table WHERE year_month = ?', (yrmm[0], ))  
                timeID = cur.fetchone()[0]    
                regex = r".+age_group':\s'([A-Za-z0-9]+\s?\-?[A-Za-z0-9]+\syears)" 
                age_range = re.findall(regex, str(month))
                cur.execute('SELECT id FROM Age_Group_Table  WHERE age_group = ?', (age_range[0], ))   
                ages = cur.fetchone()[0]   
                cur.execute('INSERT OR IGNORE INTO COVID_Deaths (year_month_id, age_group_id, num_deaths) VALUES (?, ?, ?)' , (timeID, ages,  month["covid_19_deaths"]))
                conn.commit()

    elif row_value == 96:
          for month in data: 
            index = 6    
            if (month["age_group"] == age_groups[index]): 
                regex = r".+start_date':\s'([0-9]+-[0-9]+)"  
                yrmm = re.findall(regex, str(month))  
                cur.execute('SELECT time_id FROM Time_Table WHERE year_month = ?', (yrmm[0], ))  
                timeID = cur.fetchone()[0]    
                regex = r".+age_group':\s'([A-Za-z0-9]+\s?\-?[A-Za-z0-9]+\syears)" 
                age_range = re.findall(regex, str(month))
                cur.execute('SELECT id FROM Age_Group_Table  WHERE age_group = ?', (age_range[0], ))   
                ages = cur.fetchone()[0]   
                cur.execute('INSERT OR IGNORE INTO COVID_Deaths (year_month_id, age_group_id, num_deaths) VALUES (?, ?, ?)' , (timeID, ages,  month["covid_19_deaths"]))
                conn.commit()   
    else:
        print("DONE RUNNING COVID DATA") 

#calculations
def tesla_monthly_average_price(cur, conn):
    cur.execute("SELECT date, high, low FROM Tesla_Stock")
    conn.commit()

    tesla_data = []
    average_daily_price = []

    for row in cur:
        tesla_data.append(row)
    
    for date in tesla_data:
        high = date[1]
        low = date[2]
        average = (high + low) / 2
        average_daily_price.append((date[0], average))
    
    months_list = ["2020-01", "2020-02", "2020-03", "2020-04", "2020-05", "2020-06", "2020-07", "2020-08", "2020-09", "2020-10", "2020-11", "2020-12", "2021-01", "2021-02", "2021-03", "2021-04"]
    
    jan20, feb20, mar20, apr20, may20, june20, july20, aug20, sept20, oct20, nov20, dec20, jan21, feb21, mar21, apr21 = ([] for i in range(16))
    
    for index in range(len(average_daily_price)):
        if months_list[0] in average_daily_price[index][0]:
            jan20.append(average_daily_price[index])

        if months_list[1] in average_daily_price[index][0]:
            feb20.append(average_daily_price[index])
        
        if months_list[2] in average_daily_price[index][0]:
            mar20.append(average_daily_price[index])
        
        if months_list[3] in average_daily_price[index][0]:
            apr20.append(average_daily_price[index])
        
        if months_list[4] in average_daily_price[index][0]:
            may20.append(average_daily_price[index])
        
        if months_list[5] in average_daily_price[index][0]:
            june20.append(average_daily_price[index])
        
        if months_list[6] in average_daily_price[index][0]:
            july20.append(average_daily_price[index])
        
        if months_list[7] in average_daily_price[index][0]:
            aug20.append(average_daily_price[index])
        
        if months_list[8] in average_daily_price[index][0]:
            sept20.append(average_daily_price[index])
        
        if months_list[9] in average_daily_price[index][0]:
            oct20.append(average_daily_price[index])
        
        if months_list[10] in average_daily_price[index][0]:
            nov20.append(average_daily_price[index])
        
        if months_list[11] in average_daily_price[index][0]:
            dec20.append(average_daily_price[index])
        
        if months_list[12] in average_daily_price[index][0]:
            jan21.append(average_daily_price[index])
        
        if months_list[13] in average_daily_price[index][0]:
            feb21.append(average_daily_price[index])
        
        if months_list[14] in average_daily_price[index][0]:
            mar21.append(average_daily_price[index])
        
        if months_list[15] in average_daily_price[index][0]:
            apr21.append(average_daily_price[index])

    average_monthly_price = []
    jan_total, feb_total, mar_total, apr_total, may_total, june_total, july_total, aug_total, sept_total, oct_total, nov_total, dec_total, jan2_total, feb2_total, mar2_total, apr2_total = (0 for i in range(16)) 

    for date in jan20:
        jan_total += date[1]
    avg_jan_price = jan_total/len(jan20)
    average_monthly_price.append((months_list[0], avg_jan_price))

    for date in feb20:
        feb_total += date[1]
    avg_feb_price = feb_total/len(feb20)
    average_monthly_price.append((months_list[1], avg_feb_price))

    for date in mar20:
        mar_total += date[1]
    avg_mar_price = mar_total/len(mar20)
    average_monthly_price.append((months_list[2], avg_mar_price))

    for date in apr20:
        apr_total += date[1]
    avg_apr_price = apr_total/len(apr20)
    average_monthly_price.append((months_list[3], avg_apr_price))

    for date in may20:
        may_total += date[1]
    avg_may_price = may_total/len(may20)
    average_monthly_price.append((months_list[4], avg_may_price))

    for date in june20:
        june_total += date[1]
    avg_june_price = june_total/len(june20)
    average_monthly_price.append((months_list[5], avg_june_price))

    for date in july20:
        july_total += date[1]
    avg_july_price = july_total/len(july20)
    average_monthly_price.append((months_list[6], avg_july_price))

    for date in aug20:
        aug_total += date[1]
    avg_aug_price = aug_total/len(aug20)
    average_monthly_price.append((months_list[7], avg_aug_price))

    for date in sept20:
        sept_total += date[1]
    avg_sept_price = sept_total/len(sept20)
    average_monthly_price.append((months_list[8], avg_sept_price))

    for date in oct20:
        oct_total += date[1]
    avg_oct_price = oct_total/len(oct20)
    average_monthly_price.append((months_list[9], avg_oct_price))

    for date in nov20:
        nov_total += date[1]
    avg_nov_price = nov_total/len(nov20)
    average_monthly_price.append((months_list[10], avg_nov_price))

    for date in dec20:
        dec_total += date[1]
    avg_dec_price = dec_total/len(dec20)
    average_monthly_price.append((months_list[11], avg_dec_price))

    for date in jan21:
        jan2_total += date[1]
    avg_jan2_price = jan2_total/len(jan21)
    average_monthly_price.append((months_list[12], avg_jan2_price))

    for date in feb21:
        feb2_total += date[1]
    avg_feb2_price = feb2_total/len(feb21)
    average_monthly_price.append((months_list[13], avg_feb2_price))

    for date in mar21:
        mar2_total += date[1]
    avg_mar2_price = mar2_total/len(mar21)
    average_monthly_price.append((months_list[14], avg_mar2_price))

    for date in apr21:
        apr2_total += date[1]
    avg_apr2_price = apr2_total/len(apr21)
    average_monthly_price.append((months_list[15], avg_apr2_price))

    return average_monthly_price

def gamestop_monthly_average_price(cur, conn):
    cur.execute("SELECT date, high, low FROM Gamestop_stock")
    conn.commit()

    gamestop_data = []
    average_daily_price = []

    for row in cur:
        gamestop_data.append(row)
    
    for date in gamestop_data:
        high = date[1]
        low = date[2]
        average = (high + low) / 2
        average_daily_price.append((date[0], average))
    
    months_list = ["2020-01", "2020-02", "2020-03", "2020-04", "2020-05", "2020-06", "2020-07", "2020-08", "2020-09", "2020-10", "2020-11", "2020-12", "2021-01", "2021-02", "2021-03", "2021-04"]
    
    jan20, feb20, mar20, apr20, may20, june20, july20, aug20, sept20, oct20, nov20, dec20, jan21, feb21, mar21, apr21 = ([] for i in range(16))
    
    for index in range(len(average_daily_price)):
        if months_list[0] in average_daily_price[index][0]:
            jan20.append(average_daily_price[index])

        if months_list[1] in average_daily_price[index][0]:
            feb20.append(average_daily_price[index])
        
        if months_list[2] in average_daily_price[index][0]:
            mar20.append(average_daily_price[index])
        
        if months_list[3] in average_daily_price[index][0]:
            apr20.append(average_daily_price[index])
        
        if months_list[4] in average_daily_price[index][0]:
            may20.append(average_daily_price[index])
        
        if months_list[5] in average_daily_price[index][0]:
            june20.append(average_daily_price[index])
        
        if months_list[6] in average_daily_price[index][0]:
            july20.append(average_daily_price[index])
        
        if months_list[7] in average_daily_price[index][0]:
            aug20.append(average_daily_price[index])
        
        if months_list[8] in average_daily_price[index][0]:
            sept20.append(average_daily_price[index])
        
        if months_list[9] in average_daily_price[index][0]:
            oct20.append(average_daily_price[index])
        
        if months_list[10] in average_daily_price[index][0]:
            nov20.append(average_daily_price[index])
        
        if months_list[11] in average_daily_price[index][0]:
            dec20.append(average_daily_price[index])
        
        if months_list[12] in average_daily_price[index][0]:
            jan21.append(average_daily_price[index])
        
        if months_list[13] in average_daily_price[index][0]:
            feb21.append(average_daily_price[index])
        
        if months_list[14] in average_daily_price[index][0]:
            mar21.append(average_daily_price[index])
        
        if months_list[15] in average_daily_price[index][0]:
            apr21.append(average_daily_price[index])

    average_monthly_price = []
    jan_total, feb_total, mar_total, apr_total, may_total, june_total, july_total, aug_total, sept_total, oct_total, nov_total, dec_total, jan2_total, feb2_total, mar2_total, apr2_total = (0 for i in range(16)) 

    for date in jan20:
        jan_total += date[1]
    avg_jan_price = jan_total/len(jan20)
    average_monthly_price.append((months_list[0], avg_jan_price))

    for date in feb20:
        feb_total += date[1]
    avg_feb_price = feb_total/len(feb20)
    average_monthly_price.append((months_list[1], avg_feb_price))

    for date in mar20:
        mar_total += date[1]
    avg_mar_price = mar_total/len(mar20)
    average_monthly_price.append((months_list[2], avg_mar_price))

    for date in apr20:
        apr_total += date[1]
    avg_apr_price = apr_total/len(apr20)
    average_monthly_price.append((months_list[3], avg_apr_price))

    for date in may20:
        may_total += date[1]
    avg_may_price = may_total/len(may20)
    average_monthly_price.append((months_list[4], avg_may_price))

    for date in june20:
        june_total += date[1]
    avg_june_price = june_total/len(june20)
    average_monthly_price.append((months_list[5], avg_june_price))

    for date in july20:
        july_total += date[1]
    avg_july_price = july_total/len(july20)
    average_monthly_price.append((months_list[6], avg_july_price))

    for date in aug20:
        aug_total += date[1]
    avg_aug_price = aug_total/len(aug20)
    average_monthly_price.append((months_list[7], avg_aug_price))

    for date in sept20:
        sept_total += date[1]
    avg_sept_price = sept_total/len(sept20)
    average_monthly_price.append((months_list[8], avg_sept_price))

    for date in oct20:
        oct_total += date[1]
    avg_oct_price = oct_total/len(oct20)
    average_monthly_price.append((months_list[9], avg_oct_price))

    for date in nov20:
        nov_total += date[1]
    avg_nov_price = nov_total/len(nov20)
    average_monthly_price.append((months_list[10], avg_nov_price))

    for date in dec20:
        dec_total += date[1]
    avg_dec_price = dec_total/len(dec20)
    average_monthly_price.append((months_list[11], avg_dec_price))

    for date in jan21:
        jan2_total += date[1]
    avg_jan2_price = jan2_total/len(jan21)
    average_monthly_price.append((months_list[12], avg_jan2_price))

    for date in feb21:
        feb2_total += date[1]
    avg_feb2_price = feb2_total/len(feb21)
    average_monthly_price.append((months_list[13], avg_feb2_price))

    for date in mar21:
        mar2_total += date[1]
    avg_mar2_price = mar2_total/len(mar21)
    average_monthly_price.append((months_list[14], avg_mar2_price))

    for date in apr21:
        apr2_total += date[1]
    avg_apr2_price = apr2_total/len(apr21)
    average_monthly_price.append((months_list[15], avg_apr2_price))

    return average_monthly_price

def calculation_tables(cur, conn):
    tesla = tesla_monthly_average_price(cur, conn)
    gamestop = gamestop_monthly_average_price(cur, conn)

    cur.execute("CREATE TABLE IF NOT EXISTS Average_Stock_Price (id INTEGER PRIMARY KEY, month_id INTEGER, stock_symbol TEXT, average_price REAL)")
    cur.execute('CREATE TABLE IF NOT EXISTS Monthly_Deaths (id INTEGER PRIMARY KEY, month_id INTEGER, deaths INT)')
    conn.commit()

    unique_id = 0

    month_id = 1
    for index in range(len(tesla)):
        price = tesla[index][1]
        symbol = "TSLA"
        
        cur.execute("INSERT OR IGNORE INTO Average_Stock_Price (id, month_id, stock_symbol, average_price) VALUES(?, ?, ?, ?)", (unique_id, month_id, symbol, price))
        conn.commit()

        month_id += 1
        unique_id += 1

    month_id = 1

    for index in range(len(gamestop)):
        price = gamestop[index][1]
        symbol = "GME"
        
        cur.execute("INSERT OR IGNORE INTO Average_Stock_Price (id, month_id, stock_symbol, average_price) VALUES(?, ?, ?, ?)", (unique_id, month_id, symbol, price))
        conn.commit()

        month_id += 1
        unique_id += 1
    
    month_id = 1
    unique_id = 0

    for index in range(16):
        cur.execute('SELECT SUM(num_deaths) from COVID_Deaths WHERE year_month_id = ?', (index + 1, )) 
        deaths = cur.fetchone()[0]
        cur.execute('INSERT OR IGNORE INTO Monthly_Deaths (id, month_id, deaths) VALUES (?, ?, ?)', (unique_id, month_id, deaths))
        conn.commit()

        month_id += 1
        unique_id += 1
   
def write_calculations(cur, conn):
    
    tesla = tesla_monthly_average_price(cur, conn)
    gamestop = gamestop_monthly_average_price(cur, conn)
    months_list = ["JANUARY 2020","FEBRUARY 2020","MARCH 2020", "APRIL 2020", "MAY 2020", "JUNE 2020", "JULY 2020",
                 "AUGUST 2020", "SEPTEMBER 2020", "OCTOBER 2020", "NOVEMBER 2020", "DECEMBER 2020", "JANUARY 2021", "FEBRUARY 2021", 
                 "MARCH 2021", "APRIL 2021"]



    cur.execute("SELECT Monthly_Deaths.month_id, Monthly_Deaths.deaths, Average_Stock_Price.stock_symbol, Average_Stock_Price.average_price FROM Monthly_Deaths JOIN Average_Stock_Price ON Monthly_Deaths.month_id = Average_Stock_Price.month_id")
    conn.commit()

    joined_data = []
    month = []
    deaths = []
    stock = []
    price = []

    for row in cur:
        joined_data.append(row)

    for data in joined_data:
        month.append(data[0])
        deaths.append(data[1])
        stock.append(data[2])
        price.append(data[3])
    
    f = open("calculations.txt", "w")


    f.write('Month, Number of Deaths, Stock Name, Average Stock Price')
    f.write("\n")
    f.write('\n')

    for index in range(len(month)):

        month_num = month[index] - 1

        row = str(months_list[month_num]) + ", " + str(deaths[index]) + ", " + str(stock[index]) + ", " + str(price[index])
        
        f.write(row)
        f.write('\n')

    f.write('\n')


    f.write("NUMBER OF DEATHS PER MONTH (1/2020 - 4/2021) FOR ALL AGES 5 - 74\n")
    f.write("\n")
    for i in range(16):
        cur.execute('SELECT SUM(num_deaths) from COVID_Deaths WHERE year_month_id = ?', (i + 1, )) 
        x = cur.fetchone()[0]
        f.write(months_list[i])
        f.write(" : ")
        f.write(str(x))
        f.write('\n')

    f.write('\n')

    f.write("AVERAGE TESLA STOCK PRICES PER MONTH (1/2020 - 4/2021)\n")
    f.write("\n")
    for index in range(16):
        f.write(months_list[index])
        f.write(" : ")
        f.write(str(tesla[index][1]))
        f.write('\n')
    
    f.write('\n')
    
    f.write("AVERAGE GAMESTOP STOCK PRICES PER MONTH (1/2020 - 4/2021)\n")
    f.write("\n")
    for index in range(16):
        f.write(months_list[index])
        f.write(" : ")
        f.write(str(gamestop[index][1]))
        f.write('\n')

    f.close()

def visualizations(cur, conn):
   
    fig, ax = plt.subplots()
    fig, ax2 = plt.subplots()

    #set the x and y axis labels and the title for TSLA
    ax.set_xlabel('Number of Deaths')
    ax.set_ylabel('Price of Stock')
    ax.set_title('Average Price of TSLA per COVID Deaths')

    #set the x and y axis labels and the title for GME
    ax2.set_xlabel('Number of Deaths')
    ax2.set_ylabel('Price of Stock')
    ax2.set_title('Average Price of GME per COVID Deaths')

    #Finding Average Tesla Stock Price with corresponding Deaths of each month
    numDeaths = []
    teslaStockPrice = []
    stock_and_deaths = []
    cur.execute('SELECT Monthly_Deaths.deaths , Average_Stock_Price.average_price FROM Monthly_Deaths JOIN Average_Stock_Price WHERE Monthly_Deaths.month_id = Average_Stock_Price.month_id AND Average_Stock_Price.stock_symbol = ?', ('TSLA', ))
    for row in cur:
        stock_and_deaths.append(row)

    stock_and_deaths = sorted(stock_and_deaths)
    
    for pair in stock_and_deaths:
        numDeaths.append(pair[0])
        teslaStockPrice.append(pair[1])
    
    p1 = ax.plot(numDeaths, teslaStockPrice, "-r")

    #Finding Average GameStop Stock Price with corresponding Deaths of each month
    numDeaths_2 = []
    gamestopStockPrice = []
    stock_and_deaths_2 = []
    cur.execute('SELECT Monthly_Deaths.deaths , Average_Stock_Price.average_price FROM Monthly_Deaths JOIN Average_Stock_Price WHERE Monthly_Deaths.month_id = Average_Stock_Price.month_id AND Average_Stock_Price.stock_symbol = ?', ('GME', ))
    for row in cur:
        stock_and_deaths_2.append(row)

    stock_and_deaths_2 = sorted(stock_and_deaths_2)

    for pair in stock_and_deaths_2:
        numDeaths_2.append(pair[0])
        gamestopStockPrice.append(pair[1])
    
    p2 = ax2.plot(numDeaths_2, gamestopStockPrice, '-b')
    
    ax.grid()
    ax2.grid()
    plt.show()

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    CACHE_FILE = dir_path + '/' + "cache_stocks.json"
    stocks = ["TSLA", "GME"]
    [get_stocks_data_from_cache(stock, CACHE_FILE) for stock in stocks]
    stocks_data = read_data_from_file("cache_stocks.json")
    covid_data = get_covid_data("'By Month'", "United States", "All Sexes")

    cur, conn = set_up_database('data.db')

    tsla_keys = get_stock_dates("TSLA", stocks_data)
    gme_keys = get_stock_dates("GME", stocks_data)
    set_up_tesla_stocks_table(stocks_data, cur, conn, tsla_keys)
    set_up_gamestop_stocks_table(stocks_data, cur, conn, gme_keys)

    set_up_time_table(covid_data, cur, conn)
    set_up_age_group_table(covid_data, cur, conn)
    age_groups = get_selected_age_group(covid_data)
    set_up_covid_deaths_table(covid_data, cur, conn, age_groups)

    #run the following code after you secure all of the data in the database
    calculation_tables(cur, conn)
    write_calculations(cur, conn)
    visualizations(cur, conn)

if __name__ == "__main__":
    main()
    