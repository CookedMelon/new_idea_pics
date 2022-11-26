# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
plt.figure(1, figsize=(6.5,5))
expl = [0.05,0.25,0.15,0.1]   #第二块即China离开圆心0.1
colors  = ["tomato","plum","yellow","aquamarine"]  #设置颜色（循环显示）
labels   = ['共青团员', '群众', '党员', '预备党员']
quants   = [95,17,8,7]
title='政治面貌'

plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.rcParams['font.sans-serif'] = ['LiSu']# 用来正常显示中文标签
def my_lebal(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}%\n({:d}人)".format(pct, absolute)
def draw_pie(labels,quants):
    plt.pie(quants, explode=expl, colors=colors, labels=labels,autopct=lambda x:my_lebal(x,quants),pctdistance=0.6, shadow=True, labeldistance=1.05, startangle=75,center=(0, 0),wedgeprops={'lw':1,'ec':'lightblue'},textprops={'fontsize': 15, 'color': 'k'})
    plt.title(title,fontweight='bold',fontdict={'fontsize': 26},y=0.98,loc='center')
    plt.legend(loc="best",bbox_to_anchor=(1.05,1.0),borderaxespad = 0.)
 
draw_pie(labels,quants)
plt.savefig('./pic/'+title+'.jpg') 
