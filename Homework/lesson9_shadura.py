import re

# task 1
print('task 1')

str_1 = 'Its_my_7_Life'
str_2 = 'it`s 4 now or never'
str_3 = 'But I ain`t gonna live forever'
str_4 = 'I_just_want_to_LIVE_7_while_I_am_alive'
str_5 = 'Yeah_this_is_for_1_who_stood_their_ground'
str_6 = 'For Tommy and Gina_who_never_backed_down'
strings = [str_1, str_2, str_3, str_4, str_5, str_6]

pattern = r'[^a-zA-Z0-9_]'

for strg in strings:
    match_str = re.findall(pattern, strg)
    if not match_str:
        print(strg)

# task 2
print('\ntask 2')

str_1 = ["example (.com)", "github (.com)", "stackoverflow (.com)"]

for word in str_1:
    end_word = re.sub(r'\(.*?\)', '', word)
    print(end_word)

# task 3
print('\ntask 3')

str_1 = 'ForTommyandGina,whoNeverBackeddown'
str_2 = re.sub(r'([A-Z])', r' \1', str_1)

print(str_2)
