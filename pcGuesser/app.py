from random import randint
import customLengthError

def evaluateInput(data):    
    return data

def getNonRepeatedNumber(numberList):
    if len(str(numberList)) == 0:
        break

    for x in numberList:
        while True:
            if randint(0,9) == numberList[x]:
                pass
    pass




# Generar numero aleatorio
#   Restricciones:
#       - Longitud de 4 digitos
#       - Digitos no repetidos: Cada nuevo numero que se genere debe verificar que no se encuentre generado.
#       - Valor comprendido entre 0000 y 9999
#       - 
# Verificar cantidad de coincidencias
#   - Se debe indicar cantidad de numeros acertados y en el lugar correcto (Bien)
#   - Se debe indicar cantidad de numeros acertados y en el lugar incorrecto (Regular)
# Condicion de salida
#   - Si se acerto a los 4 numeros en el orden correcto se devuelve "Juego Terminado", deteniendo la ejecucion


def generateRandomNumber(fromValue, untilValue, length):
    randomNumberGenerated = ""
    for x in range(length):
        
        randomNumberGenerated = randomNumberGenerated + getNonRepeatedNumber(randomNumberGenerated)
    
    return randomNumberGenerated

randomNumber = generateRandomNumber(0, 9, 4)


# ADD data type validation

while ( True ):
    
    try:
        inputRecieved = int(input("Enter a value:"))
        
        if len(str(inputRecieved)) < 4:
            raise customLengthError.LengthTooSmallError
        elif len(str(inputRecieved)) > 4:
            raise customLengthError.LengthTooLargeError
        #continue

    except ValueError:
        print("Input value must be a number!")
        continue
    except customLengthError.LengthTooSmallError:
        print("El numero ingresado es menor a 4 digitos")
    except customLengthError.LengthTooLargeError:
        print("El numero ingresado es mayor a 4 digitos")

    

    if inputRecieved < 11111111 :
        evaluateInput(inputRecieved)
        print ( randomNumber )
    else:
        break
    
    

print("out of loop")
    
