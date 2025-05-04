print('Gullible')
while True:
    print('Do you want to know how to keep a gullible person busy for hours? Y/N')
    response = input('> ')
    if response.lower() == 'no' or response.lower() == 'n':
        break
    elif response.lower() == 'yes' or response.lower() == 'y':
        continue
    else:
        print('"{}" is not a valid yes/no response.'.format(response))
print('Thank you. Have a nice day.')
    
