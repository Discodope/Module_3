call= 0
def count_calls():
    global call
    call += 1

def string_info(string1):
    count_calls()
    name = (len(string1), string1.upper(), string1.lower())
    return name

def is_contain(string2, lst):
    count_calls()
    for i in lst:
        if i.lower() in string2.lower():
            return True

    return False

print(string_info('Capybara'))

print(string_info('Armageddon'))

print(is_contain('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN

print(is_contain('cycle', ['recycling', 'cyclic'])) # No matches

print(call)