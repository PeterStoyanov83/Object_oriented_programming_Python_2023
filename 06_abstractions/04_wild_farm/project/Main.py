from project.food import Meat, Vegetable, Seed, Fruit
from project.animals.birds import Owl, Hen
from project.animals.mammals import Mouse, Dog, Cat, Tiger

# Creating some instances of animals
owl = Owl("Ollie", 1.2, 1.5)
hen = Hen("Henny", 0.9, 0.8)
mouse = Mouse("Mickey", 0.1, "Urban")
dog = Dog("Rex", 30.0, "Suburban")
cat = Cat("Whiskers", 4.0, "Urban")
tiger = Tiger("Simba", 200.0, "Jungle")

# Creating some instances of food
meat = Meat(5)
veggie = Vegetable(3)
fruit = Fruit(4)
seed = Seed(10)

# Feeding animals
print(owl.feed(meat))
print(hen.feed(veggie))
print(mouse.feed(fruit))
print(dog.feed(meat))
print(cat.feed(veggie))
print(tiger.feed(meat))

# Trying to feed animals with food they do not eat
print(owl.feed(veggie))  # Owl does not eat Vegetable!
print(mouse.feed(meat))  # Mouse does not eat Meat!
print(cat.feed(seed))  # Cat does not eat Seed!
print(dog.feed(fruit))  # Dog does not eat Fruit!
print(tiger.feed(veggie))  # Tiger does not eat Vegetable!

# Checking the details of animals after feeding
print(owl)
print(hen)
print(mouse)
print(dog)
print(cat)
print(tiger)
