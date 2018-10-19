string = "random-string"
sstr = 'A'
for i in range(65):
    copy = string
    # copy = sstr
    for x in copy:
        letter = ord(x)+i
        if(letter >= 126):
            letter = 32 + (letter%126)
        print(chr(letter), end='', flush=True)
    print('\n')

