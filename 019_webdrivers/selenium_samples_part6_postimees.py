from selenium import webdriver
import pandas as pd
import datetime

url = 'https://rus.postimees.ee/'
pd.set_option('display.max_columns', 5)

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

articles = driver.find_elements('class name', 'list-article__text')

article_list = []
for article in articles:
    link = article.find_element('class name', 'list-article__url').get_attribute('href')
    heading = article.find_element('class name', 'list-article__headline').text
    article_item = {
        'heading': heading,
        'link': link
    }
    article_list.append(article_item)

df = pd.DataFrame(article_list)
print(df)
print(df.loc[1]['heading'])
df.to_csv(f'{datetime.date.today().strftime(f"%Y%m%d")}.csv')
driver.quit()

