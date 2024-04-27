def writeFile(filename):
    outfile = open(filename, 'w')
    content = outfile.write('Hello Word!')
    outfile.close()
    print(content)

writeFile('teste.txt')