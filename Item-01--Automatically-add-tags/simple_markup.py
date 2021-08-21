import sys,re
from util import *

print('<html><title>...</title><body>')

title = True
for block in blocks(sys.stdin):  #sys.stdin是一个标准化输入的方法
  block = re.sub(r'\*(.+?)\*',r'<em>\1</em>',block)   #sub 匹配字符替换

  if title:
    print('<h1>')
    print(block)
    print('</h1>')
    title = False
  else:
    print('<p>')
    print(block)
    print('</p>')

print('</body></html>')