import nltk
from newspaper import Article
from textblob import TextBlob
#  only for initial use - nltk.download('punkt')


def summarise_my_article(myUrl):
    url = myUrl
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
    sentiment = ''
    if analysis.polarity > 0:
        sentiment = "article shows positive sentiment 😊👍"
    elif analysis.polarity < 0:
        sentiment = "article shows negative sentiment 👎😢"
    else:
        sentiment = "neutral sentiment 🙄"
    return {'title': article.title, 'authors': article.authors, 'published_date': article.publish_date, 'summary': article.summary, 'sentiment': sentiment}
