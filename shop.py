from texttable import Texttable

class Customer:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance


class Product:
    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity


class Shop:
    def __init__(self):
        self.cart = []
    

    def add_item(self, product):
        self.cart.append((product))


    def show_items(self):
        if(len(self.cart)==0):
            print('\nThere is no items in cart\n')
            return 0

        print('\nItems in cart\n')
        print ('{:<8} {:<15} {:<15} {:<15} {:<15}'.format('Option','Product-name','Unit-Price', 'Quantity', 'Product-Price'))

        x = 0
        total = 0
        for i in self.cart:
            x += 1
            print ('{:<8} {:<15} {:<15} {:<15} {:<15}'.format(x, i.name, i.price, i.quantity, i.price*i.quantity))
            total += i.price*i.quantity

        print('In Total price: ', total, '\n\n')


    def edit_quantity(self):
        print('Select which products quantity to update')
        
        ch = int(input('Enter option: '))
        if(ch==0 or ch>len(self.cart)):
            print('\nWrong input\n')
            return

        x = 1
        for i in self.cart:
            if(x==ch):
                qt = int(input('Enter new quantity: '))
                i.quantity = qt
                print('\nProducts quantity updated successfully\n')
                break
            else:
                x+=1

    
    def delete_item(self):
        print('Select which product to delete')
        
        ch = int(input("Enter option: "))
        if(ch==0 or ch>len(self.cart)):
            print('\nWrong input\n')
            return

        x = 1
        for i in self.cart:
            if(x==ch):
                self.cart.remove(i)
                print('\nProducts deleted successfully\n')
                break
            else:
                x+=1
    
    
    def get_total(self):
        x = 0
        total = 0
        for i in self.cart:
            x += 1
            total += i.price*i.quantity
        return total


    def cart_clear(self):
        self.cart.clear()



name = input('\nCustomer name: ')
balance = int(input('Total balance: '))
print('\n')
customer = Customer(name, balance)

cart = Shop()
items = (['1', 'Rice', 70, 'Orginal Miniket'], ['2', 'Oil', 180, 'Soyabin Oil'], ['3', 'Meat', 230, 'Halal Chicken'], ['4', 'Egg', 140, 'One Dozen'], ['5', 'Vegetables', 50, 'Fresh Vegetables'])
       
while True:
    print('1. Buy new item\n2. Show products in cart\n3. Edit quantity of product\n4. Delete product\n5. Place order')
    choice = input('\nEnter choice: ')

    # 1. Buy new item
    if choice == '1':           
        chart = Texttable()
        chart.add_rows([['Option','Name', 'Unit Price', 'Description'], items[0], items[1], items[2], items[3], items[4]])
        print(chart.draw())
        
        option = int(input('Enter option: ')) - 1
        name = items[option][1]
        price = items[option][2]
        description = items[option][3]
        quantity = int(input('Enter quantity: '))

        new_item = Product(name, price, description, quantity)
        cart.add_item(new_item)

        print('\n\nAdded item in cart Successfully')
        print('Product: ', name, '\nUnit price: ', price, '\nQuantity: ', quantity, '\nProduct price: ', price*quantity, '\n\n') 


    # 2. Show products in cart  
    elif choice == '2': 
        cart.show_items()        


    # 3. Edit quantity of product
    elif choice == '3':   
        it = cart.show_items()

        if(it!=0):
            cart.edit_quantity()


    # 4. Delete product on cart
    elif choice == '4':  
        it = cart.show_items()

        if(it!=0):
            cart.delete_item()


    # 5. Place Order
    elif choice == '5':  
        it = cart.show_items()

        if(it!=0):
            total = cart.get_total()  
            
            if(total>customer.balance):
                print('Have not enough money!\n\nLeave shop? -- Enter: 0\nStay shop? -- Enter: 1\n')
                lv = int(input('Enter 0 or 1: '))
                print('\n')
                if(lv == 0):
                    print(f'Come back Again Mr.{customer.name}!\n')
                    break
            else:
                print('Place order now?\n\nYes? -- Enter: 0\nNo? -- Enter: 1\n')
                lv = int(input('Enter 0 or 1: '))
                print('\n')
                if(lv == 0):
                    cart.cart_clear()
                    print('Total price: ', total)
                    print(f'Thank You, Come back Again Mr.{customer.name}!\n')
                    break