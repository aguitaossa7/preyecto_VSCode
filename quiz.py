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
    # Esta función de darnos de forma aleatoria una pregunta y sus respuestas.
    # La salida de la función debe ser: pregunta, 
    #                                   [respuesta_a, respuesta_b, respuesta_c, respuesta_d,]
    #                                   opción correcta: indice lista
    lectura_json = read_json_file(r"preguntas_tema_1.json")
    datos_list = lectura_json["data"]
    pregunta_dict = datos_list.pop(randint(0,len(datos_list)))
    pregunta = pregunta_dict["pregunta"]
    respuestas = pregunta_dict["respuestas"]
    opc_correcta = pregunta_dict["opc_correcta"]
    return pregunta, respuestas, opc_correcta


def parse_question(question: str, options: list[str]) -> str:
    # Debe tomar la pregunta y parsearla a una cadena de texto amigable para el usuario.
    # Se incluye en la primera linea la pregunta, un espacio y en cada nueva linea una respuesta.
    # Cada respuesta debe ir precdida de a), b), c), d).
    pregunta_str = "\n%s\n" % question
    respuesta_str = ""
    for i, option in enumerate(options):
        respuesta_str += "\n%s\n" % (option)
    parse_question =  pregunta_str + respuesta_str
    return parse_question
    


def answer_question(correct: str) -> bool:
    # Usando la funcion de Python input, le pedimos su respuesta al usuario.
    # Comprobamos si la respuesta es correcta y retornamos True o False
    respuesta_user = input("Tu respuesta es: ")
    diccionario = {"a" : 0,  "b" : 1, "c" : 2, "d" : 3}
    respuesta_user = diccionario[respuesta_user]
    if respuesta_user == correct:
        return True
    else:
        return False

def show_correct(question, options, correct) -> None:    
    # Esta función debe tomar la opción correcta y mostrarla por pantalla
    print("Has fallado, la respuesta es: " + options[correct])

def show_counters(correct_question_num: int, total_question_num: int) -> None:
    # Muestra por pantalla un texto donde se indique la proporción de aciertos
    print("Has acertado " + str(correct_question_num) + " de " + str(total_question_num))
    

def run_quiz():
    correct_question_num = 0
    total_question_num = 0
    while True:
        # Llamada a la funciones:
        question, options, correct = get_question_data() # Debe leer del diccionario JSON los datos de la pregunta.
        parsed_question = parse_question(question, options)
        print(parsed_question)
        question_flag = answer_question(correct)
        if question_flag == False:
            show_correct(question, options, correct)
        else:
            correct_question_num +=1
        total_question_num += 1
        # Llamar a la función
        show_counters(correct_question_num, total_question_num)
        sleep(0.5)

if __name__ == "__main__":
    run_quiz()
