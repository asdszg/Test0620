# -*- coding: utf-8 -*-

import os
import uuid
import urllib2
import cookielib
import xml.dom.minidom
from bs4 import BeautifulSoup
# # 文件保存路径
# path = "D:\\ljq"
# #读取你爬下来的文件路径
# dir="C:\\Users\\szg\\Desktop\\better-pos"

# '''创建文件目录，并返回该目录'''
# def mkdir(path):
#     # 去除左右两边的空格
#     path=path.strip()
#     # 去除尾部 \符号
#     path=path.rstrip("\\")

#     if not os.path.exists(path):
#         os.makedirs(path)
        
#     return path

# if __name__ == "__main__":

#     for root,dirs,files in os.walk(dir):
#         for file in files:
#             print os.path.join(root,file)
#             filexml = os.path.join(root,file)
#             DOMTree = xml.dom.minidom.parse(filexml)
#             collection = DOMTree.documentElement
#             items = collection.getElementsByTagName("item")
#             for item in items:
#                 url1 = item.getElementsByTagName('asd')[0].childNodes[0].data
#                 url = "http://www.gettyimages.co.uk"+url1+"/license"
#                 response = urllib2.urlopen(url)  
#                 html = response.read()  
#                 soup = BeautifulSoup(html, "html.parser")
#                 # save_file("d:/ljq/", unique_str()+".jpg", get_file(url))
#                 print soup.h1
#                 img = soup.find(attrs={"ng-if":"!isModalOpen"})
#                 print img
#                 print "---------"
#                 imageurl = img.img.get("src")
#                 print "----------"
#                 file_name = soup.h1.string+".jpg"
#                 mkdir(path)
#                 if(not path.endswith("/")):
#                     path=path+"/"
#                 file=open(path+file_name, "wb")  
#                 data = urllib2.urlopen(imageurl).read()
#                 if data:

#                     file.write(data)
#                     file.flush() 
#                     file.close()
#                 else:
#                     print "图片没有下载"

#                 flag = soup.find(attrs={"class": "asset-caption"})
#                 if flag==None:    
#                     print "None"
#                     print "一个图片信息over"
#                     continue
#                 else:
#                     print flag
#                     print soup.find(attrs={"class": "asset-caption"}).string
#                     print "一个图片信息over"

#             print "一个文件完毕"
#         print "一个文件夹over"
#这是什么鬼东西
#原始路径
path = "C:\\Users\\szg\\Desktop\\better-pos"
#进入的文件夹
wenjianname = "111"
new_path = os.path.join(path, wenjianname)
if not os.path.isdir(new_path):
    os.makedirs(new_path)
file_object = open(new_path+"\\111.txt", 'w')
data='111'
file_object.write(data)
file_object.close( )
print "over"
