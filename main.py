with open("./Input/Names/invited_names.txt", mode="r") as file:
    names = file.readlines()

    for name in names:
        name = name.strip()
        with open("Input/Letters/starting_letter.txt", mode="r") as l:
            letter = l.read()
            new_letter = letter.replace("[name]", name.strip())

            with open(f"./Output/ReadyToSend/{name}_letter.txt", mode="x") as new_file:
                new_file.write(new_letter)
