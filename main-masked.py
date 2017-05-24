from os import path
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

files_dir = 'files/text/'
imgs_dir = files_dir + 'imgs/'

img_filename = 'neo.png'
img_mask_filename = 'neo-mask.jpg'
mask = np.array(Image.open(path.join(imgs_dir, img_mask_filename)))

stopwords = set(STOPWORDS)
stopwords.add('vá')
stopwords.add('vou')
stopwords.add('vamos')
for word in open(path.join(files_dir, 'stopwords-pt.txt'), 'r').read().split('\n'):
    stopwords.add(word)

text = open(path.join(files_dir, 'Matrix.srt'), 'r').read()

wc = WordCloud(background_color='white', max_words=300, stopwords=stopwords, mask=mask)
wc.generate(text)

image_colors = ImageColorGenerator(mask)
plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis("off")
plt.figure()
# plt.show()

wc.to_file(path.join(imgs_dir, img_filename))
