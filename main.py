import requests
import csv
import time
import os
 
def requester(attempts):
    print(f"Attempt {attempts}")

    base_url = 'https://geocoding.geo.census.gov/geocoder/locations/addressbatch'
    parameters = {'benchmark' : 'Public_AR_Current'}
    files = {'addressFile': open('records.csv', 'rb')}

    with open('responses.csv', 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)

        response = requests.post(base_url, params=parameters, files=files, allow_redirects=True)
        info = [(response.status_code, response.text)]

        print(response.status_code)
        print(response.text[:100])

        if "invalid" in response.text or response.status_code != 200:
            csv_writer.writerows(info)

attempts = 0
while True:
    os.system('cls')
    attempts = attempts + 1
    requester(attempts=attempts)
    time.sleep(60)
    