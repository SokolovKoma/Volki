import re


text = open('data.txt').read().lower()
text1 = re.findall(r'\S+', text)
print(text1)
for i in range(len(text1)):
    text1[i] = ''.join(re.findall(r'[а-яё]', text1[i]))
    if len(text1[i]) == 1 and text1[i] not in ['у', 'и', 'а', 'с', 'о']:
        text1[i] = ''
print(text1)
t = open('preprocessed.txt', 'w')
t.write(' '.join(text1))
t.close()
