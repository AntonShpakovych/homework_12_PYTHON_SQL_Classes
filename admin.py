
import psycopg2
from setup import *
from connection import Connection


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

    def get_order_info(self, selector=''):
        if self._connectDb(self.login, self.password):
            table = ('orders',)
            fields = ('*',)
            selector = ''
            result = self._getData(table, fields, selector)
            return result
        else:
            return 'Incorrect login or password'


if __name__ == '__main__':
    admin1 = Admin('admin', 'admin')
    orders = admin1.get_order_info()
    print(orders)
