from storage import *
import random
import time
import os
import sys
#region Sell
def Inputdict(list_treasure):
    while True:
        os.system("clear")
        dic_test = {}
        name = input("name of treasure: ")
        price = int(input("price you want to sell: "))
        dic_test["name"] = name
        dic_test["price"] = price
        list_treasure[len(list_treasure) + 1] = dic_test
        user_input = input("do you want to sell more?? Y or N").lower()
        if user_input == "y":
            continue
        if user_input == "n":
            menu()
#endregion

#region Buy
def display_list(list_treasure):
    os.system("clear")
    x = [i for i in list_treasure.keys()]
    for i in range(0,len(x)):
        print(f"{x[i]} : {list_treasure[x[i]]['name']}")
    print("type q for exit")
    user_input = input("Choose the treasure to bid :").lower()
    keys = [i for i in list_treasure.keys()]
    for name in keys:
        if user_input == name.lower():
            display = [str(x) + ": " + str(y) for x, y in list_treasure[name].items()]
            for i in range(0, len(display)):
                print(f"{display[i]}")
            bid(customer_name_dic,list_treasure,user_input)
    if user_input == "q":
        menu()
def bid(customer_name_dic,list_treasure,user_input):
    os.system("clear")
    while True:
        print(user_input)
        cus1_price = int(input("What's the price will you pay for it?? :"))
        cus2_price = 0
        cus3_price = 0
        if cus1_price > 150000:
            print(f"{customer_name_dic['cus2']} refuse to rise up")
            cus2_price = -1
        else:
            cus2_price = random.randint(cus1_price,150000)
            print(f"{customer_name_dic['cus2']} pay {cus2_price} for it")
        if cus1_price > 900000:
            print(f"{customer_name_dic['cus3']} refuse to rise up")
            cus3_price = -1
        else:
            if cus1_price > 150000:
                cus3_price = random.randint(cus1_price,900000)
            else:
                cus3_price = random.randint(cus2_price,900000)
            print(f"{customer_name_dic['cus3']} pay {cus3_price} for it")
        if cus2_price == -1 and cus3_price == -1:
            print(f"{customer_name_dic['cus1']} win the auction")
            time.sleep(3)
            display_list(list_treasure)
        user_choice = input("if you want to continue, type 1. type 2 for exit ")
        if user_choice == "1":
            continue
        if user_choice == "2":
            print(f"{customer_name_dic['cus3']} win the auction")
            time.sleep(3)
            display_list(list_treasure)
    display_list(list_treasure)
def menu():
    os.system("clear")
    while True:
        a = input("type 1 if you want to sell something \ntype 2 for join a auction\ntype q for exit \n")
        if a == "1":
            sys.stdin.flush()
            Inputdict(list_treasure)
        if a == "2":
            sys.stdin.flush()
            display_list(list_treasure)
        if a == "q":
            exit()
#endregion