from os import path
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

files_dir = 'files/text/'
imgs_dir = files_dir + 'imgs/'

# text_file = 'Matrix.srt'
text_file = 'senhor_dos_aneis.srt'

stopwords = set(STOPWORDS)
for word in open(path.join(files_dir, 'stopwords-pt.txt'), 'r').read().split('\n'):
    stopwords.add(word)

text = open(path.join(files_dir, text_file), 'r').read()

plt.figure()

wc = WordCloud(background_color='white', max_words=30, stopwords=stopwords)
wc.generate(text)

plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()