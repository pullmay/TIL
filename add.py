# 実行例: python add.py 200515

import sys

path = './diary/index.html'

# https://note.nkmk.me/python-file-io-open-with/
with open(path, encoding='utf-8') as f:
    html = f.readlines()

targetRow = 21 # 追記する行
args = sys.argv # ['.\\add.py', '200515']
# print(type(args)) # list
# print(args[1]) # '200515
# print(type(args[1])) # str

yy = '20' + args[1][0:2] # 2020
mm = args[1][2:4] # 05
dd = args[1][4:6] # 15

addText = '\t\t\t\t\t<li><a href=\"https://pullmay.github.io/TIL/diary/' + args[1] + '.html\">' + yy + '年' + mm + '月' + dd + '日</a></li>\n'

# https://note.nkmk.me/python-grep-like/
# 例外処理をしておきたい
# すでに書き込まれている場合はpassみたいな感じ
# print(html[targetRow])
with open(path, encoding='utf-8', mode='w') as f:
    if html[targetRow] != addText:
        html.insert(targetRow, addText)
        f.writelines(html)
    else:
        f.writelines(html)
