# Write your solution here
def search(products: list, criterion: callable):
    products_list = []
    for product in products:
        if criterion(product):
            products_list.append(product)
    return products_list
    