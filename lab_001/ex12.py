# 12) Assuming that the population of country A is of the order of 
# 80,000 with an annual growth rate of 3% and that the population of 
# B is 200,000 with an annual growth rate of 1.5%. Write a program 
# that calculates and writes down the number of years it takes for the 
# population of country A to exceed or equal the population of country 
# B, maintaining growth rates.

population_a = 80000
rate_a = 0.03

population_b = 200000
rate_b = 0.015

count_yars = 0

while(population_a < population_b):
    population_a += population_a * rate_a
    population_b += population_b * rate_b
    count_yars += 1

print("After ", count_yars, "years")
print("population_a:", population_a)
print("population_b:",population_b)