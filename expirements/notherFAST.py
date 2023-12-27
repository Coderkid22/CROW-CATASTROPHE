filePath = input('what is the file path and if its in a dir then put the dirs name to?: ')
old_text = input('what are the char(s) you want to replace?: ')
new_text = input('what do you want to replace it with?:  ')
print(f'{filePath} {old_text} {new_text}')
 
 
with open(filePath, 'r') as file:
    lines = file.readlines()
lines = [line.replace(old_text, new_text) for line in lines]
with open(filePath, 'w') as file:
    file.writelines(lines)