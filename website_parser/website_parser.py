from bs4 import BeautifulSoup
import requests

response = requests.get("https://medium.com/techieconnect")
# print(response.text[:100])
# print("\n\n\nAnd content is")
# print(response.content[:20])

soup = BeautifulSoup(response.text, "html.parser")
article_title = soup.find(name="h1", class_="js-collectionName")
print("Blog Name:", article_title.getText(), "\n")

articles_list = soup.find_all(class_="u-breakWord")
# articles_list = soup.select(selector="js-collectionName")
# print(articles_list)

# for i in range(len(articles_list)):
#     article = articles_list[i]
#     print(f"{i+1}. {article.getText()}")

# Another way
articles_title = [article.getText() for article in articles_list]
print(articles_title)
