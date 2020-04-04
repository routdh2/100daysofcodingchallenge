#program to create a laptop class in python
if __name__=="__main__":
    class Laptop:
        def __init__(self,brand,price,processor,ram,battery_life):
           self.brand=brand
           self.price=price
           self.processor=processor
           self.ram=ram
           self.battery_life=str(battery_life)+" hours"
        def show_details(self):
            print({"brand":self.brand,"price":self.price,"processor":self.processor,"ram":str(self.ram)+" GB","battery_life":self.battery_life})
        def extend_ram(self,ram_size):
            self.ram+=ram_size

    hp_laptop=Laptop("HP",30000,"Intel i3",4,4.5)
    asus_laptop=Laptop("Asus",34000,"AMD Ryzen5",4,6)
    hp_laptop.show_details()
    asus_laptop.show_details()
    asus_laptop.extend_ram(8)
    asus_laptop.show_details()
    print(hp_laptop.battery_life)
