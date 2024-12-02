def get_multiplied_digits(number):
    str_number = str(number)
    if len(str_number) > 1:
        first = int(str_number[0])
        return first * get_multiplied_digits(int(str_number[1:]))
    for i in str_number:
        if i == '0':
            return 1
    else:
        return int(str_number)
res1 = get_multiplied_digits(402030)
print(res1)
