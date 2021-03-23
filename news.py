import os
import jieba
from jieba import analyse
from docx import Document
tfidf = analyse.extract_tags
doc = Document(os.path.join("text","news.doc"))
paras = []
for each in doc.paragraphs:
    paras.append(each.text)
string = " ".join(paras)
for it in paras:
    seg_list = jieba.cut(it, cut_all=False)
    # print("Full Mode: " + "/ ".join(seg_list))  
    keywords = tfidf(it)
    print("key words: " +"/ ".join(keywords))
keywords = tfidf(string)
print("key words: " +"/ ".join(keywords))