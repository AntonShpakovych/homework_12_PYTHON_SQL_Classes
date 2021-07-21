import psycopg2
from setup import *
from connection import Connection
from pprint import pprint


class RegisteredCustomer(Connection):

    def __init__(self, first_name, last_name, city, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.login = email
        self.password = password

    def get_self_info(self, selector=''):
        role = 'customer'
        if self._connectDb(self.login, self.password, role):
            table = ('customer',)
            fields = ('*',)
            selector = f"""where first_name = '{self.first_name}' and last_name = '{self.last_name}' """
            result = self._getData(table, fields, selector)
            return result
        else:
            return 'Incorrect login or password'

    def create_order(self, data):
        role = 'customer'
        if self._connectDb(self.login, self.password, role):
            table = 'orders'
            result = self._postData(table, data)
            return result
        else:
            return 'Incorrect login or password'

    def delete_order(self, selector):
        role = 'customer'
        if self._connectDb(self.login, self.password, role):
            table = 'orders'
            selector = f"date_of_order = '{selector}'"
            result = self._deleteData(table,  selector)
            return result
        else:
            return 'Incorrect login or password'

    def get_product_info(self, category, selector=''):
        role = 'customer'
        if self._connectDb(self.login, self.password, role):
            table = ('product p inner join product_category pc ',)
            fields = ('product_name', 'unit_price',)
            categoryes = ['product_name', 'unit_price']
            if category and category in categoryes and selector:
                where = f"""where {category} = '{selector}'"""
            else:
                where = ''
            selector = f"""on p.category_name  = pc.id {where}"""
            result = self._getData(table, fields, selector)

            fieldNames = ["product_name", "unit_price", ]
            сhangeRes = []
            for item in result:
                cort = {}
                for index, element in enumerate(item):
                    cort[fieldNames[index]] = element
                сhangeRes.append(cort)
            return сhangeRes

        else:
            return 'Incorrect login or password'


if __name__ == '__main__':
    cust = RegisteredCustomer(
        'Mavk', 'Kvam', 2, 'mavklog', 'mavkpass')
    # -------------------------------
    # data = [{
    #         'employee_id': 1,
    #         'city_id': 2,
    #         'date_of_order': '2021-04-10',
    #         'customer_id': 2,
    #         'product_id': 2,
    #         'price': 252
    #         }]
    # put = cust.create_order(data)
    # print(put)
    # -------------------------------
    # orders = cust.get_product_info()
    # print(orders)

    # -------------------------------
    # idf = cust._getNextId('orders')
    # print(idf)
    # -------------------------------
    # dele = cust.delete_order('2021-04-10')
    # print(dele)
    pprint(cust.get_product_info('unit_price', '40'))
