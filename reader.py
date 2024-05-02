import json

def read_json_file(file_path):

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{file_path}'")
        return None
    except json.JSONDecodeError:
        print(f"Error: No se pudo decodificar el archivo JSON '{file_path}'")
        return None
