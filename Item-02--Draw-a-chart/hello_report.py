# coding=gbk

from reportlab.graphics.shapes import Drawing,String
from reportlab.graphics import renderPDF

d = Drawing(100,100)   #���ƾ��ο�ĳ���
s = String(50,50,'hello,word!',textAnchor='middle') #500,500:�����ı������С
s1 = String(50,50,'Jenny!',textAnchor='middle') #500,500:�����ı������С

d.add(s)  #add() �������ڸ��������Ԫ�أ������ӵ�Ԫ���ڼ������Ѵ��ڣ���ִ���κβ���

renderPDF.drawToFile(d,'hello.pdf','A simple PDF file')