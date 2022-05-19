import requests
import pandas as pd

date = 1
message_notification = 1
while 1 <= date <= 31:
    if 1 <= date <= 31:
        date = str(date)
        response = requests.get(f"https://api.nasa.gov/neo/rest/v1/feed?start_date=2016-07-{date}&end_date=2016-07-{date}&api_key=qJuirK8yAyaPUufRVd52PCV7zklVV9GL8KhcPFzu")
        response1 = response.json()["near_earth_objects"]
        if len(str(date)) == 1:
            index = 0
            while True:
                try:
                    asteroid = response1[f"2016-07-0{date}"][index]['is_potentially_hazardous_asteroid']
                    if asteroid == True:
                        with open("astorid.csv", "a") as file:
                            file.write(str(response1[f"2016-07-0{date}"][index])+"\n")
                    else:
                        pass
                    index += 1
                except IndexError:
                    break
        else:
            index = 0
            while True:
                try:
                    asteroid = response1[f"2016-07-{date}"][index]['is_potentially_hazardous_asteroid']
                    if asteroid == True:
                        with open("astorid.csv", "a") as file:
                            file.write(str(response1[f"2016-07-{date}"][index])+"\n")
                    else:
                        pass
                    index += 1
                except IndexError:
                    break
        if message_notification == 1:
            print ('\nPlease wait until the result message...\n')
            message_notification = 0
        else:
            pass   
    else:
        print('Oopss!')
    date = int(date)
    date += 1

result = pd.read_csv('astorid.csv')
print('\nThere are', len(result), 'line(s) in the astorid.csv file\n')