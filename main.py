from os import path
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

path.os.path.dirname(path.os.path.realpath('__file__'))

# text = open('NPAY-679.txt', 'r').read()
# text = open('PAG-6411.txt', 'r').read()

# adiciona os stopwords
stopwords = set(STOPWORDS)
for word in open('stopwords-pt.txt', 'r').read().split('\n'):
    stopwords.add(word)

# cria a wordcloud definindo fonte tamanho maximo
plt.figure()
# plt.imshow(WordCloud(max_font_size=40, stopwords=stopwords).generate(open('NPAY-679.txt', 'r').read()), interpolation="bilinear")
# plt.imshow(WordCloud(max_font_size=40, stopwords=stopwords).generate(open('PAG-6411.txt', 'r').read()), interpolation="bilinear")
# plt.imshow(WordCloud(max_words=20, max_font_size=40, stopwords=stopwords).generate(open('1007.txt', 'r').read()), interpolation="bilinear")
# plt.imshow(WordCloud(max_words=30, max_font_size=40, stopwords=stopwords).generate(open('silvio-santos.txt', 'r').read()), interpolation="bilinear")
plt.imshow(WordCloud(max_words=30, max_font_size=40, stopwords=stopwords).generate(open('poscomp2016.txt', 'r').read()), interpolation="bilinear")
plt.axis("off")
plt.show()

# Salva o arquivo da imagem
# wordcloud.to_file(path.join(d, "word_cloud_2.png"))