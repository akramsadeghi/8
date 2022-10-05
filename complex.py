
result = {}
def total(x,y):
    
    result['r'] = a['r'] + b['r']
    result['i'] = a['i'] + b['i']
    return result
    

def subtraction(x,y):
    result['r'] = a['r'] - b['r']
    result['i'] = a['i'] - b['i']   
    return result
    

def multi(x,y):
    result['r']=(x['r']*y['r'])-(x['i']*y['i']) 
    result['i']=(x['i']*y['r'])+(x['r']*y['i'])
    return result
    

def division(x,y):
    result['r']=((x['r']*y['r'])+(x['i']*y['i']))/((y['r']**2)+(y['i']**2)) 
    result['i']=((x['i']*y['r'])-(x['r']*y['i']))/((y['r']**2)+(y['i']**2))
    return result
    


def show_menu():

    print('1-sum ')
    print('2-subtraction ')
    print('3-multiplication ')
    print('4-Division ')

a={}
b={}
print("hello, welcome toSimple Math")
show_menu()
choice = int(input('please choose a number:  '))
print("adad mokhtalet aval ra vared konid")
a['i'] = float(input('adad mohumi aval:  '))
a['r'] = float(input('adad haghighi aval:  '))
print("adad mokhtalet dovom ra vared konid")
b['i'] = float(input('adad mohumi dovom:  '))
b['r'] = float(input('adad haghighi dovom:  '))
print("kasr aval:  ",a['r'],"+",a['i'],"i")
print("kasr dovom:  ",b['r'],"+",b['i'],"i")
if choice==1:
    e = total(a,b)
if choice==2:
    e = subtraction(a,b)
if choice==3:
    e = multi(a,b)
if choice==4:
    e = division(a,b)
print(result['r'],"+",result['i'],"i")                
