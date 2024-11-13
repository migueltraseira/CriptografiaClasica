import string
from collections import Counter
import numpy as np

# Función para sanear el texto
def sanitize_text(cipher_text):
    cleaned_text = cipher_text.replace(' ', '').upper()
    numbers = [ord(char) - ord('A') for char in cleaned_text if char in string.ascii_uppercase]
    return numbers

# Función para calcular el índice de coincidencia
def index_of_coincidence(text):
    n = len(text)
    freq = Counter(text)
    return sum([freq[c] * (freq[c] - 1) for c in freq]) / (n * (n - 1))

# Función para encontrar la longitud de la clave
def find_key_length(cipher_numbers, max_length=20):
    ic_values = []
    for length in range(1, max_length + 1):
        sequences = [cipher_numbers[i::length] for i in range(length)]
        avg_ic = sum(index_of_coincidence(seq) for seq in sequences) / length
        ic_values.append(avg_ic)
    return ic_values.index(max(ic_values)) + 1

# Función para descifrar usando una clave
def vigenere_decrypt(cipher_numbers, key):
    plaintext = []
    for i, num in enumerate(cipher_numbers):
        shift = key[i % len(key)]
        plain_num = (num - shift) % 26
        plaintext.append(chr(plain_num + ord('A')))
    return ''.join(plaintext)

# Frecuencias de letras en inglés
english_freqs = {
    'A': 0.082, 'B': 0.015, 'C': 0.028, 'D': 0.043, 'E': 0.127, 'F': 0.022,
    'G': 0.020, 'H': 0.061, 'I': 0.070, 'J': 0.002, 'K': 0.008, 'L': 0.040,
    'M': 0.024, 'N': 0.067, 'O': 0.075, 'P': 0.019, 'Q': 0.001, 'R': 0.060,
    'S': 0.063, 'T': 0.091, 'U': 0.028, 'V': 0.010, 'W': 0.024, 'X': 0.002,
    'Y': 0.020, 'Z': 0.001
}

# Función para encontrar la clave
def find_key(cipher_numbers, key_length):
    key = []
    for i in range(key_length):
        sequence = cipher_numbers[i::key_length]
        best_shift = 0
        best_score = float('-inf')
        for shift in range(26):
            decrypted = [(c - shift) % 26 for c in sequence]
            freq = Counter(decrypted)
            score = sum(freq[j] * english_freqs[chr(j + 65)] for j in range(26))
            if score > best_score:
                best_score = score
                best_shift = shift
        key.append(best_shift)
    return key

# Texto cifrado
cipher_text = "KVQMR KJSZG RJNOE IAKKF GCGWU WRHRU FIXDA GKOBP EGRQT TBZLF XAFHV ODWVL YHTEY WKHQR SSJHQ NRVKC FHRLY CZGVF JWPEG ZVSZT EWEQT MRFKC RTUWT OYPSW RFUNT VRBSE ELYSS AHDUW ECUSI UQDGZ VGBEN JRGTE USUPQ EAAEG FRHUK SPBLU YOZCR AKGFU PCWOE TVFKV QTBOV FMNQX FFFWB VRMEW NKECF SVYYH QDOQF IDTEG FDEOA LYSFH VJURM YVLNO ESVYY HQDOQ RGALQ AVFFA XWERA WASER PEYAM SDEQL FQUCR JFVQR RSUWF TUJFI SHNFU HTEAJ VQUTR VZHMT NHRFM DRGWH TEGJF CBSOJ ZBSIA YKVQG EWRHQ SGJVX AIPAE UFOND C"

# Sanear el texto
cipher_numbers = sanitize_text(cipher_text)

# Encontrar la longitud de la clave
key_length = find_key_length(cipher_numbers)

# Encontrar la clave
key = find_key(cipher_numbers, key_length)

# Descifrar el texto
decrypted_text = vigenere_decrypt(cipher_numbers, key)

print(f"Longitud de la clave: {key_length}")
print(f"Clave: {''.join([chr(k + 65) for k in key])}")
print(f"Texto descifrado: {decrypted_text}")