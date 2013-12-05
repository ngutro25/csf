alphabet_list = "abcdefghijklmnopqrstuvwxyz"
cipher_list =list(alphabet_list)




def encrypt(message_txt):
    for x in message_txt:
        c = alphabet_list.index(x)
        y = cipher_list(c)
    return cipher_txt
        
print encrypt("whatisabaggin")
        
def encrypt(message_txt):
    pass