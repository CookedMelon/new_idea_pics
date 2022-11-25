import matplotlib.pyplot as plt
from matplotlib import font_manager
for font in font_manager.fontManager.ttflist:
    if 'SIMLI.TTF' in font.fname:
        print(font.name, font.fname)
    # print(font.name,'-',font.fname)