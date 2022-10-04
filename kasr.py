

def total(x,y):
    result = {}
    if x['m']%y['m']==0 or y['m']%x['m']==0:
        if x['m']>y['m']:
            q=x['m']/y['m']
            result['s']=x['s']+y['s']*q
            result['m']=x['m']    
        else:
            p=y['m']/x['m']
            result['s']=p*x['s']+y['s']
            result['m']=y['m']
            
            
    else:
        result['s']=x['s']*y['m']+y['s']*x['m']
        result['m']=x['m']*y['m']
        
    return result
    

def subtraction(x,y):
    result = {}
    if x['m']%y['m']==0 or y['m']%x['m']==0:
        if x['m']>y['m']:
            q=x['m']/y['m']
            result['s']=x['s']-y['s']*q
            result['m']=x['m']
            
        else:
            p=y['m']/x['m']
            result['s']=p*x['s']-y['s']
            result['m']=y['m']      
    else:
        result['s']=x['s']*y['m']-y['s']*x['m']
        result['m']=x['m']*y['m']
        
    return result
    

def multi(x,y):
    result = {}
    result['s']=x['s']*y['s'] 
    result['m']=x['m']*y['m']
    return result
    

def division(x,y):
    result = {}
    result['s']=x['s']*y['m'] 
    result['m']=x['m']*y['s']
    return result
    


def show_menu():

    print('1-sum deduction')
    print('2-subtraction deduction')
    print('3-multiplication deduction')
    print('4-Division deduction ')

a={}
b={}
print("hello, welcome toSimple Math")
show_menu()
choice = int(input('please choose a number'))
print("kasr aval ra vared konid")
a['s'] = float(input('surat kasr aval:  '))
a['m'] = float(input('makhraj kasr aval:  '))
print("kasr dovom ra vared konid")
b['s'] = float(input('surat kasr dovom:  '))
b['m'] = float(input('makhraj kasr dovom:  '))
print("kasr aval:  ",a['s'],"/",a['m'])
print("kasr dovom:  ",b['s'],"/",b['m'])
if choice==1:
    e = total(a,b)
if choice==2:
    e = subtraction(a,b)
if choice==3:
    e = multi(a,b)
if choice==4:
    e = division(a,b)
print(e)                

  



