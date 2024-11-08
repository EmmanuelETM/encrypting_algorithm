def encrypt(text, key):
    encrypted_text = ""
    key_length = len(key)

    #Desplazar cada carácter con el valor de la clave correspondiente
    for i, char in enumerate(text):
        #Obtener valor ASCII de la clave
        byte = ord(key[i % key_length])  
        #Desplazamiento del carácter
        encrypted = chr(ord(char) + byte) 
        encrypted_text += encrypted

    return encrypted_text

def decrypt(encrypted_text, key):
    decrypted_text = ""
    length = len(key)

    #Desplazar en sentido contrario
    for i, char in enumerate(encrypted_text):
        #Obtener valor ASCII de la clave
        byte = ord(key[i % length])  
        #Desplazamiento inverso
        decrypted = chr(ord(char) - byte) 
        decrypted_text += decrypted

    return decrypted_text


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
    

def write_to_file(file_path, encrypted_text, decrypted_text):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write("===================== TEXTO ENCRIPTADO =====================\n")
        file.write(encrypted_text + "\n\n")
        file.write("\n\n===================== TEXTO DESENCRIPTADO =====================\n")
        file.write(decrypted_text + "\n")
    print(f"\nFile created. Data has been writen'{file_path}'.")


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



def main():
    print("Encrypt/Decrypt program!!!\n\n")
    
    file_path = input("Enter the route of the file (Ex. text.txt): ")
    text = read_text_from_file(file_path)
    
    if text is None or not valid_paragraphs(text):
        print("\n\nThat text is not valid!!")
        return
    
    print("\nText read correctly!\n")
    
    encryption_key = input("Enter the encrypt key (8 characters): ")
    while len(encryption_key) < 8:
        print("\nThe key must have 8 characters")
        key = input("\nPlease, enter a valid key (8 characters): ")

    encrypted_text = encrypt(text, encryption_key)

    decryption_key = input("\nEnter the key to decrypt the text: ")
    while decryption_key != encryption_key:
        print("The keys don't match")
        decryption_key = input("Please, enter the correct key: ")

    decrypted_text = decrypt(encrypted_text, decryption_key)

    output_file = "output.txt"
    write_to_file(output_file, encrypted_text, decrypted_text)


if __name__ == "__main__":
    main()



