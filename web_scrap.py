from selenium import webdriver
from bs4 import BeautifulSoup 
import pandas as pd

def main():
    # setting up
    # driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
    driver = webdriver.Edge('/usr/lib/msedgedriver.exe')
    date = []
    weather_discribe = []
    temperature = []
    humidity = []
    rain_prob = []
    driver.get("https://www.hko.gov.hk/tc/wxinfo/currwx/fnd.htm")
    content = driver.page_source
    # print(content)
    # parsing the HTML document
    soup = BeautifulSoup(content, "html5lib")
    for data in soup.findAll('div', attrs={"class":"old_fnd_item"}):
        d,p= data.findAll('div', attrs={"class":"old_fnd_upper"})
        date.append(d.text)
        weather_discribe.append(p.next.attrs['alt'])
        temperature.append(data.find('div', attrs={"class": "old_fnd_min_temp"}).text.replace('|','-'))
        humidity.append(data.find('span', attrs={"class": 'old_fnd_hum_val'}).text)
        rain_prob.append(data.find('div', attrs={"class": "psr_value"}).text)

    driver.close()

    for i in range(len(weather_discribe)):
        print(f"{date[i]}, {weather_discribe[i]}, {temperature[i]}, {humidity[i]}, {rain_prob[i]}")
    
    df = pd.DataFrame({'Date': date,'weather discribe':weather_discribe,'temperature':temperature, 'humidity': humidity, 'rain probability': rain_prob}) 
    df.to_csv('weather_prediction.csv', index=False, encoding='utf-8-sig')



if __name__ == "__main__":
    main()