
from unittest import result

def Standard_time(x,y):
    load()
    if t1['s']==60 :
        t1['m'] = t1['m']+1
    if t1['s'] > 60 :
        b = int(t1['s']/ 60)
        a = t1['s']% 60
        t1['m'] = t1['m']+b
        t1['s'] = a
    if t1['m']==60 :
        t1['h'] = t1['h']+1
    if t1['m'] > 60 :
        b = int(t1['h']/ 60)
        a = t1['m']% 60
        t1['h'] = t1['h']+b
        t1['m'] = a
    print(t1)
    if t2['s']==60 :
        t2['m'] = t1['m']+1
    if t2['s'] > 60 :
        b = int(t2['s']/ 60)
        a = t2['s']% 60
        t2['m'] = t1['m']+b
        t2['s'] = a
    if t2['m']==60 :
        t2['h'] = t2['h']+1
    if t2['m'] > 60 :
        b = int(t2['h']/ 60)
        a = t2['m']% 60
        t2['h'] = t2['h']+b
        t2['m'] = a
    print(t2)

def total_time(x,y):
    Standard_time(t1,t2)
    result={} 
    result['s'] = t1['s'] + t2['s']
    result['m'] = t1['m'] + t2['m']
    result['h'] = t1['h'] + t2['h']
    if result['s']==60 :
        result['m'] = result['m']+1
        result['s']= 0
    if result['s'] > 60 :
        b = int(result['s']/ 60)
        a = result['s']% 60
        result['m'] = result['m']+b
        result['s'] = a
    if result['m']==60 :
        result['h'] = result['h']+1
        result['m']= 0
    if result['m'] > 60 :
        b = int(result['m']/ 60)
        a = result['m']% 60
        result['h'] = result['h']+b
        result['m'] = a

    return result

def subtraction_time(x,y):
    Standard_time(t1,t2)
    result={} 
    if t2['s']< t1['s']:
        t2['m'] = t2['m'] - 1
        t2['s'] = t2['s'] + 60
    if t2['m']< t1['m']:
        t2['h'] = t2['h'] - 1
        t2['m'] = t2['m'] + 60

    result['s'] = t2['s'] - t1['s']
    result['m'] = t2['m'] - t1['m']
    result['h'] = t2['h'] - t1['h']
    return result

def second_time(x):
    total_second = float(input("please enter total second:"))
    t1['h'] = int(total_second/3600)
    if t1['h']>24:
        days=int(t1['h']/24)
        t1['h']=t1['h']%24
        print(" conver to day :", days,'day and :')

    t1['m'] = (total_second%3600)//60

    t1['s'] = ((total_second%3600)%60)
    print(t1 )

def time_second(x):
    t1['h'] = int(input('saat zaman aval:  '))
    t1['m'] = int(input('daghigheh zaman aval:  '))
    t1['s'] = int(input('sanieh zaman aval:  '))
    if t1['s']==60 :
        t1['m'] = t1['m']+1
    if t1['s'] > 60 :
        b = int(t1['s']/ 60)
        a = t1['s']% 60
        t1['m'] = t1['m']+b
        t1['s'] = a
    if t1['m']==60 :
        t1['h'] = t1['h']+1
    if t1['m'] > 60 :
        b = int(t1['h']/ 60)
        a = t1['m']% 60
        t1['h'] = t1['h']+b
        t1['m'] = a
    print(t1)
    
    second_time = t1['h']*3600+t1['m']*60+t1['s']
    #print("ثانیه",second_time)
    return(second_time)

def show_menu():

    print('1-sum time')
    print('2-subtraction time')
    print('3-second to time')
    print('4-time to second ')


t1={}
t2={}
def load():
    print("zaman aval ra vared konid")
    t1['h'] = int(input('saat zaman aval:  '))
    t1['m'] = int(input('daghigheh zaman aval:  '))
    t1['s'] = int(input('sanieh zaman aval:  '))
    print("kasr dovom ra vared konid")
    t2['h'] = int(input('saat zaman dovom:  '))
    t2['m'] = int(input('daghigheh zaman dovom:  '))
    t2['s'] = int(input('sanieh zaman dovom:  '))
    


show_menu()
choice = int(input('please choose a number'))

if choice==1:
    Total =total_time(t1,t2)
    print("total time :  ",Total)
if choice==2:
    Total = subtraction_time(t1,t1)
    print("subtraction time :  ",Total)
if choice==3:
    Total = second_time(t1)
if choice==4:
    Total = time_second(t1)
    print(Total , "sanieh")

#print("total time :  ",Total)

