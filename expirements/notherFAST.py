filePath = input('what is the file path and if its in a dir then put the dirs name to?: ')
old_text = input('what are the char(s) you want to replace?: ')
new_text = input('what do you want to replace it with?:  ')
print(f'{filePath} {old_text} {new_text}')
 
 
with open(filePath, 'r') as file:
    lines = file.readlines()

start_line = 32
end_line = 104

lines = [line.replace(old_text, new_text) if start_line <= i <= end_line else line for i, line in enumerate(lines, start=1)]
with open(filePath, 'w') as file:
    file.writelines(lines)