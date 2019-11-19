import wordcloud
import jieba

f = open("government_report.txt","r",encoding="utf-8")
txt = f.read()
f.close()
ls = jieba.lcut(txt)
w = wordcloud.WordCloud(width=1200,height=800,background_color="white",font_path = "msyh.ttc",
min_font_size=6)
w.generate(" ".join(ls))
w.to_file("goverment report wordcloud.jpg")