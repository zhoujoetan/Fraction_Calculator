from Fraction import *
def evaluate(fraction, inputString):
    """Evaluates the expression specified by inputString using fraction as the initial value"""
    #split the string to list
    #read the list one by one
        #if it is a uniary operator, perform the operation to current fraction
        #if it is a binary operator
            #if there is already a binary operator
                #raise valueError
            #otherwise we store it
        #if it is a operand, check if there is a binary operator
            #if there is a binary operator
                #perfrom the calcuation, store the result
                #otherwise,directly store the operand
    currentFraction = fraction
    currentOperator = None
    inputList = inputString.split()
    operation = {'+': Fraction.add,
                 '-': Fraction.subtract,
                 '*': Fraction.multiply,
                 '/': Fraction.divide}
    for currentElement in inputList:
        if currentElement.lower().startswith('a'):
            currentFraction =  currentFraction.absValue()
        
        elif currentElement.lower().startswith('n'):
            currentFraction = currentFraction.negate()

        elif currentElement.lower().startswith('c'):
            currentFraction = Fraction(0,1)
            currentOperator = None

        elif currentElement.lower().startswith('q'):
            raise EOFError

        elif currentElement in ['/', '*', '+', '-']:
            if currentOperator != None:
                raise ValueError
            currentOperator = currentElement

        else:
            tempList = currentElement.split('/', 1)
            #whole number case
            if len(tempList) == 1 and (int(tempList[0]) or tempList[0].isdigit()):
                tempFraction = Fraction(int(tempList[0]),1)
            elif (int(tempList[0]) or tempList[0].isdigit()) \
                 and (int(tempList[1]) or tempList[1].isdigit()):
                tempFraction = Fraction(int(tempList[0]), int(tempList[1]))
            else:
                #invalid input
                currentFraction = Fraction(0,1)
                currentOperator = None
                raise ValueError
            if currentOperator != None:
                #invoke the function defined in the operator dictionary
                currentFraction = operation[currentOperator](currentFraction, 
                                                             tempFraction) 
                currentOperator = None
            else:
                currentFraction = tempFraction

    return currentFraction

def main():
    fraction = Fraction(0,1)
    print("Welcome to the calculator. Made by Tan Zhou and Swati Goswami")
    while True:
        try:
            inputString = input("Enter the expression to be calculated:")
            fraction = evaluate(fraction, inputString)
            print("The result of inputString is :",fraction)
        except EOFError:
            print("Goodbye")
            return None
        except:
            fraction = Fraction(0,1)
            print("Error")





            
        
        
