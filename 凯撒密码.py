#字母移位

alphabet = 'abcdefghijklmnopqrstuvwxyz'
shift = 5
new_alphabet = alphabet[shift:] + alphabet[:shift]
#创建字符转换表
translation_table = str.maketrans(alphabet,new_alphabet)
text = "hello world"
#字符转换
encrypted_text = text.translate(translation_table)
print(encrypted_text)