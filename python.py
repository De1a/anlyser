import re
keyword = {'if', 'int', 'for', 'while', 'do', 'return', 'break', 'continue'}

Symbol = {'+', '-', '*', '/', '=', '', '<', '=', '<=', '!='}
Symbol2 = {',', ';', '{', '}', '(', ')'}

# 总正则表达式
# all=re.compile('(\d+\.\d+[eE][-+]?\d+|\d+\.\d+|[1-9]\d*|0[0-7]+|0x[0-9a-fA-F]+|[a-zA-Z_]\w*|&gt;&gt;|&lt;&lt;|::|-&gt;|\.|\+=|\-=|\*=|/=|%=|&gt;=|&lt;=|==|!=|&amp;&amp;|\|\||\+|\-|\*|/|=|&gt;|&lt;|!|^|%|~|\?|:|,|;|\(|\)|\[|\]|\{|\}|\'|\")')
all = re.compile('([0-9]+[a-z|A-Z|_]+[0-9]*|\d+\.\d+[eE][-+]?\d+|\d+\.\d+|[1-9]\d*|0[0-7]+|0x[0-9a-fA-F]+|'
                 '[a-z|A-Z|0-9|_]*\".*?\"[a-z|A-Z|0-9|_]*|[a-zA-Z_]\w*|\".*\"|>>|<<|'
                 '::|->|\+=|\-=|\*=|/=|%=|>=|<=|==|!=|&&|\|\||\+|\-|\*|/|=|>|'
                 '<|!|\^|%|\~|\?|:|,|;|\(|\)|\[|\]|\{|\}|\"|\')')


def Judge(s):
    if s[0].isalpha() and s in keyword:  # 判断保留字
        print('(', 1, ',', '"', s, '"', ')', sep='')
    elif s[0].isalpha() and s not in keyword and s.isalnum():  # 判断标识符
        print('(', 2, ',', '"', s, '"', ')', sep='')
    elif s.isdigit():  # 判断数字
        print('(', 3, ',', '"', s, '"', ')', sep='')
    elif s in Symbol:  # 判断运算符
        print('(', 4, ',', '"', s, '"', ')', sep='')
    elif s in Symbol2:  # 判断边界符
        print('(', 5, ',', '"', s, '"', ')', sep='')

    else:
        if len(s) >= 2 and s[0] == '"' and s[-1] == '"'or s=='\n':  # 判断字符串
            print(end="")
        else:
            print('(', 'error', ',', '"', s, '"', ')', sep='')  # 没定义或者错误串


if __name__ == '__main__':
    # 读取文件
    f = open('./test.txt', 'r')
    result = []
    for line in f:
        if len(line) == 1:
            result.extend(line)
        else:
            result.extend(all.findall(line))
    # print(result)
    # 去掉列表中残留的空字符
    for i in result:
        if '' in result:
            result.remove('')

    # 词法分析
    for i in result:
        Judge(i)
