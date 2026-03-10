from wordcloud import WordCloud
import numpy as np
from PIL import Image
##pip install wordcloud
##pip install numpy
##pip install Pillow

text = '''Love is a river that flows so free,
A beautiful sight for all to see.
It glides around every bend,
A source of life that never ends'''

mask = np.array(Image.open('circle.png'))
wc = WordCloud(background_color= 'white', mask=mask, contour_width=3, contour_color='steelblue')

wc.generate(text)
wc.to_file('wc_result.png')