f = open('test.txt', 'w+')
f.write('hello world\n' * 5)
f.seek(0)
print(f.read())
f.close()

f = open('test.txt', 'r')
content = f.read()
f.close()


f = open('test.txt', 'w')
f.write(content.upper())
f.close()

f = open('test.txt', 'r')
lines = f.readlines()
lines[2] = lines[2].capitalize()
f.close()

f = open('test.txt', 'w')
f.writelines(lines)
f.close()

with open('test.txt', 'a') as f:
    f.write('I Love Python')
