from utils.functions import *

def SpeechToText():
    # Mostrar opciones al usuario para convertir voz a texto
    print('\n')
    print('Seleccione cómo desea convertir el audio:')
    print('1. Convertir mi voz a texto')
    print('2. Convertir un archivo de audio del sistema a texto')
    
    # Leer la opción seleccionada por el usuario
    option = input('\n→')

    # Procesar la opción seleccionada
    match option:
        case '1':
            # Obtener texto ingresado por voz del usuario
            text = getAudioUser()
            if text:
                print(f'Voz ingresada por el usuario: {text}')
            else:
                print('No se pudo reconocer la voz o ocurrió un error.')
        case '2':
            # Obtener texto desde un archivo de audio del sistema
            text = getWavFile()
            if text:
                print(f'Texto del audio seleccionado del archivo: {text}')
            else:
                print('No se seleccionó ningún archivo o el archivo está vacío o no se pudo procesar.')
        case _:
            # Manejar una opción no válida
            print('Opción no válida. Por favor, seleccione una opción válida.')

if __name__ == '__main__':
    SpeechToText()
