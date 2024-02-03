import pulp

model = pulp.LpProblem("Maximize Profit", pulp.LpMaximize)

x = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')  # Quantity of lemonade
y = pulp.LpVariable('Fruit juice', lowBound=0, cat='Integer')  # Quantity of fruit juice


# defining function
model += x + y, "Profit"

# defining constraints
water_constraint = 2*x + y <= 100, "Water"
sugar_constraint = x <= 50, "Sugar"
lemon_juice_constraint = x <= 30, "Lemon juice"
fruit_puree_constraint = 2*y <= 40, "Fruit puree"


model += water_constraint
model += sugar_constraint
model += lemon_juice_constraint
model += fruit_puree_constraint

# solving
model.solve()

# results
print("Manufacturing of lemonade (q):", x.varValue) 
print("Manufacturing of fruit juice (q)", y.varValue)

# 30 items of lemonade and 20 items of fruit juice - total 50 items
