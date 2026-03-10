from wordcloud import WordCloud, STOPWORDS
import wikipedia

wiki = wikipedia.page('Artificial intelligence')
text = wiki.content

s_words = STOPWORDS.union({'use', 'will'})
wc = WordCloud(stopwords=s_words)
wc.generate(text)
wc.to_file('wiki_res.png')