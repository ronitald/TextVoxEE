# Importación de librerías necesarias
import sys
from PyQt5.QtWidgets import QApplication, QFileDialog

def getTextUser():
    # Solicitar al usuario que ingrese el texto que desea convertir.
    text = input('Escribe el texto que deseas convertir:\n') 
    return text

def getTextFile(nameFile=None):
    # Obtener el texto de un archivo.
    if nameFile is None:
        # Crear la aplicación Qt si no se proporciona un nombre de archivo
        app = QApplication(sys.argv)

        # Configurar opciones del diálogo de archivo
        options = QFileDialog.Options()
        selected_file, _ = QFileDialog.getOpenFileName(
            None,
            "Selecciona un archivo de texto",
            "",
            "Archivos de texto (*.txt);;Todos los archivos (*)",
            options=options
        )

        if selected_file:
            try:
                # Leer el contenido del archivo seleccionado
                with open(selected_file, 'r', encoding='utf-8') as file:
                    text = file.read()
                return text  
            except Exception as e:
                # Manejar cualquier error 
                return f'Ocurrió un error: {e}'
        else:
            return 'No se seleccionó ningún archivo.'
    else:
        try:
            # Leer el contenido del archivo especificado por nameFile
            with open(nameFile, 'r', encoding='utf-8') as file:
                text = file.read()
            return text  
        except FileNotFoundError:
            return 'Archivo no encontrado.'  
        except Exception as e:
            # Manejar cualquier error
            return f'Ocurrió un error: {e}'
