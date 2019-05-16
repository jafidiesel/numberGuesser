from random import randint, sample
import customLengthError

# Generar numero aleatorio
#   Restricciones:
#       - Longitud de 4 digitos
#       - Digitos no repetidos: Cada nuevo numero que se genere debe verificar que no se encuentre generado.
#       - Valor comprendido entre 0000 y 9999
#       
# Verificar cantidad de coincidencias
#   - Se debe indicar cantidad de numeros acertados y en el lugar correcto (Bien)
#   - Se debe indicar cantidad de numeros acertados y en el lugar incorrecto (Regular)
# Condicion de salida
#   - Si se acerto a los 4 numeros en el orden correcto se devuelve "Juego Terminado", deteniendo la ejecucion

randomNumber = sample(range(10), 4)
print(randomNumber)

def evaluateInput(data):
    regularMatches = 0
    correctMatches = 0
    xindex = 0
    yindex = 0
    for x in str(randomNumber):
        for y in str(data):
            if x == y:
                if xindex == yindex:
                    correctMatches += 1 
                else:
                    regularMatches += 1
            yindex += 1
        xindex += 1
    

    return (str(regularMatches) + "R", correctMatches)



while ( True ):
    
    try:
        #ADD value validation
        inputRecieved = str(input("Enter a value:"))

        if not(int(inputRecieved)):
                    
        if not(int(inputRecieved)):
            raise ValueError
        elif len(inputRecieved) < 4:
            raise customLengthError.LengthTooSmallError
            continue
        elif len(inputRecieved) > 4:
            raise customLengthError.LengthTooLargeError
            continue
        else:
            print(evaluateInput(inputRecieved))


    except ValueError:
        print("Input value must be a number!")
        continue
    except customLengthError.LengthTooSmallError:
        print("El numero ingresado es menor a 4 digitos. Ingrese un numero de 4 digitos.")
    except customLengthError.LengthTooLargeError:
        print("El numero ingresado es mayor a 4 digitos. Ingrese un numero de 4 digitos.")

    
        
    

print("out of loop")
    
