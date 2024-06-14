from selenium import webdriver
# install selenium and keep running the code ignore smadav 
Keyword =input ('Enter the search term ')
# make sure to chech out your system chrome driver on chrome
browser = webdriver.Chrome()
browser.get ('https://google.co.in/search?q='+Keyword)

# run it using termina 'python google_search.py'