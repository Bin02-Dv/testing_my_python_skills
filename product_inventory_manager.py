import re

add_product_input = input("Enter a list of product name(s): ")

cleaned_text = re.sub(r'[^\w\s]', '', add_product_input.lower())

list_of_products = cleaned_text.strip().split()

products = {}

for product in list_of_products:
    products[product.capitalize()] = products.get(product, "None")

for name in products:
    print(name)