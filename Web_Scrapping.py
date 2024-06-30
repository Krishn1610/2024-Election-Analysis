import requests
from bs4 import BeautifulSoup
import pandas as pd

#Specifying the URL
url = 'https://results.eci.gov.in/PcResultGenJune2024/candidateswise-S063.htm'

#Fetching the webpage
response = requests.get(url)
if response.status_code == 200:
    webiste_content = response.content

    #Parsing the webpage content
    soup = BeautifulSoup(webiste_content, 'html.parser')

    # Extracting data
    data = []
    web_table = soup.find('table')  
    headers = [header.text for header in web_table.find_all('th')]
    for row in web_table.find_all('tr'):
        columns = row.find_all('td')
        if columns:
            data.append([column.text for column in columns])
    
    #Saving into an Excel file
    df = pd.DataFrame(data, columns=headers)
    df.to_excel('krishn1.xlsx', index=False)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
