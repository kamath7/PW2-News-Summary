import tkinter as tk 
import nltk 
from newspaper import Article

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