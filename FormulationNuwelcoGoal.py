import pulp

# Define the problem
prob = pulp.LpProblem("Goal_Programming_Production", pulp.LpMinimize)

# Decision variables
hoppers = pulp.LpVariable('Hoppers', lowBound=0, cat='Integer')
explosive_cars = pulp.LpVariable('Explosive_cars', lowBound=0, cat='Integer')

# Deviation variables for goals
d1_minus = pulp.LpVariable('d1_minus', lowBound=0)  # Labour hours (no overtime)
d1_plus = pulp.LpVariable('d1_plus', lowBound=0)
d2_minus = pulp.LpVariable('d2_minus', lowBound=0)  # Profit
d2_plus = pulp.LpVariable('d2_plus', lowBound=0)
d3_minus = pulp.LpVariable('d3_minus', lowBound=0)  # Labour hours (Eskom)
d3_plus = pulp.LpVariable('d3_plus', lowBound=0)
d4_minus = pulp.LpVariable('d4_minus', lowBound=0)  # Bolt usage
d4_plus = pulp.LpVariable('d4_plus', lowBound=0)
d5_minus = pulp.LpVariable('d5_minus', lowBound=0)  # Nut usage
d5_plus = pulp.LpVariable('d5_plus', lowBound=0)

# Objective function: Minimize the sum of deviations
prob += (d1_minus + d1_plus + d2_minus + d2_plus + d3_minus + d3_plus + d4_minus + d4_plus + d5_minus + d5_plus), "Minimize Deviations"

# Goal constraints
prob += (4 * hoppers + 6 * explosive_cars) - d1_plus + d1_minus == 180, "Labour hours (no overtime)"
prob += (100000 * hoppers + 125000 * explosive_cars) - d2_plus + d2_minus == 2500000, "Maximize profit"
prob += (4 * hoppers + 6 * explosive_cars) - d3_plus + d3_minus == 150, "Labour hours (Eskom)"
prob += (100 * hoppers + 150 * explosive_cars) - d4_plus + d4_minus == 3500, "Limit usage of bolts"
prob += (100 * hoppers + 150 * explosive_cars) - d5_plus + d5_minus == 3500, "Limit usage of nuts"

# Normal constraints
prob += 5 * hoppers + 10 * explosive_cars <= 250, "Welding rods wire"
prob += 10 * hoppers <= 135, "Steel plate 3mm"
prob += 15 * explosive_cars <= 300, "Steel plate 5mm"
prob += 4 * hoppers + 4 * explosive_cars <= 125, "Cast iron wheels"
prob += hoppers <= 15, "Dolly wheel"
prob += 5 * hoppers + 10 * explosive_cars <= 250, "Paint coating"
prob += 4 * hoppers + 6 * explosive_cars <= 200, "Buffers"
prob += 8 * hoppers + 12 * explosive_cars <= 300, "Wheel rubber"
prob += 2 * explosive_cars <= 50, "Rubber lining"

# Production limits
prob += hoppers == 10, "Max hoppers"
prob += explosive_cars == 15, "Max explosive cars"

# Solve the problem
prob.solve()

# Output the results
print(f"Status: {pulp.LpStatus[prob.status]}")
print(f"Hoppers produced: {pulp.value(hoppers)}")
print(f"Explosive cars produced: {pulp.value(explosive_cars)}")
print(f"Total Profit: {100000 * pulp.value(hoppers) + 125000 * pulp.value(explosive_cars)}")

# Deviations
print(f"Labour hours (no overtime) deviation: {pulp.value(d1_minus)} under, {pulp.value(d1_plus)} over")
print(f"Profit deviation: {pulp.value(d2_minus)} under, {pulp.value(d2_plus)} over")
print(f"Labour hours (Eskom) deviation: {pulp.value(d3_minus)} under, {pulp.value(d3_plus)} over")
print(f"Bolt usage deviation: {pulp.value(d4_minus)} under, {pulp.value(d4_plus)} over")
print(f"Nut usage deviation: {pulp.value(d5_minus)} under, {pulp.value(d5_plus)} over")
