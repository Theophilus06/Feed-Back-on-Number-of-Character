name = input('Pls Insert Your Name ')
if len(name) < 3:
    print('Name must be at least 3 characters')
elif len(name) >8:
    print('name can be a maximum of 8 characters')
else:
    print('name looks Good')