def read_text_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print(f"Error: El archivo '{file_path}' no se encuentra.")
        return None
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None


def valid_paragraphs(text):
    paragraphs = text.split("\n\n")  
    
    #Verificar que haya al menos 2 párrafos
    valid_paragraphs = 0
    for paragraph in paragraphs:
        #Contar las palabras del párrafo
        word_count = len(paragraph.split())  
        #Verificar si el párrafo tiene al menos 95 palabras
        if word_count >= 95:  
            valid_paragraphs += 1
    
    return valid_paragraphs >= 2
