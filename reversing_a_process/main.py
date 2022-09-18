def decode(r):
    num = ""
    text = ""
    decoded_text = ""
    for l in r:
        if l.isdigit():
            num+=l
        else:
            text += l
    num = int(num)

    for c in text:
        err = False
        for i in range(26):
            if num * i % 26 == ord(c) - ord('a') and err == False:
                decoded_text += chr(i+97)
                err = True
            elif err == True and num * i % 26 == ord(c) - ord('a'):
                return "Impossible to decode"
            else:
                continue
    return decoded_text