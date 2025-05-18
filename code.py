def cesar_cipher(text, shift, mode='encrypt'):
    result = ""
    text = text.lower()

    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            original_index = ord(char) - ord('a')
            new_index = (original_index + shift) % 26
            result += chr(new_index + ord('a'))
        else:
            result += char

    return result


# Elegir modo
while True:
    choice = input("¿Deseas cifrar o descifrar? (escribe 'cifrar' o 'descifrar'): ").strip().lower()
    if choice in ['cifrar', 'descifrar']:
        break
    else:
        print("Opción no válida. Intenta de nuevo.")

# Ingreso del mensaje
message = input("Ingresa el mensaje: ")

# Ingreso del desplazamiento con validación
while True:
    try:
        shift = int(input("¿Cuántas posiciones deseas desplazar las letras? "))
        break
    except ValueError:
        print("Por favor, ingresa un número entero válido.")

# Determinar modo
mode = 'encrypt' if choice == 'cifrar' else 'decrypt'

# Ejecutar y mostrar resultado
final_message = cesar_cipher(message, shift, mode)
print("Resultado:", final_message)
