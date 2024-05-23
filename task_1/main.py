"""Model that determines how much Lemonade and Fruit Juice should be produced to maximize the total number of products"""

from pulp import LpMaximize, LpProblem, LpVariable

# Define the problem
prob = LpProblem("BeverageProduction", LpMaximize)

# Define decision variables
lemonade = LpVariable("Lemonade", lowBound=0, cat="Integer")
fruit_juice = LpVariable("Fruit_Juice", lowBound=0, cat="Integer")

# Define objective function
prob += lemonade + fruit_juice, "Total_Products_Produced"

# Define constraints
prob += 2 * lemonade + fruit_juice <= 100, "Water_Constraint"
prob += lemonade <= 50, "Sugar_Constraint"
prob += lemonade <= 30, "Lemon_Juice_Constraint"
prob += 2 * fruit_juice <= 40, "Fruit_Puree_Constraint"
prob += lemonade >= 0, "Non_Negative_Lemonade"
prob += fruit_juice >= 0, "Non_Negative_Fruit_Juice"

# Solve the problem
prob.solve()

# Print the results
print("Optimal Production Plan:")
print("Lemonade:", round(lemonade.varValue))
print("Fruit Juice:", round(fruit_juice.varValue))
print("Total Products Produced:", round(prob.objective.value()))
