from Individual import individual
import Individual
import Recombinations

creator = individual(['O_0', 'O_1'], ['A_0','A_1'],['V_0','V_1'],['add','sub','mul','div','and','or','not','if'])
p1 = creator.generate_program(4)
p2 = creator.generate_program(4)

print(p1)
print(Individual.printProgram(p1))
print(p2)
print(Individual.printProgram(p2))

# One-Point crossover 
p1_c, p2_c = Recombinations.linear_crossover(p1,p2)
print('----------')
print(p1_c)
print(Individual.printProgram(p1_c))
print(p2_c)
print(Individual.printProgram(p2_c))

