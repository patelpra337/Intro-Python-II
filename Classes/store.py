from category import Category

class Store:
    def __init__(self, name, categories):
        self.name = name
        self.categories = categories

    def __str__(self):
        output = f"Welcome to {self.name}!"
        for category in self.categories:
            output += f'\n {str(category)}'
        return output

    def __repr__(self):
        return f"self.name = {self.name} ; self.categories = {self.categories}"


shoes_category = Category("Sport Shoes", "All your needs for shoes", [])
baseball_category = Category("Baseball", "Astro's Fans Welcome", [])
basketball_category = Category("Basketball", "Indoor and outdoor products", [])
football_category = Category("Football", "Texans football equipment", [])

sports_store = Store("Acadamy Sports", [shoes_category, baseball_category, basketball_category, football_category])
deparment_store = Store("Walmart", ["Dairy", "Meats", "Bread", "Produce", "Clothing", "Electroncs", "Mechincal"])

print(deparment_store)
print(sports_store)