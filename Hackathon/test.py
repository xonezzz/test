import datetime
import json
tovar = [
    {
        'id': 1,
        'name': 'banana',
        'price': 30,
        # 'data': datetime.datetime(2022, 10, 8),
        'discription': 'delicious',
        'status': True 
    }
]
FILE_PATH = 'data.json'

def get_data():
    with open ('data.json', 'w') as file:
        return json.load(file)

def get_id():
    with open('id.txt', 'r') as file:
        id = int(file.read())
        id +=1
    with open('id.txt', 'w') as file:
        file.write(str(id))
    return id 

def created_product():
    data = get_data()
    product = ({
        'id': int(input('Введите id')),
        'name': input('Введите название продукта'),
        'price': int(input('Введите цену продукта')),
        'discription': input('Введите описание товара')
    })
    data.append(product)
    with open(FILE_PATH, 'w') as file:
        json.dump(data, file)
    return "Продукт создан"
    
def update_product():
    data = get_data()
    id = int(input('Введите id для изменения продукта'))
    product = list(filter(lambda x: x['id'] == id, data))
    if not product:
        return "Нет такого продукта"
    index_ = data.index(product[0])
    info = input('Что вы хотите изменить? \n 1 - id \n 2 - name \n 3 - discription \n 4 - price')
    if info == '1':
        data[index_] ['id'] = int(input('Введите id товара'))
    elif info == '2':
        data[index_] ['name'] = input('Введите новое название продукта')
    elif info == '3':
        data[index_] ['discription'] = input('Введите описание товара ')
    elif info == '4':
        data[index_] ['price'] = int(input('Введите цену товара'))
    else:
        return 'Такой команды нет!'    

