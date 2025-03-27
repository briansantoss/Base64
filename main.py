import base64

word = input('Enter a word: ')
encode = base64.base64_encode(word)
print('Encoded:', encode)

decode = base64.base64_decode(encode)
print('Decoded:', decode)