import string

# Texto cifrado
cipher_text = ("NOYZU XEOYV ATIZA GZKJC OZNIU JKYZN KENGB KJKIO JKJZN KUAZI USKYU LHGZZ RKYGT JRKJZ UZNKJ KGZNY ULQOT MYGTJ WAKKT YONGB KZNKX KLUXK HKKTG HRKZU IGRRA VUTYZ UXOKY ULVUR OZOIG ROTZX OMAKG TJZGR KYULR OLKGT JJKGZ NZUOR RAYZX GZKZN KQKEZ AXTOT MVUOT ZYOTZ NKKBU RAZOU TGXEJ KBKRU VSKTZ ULIUJ KYZNK NOYZU XEULI UJKYO YYUOT UXJOT GZKRE XOINZ NGZON GBKHK KTLUX IKJZU RKGBK UAZSG TELGY IOTGZ OTMYZ CNOIN UXOKY OTZAX TSKGT YZNGZ SEGII UATZO YTUZJ KLOTO ZOBKO LEUAC UARJR OQKZU LOTJU AZSUX KGHUA ZEUAX LGBUX OZKZG RKUXE UAXLG BUXOZ KIUJK HXKGQ KXZNK TOCUA RJXKL KXEUA ZUZNK ROYZU LLAXZ NKXXK GJOTM CNOIN YNUAR JNKRV ZNUYK XKGJK XYCNU CUARJ ROQKZ UYZAJ EZNKY AHPKI ZOTSU XKJKZ GOR")

# Paso 1: Saneamiento del texto cifrado (quitar espacios y convertir a minúsculas)
sanitized_cipher_text = ''.join(filter(str.isalpha, cipher_text)).lower()

# Paso 2: Definir el alfabeto y su longitud
alphabet = string.ascii_lowercase
N = len(alphabet)

# Función para convertir texto a números según posición en el alfabeto
def text_to_numbers(text):
    return [alphabet.index(char) for char in text]

# Función para convertir números a texto según posición en el alfabeto
def numbers_to_text(numbers):
    return ''.join(alphabet[num] for num in numbers)

# Función de descifrado usando la fórmula dada con clave k
def decrypt_with_key(cipher_numbers, key):
    decrypted_numbers = [(num + (N - key)) % N for num in cipher_numbers]
    return numbers_to_text(decrypted_numbers)

# Paso 3: Convertir el texto cifrado a números
cipher_numbers = text_to_numbers(sanitized_cipher_text)

# Paso 4 y 5: Probar cada clave y verificar si el texto tiene sentido en inglés
# Función para verificar si el texto contiene palabras comunes en inglés
def is_english_text(text):
    # Lista de palabras comunes en inglés
    common_words = ["the", "and", "to", "of", "in", "it", "is", "on", "that", "by"]
    # Contamos cuántas de estas palabras están en el texto descifrado
    return sum(word in text for word in common_words) > 5

# Probar cada clave posible
for key in range(N):
    # Descifrar el texto con la clave actual
    decrypted_text = decrypt_with_key(cipher_numbers, key)
    
    # Verificar si el texto tiene sentido en inglés
    if is_english_text(decrypted_text):
        print(f"Clave de descifrado encontrada: {key}")
        
        # Paso final: Restaurar formato con espacios y otros caracteres
        formatted_decrypted_text = []
        idx = 0  # Índice para iterar el texto descifrado limpio
        
        # Iteramos en el texto original para añadir los caracteres de formato
        for char in cipher_text:
            if char.isalpha():  # Si es una letra, añadimos el siguiente caracter descifrado
                formatted_decrypted_text.append(decrypted_text[idx])
                idx += 1
            else:  # Si no es una letra, lo añadimos directamente (espacio, coma, etc.)
                formatted_decrypted_text.append(char)
        
        # Unimos la lista final en un solo string y mostramos el resultado
        formatted_decrypted_text = ''.join(formatted_decrypted_text)
        
        print("Texto descifrado con formato:")
        print(formatted_decrypted_text)
        break