def lines(file):
  for line in file:yield line  #yield生成器
  yield '\n'

def blocks(file):
  block = []
  for line in lines(file):
    if line.strip():   #strip返回移除字符串头尾指定的字符序列生成的新字符串
      block.append(line)  #该方法无返回值，但是会修改原来的列表
    elif block:
      yield ''.join(block).strip()  #join 返回通过指定字符连接序列中元素后生成的新字符串。
      block = []