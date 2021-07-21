
import psycopg2
from setup import *
from connection import Connection
from pprint import pprint
from datetime import date
from cus import respprint


class Admin(Connection):

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def register_self(self, data):
        table = 'login'
        if self._connectDb(self.login, self.password):
            if self._auditDb(table, list(data[0].values())[0]):
                result = self._postData(table, data)
                return result
            else:
                return 'A user with this login already exists'

        else:
            return 'Incorrect login or password'

    def add_product(self, data):
        if self._connectDb(self.login, self.password):
            table = 'product'
            result = self._postData(table, data)
            return result
        else:
            return 'Incorrect login or password'

    def add_pr_category(self, data):
        if self._connectDb(self.login, self.password):
            table = 'product_category'
            result = self._postData(table, data)
            return result
        else:
            return 'Incorrect login or password'

    def add_employee(self, data):
        if self._connectDb(self.login, self.password):
            table = 'employee'
            result = self._postData(table, data)
            return result
        else:
            return 'Incorrect login or password'

    def delete_product(self, selector):
        if self._connectDb(self.login, self.password):
            table = 'product'
            selector = f"product_name = '{selector}'"
            result = self._deleteData(table,  selector)
            return result
        else:
            return 'Incorrect login or password'

    def delete_pr_category(self, selector):
        if self._connectDb(self.login, self.password):
            table = 'product_category'
            selector = f"category_name = '{selector}'"
            result = self._deleteData(table,  selector)
            return result
        else:
            return 'Incorrect login or password'

    def delete_employee(self, selector):
        if self._connectDb(self.login, self.password):
            table = 'employee'
            selector = f"first_name = '{selector}'"
            result = self._deleteData(table,  selector)
            return result
        else:
            return 'Incorrect login or password'

    def delete_customer(self, selector):
        if self._connectDb(self.login, self.password):
            table = 'customer'
            selector = f"first_name = '{selector}'"
            result = self._deleteData(table,  selector)
            return result
        else:
            return 'Incorrect login or password'

    def edit_product(self, data, selector):
        if self._connectDb(self.login, self.password):
            table = 'product'
            result = self._updateData(table, data, selector)
            return result
        else:
            return 'Incorrect login or password'

    def edit_pr_category(self, data, selector):
        if self._connectDb(self.login, self.password):
            table = 'product_category'
            result = self._updateData(table, data, selector)
            return result
        else:
            return 'Incorrect login or password'

    def edit_employee(self, data, selector):
        if self._connectDb(self.login, self.password):
            table = 'employee'
            result = self._updateData(table, data, selector)
            return result
        else:
            return 'Incorrect login or password'

    def get_order_info(self, category, selector=''):
        if self._connectDb(self.login, self.password):
            categoryes = ['city_name', 'date_of_order', 'product_name']
            table = ('orders o',)
            fields = ("""o.id, concat(e.first_name,' ', e.last_name) as "employee", c.city_name, o.date_of_order, concat(c2.first_name,' ', c2.last_name) as "customer", p.product_name, o.price """,)
            if category and category in categoryes and selector:
                where = f"""where {category} = '{selector}'"""
            else:
                where = ''
            selector = f"""  inner JOIN employee e on e.id = o.employee_id 
                            inner JOIN city c on c.id = o.city_id 
                            inner JOIN customer c2 on c2.id = o.customer_id 
                            inner JOIN product p on p.id = o.product_id {where}"""
            result = self._getData(table, fields, selector)
            fieldNames = ["id", "employee", "city_name",
                          "date_of_birth", "customer", "product_name", 'price']
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
    admin1 = Admin('admin', 'admin')
    orders = admin1.get_order_info('city_name', 'London')
    pprint(orders)
