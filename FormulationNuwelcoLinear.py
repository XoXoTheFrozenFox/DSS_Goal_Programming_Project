import pulp                                                                                 

# Create a linear programming problem
lp_problem = pulp.LpProblem("Maximize_Z", pulp.LpMaximize)

# Define decision variables
X1 = pulp.LpVariable("X1", lowBound=0, cat='Continuous')
X2 = pulp.LpVariable("X2", lowBound=0, cat='Continuous')

# Coefficients for the objective function
coef_X1 = 100000
coef_X2 = 125000

# Objective function
lp_problem += coef_X1 * X1 + coef_X2 * X2, "Z"

# Constraints
lp_problem += 5 * X1 + 10 * X2 <= 250
lp_problem += 10 * X1 <= 135
lp_problem += 15 * X2 <= 300
lp_problem += 4 * X1 + 4 * X2 <= 125
lp_problem += X2 <= 15
lp_problem += 100 * X1 + 150 * X2 <= 5500
lp_problem += 4 * X1 + 6 * X2 <= 200
lp_problem += 8 * X1 + 12 * X2 <= 300
lp_problem += 2 * X2 <= 50
lp_problem += 4 * X1 + 6 * X2 <= 180
lp_problem += X1 == 10
lp_problem += X2 == 15

# Solve the problem
lp_problem.solve()

# Print the results
print(f"Status: {pulp.LpStatus[lp_problem.status]}")
print(f"X1 = {X1.varValue}")
print(f"X2 = {X2.varValue}")
print(f"Z = {pulp.value(lp_problem.objective)}")