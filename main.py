from pyfiglet import Figlet

def show_list():
    for i in range(len(products)):
        print(products[i])

def show_menu():
    print('1_add product')
    print('2_edit product')
    print('3_delete product')
    print('4_search')
    print('5_show list')
    print('6_buy')
    print('7_exit')
def load():
    print('Loading...')
    myfile=open('E:\Python course\session6\MahsaStore\store\db.txt','r')
    data=myfile.read()
    #print(data)
    products_list=data.split('\n')
    # for i in range (len(products_list)):
    #     product_info=products_list[i].split(',')
    #     print(product_info)

    for i in range(len(products_list)):
        product_info=products_list[i].split(',')
        mydict={}
        mydict['id']=product_info[0]
        mydict['name']=product_info[1]
        mydict['price']=product_info[2]
        mydict['count']=product_info[3]
        products.append(mydict)
    print('welcome')
#print(product_list)
def insert_item():
    id=int(input('insert item id'))
    name=input('inser item name: ')
    price=int(input('insert item price: '))
    count=int(input('insert item number of products: '))
    mydic={'id':id,'name':name,'price':price,'count':count}
    
    products.append(mydic)
def search_item():
    ToFind=int(input('insert the item id or name to change: '))
    for i in range (len(products)):
        if products[i]['id']==ToFind or products[i]['name']==ToFind: 
            b=i
        #else:
           # print('No adjustance...!')
            #
            # break
    return b
    
        

products=[]
load()
f = Figlet(font='standard')
print (f.renderText('Mahsa Store'))
show_menu()

choice = int(input('Please choose a number: '))
if choice==1:
    insert_item()
    show_list()
    
elif choice==2:
    
    i=search_item()
    print(i)
    products[i]=insert_item()
    show_list()
    

elif choice==3:
    pass
elif choice==4:
    pass
elif choice==5:
    show_list()
elif choice==6:
    pass
elif choice==7:
    pass

