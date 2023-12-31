from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/newest")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="a", rel="nofollow noreferrer")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)


article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_upvotes)


most_upvotes = max(article_upvotes)
index_upvotes = article_upvotes.index(most_upvotes)
print(article_texts[index_upvotes])
print(article_links[index_upvotes])
print(most_upvotes)



