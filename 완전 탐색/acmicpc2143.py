dec = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
usr_input = input()

for t in dec:
    usr_input = usr_input.replace(t, '!')
print(len(usr_input))