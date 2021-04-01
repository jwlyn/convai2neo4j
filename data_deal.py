import json

with open('C:/Users/Desktop/personachat_self_original.json', encoding='utf-8') as f:
    line = f.read()

d = json.loads(line)

for i in d['train']:
    with open('train.txt','a+', encoding='utf-8') as a:
        a.write(str(i['personality']))
        a.write('\n')



