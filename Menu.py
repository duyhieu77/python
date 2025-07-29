class Product:
    def __init__(self, product_id, name, price, source):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.source = source

    def __str__(self):
        return f"ID: {self.product_id}, Name: {self.name}, Price: {self.price}, Source: {self.source}"

products = []

def add_product():
    product_id = input("Enter product ID: ")
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    source = input("Enter product source: ")
    products.append(Product(product_id, name, price, source))
    print("Product has been added.")

def display_products():
    if not products:
        print("No products available.")
        return
    for product in products:
        print(product)

def filter_products():
    price_limit = float(input("Enter price to filter products (less than this number): "))
    filtered = [product for product in products if product.price < price_limit]
    if not filtered:
        print("No products match the criteria.")
    else:
        for product in filtered:
            print(product)

def update_product():
    product_id = input("Enter the product ID to update: ")
    for product in products:
        if product.product_id == product_id:
            product.name = input("Enter new name: ")
            product.price = float(input("Enter new price: "))
            product.source = input("Enter new source: ")
            print("Product has been updated.")
            return
    print("Product not found.")

def delete_product():
    product_id = input("Enter the product ID to delete: ")
    global products
    products = [product for product in products if product.product_id != product_id]
    print("Product has been deleted.")

def main_menu():
    while True:
        print("\n--- Menu ---")
        print("1. Add product")
        print("2. Display product list")
        print("3. Filter products")
        print("4. Update product")
        print("5. Delete product")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_product()
        elif choice == '2':
            display_products()
        elif choice == '3':
            filter_products()
        elif choice == '4':
            update_product()
        elif choice == '5':
            delete_product()
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()