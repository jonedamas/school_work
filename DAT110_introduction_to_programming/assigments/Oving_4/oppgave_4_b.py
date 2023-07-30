

file_name = input('Input file name: ')

main_dict = dict()

with open(file_name, 'r') as main_file:
    for line in main_file:
        stripped_line = line.strip()

        if stripped_line[:5] == 'From:':
            start_index = stripped_line.find('@') + 1
            end_index = stripped_line.find('>')
            key = stripped_line[start_index:end_index]
            if key in main_dict:
                main_dict[key] += 1
            else:
                main_dict[key] = 1


# Alphabetically sorting:

alpha_sorted_key_list = list()

for key in main_dict:
    alpha_sorted_key_list.append(key)
alpha_sorted_key_list.sort()

print()
print('Alphabeticaly sorted:')

for domain in alpha_sorted_key_list:
    print(f'Domain: {domain}  Frequency: {main_dict[domain]}')

# Frequency sorting:

highest_value = 0
for key in main_dict:
    if main_dict[key] > highest_value:
        highest_value = main_dict[key]

print()
print('Frequency sorted:')

while highest_value > 0:
    for key in main_dict:
        if main_dict[key] == highest_value:
            print(f'Domain: {key}  Frequency: {main_dict[key]}')
    highest_value -= 1
