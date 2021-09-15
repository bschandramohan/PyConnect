from selenium import webdriver

chrome_driver_path="/Users/Chandra/Softwares/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://medium.com/TechieConnect")  # Opens up a web-browser with the URL
article_title = driver.find_element_by_css_selector("h1.js-collectionName")  # Gets elements in the website opened
print("Title: ", article_title.text, "\n\n")

articles_list = driver.find_elements_by_class_name("u-breakWord")

articles_title_list = [article.text for article in articles_list]
print(articles_title_list)

driver.close()
