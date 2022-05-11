# +----------------------------------------------------------------------
# | Author:Stark
# +----------------------------------------------------------------------
# | Date:2022/5/11
# +----------------------------------------------------------------------
# | Desc: 运行环境 Python 3.10.4 jieba 分词\过滤
# +----------------------------------------------------------------------

import jieba
import jieba.posseg as psg

word = "啊啊啊啊啊 , 我超爱嘉嘉牌地宝的啊!   大大求更新啊   我爱您啊"
words = list(jieba.cut(word))

# 添加过滤规则
stop_words = [" ", "!", ","]

filter_words = []
for x in words:
    if x not in stop_words:
        filter_words.append(x)
print(filter_words)

words5 = [(w.word, w.flag) for w in psg.cut(word)]

print(words5)

# paddle tag table 保留词
saved = ['n','r']
words5 = [x for x in words5 if x[1] in saved ]
print(words5)
