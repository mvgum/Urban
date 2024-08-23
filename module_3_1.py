# Домашняя работа по уроку "Пространство имён"


calls = 0
def count_calls():
    global calls
    calls += 1
    return calls


def string_info(string ):
    count_calls()
    len_string = len(string )
    up_string = string .upper()
    low_string = string .lower()
    return (len_string, up_string, low_string)


def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    for elem in list_to_search:
        if string == elem.lower():
            return True
    return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
