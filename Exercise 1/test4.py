def find_first_2_letter_word(xs):
    for wd in xs:
        if len(wd) == 2:
            print(wd)
            return ""
    return ""

find_first_2_letter_word(["and", "how", "do", "you", "do"])
print()
print()