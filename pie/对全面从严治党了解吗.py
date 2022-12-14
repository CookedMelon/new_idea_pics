# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
plt.figure(1, figsize=(7,5))
expl = [0.20,0.0,0.15,0.10]
colors  = ["tomato","cornflowerblue","cyan","yellow"]
labels   = ['非常了解', '比较了解', '不太了解', '完全不了解']
quants   = [10,44,28,3]
title='对全面从严治党了解程度'

plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.rcParams['font.sans-serif'] = ['LiSu']# 用来正常显示中文标签
def my_lebal(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}%\n({:d}人)".format(pct, absolute)
def draw_pie(labels,quants):
    plt.pie(quants, explode=expl, colors=colors, labels=labels,autopct=lambda x:my_lebal(x,quants),pctdistance=0.6, shadow=True, labeldistance=1.1, startangle=20,center=(0, 0),wedgeprops={'lw':1,'ec':'lightblue'},textprops={'fontsize': 15, 'color': 'k'})
    plt.title(title,fontweight='bold',fontdict={'fontsize': 26},y=0.98)
    plt.legend(loc="best",bbox_to_anchor=(1.05,1.0),borderaxespad = 0.)
 
draw_pie(labels,quants)
plt.savefig('./pic/'+title+'.jpg') 