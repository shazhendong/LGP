import ArithmeticOperations
import LogicOperations

obj = ArithmeticOperations.add('A','B','C')
print(obj)

obj = ArithmeticOperations.sub('A','B','C')
print(obj)

obj = ArithmeticOperations.mul('A','B','C')
print(obj)

obj = ArithmeticOperations.div_protected('A','B','C')
print(obj)

print(LogicOperations.AND('A','B','C'))
print(LogicOperations.OR('A','B','C'))
print(LogicOperations.NOT('A','B'))