from data import stores
from components import Cart

site_name = "The Place With Stuff"

def welcome():
    print("Welcome to %s\nFeel free to shop throughout the stores we have, and only checkout once!" % site_name)

def print_stores():
    for store in stores:
        print(store)

def get_store(store_name):
    for store in stores:
        if store.name.lower() == store_name.lower():
            return store
    return False

def pick_store():
    for store in stores:
        print (store.name)
    selected_store = input('Pick a store by typing its name. Or type "checkout" to pay your bills and say your goodbyes. ')
    store_obj = get_store(selected_store)
    while not(selected_store == 'checkout') and store_obj==False:
        selected_store = input('No store with that name. Please try again. ')
        store_obj = get_store(selected_store)

    if selected_store == "checkout":
        return "checkout"
    return store_obj

def pick_products(cart, picked_store):
    picked_store.print_products()
    print("Select a product you would like to purchase. ")
    selected_product = input('Type "back" when you want to select another store or "checkout" when you\'re done.')
    while not (selected_product == "back" or selected_product == "checkout"):
        for product in picked_store.products:
            if product.name.lower() == selected_product.lower():
                cart.add_to_cart(product)

        if not selected_product.lower() in [product.name.lower() for product in picked_store.products]:
            selected_product = input('No product with that name. Please try again. ')
        else:
            selected_product = input('What else do you want? ')
    return selected_product


def shop():
    cart = Cart()
    selected_store = pick_store()
    response = pick_products(cart, selected_store)
    while not response == "checkout":
        selected_store = pick_store()
        response = pick_products(cart, selected_store)
    cart.checkout()

def thank_you():
    print("Thank you for shopping with us at %s" % site_name)
