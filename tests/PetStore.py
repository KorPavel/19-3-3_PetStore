import requests
import json
from datetime import datetime, timezone
import random
from config import *


def print_info(title, resp):
    sp = title.split(' /')
    print(f'\x1B[1;93m{sp[0]}\x1B[0m\t', *sp[1:])
    print(f'\tStatus-code: \x1B[1;{str(91 + (resp.status_code == 200))}m'
          f'{resp.status_code}\x1B[0m\n\tBody: {resp.json()}')


print('\n' + '=' * 18 + '  USER  ' + '=' * 18)  # ================  USER  ==================

# GET /user/login  Logs user into the system
username = user_body['username']
password = user_body['password']

res = requests.get(f'{base_url}/user/login?login={username}&password={password}',
                   headers={'accept': 'application/json'})

print_info('\nGET /user/login\t\t"Logs user into the system"', res)
print('\tHeader:', res.headers)

# POST /user  Create user
body = json.dumps(user_body, ensure_ascii=False).encode('utf-8')

res = requests.post(f'{base_url}/user', headers=headers, data=body)
print_info('\nPOST /user\t\t"Create user"', res)


# PUT /user/{username} Updated user
username = user_body['username']
body = json.dumps(updated_user_body, ensure_ascii=False).encode('utf-8')

res = requests.put(f'{base_url}/user/{username}', headers=headers, data=body)
print_info(f'\nPUT /user/{username}\t\t"Updated user"', res)


# GET /user/{username} Get user by user name (before delete)
username = updated_user_body['username']

res = requests.get(f'{base_url}/user/{username}', headers={'accept': 'application/json'})
print_info(f'\nGET /user/{username}\t\t"Get user by user name (before delete)"', res)


# DELETE /user/{username} Delete user
username = updated_user_body['username']

res = requests.delete(f'{base_url}/user/{username}', headers={'accept': 'application/json'})
print_info(f'\nDELETE /user/{username}\t\t"Delete user"', res)


# GET /user/{username} Get user by user name (after delete)
username = updated_user_body['username']

res = requests.get(f'{base_url}/user/{username}', headers={'accept': 'application/json'})
print_info(f'\nGET /user/{username}\t\t"Get user by user name (after delete)" expected code 404', res)


# POST /user/createWithList Creates list of users with given input array
body = json.dumps(users_list)

res = requests.post(f'{base_url}/user/createWithList', headers=headers, data=body)
print_info('\nPOST /user/createWithList\t\t"Creates list of users with given input array"', res)


# POST /user/createWithArray Creates list of users with given input array
body = json.dumps(users_list)

res = requests.post(f'{base_url}/user/createWithArray', headers=headers, data=body)
print_info('\nPOST /user/createWithArray\t\t"Creates list of users with given input array"', res)


# GET /user/logout  Logs out current logged in user session
res = requests.get(f'{base_url}/user/logout', headers={'accept': 'application/json'})
print_info('\nGET /user/logout\t\t"Logs out current logged in user session"', res)


print('\n' + '=' * 18 + '  STORE  ' + '=' * 18)  # ===============  STORE  ==================
# POST /store/order  Place an order for a pet
now = datetime.now(timezone.utc)
body = order
body['shipDate'] = now.isoformat()
body = json.dumps(body)

res = requests.post(f'{base_url}/store/order', headers=headers, data=body)
orderid_for_delete = res.json()['id']
print_info('\nPOST /store/order\t\t"Place an order for a pet"', res)


# GET /store/order/{orderId}  Find purchase order by ID
orderId = random.randint(1, 10)

res = requests.get(f'{base_url}/store/order/{orderId}', headers={'accept': 'application/json'})
print_info(f'\nGET /store/order/{orderId}\t\t"Find purchase order by ID"', res)


# DELETE /store/order/{orderId}  Delete purchase order by ID
orderId = orderid_for_delete

res = requests.delete(f'{base_url}/store/order/{orderId}', headers={'accept': 'application/json'})
print_info(f'\nDELETE /store/order/{orderId}\t\t"Delete purchase order by ID"', res)


# GET /store/inventory  Returns pet inventories by status
res = requests.get(f'{base_url}/store/inventory', headers={'accept': 'application/json'})
print_info('\nGET /store/inventory\t\t"Returns pet inventories by status"', res)


print('\n' + '=' * 18 + '  PET  ' + '=' * 18)  # ==============  PET  ================

# POST /pet  Add a new pet to the store
body = pet_body
body['name'] = 'Krosh'
body['category']['name'] = 'кролик'
body['tags'][0]['name'] = 'смешарик'
body['tags'].append({"id": 0, "name": "Крош"})
body['status'] = 'test-1'
body = json.dumps(body, ensure_ascii=False).encode('utf-8')

res = requests.post(f'{base_url}/pet', headers=headers, data=body)
petid = res.json()['id']
print_info('\nPOST /pet\t\t"Add a new pet to the store"', res)


# GET /pet/findByStatus  Finds Pets by status
status = 'test-1'

res = requests.get(f'{base_url}/pet/findByStatus?status={status}', headers={'accept': 'application/json'})
print_info('\nGET /pet/findByStatus\t\t"Finds Pets by status"', res)


# PUT /pet  Update an existing pet
body = pet_body
body['id'] = petid
body['name'] = 'Losyash'
body['category']['name'] = 'лось'
body['tags'][0]['name'] = 'смешарик'
body['tags'].append({"id": 1, "name": "Лосяш"})
body['status'] = 'test-1'
body = json.dumps(body, ensure_ascii=False).encode('utf-8')

res = requests.put(f'{base_url}/pet', headers=headers, data=body)
print_info('\nPUT /pet\t\t"Update an existing pet"', res)


# POST /pet/{petId}/uploadImage  Uploads an image
petId = petid
image = 'krosh-8.jpg'
files = {'file': (image, open(image, 'rb'), 'image/jpeg')}

res = requests.post(f'{base_url}/pet/{petId}/uploadImage', headers={'accept': 'application/json'}, files=files)
print_info(f'\nPOST /pet/{petId}/uploadImage\t\t"Uploads an image"', res)


# GET /pet/{petId}  Find pet by ID
petId = petid

res = requests.get(f'{base_url}/pet/{petId}', headers={'accept': 'application/json'})
print_info(f'\nGET /pet/{petId}\t\t"Find pet by ID"', res)


# POST /pet/{petId}  Updates a pet in the store with form data
petId = petid
name = 'Krosh'
status = 'test-2'
body = f'name={name}&status={status}'

res = requests.post(f'{base_url}/pet/{petId}', headers=headers1, data=body)
print_info(f'\nPOST /pet/{petId}\t\t"Updates a pet in the store with form data"', res)


# DELETE /pet/{petId}  Deletes a pet
petId = petid

res = requests.delete(f'{base_url}/pet/{petId}', headers={'accept': 'application/json'})
print_info(f'\nDELETE /pet/{petId}\t\t"Deletes a pet"', res)
