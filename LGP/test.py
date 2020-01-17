from Individual import individual

obj = individual(['O_0', 'O_1'], ['A_0','A_1'],['V_0','V_1'],['add','sub','mul','div','and','or','not'])
obj.generate_program(10)