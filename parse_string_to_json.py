#include json library
import json

#json string data
#order_data = input("Enter input order data: ")
#order_data = '{"order_id": "OD1234", "item_name": "Cookies", "item_qty": "2", "category": "Snacks"}'
order_data = input("Enter order data: ")
print(f'Your input is:  {order_data}')

#check data type with type() method
print(type(order_data))

#convert string to  object of type dictionary
order_data_json = json.loads(order_data)

#check new data type
print(type(order_data_json))

#access each variable in dictionary
print(order_data_json["order_id"])