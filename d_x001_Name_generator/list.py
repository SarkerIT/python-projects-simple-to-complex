# my_list = [12, 13, 14, 15, 16]

# my_list.append(10)

# my_list.extend([1, 2, 3])

# print(my_list)

## Treasure Hiding (hide the treasure)
line1 = [" ", " ", " "]
line2 = [" ", " ", " "]
line3 = [" ", " ", " "]

map = [line1, line2, line3]
print("Hiding treasure: Mark the spot")
position = input()
letter = position[0].lower()

abc = ["a", "b", "c"]
letter_index = abc.index(letter)

number_index = int(position[1]) - 1
map[letter_index][number_index] = "X"

# print(letter_index, number_index)
print(f"{line1}\n{line2}\n{line3}\n")
