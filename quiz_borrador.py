"""
Aplicación CLI que nos permita repasar los conceptos
teóricos vistos en clase.

La aplicación al iniciarse nos muestra en la terminal una pregunta y
cuatro opciones de respuesta. El usaurio debe elegir una de ellas. En caso de
ser correcta el programa pasa a la siguiente. En caso de no serlo se muestra
en pantalla la opción correcta.

Además, cada vez que el usuario introduce una respuesta debemos mostrar en pantalla
la proporción de preguntas acertadas frentre al total de preguntas realizadas.

Esto representa una plantilla para la generación del programa base.
"""
from time import sleep
from reader import read_json_file
from random import randint

def get_question_data() -> tuple[str, list[str], int]:
   
    lectura_json = read_json_file(r"C:\Users\AsataM\Desktop\proyecto\preguntas\preguntas_tema_1.json")
    datos = lectura_json["data"][randint(0,5)]
    pregunta = datos["pregunta"]
    respuestas = datos["respuestas"]
    opc_correcta = datos["opc_correcta"]
    return (pregunta, respuestas, opc_correcta)

   # datos {"[pregunta] [respuestas] [opc_correcta]"}
    # return pregunta

question = get_question_data()
print(question)

