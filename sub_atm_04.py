#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 16:28:28 2019

@author: liu640
"""

import csv 

card_list = []
with open('mycsvfile.csv') as fr:
        fread=csv.reader(fr)
        for card_dict in fread:
                print(card_list)
                card_dictOld = {"name":card_dict[0],"y_account":card_dict[1],"y_code":card_dict[2],"y_ini_money":int(card_dict[3])}
                card_list.append(card_dictOld)
#card_dict={}
 
def new_card():

                    
#   global card_list
    name = input("請輸入姓名：")
    y_account = input("請輸入帳號：")
    y_code = input("請輸入初始密碼(0000)：")
    y_ini_money =int( input("請輸入初始金額："))
    # 2. 將用戶信息保存到一個字典
    card_dict = {"name": name,
                 "y_account": y_account,
                 "y_code": y_code,
                 "y_ini_money": y_ini_money}

    # 3. 將用戶字典添加到用戶列表
    card_list.append(card_dict)
  
    with open('mycsvfile.csv','w', newline='') as f:
        w = csv.writer(f)
        #w.writerow(card_dict.keys())
        for card_dict in card_list:  
            w.writerow(card_dict.values())  
    with open('mycsvfile.csv') as fr:
        fread=csv.reader(fr)
        for row in fread:
            print(row)
            
    
def chpassword():

    # 5. 首次登入需修改密碼
    in_account = input("請輸入您的賬號：")
    in_code = input("請輸入您的密碼：")
    print(card_list)
    for card_dict in card_list:
        print('99999')
        print(card_dict["y_account"], in_account, card_dict["y_code"] , in_code)
        if card_dict["y_account"] == in_account and card_dict["y_code"] == in_code:
            print("登錄成功，請變更密碼!")
            card_dict["y_code"]=input("請您輸入要更新的密碼：")
            print(card_dict['name']+"密碼變更成功")
            break

    with open('mycsvfile.csv','w') as f:
        w = csv.writer(f)
        #w.writerow(card_dict.keys())
        for card_dict in card_list:  
            w.writerow(card_dict.values())  
    with open('mycsvfile.csv') as fr:
        fread=csv.reader(fr)
        for row in fread:
            print(row)

def login():
    # 6. 登入ATM系統                 
#        i=3
    in_account = input("請輸入您的賬號：")
    in_code = input("請輸入您的密碼：")
    
    for v in range(len(card_list)):
    
        if in_account == card_list[v]["y_account"] and in_code == card_list[v]["y_code"]:
            
            print("恭喜登錄成功")
            
            break
            
        else:
            print("帳號密碼錯誤一次")
            in_account = input("請輸入您的賬號：")
            in_code = input("請輸入您的密碼：")
    
            for v in range(len(card_list)):
    
                if in_account == card_list[v]["y_account"] and in_code == card_list[v]["y_code"]:
            
                    print("恭喜登錄成功")
            
            
            






























       
#        while i>=3:    
# =============================================================================
#     for card_dict in card_list:
#         if card_dict["y_account"] == in_account and card_dict["y_code"] == in_code:
#             print("歡迎使用 簡易版ATM功能")
#             break #感覺會有問題
#         else:
#             print("帳號或密碼錯誤1次")
#             print(card_list)
#             print(card_dict)
#             print(card_dict["y_account"],card_dict["y_code"])
#             in_account = input("請輸入您的賬號：")
#             in_code = input("請輸入您的密碼：")
#             if card_dict["y_account"] == in_account and card_dict["y_code"] == in_code:
#                 print("歡迎使用 簡易版ATM功能")
#                 break #感覺會有問題
#             else:
#                 print("帳號或密碼錯誤2次")
#                 in_account = input("請輸入您的賬號：")
#                 in_code = input("請輸入您的密碼：")
#                 if card_dict["y_account"] == in_account and card_dict["y_code"] == in_code:
#                     print("歡迎使用 簡易版ATM功能")
#                     break #感覺會有問題
#                 else:
#                     print("輸入錯誤，回到主選單")
#                     break #感覺會有問題 
# =============================================================================
def save_money():   
    # 7. 存款  
    in_account = input("請輸入您的賬號：")
    in_code = input("請輸入您的密碼：")
    de_money= int(input("請輸入您的存款金額："))
    for card_dict in card_list:
        if card_dict["y_account"] == in_account and card_dict["y_code"] == in_code:
            card_dict["y_ini_money"]+=de_money
            print("您成功存款{}元".format(de_money))
            print("您存款總共有"+str(card_dict["y_ini_money"])+"元")        
# =============================================================================
#     for v in range(len(card_list)):
#     
#         if in_account == card_list[v]["y_account"] and in_code == card_list[v]["y_code"]:
#             print("歡迎使用存款功能")
#             card_list[v]["y_ini_money"]+=de_money
#             print("您成功存款{}元".format(de_money))
#             print("您存款總共{}元".format(card_list[v]["y_ini_money"]))
# =============================================================================
            
            
    with open('mycsvfile.csv','w') as f:
        w = csv.writer(f)
        #w.writerow(card_dict.keys())
        for card_dict in card_list:  
            w.writerow(card_dict.values())  
    with open('mycsvfile.csv') as fr:
        fread=csv.reader(fr)
        for row in fread:
            print(row)       

def get_money():
    # 8. 取款       
    in_account = input("請輸入您的賬號：")
    in_code = input("請輸入您的密碼：")
    out_money= int(input("請輸入您的取款金額：")) 

    for card_dict in card_list:
        if card_dict["y_account"] == in_account and card_dict["y_code"] == in_code:
            card_dict["y_ini_money"]-=out_money
            print("您成功取款{}元".format(out_money))
            print("您存款總共剩"+str(card_dict["y_ini_money"])+"元")
    
    with open('mycsvfile.csv','w') as f:
        w = csv.writer(f)
        #w.writerow(card_dict.keys())
        for card_dict in card_list:  
            w.writerow(card_dict.values())  
    with open('mycsvfile.csv') as fr:
        fread=csv.reader(fr)
        for row in fread:
            print(row)
            
