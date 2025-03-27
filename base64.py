BASE64_TABLE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

BLOCKS_NUM = 3
GROUPS_LEN = 6

PADDING_CHAR = '=' # Define o caractere usado para preenchimento

def base64_encode(input_str: str):
    # Codifica a entrada usando utf-8 e salva os bytes na memória
    input_str = input_str.encode('utf-8')

    # Obtém a representação em bits da entrada
    input_bits = ''.join(f'{byte:08b}' for byte in input_str)

    # Calcula a quantidade de preenchimento (caso necessário)
    padding_num = BLOCKS_NUM - len(input_str) % BLOCKS_NUM if len(input_bits) % BLOCKS_NUM else 0

    # Organiza os bits em grupos de 6 bits
    # realizando o preenchimento a direita com zeros (caso preciso)
    groups = [''.join(input_bits[i: i + GROUPS_LEN].ljust(GROUPS_LEN, '0')) for i in range(0, len(input_bits), GROUPS_LEN)]
    return ''.join([BASE64_TABLE[int(group, 2)] for group in groups]) + PADDING_CHAR * padding_num

def base64_decode(input_str: str) -> str:
    # Retira o preenchimento na string (caso tenha)
    input_str = input_str.rstrip(PADDING_CHAR)

    input_bits = ''.join(f'{BASE64_TABLE.index(char):06b}' for char in input_str)

    # Obtém os bytes da "string" pré-decodificada
    # e eliminando blocos incompletos (menos de 8 bits)
    blocks = [input_bits[i: i + 8] for i in range(0, len(input_bits), 8) if len(input_bits[i: i + 8]) == 8]
    return ''.join(chr(int(byte, 2)) for byte in blocks)
