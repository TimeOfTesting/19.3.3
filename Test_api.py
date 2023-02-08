import json
import requests


print("Работа с блоком User")


print('Добавление нового пользователя')
user = {
  "id": 3445465,
  "username": "Liza",
  "firstName": "Kapustina",
  "lastName": "Liza",
  "email": "liza@liza.ru",
  "password": "123456789",
  "phone": "11154545646",
  "userStatus": 0
}
res_add_user = requests.post('https://petstore.swagger.io/v2/user', data=json.dumps(user, ensure_ascii=False), headers={'accept': 'application/json', 'Content-Type': 'application/json'})
print(f'Статус кода POST: {res_add_user}')
print(res_add_user.json())

print('Поиск пользователя по логину')
login = {'username': 'Liza', 'password': '123456789'}
res_get_user = requests.get('https://petstore.swagger.io/v2/user/login', params=login, headers={'accept': 'application/json'})
print(f'Статус кода GET: {res_get_user}')
print(res_get_user.json())

print('Поиск по имени пользователя')
get_user_name = 'Liza'
res_get_user_name = requests.get(f'https://petstore.swagger.io/v2/user/{get_user_name}', headers={'accept': 'application/json'})
print(f'Статус кода GET: {res_get_user_name}')
print(res_get_user_name.json())

print('Изменение имени у пользователя')
user_name = 'Liza'
put_user = {
  "id": 3445465,
  "username": "Lizaaaa",
  "firstName": "Lizaaaa",
  "lastName": "Lizaaaa",
  "email": "liza@liza.ru",
  "password": "123456789",
  "phone": "7777777777",
  "userStatus": 0
}
res_put_user = requests.put(f'https://petstore.swagger.io/v2/user/{user_name}', data=json.dumps(put_user, ensure_ascii=False),
                            headers={'accept': 'application/json', 'Content-Type': 'application/json'})
print(f'Статус кода PUT: {res_put_user}')
print(res_put_user.json())

print('Удаление пользователя')
delete_user = 'Lizaaaa'
res_delete_user = requests.delete(f'https://petstore.swagger.io/v2/user/{delete_user}',
                            headers={'accept': 'application/json'})
print(f'Статус кода DELETE: {res_delete_user}')
print(res_delete_user.json())


print("Работа с блоком Pet")


print('Найти всех питомцев')
status = {'status': ['available', 'pending', 'sold']}
res_get_pets = requests.get('https://petstore.swagger.io/v2/pet/findByStatus', params=status, headers={'accept': 'application/json'})
print(f'Статус кода GET: {res_get_pets}')
print(res_get_pets.json())

print("Изменить имя и статус питомца по ID")
id_pet = '9223372036854258971'
new_info = {'name': 'Кошка', 'status': 'pending'}
res_post_pet = requests.post(f'https://petstore.swagger.io/v2/pet/{id_pet}', data=new_info, headers={'accept': 'application/json'})
print(f'Статус кода POST: {res_post_pet}')
print(res_post_pet.json())

print("Найти питомца по ID")
id_pet = '9223372036854258971'
res_get_pet_id = requests.get(f'https://petstore.swagger.io/v2/pet/{id_pet}', headers={'accept': 'application/json'})
print(f'Статус кода GET: {res_get_pet_id}')
print(res_get_pet_id.json())

print("Добавление фотографии питомца")
files = {'file': open('cat.jpg', 'rb')}
id_pet = '9223372036854258971'
res_post_pet_file = requests.post(f'https://petstore.swagger.io/v2/pet/{id_pet}/uploadImage', files=files, headers={'accept': 'application/json'})
print(f'Статус кода POST: {res_post_pet_file}')
print(res_post_pet_file.json())

print('Удаление питомца')
api_key = '123456789'
id_pet = '9223372036854258959'
res_delete_pet = requests.delete(f'https://petstore.swagger.io/v2/pet/{id_pet}', headers={'accept': 'application/json'})
print(f'Статус кода DELETE: {res_delete_pet}')
print(res_delete_pet.json())



print("Работа с блоком Store")


print('Размещение заказа на покупку питомца')
by_pet = {
  "id": 9,
  "petId": 9223372036854258971,
  "quantity": 1,
  "shipDate":
  "2023-02-07T18:57:05.626Z",
  "status": "placed",
  "complete": 'true'
}
res_by_pet = requests.post('https://petstore.swagger.io/v2/store/order', data=json.dumps(by_pet, ensure_ascii=False), headers={'accept': 'application/json', 'Content-Type': 'application/json'})
print(f'Статус кода POST: {res_by_pet}')
print(res_by_pet.json())

print('Поиск заказа по ID')
order_id = '9'
res_get_order = requests.get(f'https://petstore.swagger.io/v2/store/order/{order_id}', headers={'accept': 'application/json', 'Content-Type': 'application/json'})
print(f'Статус кода GET: {res_get_order}')
print(res_get_order.json())

print('Удаление заказа по ID')
order_id = '9'
res_delete_order = requests.delete(f'https://petstore.swagger.io/v2/store/order/{order_id}', headers={'accept': 'application/json', 'Content-Type': 'application/json'})
print(f'Статус кода DELETE: {res_delete_order}')
print(res_delete_order.json())



