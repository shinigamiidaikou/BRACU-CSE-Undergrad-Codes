# Write a Python program to find the largest and smallest word in a string.
# [you are not allowed to use max() and min()]

# **Sample Input** :
# It is a string with the smallest and largest word.

# **Sample Output** :
# The largest word is "smallest" and the smallest word is 'a'.


main_string = input()
temporary_string = ""
string_List = []

for i in range(len(main_string)):
    if main_string[i] != " ":
        if i == len(main_string) - 1 or main_string[i] == ".":
            temporary_string += main_string[i]
            string_List.append(temporary_string)
        else:
            temporary_string += main_string[i]
    else:
        string_List.append(temporary_string)
        temporary_string = ""

print(string_List)

Large_count = 0
smaLL_count = len(main_string)
Largest_string = ""
smaLLest_string = ""

for item in string_List:
    if Large_count < len(item):
        Large_count = len(item)
        Largest_string = item
    elif smaLL_count > len(item):
        smaLL_count = len(item)
        smaLLest_string = item

print(f"The largest word is \"{Largest_string}\" and the smallest word is \'{smaLLest_string}\'.")
