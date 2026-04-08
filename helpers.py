import random
import string


# метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string
        
def generate_order_payload(color=None):
    payload = {
        "firstName": generate_random_string(10),
        "lastName": generate_random_string(10),
        "address": generate_random_string(20),
        "metroStation": 1,
        "phone": generate_random_string(11),
        "rentTime": 1,
        "deliveryDate": "2024-05-20",
        "comment": generate_random_string(30)
    }
    
    if color is not None:
        payload["color"] = color
        
    return payload