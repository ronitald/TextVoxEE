from textToSpeech import textToSpeech
from speechToText import SpeechToText

def main():
    print('Seleccione la operación deseada:')
    print('1. Convertir voz a texto')
    print('2. Convertir texto a voz')

    option = input('\n→')

    match option:
        case '1':
            SpeechToText()
        case '2':
            textToSpeech()
        case _:
            print('Opción no válida. Por favor, seleccione una opción válida.')

if __name__ == '__main__':
    main()