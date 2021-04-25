import sqlite3
import json
import os
import requests
import re

def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

def get_data(group_in, state_in, sex_in):
    base_url = "https://data.cdc.gov/resource/9bhg-hcku.json?$where=`group`={}&state={}&sex={}"

    group = group_in
    state = state_in
    sex = sex_in

    request_url = base_url.format(group, state, sex)
   
    r = requests.get(request_url)
    data = r.text
    dict_list = json.loads(data)
    
    return dict_list

def setupTimeTable(data, cur, conn):

    cur.execute("CREATE TABLE IF NOT EXISTS TimeTable (time_id INT, YearandMonth TEXT UNIQUE)")

    id = 0
    for month in data:
        if (month["age_group"] == "All Ages"):
            id += 1
            regex = r".+start_date':\s'([0-9]+-[0-9]+)"
            yrmm = re.findall(regex, str(month))
            cur.execute('INSERT OR IGNORE INTO TimeTable (time_id, YearandMonth) VALUES (?, ?)', (id, yrmm[0]))
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

def setupAgeGroupTable(data, cur, conn):
    cur.execute("CREATE TABLE IF NOT EXISTS AgeGroupTable(id INT , Age_Group TEXT UNIQUE)")
    age_groups = get_selected_age_group(data)
    
    for i in range(7):
        cur.execute('INSERT OR IGNORE INTO AgeGroupTable (id, Age_Group) VALUES (?, ?)', (i + 1, age_groups[i]))
    conn.commit()

def setupCoviddeathsTable(data, cur, conn, AGE_GROUPS):
    
    cur.execute("CREATE TABLE IF NOT EXISTS Coviddeaths (YearandMonth_id INT, age_group_id INT, numDeaths INT)")

    cur.execute('SELECT COUNT(YearandMonth_id) FROM Coviddeaths')
    row_value = cur.fetchone()[0]

    if row_value == 0:  
        for month in data: 
            index = 0    
            if (month["age_group"] == AGE_GROUPS[index]): 
                regex = r".+start_date':\s'([0-9]+-[0-9]+)"  
                yrmm = re.findall(regex, str(month))  
                cur.execute('SELECT time_id FROM TimeTable WHERE YearandMonth = ?', (yrmm[0], ))  
                timeID = cur.fetchone()[0]    
                regex = r".+age_group':\s'([A-Za-z0-9]+\s?\-?[A-Za-z0-9]+\syears)" 
                age_range = re.findall(regex, str(month))
                cur.execute('SELECT id FROM AgeGroupTable WHERE Age_Group = ?', (age_range[0], ))   
                ages = cur.fetchone()[0]   
                cur.execute('INSERT OR IGNORE INTO Coviddeaths (YearandMonth_id, age_group_id, numDeaths) VALUES (?, ?, ?)' , (timeID, ages,  month["covid_19_deaths"]))
                conn.commit()  

    elif row_value == 16:
          for month in data: 
            index = 1    
            if (month["age_group"] == AGE_GROUPS[index]): 
                regex = r".+start_date':\s'([0-9]+-[0-9]+)"  
                yrmm = re.findall(regex, str(month))  
                cur.execute('SELECT time_id FROM TimeTable WHERE YearandMonth = ?', (yrmm[0], ))  
                timeID = cur.fetchone()[0]    
                regex = r".+age_group':\s'([A-Za-z0-9]+\s?\-?[A-Za-z0-9]+\syears)" 
                age_range = re.findall(regex, str(month))
                cur.execute('SELECT id FROM AgeGroupTable WHERE Age_Group = ?', (age_range[0], ))   
                ages = cur.fetchone()[0]   
                cur.execute('INSERT OR IGNORE INTO Coviddeaths (YearandMonth_id, age_group_id, numDeaths) VALUES (?, ?, ?)' , (timeID, ages,  month["covid_19_deaths"]))
                conn.commit() 

    elif row_value == 32:
          for month in data: 
            index = 2    
            if (month["age_group"] == AGE_GROUPS[index]): 
                regex = r".+start_date':\s'([0-9]+-[0-9]+)"  
                yrmm = re.findall(regex, str(month))  
                cur.execute('SELECT time_id FROM TimeTable WHERE YearandMonth = ?', (yrmm[0], ))  
                timeID = cur.fetchone()[0]    
                regex = r".+age_group':\s'([A-Za-z0-9]+\s?\-?[A-Za-z0-9]+\syears)" 
                age_range = re.findall(regex, str(month))
                cur.execute('SELECT id FROM AgeGroupTable WHERE Age_Group = ?', (age_range[0], ))   
                ages = cur.fetchone()[0]   
                cur.execute('INSERT OR IGNORE INTO Coviddeaths (YearandMonth_id, age_group_id, numDeaths) VALUES (?, ?, ?)' , (timeID, ages,  month["covid_19_deaths"]))
                conn.commit()  

    elif row_value == 48:
          for month in data: 
            index = 3   
            if (month["age_group"] == AGE_GROUPS[index]): 
                regex = r".+start_date':\s'([0-9]+-[0-9]+)"  
                yrmm = re.findall(regex, str(month))  
                cur.execute('SELECT time_id FROM TimeTable WHERE YearandMonth = ?', (yrmm[0], ))  
                timeID = cur.fetchone()[0]    
                regex = r".+age_group':\s'([A-Za-z0-9]+\s?\-?[A-Za-z0-9]+\syears)" 
                age_range = re.findall(regex, str(month))
                cur.execute('SELECT id FROM AgeGroupTable WHERE Age_Group = ?', (age_range[0], ))   
                ages = cur.fetchone()[0]   
                cur.execute('INSERT OR IGNORE INTO Coviddeaths (YearandMonth_id, age_group_id, numDeaths) VALUES (?, ?, ?)' , (timeID, ages,  month["covid_19_deaths"]))
                conn.commit() 

    elif row_value == 64:
          for month in data: 
            index = 4    
            if (month["age_group"] == AGE_GROUPS[index]): 
                regex = r".+start_date':\s'([0-9]+-[0-9]+)"  
                yrmm = re.findall(regex, str(month))  
                cur.execute('SELECT time_id FROM TimeTable WHERE YearandMonth = ?', (yrmm[0], ))  
                timeID = cur.fetchone()[0]    
                regex = r".+age_group':\s'([A-Za-z0-9]+\s?\-?[A-Za-z0-9]+\syears)" 
                age_range = re.findall(regex, str(month))
                cur.execute('SELECT id FROM AgeGroupTable WHERE Age_Group = ?', (age_range[0], ))   
                ages = cur.fetchone()[0]   
                cur.execute('INSERT OR IGNORE INTO Coviddeaths (YearandMonth_id, age_group_id, numDeaths) VALUES (?, ?, ?)' , (timeID, ages,  month["covid_19_deaths"]))
                conn.commit() 
    elif row_value == 80:
          for month in data: 
            index = 5    
            if (month["age_group"] == AGE_GROUPS[index]): 
                regex = r".+start_date':\s'([0-9]+-[0-9]+)"  
                yrmm = re.findall(regex, str(month))  
                cur.execute('SELECT time_id FROM TimeTable WHERE YearandMonth = ?', (yrmm[0], ))  
                timeID = cur.fetchone()[0]    
                regex = r".+age_group':\s'([A-Za-z0-9]+\s?\-?[A-Za-z0-9]+\syears)" 
                age_range = re.findall(regex, str(month))
                cur.execute('SELECT id FROM AgeGroupTable WHERE Age_Group = ?', (age_range[0], ))   
                ages = cur.fetchone()[0]   
                cur.execute('INSERT OR IGNORE INTO Coviddeaths (YearandMonth_id, age_group_id, numDeaths) VALUES (?, ?, ?)' , (timeID, ages,  month["covid_19_deaths"]))
                conn.commit()

    elif row_value == 96:
          for month in data: 
            index = 6    
            if (month["age_group"] == AGE_GROUPS[index]): 
                regex = r".+start_date':\s'([0-9]+-[0-9]+)"  
                yrmm = re.findall(regex, str(month))  
                cur.execute('SELECT time_id FROM TimeTable WHERE YearandMonth = ?', (yrmm[0], ))  
                timeID = cur.fetchone()[0]    
                regex = r".+age_group':\s'([A-Za-z0-9]+\s?\-?[A-Za-z0-9]+\syears)" 
                age_range = re.findall(regex, str(month))
                cur.execute('SELECT id FROM AgeGroupTable WHERE Age_Group = ?', (age_range[0], ))   
                ages = cur.fetchone()[0]   
                cur.execute('INSERT OR IGNORE INTO Coviddeaths (YearandMonth_id, age_group_id, numDeaths) VALUES (?, ?, ?)' , (timeID, ages,  month["covid_19_deaths"]))
                conn.commit()   
    else:
        print("DONE RUNNING CODE") 
        calculations(cur, conn)


def calculations(cur, conn):
    f = open("calculations.txt", "w")
    months_list = ["JANUARY 2020","FEBRUARY 2020","MARCH 2020", "APRIL 2020", "MAY 2020", "JUNE 2020", "JULY 2020",
                 "AUGUST 2020", "SEPTEMBER 2020", "OCTOBER 2020", "NOVEMBER 2020", "DECEMBER 2020", "JANUARY 2021", "FEBRUARY 2021", 
                 "MARCH 2021", "APRIL 2021"]

    cur.execute('CREATE TABLE IF NOT EXISTS Calculations (date UNIQUE, deaths INT)')
    
    for i in range(len(months_list)):
        cur.execute('SELECT SUM(numDeaths) from Coviddeaths WHERE YearandMonth_id = ?', (i + 1, )) 
        deaths = cur.fetchone()[0]
        cur.execute('INSERT OR IGNORE INTO Calculations (date, deaths) VALUES (?, ?)', (months_list[i], deaths ))
  

    conn.commit()
    f.write("NUMBER OF DEATHS PER MONTH (1/2020 - 4/2021) FOR ALL AGES 5 - 74\n")
    f.write("\n")
    for i in range(16):
        cur.execute('SELECT SUM(numDeaths) from Coviddeaths WHERE YearandMonth_id = ?', (i + 1, )) 
        x = cur.fetchone()[0]
        f.write(months_list[i])
        f.write(" : ")
        f.write(str(x))
        f.write('\n')

    conn.commit()
    f.close()


def main(): 
    json_data = get_data("'By Month'", "United States", "All Sexes")
    cur, conn = setUpDatabase('covid.db')
    setupTimeTable(json_data, cur, conn)
    setupAgeGroupTable(json_data, cur, conn)
    
    AGEGROUPS = get_selected_age_group(json_data)
    setupCoviddeathsTable(json_data, cur, conn, AGEGROUPS)

    
    conn.close()
    
if __name__ == "__main__":
    main()