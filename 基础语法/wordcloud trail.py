import wordcloud
import jieba
txt = "程序设计语言是计算机能够理解和识别用户操作意图的一种交互体系"
c = wordcloud.WordCloud(width=1000,height=700,font_path="msyh.ttc")
c.generate(" ".join(jieba.lcut(txt)))
c.to_file("myjpg.jpg")