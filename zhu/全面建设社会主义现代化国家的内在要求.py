# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
plt.figure(1, figsize=(6.5,7))
expl = [0.05,0.05,0.05,0.1]
colors  = ["cornflowerblue","yellow","tomato","coral"]
labels   = ['尊重自然', '顺应自然', '保护自然','坚持改革开放']
quants   = [74,63,81,69]
title='全面建设社会主义现代化国家的\n内在要求'
title2='全面建设社会主义现代化国家的内在要求'
sum=85


plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.rcParams['font.sans-serif'] = ['LiSu']# 用来正常显示中文标签
def my_lebal(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:d}人\n{:.1f}%".format(absolute,pct)
def draw_bar(labels,quants):
    plt.bar(range(len(quants)),quants,color=colors,ec='lightblue',hatch='/')
    plt.xticks(range(len(quants)),labels,fontsize=15)
    plt.yticks(fontsize=15)
    plt.title(title,fontweight='bold',fontdict={'fontsize': 26},y=1.02)
    plt.legend(loc="best",bbox_to_anchor=(1.05,1.0),borderaxespad = 0.)
    plt.ylabel('人数（共'+str(sum)+"人）",fontsize=15)
    plt.ylim(0,sum+5)

    # 显示数据标签
for a,b in zip(range(len(labels)), quants):
    text=my_lebal(b,quants)
    plt.text(a,b,
            text,
            ha='center', 
            va='bottom',
    )
draw_bar(labels,quants)
plt.savefig('./pic/'+title2+'.jpg') 