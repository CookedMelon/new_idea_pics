# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
plt.figure(1, figsize=(6,6))
expl = [0.05,0.05,0.05,0.15]   #第二块即China离开圆心0.1
colors  = ["tomato","cornflowerblue","yellow","coral"] 
labels   = ['个人兴趣', '教学要求', '线上推送', '自身发展']
quants   = [21,48,5,11]
title='观看原因'

plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.rcParams['font.sans-serif'] = ['LiSu']# 用来正常显示中文标签
def my_lebal(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}%\n({:d}人)".format(pct, absolute)
def draw_pie(labels,quants):
    plt.pie(quants, explode=expl, colors=colors, labels=labels,autopct=lambda x:my_lebal(x,quants),pctdistance=0.6, shadow=True, labeldistance=1.0, startangle=50,center=(0, 0),wedgeprops={'lw':1,'ec':'lightblue'},textprops={'fontsize': 15, 'color': 'k'})
    plt.title(title,fontweight='bold',fontdict={'fontsize': 26},y=0.98)
 
draw_pie(labels,quants)
plt.savefig('./pictures/pic/'+title+'.jpg') 