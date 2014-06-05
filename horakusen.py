# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid.axislines import SubplotZero


# 図の背景の諸体裁を設定

# 作図スペースを用意(?)。個々のコードの意味がわかりません。	
fig = plt.figure(1)
ax = SubplotZero(fig, 111)
fig.add_subplot(ax)

# 軸の設定
ax.axhline(linewidth=1.2, color="black")
ax.axvline(linewidth=1.2, color="black")

# 軸に矢印
for direction in ["xzero", "yzero"]:
	ax.axis[direction].set_axisline_style("-|>")
	ax.axis[direction].set_visible(True)

# 四方のaxis(?)、spine(?)を消す	
for direction in ["left", "right", "bottom", "top"]:
	ax.axis[direction].set_visible(False)

# 軸に名前を付ける。位置は適宜設定。	
plt.figtext(0.93, 0.37, 'x')  
plt.figtext(0.505, 0.95, 'y')

# 軸の目盛を消す。表示するy軸の範囲を設定(グラフが見易くなるよう適宜設定)。
plt.xticks([])
plt.yticks([])		
plt.ylim(-3.5,6.5)


# 図を描く条件設定

# 元になる関数を定義
def f(x, t):
    return t * x - t**2

# 変数
savever = 'png' # 'png' or 'pdf'
fignum = 3 # 0 or 1

if fignum == 0:  
    p = 5    #xの範囲　-p<=x<=p (左右対称にするため)
    r = 2    #tの範囲　-r<=t<=r (同上)
    n = 12   #接線の本数

if fignum == 1:
    p = 5
    r = 3
    n = 30
	
# 包絡線を作る
x = np.linspace(-p,p,2)    # 直線なのでプロットする点は２点でいいかと。xはリストと同じ性質(?)なのに、どうしてf関数のxに入れるのかわかりません。(arrayだから？)
t = np.linspace(-r,r,n)  # 傾きはn-1等分で均等に。lispaceで範囲内をn-1等分したarray(配列？)を用意。
for i in t:
	y = f(x, t=i)
	ax.plot(x, y, 'k-', linewidth=1.0, alpha=0.6)
plt.savefig('envelope' + str(fignum) + '.' + savever)
plt.show()