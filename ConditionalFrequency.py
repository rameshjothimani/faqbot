import nltk

nltk.download('book')
from nltk import FreqDist
from nltk.corpus import brown

items = ['apple', 'apple', 'kiwi', 'cabbage', 'cabbage', 'potato']
print(nltk.FreqDist(items))
c_items = [('F', 'apple'), ('F', 'apple'), ('F', 'kiwi'), ('V', 'cabbage'), ('V', 'cabbage'), ('V', 'potato')]
cfd = nltk.ConditionalFreqDist(c_items)
cfd.conditions()
print(cfd['F'])

cfd = nltk.ConditionalFreqDist(
    [(genre, word) for genre in brown.categories() for word in brown.words(categories=genre)])
print(cfd.items())
print(cfd.conditions())
cfd.tabulate(conditions=['government'], samples=['leadership'])
news_fd = cfd['news']
print(news_fd)
print(news_fd.most_common(3))