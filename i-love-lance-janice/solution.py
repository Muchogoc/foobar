import string


def solution(input):
    letters = list(str(input))
    output = ""

    if len(letters) == 0:
        return output

    for index, letter in enumerate(letters):
        if not letter.isdigit() and letter.islower():
            alphabet = list(string.ascii_lowercase)

            # x --> index of letter in alpabet
            x = alphabet.index(letter)
            # 26 letters in alphabet, 25 index of 'z' in list
            new_letter = alphabet[25 - x]

            letters[index] = new_letter

    return output.join(letters)
