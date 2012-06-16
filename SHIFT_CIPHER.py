import string
def shift_cipher():
    
    text = unicode(raw_input("Please enter Plaintext to Cipher: "), "UTF-8")
    k = int(raw_input("Please enter the shift: "))

    in_alphabet = unicode(string.ascii_lowercase)
    out_alphabet = in_alphabet[k:] + in_alphabet[:k]

    translation_table = dict((ord(ic), oc) for ic, oc in zip(in_alphabet, out_alphabet))

    print text.translate(translation_table)


if __name__=="__main__":
    '''try following input text'''
    '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj'''
    
    shift_cipher()
