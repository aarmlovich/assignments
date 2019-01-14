#reading a text file

with open('name.txt') as f:
    my_name = f.read()

print(my_name)

#writing a text file

with open('hello.txt', 'w') as f:
    f.write('Hello, my name is ')
    f.write(my_name)
    f.write('\n')