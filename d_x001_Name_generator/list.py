# my_list = [12, 13, 14, 15, 16]

# my_list.append(10)

# my_list.extend([1, 2, 3])

# print(my_list)

## Treasure Hiding (hide the treasure)
sublist1 = [" ", " ", " "]
sublist2 = [" ", " ", " "]
sublist3 = [" ", " ", " "]

master_list = [sublist1, sublist2, sublist3]
print("Hiding treasure: Mark the spot (example, a1 c3 etc)")
position = input()
letter = position[0].lower()

abc = ["a", "b", "c"]  # make this list to match the input
letter_index = abc.index(letter)  # what is the index of the letter

number_index = int(position[1]) - 1
master_list[letter_index][number_index] = "X"

# print(letter_index, number_index)
print(f"{sublist1}\n{sublist2}\n{sublist3}\n")
