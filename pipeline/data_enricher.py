import requests
from api_client import APIClient
import pandas as pd

class DataEnricher:

        def get_the_product_user():
                product1 = APIClient()
                products = product1.get_all_products()

                df_products = pd.DataFrame(products)
                #print(df_products.head())
                df_products.to_csv("product.csv", index=False)

                #print("Done with PRODUCTS, moving on to USERS")

                user1 = APIClient()
                users = user1.get_all_users()

                df_users = pd.DataFrame(users)
                #print(df_users.head())
                df_users.to_csv("user.csv", index=False)


                # to merge the two tables 
                MERGED  = pd.merge(df_products, df_users , on= "id", how="left")  #TO MERGER THE TWO DATAFRAME


                # To add Revenue column

                MERGED["revnue"] = MERGED["price"] * MERGED["count"]
                MERGED.to_csv("Merged_Data", index=False)

                


