# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
plt.figure(1, figsize=(6.5,5))
expl = [0.05,0.15,0,0.1,0.05,0.1]   #第二块即China离开圆心0.1
colors  = ["cornflowerblue","tomato","coral","lightgreen","yellow","orange"]  #设置颜色（循环显示）
labels   = ['党建', '国防', '科技发展', '教育','民生','生态建设']
quants   = [9,31,28,26,42,11]
title='最关注的方面'

plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.rcParams['font.sans-serif'] = ['LiSu']# 用来正常显示中文标签
def my_lebal(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}%\n({:d}人)".format(pct, absolute)
def draw_pie(labels,quants):
    plt.pie(quants, explode=expl, colors=colors, labels=labels,autopct=lambda x:my_lebal(x,quants),pctdistance=0.6, shadow=True, labeldistance=1.05, startangle=85,center=(0, 0),wedgeprops={'lw':1,'ec':'lightblue'},textprops={'fontsize': 15, 'color': 'k'})
    plt.title(title,fontweight='bold',fontdict={'fontsize': 26},y=1,loc='center')
    plt.legend(loc="best",bbox_to_anchor=(1.05,1.0),borderaxespad = 0.)
 
draw_pie(labels,quants)
plt.savefig('./pic/'+title+'.jpg') 