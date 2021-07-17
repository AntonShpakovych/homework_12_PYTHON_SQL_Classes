import psycopg2
from setup import *
from faker import Faker

faker = Faker()
connection = psycopg2.connect(
    user=USER,
    password=PASSWORD,
    host=HOST,
    port=PORT,
    database='shop_db'
)

cursor = connection.cursor()

list_with_product_cheese = ['Mozzarella', 'Cheddar', 'Gouda', 'Feta', 'Brie', 'Parmesan', 'Asiago',
                            'Bocconcini', 'Burrata', 'Camembert', 'Cheese Curds', 'Colby', 'Colby-Jack Cheese', 'Cotija', 'Cream cheese', 'Emmental', 'Gruyere', 'Halloumi', 'Havarti', 'Jarlsberg']
list_with_price_for_cheese = [100, 200, 300, 400, 500, 600, 250,
                              350, 550, 330, 170, 340, 650, 340, 270, 160, 170, 180, 190, 210]
# for i in range(len(list_with_product_cheese)):
#     cursor.execute(
#         f"""INSERT INTO product(id,product_name,unit_price,category_name) VALUES('{i+7}','{list_with_product_cheese[i]}','{list_with_price_for_cheese[i]}','{1}')""")
# connection.commit()


list_with_product_fruits = ['Apricots', 'Avocado', 'Banana', 'Blackberries', 'Blackcurrant', 'Blueberries', 'Breadfruit', 'Cantaloupe', 'Carambola', 'Cherimoya', 'Cherries', 'Clementine', 'Coconut Meat',
                            'Cranberries', 'Custard-Apple', 'Date Fruit', 'Durian', 'Elderberries', 'Feijoa', 'Figs']
list_with_price_for_fruits = [10, 20, 30, 40, 50, 60, 70, 80,
                              90, 100, 200, 250, 300, 350, 400, 450, 500, 550, 600, 700]
# for i in range(len(list_with_product_fruits)):
#     cursor.execute(
#         f"""INSERT INTO product(id,product_name,unit_price,category_name) VALUES('{i+27}','{list_with_product_fruits[i]}','{list_with_price_for_fruits[i]}','{2}')""")
# connection.commit()

list_with_product_meat = ['Bacon', 'Ham', 'Jamon', 'Prosciutto', 'Salami', 'Sausages', 'Beef', 'Lamb', 'Mutton', 'Chicken',
                          'Venison', 'Duck', 'Wild Boar', 'Bison', 'Goose', 'Rabbit', 'Pheasant', 'Organ Meat', 'Cured Meat', 'Dried Meat Products']
list_with_price_for_meat = [100, 200, 300, 400, 500, 600, 700,
                            800, 900, 1000, 250, 300, 370, 450, 550, 660, 650, 430, 780, 330]
# for i in range(len(list_with_product_meat)):
#     cursor.execute(
#         f"""INSERT INTO product(id,product_name,unit_price,category_name) VALUES('{i+47}','{list_with_product_meat[i]}','{list_with_price_for_meat[i]}','{3}')""")
# connection.commit()

list_with_product_fish = ['African glass catfish', 'Basking shark', 'Banjo', 'Beaked salmon', 'Beluga sturgeon', 'Blue-redstripe danio', 'Coolie loach',
                          'Escolar', 'Frilled shark', 'Great white shark', 'Knifejaw', 'Loosejaw', 'Mud minnow', 'Orfe', 'Pilot fish', 'Quillback', 'Southern smelt', 'Skilfish', 'Temperate perch', 'Treefish']
list_with_price_for_fish = [100, 200, 300, 400, 500, 600, 700, 800,
                            900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]
# for i in range(len(list_with_product_fish)):
#     cursor.execute(
#         f"""INSERT INTO product(id,product_name,unit_price,category_name) VALUES('{i+67}','{list_with_product_fish[i]}','{list_with_price_for_fish[i]}','{4}')""")
# connection.commit()
list_with_product_drink = ['Cola', 'Pepsi', 'Fanta', 'Sprite', 'Beer', 'Wine', 'Milk', 'Orange Juice',
                           'Hot chocolate', 'Milkshake', 'Iced tea', 'Tomato juice', 'Water', 'Coconut milk', 'Smoothie', 'Lemonade', 'Rum', 'Vodka', 'Whiskey', 'Brandy']
list_with_price_for_drink = [10, 10, 10, 10, 15, 100, 20,
                             30, 40, 20, 10, 23, 10, 140, 70, 50, 250, 170, 300, 300]
for i in range(len(list_with_product_fish)):
    cursor.execute(
        f"""INSERT INTO product(id,product_name,unit_price,category_name) VALUES('{i+87}','{list_with_product_drink[i]}','{list_with_price_for_drink[i]}','{5}')""")
connection.commit()
list_city = []
for i in range(0, 50):
    list_city.append(faker.city())

# for i in range(0, len(list_city)):
#     cursor.execute(f"""INSERT INTO city(city_name) VALUES('{list_city[i]}')""")
# connection.commit()

cursor.close()
connection.close()
