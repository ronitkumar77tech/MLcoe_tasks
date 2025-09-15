class List:
    def __init__(self, token, name, price, category):
        self.token = token
        self.name = name
        self.price = price
        self.category = category
    def __str__(self):
        return f"{self.token}\t{self.name}\t ${self.price:.2f}\t{self.category}"
class Foods:
    def __init__(self):
        self.foods = [ List(1,'Samosa',10,'Desi'),
                      List(2,'Kachodi',25,'Desi'),
                      List(3,'Burger',35,'FastFood'),
                      List(4,'Limeca',20,'Beverage'),
                      List(5,'Jalebi',15,'Sweets'),
                      List(6,'Lassi',15,'Beverage'),
                      List(7,'Laddoo',5,'Sweets')]
    def showList(self):
        print("List items:")
        print("Token\tName\tPrice\tCategory")
        for foods in self.foods:
            print(f"{foods}\n")
    def getItem(self,token):
        for food in self.foods:
            if food.token ==token:
                return food
        return None
items= Foods()
while True:
    print("Propagation Panel:\n1. Show Menu Card\n2. Order Food\n3. Exit")
    choice=int(input())
    match choice:
        case 1:
            items.showList()
        case 2:
            total=0
            fd=input("Dear customer, tell your token(s) for the order please_ ")
            order= fd.split()
            print("Order placed-")
            for token_s in order:
                token=int(token_s)
                i=items.getItem(token)
                if i:
                    print(f"{i.name}-${i.price}")
                    total+=i.price
                else:
                    print("Invalid token input...check please")
            print(f"Total Bill: {total:.2f}")
        case 3:
            print("Thanks for visiting us...")
            exit()
        case _:
            print("Invalid choice...!")
