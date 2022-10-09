from test import *

while True:
    print("Введите команду \n c - created \n r - reduct \n w - watch \n a - all product \n d - delete")
    users = input(' -> ')
    if users == 'c':
        print(created_product())
    elif users  == 'r':
        print(update_product())
    elif users == 'w':
        print(get_one_product())
    elif users == 'a':
        print(get_data())
    elif users == 'd':
         print(delete_product()) 

# main()