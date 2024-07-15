def calculator(op1,operation,op2):
    if operation == '+':
        result=op1+op2
    elif operation == '-':
        result=op1-op2
    elif operation == '*':
        result=op1*op2
    elif operation == '/':
        result=op1/op2
    return result
print('==================CALCULATOR======================')
operand1=float(input('Enter the first operand:'))
operator=input('Enter the operation you want to perform (+,-,*,/):')
operand2=float(input('Enter the second operand:'))
print(operand1,operator,operand2)
calculatedresult=calculator(operand1,operator,operand2)
print('=',calculatedresult)
