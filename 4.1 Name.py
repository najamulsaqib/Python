def design_name(name, ln):
    for i in range(0, ln):
        if name[i] == "A" or name[i] == "a":
            ch = "卂"
            print(ch, end='')
        elif name[i] == "B" or name[i] == "b":
            ch = "乃"
            print(ch, end='')
        elif name[i] == "C" or name[i] == "c":
            ch = "匚"
            print(ch, end='')
        elif name[i] == "D" or name[i] == "d":
            ch = "ᗪ"
            print(ch, end='')
        elif name[i] == "E" or name[i] == "e":
            ch = "乇"
            print(ch, end='')
        elif name[i] == "F" or name[i] == "f":
            ch = "千"
            print(ch, end='')
        elif name[i] == "G" or name[i] == "g":
            ch = "Ꮆ"
            print(ch, end='')
        elif name[i] == "H" or name[i] == "h":
            ch = "卄"
            print(ch, end='')
        elif name[i] == "I" or name[i] == "i":
            ch = "丨"
            print(ch, end='')
        elif name[i] == "J" or name[i] == "j":
            ch = "ﾌ"
            print(ch, end='')
        elif name[i] == "K" or name[i] == "k":
            ch = "Ҝ"
            print(ch, end='')
        elif name[i] == "L" or name[i] == "l":
            ch = "ㄥ"
            print(ch, end='')
        elif name[i] == "M" or name[i] == "m":
            ch = "爪"
            print(ch, end='')
        elif name[i] == "N" or name[i] == "n":
            ch = "几"
            print(ch, end='')
        elif name[i] == "O" or name[i] == "o":
            ch = "ㄖ"
            print(ch, end='')
        elif name[i] == "P" or name[i] == "p":
            ch = "卩"
            print(ch, end='')
        elif name[i] == "Q" or name[i] == "q":
            ch = "Ɋ"
            print(ch, end='')
        elif name[i] == "R" or name[i] == "r":
            ch = "尺"
            print(ch, end='')
        elif name[i] == "S" or name[i] == "s":
            ch = "丂"
            print(ch, end='')
        elif name[i] == "T" or name[i] == "t":
            ch = "ㄒ"
            print(ch, end='')
        elif name[i] == "U" or name[i] == "u":
            ch = "ㄩ"
            print(ch, end='')
        elif name[i] == "V" or name[i] == "v":
            ch = "ᐯ"
            print(ch, end='')
        elif name[i] == "W" or name[i] == "w":
            ch = "山"
            print(ch, end='')
        elif name[i] == "X" or name[i] == "x":
            ch = "乂"
            print(ch, end='')
        elif name[i] == "Y" or name[i] == "y":
            ch = "ㄚ"
            print(ch, end='')
        elif name[i] == "Z" or name[i] == "z":
            ch = "乙"
            print(ch, end='')
        elif name[i] == " ":
            print(" ", end='')
        else:
            print(name[i], end='')

# Main
name = input("Enter your name: ")
ln = len(name)
design_name(name, ln)