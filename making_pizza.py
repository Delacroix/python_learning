#type_1
import pizza_m
#type_2
from pizza_m import make_pizza
#type_rename
from pizza_m import make_pizza as mp

pizza_m.make_pizza(16, 'pepperoni')
pizza_m.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

make_pizza(16, 'pepperoni')

mp(16, 'pepperoni')