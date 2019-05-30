def get_summ(one, two, delimiter='&'):
    return str.upper(one) + str(delimiter) + str.upper(two)
print(get_summ('learn', 'python', '-'))