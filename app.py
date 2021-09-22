import tkinter as tk
import nltk
from newspaper import Article
from textblob import TextBlob
nltk.download('punkt')
url = "https://timesofindia.indiatimes.com/india/will-focus-on-covid-terror-climate-crisis-at-un-pm-modi/articleshow/86439798.cms"
article = Article(url)
article.download()
article.parse()

article.nlp()
print('Title: {0}'.format(article.title,))
print('Authors: {0}'.format(article.authors,))
print('Published Date: {0}'.format(article.publish_date,))
print('Summary: {0}'.format(article.summary,))

analysis = TextBlob(article.text)
print(analysis.polarity)  # basically the sentiment
if analysis.polarity > 0: 
    print("article shows positive sentiment 😊👍")
elif analysis.polarity < 0:
    print("article shows negative sentiment 👎😢")
else:
    print("neutral sentiment 🙄")