file = open('./hello.txt')
content = file.read()
print(content)
contentLines = file.readlines()
print(contentLines)
file.close()

fileWriteable = open('./hello.txt', 'w')  # writes over existing file, a will append
fileWriteable.write('Hello\nPython!')
fileWriteable.close()
