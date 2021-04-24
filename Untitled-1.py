

def set_up_gamestop_stocks_table(data, cur, conn, time_frame):
    cur.execute("CREATE TABLE IF NOT EXISTS Gamestop_Stock (date TEXT PRIMARY KEY, open REAL, high REAL, low REAL, close REAL, volume REAL)")
    conn.commit()

    gme_url = create_request_url("GME")

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