# coding=gbk

from reportlab.graphics.shapes import Drawing,String
from reportlab.graphics import renderPDF

d = Drawing(100,100)   #控制矩形框的长宽
s = String(50,50,'hello,word!',textAnchor='middle') #500,500:控制文本字体大小
s1 = String(50,50,'Jenny!',textAnchor='middle') #500,500:控制文本字体大小

d.add(s)  #add() 方法用于给集合添加元素，如果添加的元素在集合中已存在，则不执行任何操作

renderPDF.drawToFile(d,'hello.pdf','A simple PDF file')