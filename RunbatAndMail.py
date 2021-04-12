import sys
import os
import time
from pynput.keyboard import Key, Controller
import re
# 组号 版本号 接收人
args=sys.argv
print("组件名",args[1], "irds版本号",args[2],"\n")
cmd="knockknock.bat "+args[1]
os.system(cmd)
time.sleep(2)
path="#######"
lines=[]
with open(path,'r') as f:
    lines=f.readlines()
    #print(lines)
target_line =lines[-1]
target_words=target_line.split(' +')
target_words=re.split(" +",target_line)
cover_word=args[1].ljust(14)
lines[-1]=cover_word+lines[-1][len(cover_word):]
time.sleep(1)
password=target_words[2]
print("ok")
print(target_words)
print(password)
with open(path,'w') as f:
    f.writelines(lines)

#zip
import zipfile #引入zip管理模块
import os
import sys #引入sys模块，获取脚本所在目录

#定义一个函数，递归读取absDir文件夹中所有文件，并塞进zipFile文件中。参数absDir表示文件夹的绝对路径。
def writeAllFileToZip(absDir,zipFile,pre):
    for f in os.listdir(absDir):
        absFile=os.path.join(absDir,f) #子文件的绝对路径
        #print(absFile[-3:])
        if absFile[-3:]=="zip":
            pass
        elif os.path.isdir(absFile): #判断是文件夹，继续深度读取。
            #relFile=absFile[len(os.getcwd())+1:] #改成相对路径，否则解压zip是/User/xxx开头的文件。
            zipFile.write(absFile,os.path.join(pre,f)) #在zip文件中创建文件夹
            writeAllFileToZip(absFile,zipFile,os.path.join(pre,f)) #递归操作
        else: #判断是普通文件，直接写到zip文件中。
            #relFile=absFile[len(os.getcwd())+1:] #改成相对路径
            zipFile.write(absFile,os.path.join(pre,f))
    return
    
zipFilePath=os.path.join(sys.path[0],"irds_resource_mapper_"+args[2]+".zip") 
#先定义zip文件绝对路径。sys.path[0]获取的是脚本所在绝对目录。
#因为zip文件存放在脚本同级目录，所以直接拼接得到zip文件的绝对路径。

zipFile=zipfile.ZipFile(zipFilePath,"w",zipfile.ZIP_DEFLATED) 
#创建空的zip文件(ZipFile类型)。参数w表示写模式。zipfile.ZIP_DEFLATE表示需要压缩，文件会变小。ZIP_STORED是单纯的复制，文件大小没变。

absDir="######"
#要压缩的文件夹绝对路径。

writeAllFileToZip(absDir,zipFile,"") #开始压缩。如果当前工作目录跟脚本所在目录一样，直接运行这个函数。
#执行这条压缩命令前，要保证当前工作目录是脚本所在目录(absDir的父级目录)。否则会报找不到文件的错误。
print("压缩成功")
#


#发邮件
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart 
my_sender='#####'    # 发件人邮箱账号
my_pass = '####'              # 发件人邮箱密码
my_user=args[3]      # 收件人邮箱账号，我这边发送给自己
def mail():
    ret=True
    try:
        msg=MIMEMultipart('mixed')
        msg['From']=formataddr(["####",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr([my_user,my_user])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        #msg['cc'] = ','.join(ccto_list)     #抄送
        ccto_list=[]
        ccto_list.append(my_sender)
        msg['cc'] = ','.join(ccto_list) 
        msg['Subject']="#####"                # 邮件的主题，也可以说是标题
        att_zip = MIMEText(open(zipFilePath, 'rb').read(),'base64','utf-8')
        att_zip["Content-Type"] = 'application/octet-stream'
        att_zip["Content-Disposition"] ="attachment; filename=\""+"irds_resource_mapper_"+args[2]+".zip\""
        "attachment; filename=\""+"irds_resource_mapper_"+args[2]+".zip\""
        msg.attach(att_zip)
        context=(
        "#####"
        )
        msg.attach(MIMEText(context, 'plain', 'utf-8'))
        server=smtplib.SMTP_SSL("######", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender,[my_user,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret=False
    return ret
 
ret=mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")


print(password)