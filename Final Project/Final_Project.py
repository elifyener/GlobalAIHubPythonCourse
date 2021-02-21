# ==========================================
#  Title:  Final Project
#  Author: elifyener
#  Date:   21 Feb 2021
# ==========================================

# Final
# Recipe Application
# Enter 3 recipes. Create a separate class for each recipe.
# Identify the products used in this recipe using the init() method.
# Write a function about how long these products should be used later.

# Don't forget to use inheritance here. Here to use inheritance. For example;
# Write a cooking function. Since this method will be common to all
# classes, you need to use inheritance here.

# Common stages in cooking
class Food():
    def __init__(self,name):
        self.name = name
        
    def cook(self, minute):
        print(f"{minute} minutes cooked.")
    def melt(self, quantity, measure, ingredient):
        print(f"{quantity} {measure} of {ingredient} melted.")
    def add(self, quantity, measure, ingredient):
        print(f"{quantity} {measure} of {ingredient} added.")
    def add_salt(self):
        print(f"Salt added.")
    def ready(self):
        print(f"{self.name} is ready!!!")
    def mix(self):
        print("ingredients are mixed.")

class Tomato_Soup(Food):
    def __init__(self, name, tomato, butter, flour, water, milk, cheddar, salt):
        self.tomato = tomato
        self.butter = butter
        self.flour = flour
        self.water = water
        self.milk = milk
        self.cheddar = cheddar
        self.salt = salt
        # Use of inheritance
        super().__init__(name)

    def showInfo(self):
        print(f"{self.name} \nIngredients: {self.tomato}, {self.butter}, {self.flour}, {self.water}, {self.milk}, {self.cheddar}, {self.salt}")
    def roast(self):
        print(f"the {self.flour} is roasted in the pot.")
    def grate(self, quantity, measure, ingredient):
        print(f"{quantity} {measure} {ingredient} grated.")
    def sprinkle(self):
        print(f"{self.cheddar} sprinkled on the soup.")

class Pilaf(Food):
    def __init__(self, name, butter, rice, noodle, water, salt):
        self.butter = butter
        self.rice = rice
        self.noodle = noodle
        self.water = water
        self.salt = salt
        super().__init__(name)
        
    def showInfo(self):
        print(f"{self.name} \nIngredients: {self.butter}, {self.rice}, {self.noodle}, {self.water}, {self.salt}")
        
    def roast(self, ingredient):
        print(f"the {ingredient} is roasted in the pot.")
        
class Tarator(Food):
    def __init__(self, name, butter, carrot, mayonnaise, garlic, yoghurt, salt):
        self.butter = butter
        self.carrot = carrot
        self.mayonnaise = mayonnaise
        self.garlic = garlic
        self.yoghurt = yoghurt
        self.salt = salt
        super().__init__(name)
        
    def showInfo(self):
        print(f"{self.name} \nIngredients: {self.butter}, {self.carrot}, {self.mayonnaise}, {self.garlic}, {self.yoghurt}, {self.salt}")
        
    def grate(self, quantity, measure, ingredient):
        print(f"{quantity} {measure} {ingredient} grated.")
    
    def wait(self):
        print(f"left to cool.")

def main():
    # Cooking stages...
    tomato_soup = Tomato_Soup("Tomato Soup", "tomato", "butter", "flour", "water", "milk", "cheddar", "salt")
    tomato_soup.showInfo()
    tomato_soup.melt(2, "tablespoon", "butter")
    tomato_soup.add(3, "tablespoon", "flour")
    tomato_soup.roast()
    tomato_soup.grate(4, "", "tomato")
    tomato_soup.add(1, "liter", "water")
    tomato_soup.mix()
    tomato_soup.cook(15)
    tomato_soup.add(1, "cup","milk")
    tomato_soup.add_salt()
    tomato_soup.cook(2)
    tomato_soup.grate(1, "slice", "cheddar")
    tomato_soup.sprinkle()
    tomato_soup.ready()
    
    print("\n")
    
    pilaf = Pilaf("Pilaf", "butter", "rice", "barley noodle", "hot water", "salt")
    pilaf.showInfo()
    pilaf.melt(2, "tablespoon", "butter")
    pilaf.add(1/2, "cup", "barley noodle")
    pilaf.roast("barley noodle")
    pilaf.add(2,"cups", "rice")
    pilaf.roast("rice")
    pilaf.add(3, "cups", "hot water")
    pilaf.add_salt()
    pilaf.mix()
    pilaf.cook(15)
    pilaf.ready()
    
    print("\n")
    
    tarator = Tarator("Tarator", "butter", "carrot", "mayonnaise", "garlic","yoghurt", "salt")
    tarator.showInfo()
    tarator.melt(1, "tablespoon", "butter")
    tarator.add(2, "cloves", "garlic")
    tarator.grate(3, "", "carrot")
    tarator.cook(10)
    tarator.wait()
    tarator.add(4, "tablespoon", "yoghurt")
    tarator.add(1, "tablespoon", "mayonnaise")
    tarator.add_salt()
    tarator.mix()
    tarator.ready()
    
if __name__ == "__main__":
    main()
