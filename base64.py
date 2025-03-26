def base64_enc(word):
    # Define o tamanho dos blocos (3 bytes)
    block_bytes_len = 3
    # Define o tamanho dos miniblocos/grupos (6 bits)
    groups_bits_len = 6

    padding_char = '='

    table_ranges = {
        'ucase_letters': ('A', 0, 25), # Armazena o intervalo reservado para letras maiúsculas (A-Z)
        'lcase_letters': ('a', 26, 51), # Armazena o intervalo reservado para letras minúsculas (a-z)
        'digits': ('0', 52, 61) # Armazena o intervalo reservado para os algarismos/dígitos da base 10 (0-9)
    }

    # Obtém a representação em byte de cada caractere
    word_bytes = [f'{ord(char):08b}' for char in word]

    # Separa os bytes da palavra em blocos de 3 bytes
    blocks = [''.join(word_bytes[i: i + block_bytes_len]) for i in range(0, len(word_bytes), block_bytes_len)]

    # Organiza cada um dos blocos de 3 bytes em 4 grupos de 6 bits cada
    blocks = [[''.join(block[i: i + groups_bits_len]) for i in range(0, len(block), groups_bits_len)] for block in blocks]

    result = ''
    for block in blocks:
        for group_of_six in block:
            for table_range in table_ranges.values():
                num = int(group_of_six, 2) # Obtendo o equivalente em decimal do grupo de 6 bits
                first_char, start, end = table_range
                if start <= num <= end: # Verificando a qual intervalo da tabela o número representado (em bits) pertence
                    normalized_num = num - start # Calculando a distância/deslocamento do número para o primeiro do intervalo
                    result += chr(normalized_num+ ord(first_char)) # Concatenando o caractere obtido por chr ao resultado da codificação
                    break
    return result
