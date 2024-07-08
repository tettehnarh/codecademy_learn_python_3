alphabet_list = "abcdefghijklmnopqrstuvwxyz"

encrypted_msg = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"

# encrypted_msg_split = encrypted_msg.split(' ')

# print(encrypted_msg_split)

decrypted_msg = ""

for char in encrypted_msg:
    if char in alphabet_list:
        char_index = alphabet_list.find(char)
        decrypted_msg += alphabet_list[(char_index + 10) % 26]
    else:
        decrypted_msg += char


print(decrypted_msg)
