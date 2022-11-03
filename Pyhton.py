#Billing Code with pyhton 
from datetime import datetime
name = input("Enter your Name: ")
lists = '''
Rice       Rs 50/kg
Salt       Rs 10/Kg
Colgate    Rs 60/Kg
Surf Excel Rs 100/Kg
Cool Drink Rs 40/Kg
Tin        Rs 50/Kg
'''
#Declarations given to all the headings 

price = 0
price_list =[]
Total_price =0
Final_price=0
ilist=[]
qlist=[]
plist=[]

#price tags to all the items
items ={'Rice':50,'Salt':10,'Colgate':60,'Surf Excel':100,'Cool Drink':40,'Tin':50,'biscuits':30,'Milk':20}

#conditions for the processing price of items

option = int(input("for list of items press 1 : "))
if option == 1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exit : "))
    if inp1==2:
      break
    if inp1==1:
        item=input("Enter your items: ")
        quantity =int(input("Enter the Quanity you want: "))
        if item in items.keys():
            price=quantity*(items[item])
            
# trail RUn 
            price_list.append((item,quantity,items,price))
            Total_price+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(Total_price*5)/100
            Final_price = gst+Total_price
        else:
            print("sorry the item is not avalilable")
    else:
        Print("the number entered is wrong, /n/t try again with correct number")
inp = input("do you want to bill the items? Yes or No : ")
if inp == 'yes':
    pass
if Final_price !=0:
    for i in range(len(price_list)):
      print(i,ilist[i],qlist[i],plist[i])
      print("Thank you, See you soon Again")

