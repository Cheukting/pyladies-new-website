import os

for root, dirs, files in os.walk('../content/post/'):
    for file in files:
        with open(root+'/'+file, 'r') as f:
            text_lines = [line for line in f]
            text_lines[0] = text_lines[0] + f'date: {file[:10]}\n'
            text="".join(text_lines)
        with open(root+'/'+file, 'w') as f:
            f.write(text)
