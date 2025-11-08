import requests
import pandas as pd
from config import ConfigManager
conf = ConfigManager()
base_url = conf.get_url()

endpoint_product = "/products"
endpoint_user = "/users"

class APIClient:



    def get_all_products(self):
        url  = base_url + endpoint_product
        response  = requests.get(url)
        
        if response.status_code == 200:
            data_product = response.json()

            product_list = []
            for i in data_product:

                list_product = {
                    "id" : i['id'],
                    "count" : i['rating']['count'],
                    "price" : i['price']
                }
                product_list.append(list_product)
            return product_list

    def get_all_users(self):
        url  = base_url + endpoint_user
        response  = requests.get(url)
        
        if response.status_code == 200:
            data_user = response.json()

            user_list = []
            for i in data_user:

                list_user = {
                    "id" : i['id'],
                    "username" : i['username'],
                    "email" : i['email']
                }
                user_list.append(list_user)
            return user_list
        
