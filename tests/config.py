# базовый URL
base_url = 'https://petstore.swagger.io/v2'

# заголовки:
headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
headers1 = {'accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}


# new user
user_body = {
  "id": 0,
  "username": "А.С. Пушкин",
  "firstName": "Александр",
  "lastName": "Пушкин",
  "email": "a_pushkin@gmail.com",
  "password": "qwert_1799",
  "phone": "+79030001122",
  "userStatus": 0
}

# updated user
updated_user_body = {
  "id": 0,
  "username": "М.Ю. Лермонтов",
  "firstName": "Михаил",
  "lastName": "Лермонтов",
  "email": "m_lermontov@gmail.com",
  "password": "qwerty_1814",
  "phone": "+79267778899",
  "userStatus": 0
}

# new pet
pet_body = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

# list of users
users_list = [
  {
    "id": 0,
    "username": "string",
    "firstName": "string",
    "lastName": "string",
    "email": "string",
    "password": "string",
    "phone": "string",
    "userStatus": 0
  }
]

# Order
order = {
  "id": 0,
  "petId": 0,
  "quantity": 0,
  "shipDate": "0",
  "status": "placed",
  "complete": True
}