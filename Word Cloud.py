
from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS


f = open('Ev_Scan.txt','r')



document = f.read()
print(len(document))

wordcloud = WordCloud(width=600, height=480, colormap="Oranges_r").generate(document)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.margins(x=0, y=0)
plt.tight_layout(pad = 0)
plt.show()