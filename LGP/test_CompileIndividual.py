from Individual import individual
import Individual

obj = individual(['a'], ['b'],['c'],['add','sub','mul','div','if'])
program = obj.generate_program(10)
codeObejct = Individual.compile_program(program)

# initilize parameter
a = 1
b = 2
c = 3

print('Before:',a,b,c)

exec(codeObejct) #run the code

print('After:',a,b,c)