# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

# below function error, needed to reorder parameters
# def add_or_remove_cash(new_total, admin_cash):
    admin_cash["admin"]["total_cash"] += new_total

def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]
   
def increase_pets_sold(pet_shop, pets_sold):
    pet_shop["admin"]["pets_sold"] += pets_sold

def get_stock_count(pet_shop):
   stock_count = len(pet_shop["pets"])
   return stock_count

def get_pets_by_breed(pet_shop, breed):
    # get list of pets from the pet_shop, look into each dictionary by the specific "breed" key and check in the value matches
    # create a container (variable) to deposit each match found in the loop
    # if there is a match, each one needs to be put in the container which will be the return
    found_pets = []
    pet_list = pet_shop["pets"]
    for pet in pet_list:
        if pet ["breed"] == breed:
            found_pets.append(pet)

    return found_pets

def find_pet_by_name(pet_shop, pet):
    pet_list = pet_shop["pets"]
    for pet_name in pet_list:
        if pet_name["name"] == pet:
            return pet_name

def remove_pet_by_name(pet_shop, name):
    pet_list = pet_shop["pets"]
    for pet in pet_list:
        if pet["name"] == name:
            pet_shop["pets"].remove(pet)

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, cash):
    customer["cash"] -= cash

def get_customer_pet_count(customer):
    customer_pets = len(customer["pets"])
    return customer_pets

def add_pet_to_customer(customer, pet):
    customer["pets"].append(pet)

# optional from now on

def customer_can_afford_pet(customer, new_pet):
    if customer["cash"] >= new_pet["price"]:
        return True
    elif customer["cash"] == new_pet["price"]:
        return True
    else:
        return False

def sell_pet_to_customer(pet_shop, pet, customer):
    #if the pet has a value, run this:
    if pet != None:
        has_customer_got_the_cash = customer_can_afford_pet(customer, pet)
        if has_customer_got_the_cash:
            
            add_pet_to_customer(customer, pet)
    
            increase_pets_sold(pet_shop, 1)

            paid_cash = pet["price"]
            remove_customer_cash(customer, paid_cash)
            add_or_remove_cash(pet_shop, paid_cash)
    #else, if pet has no value, state "Pet not found"
    


