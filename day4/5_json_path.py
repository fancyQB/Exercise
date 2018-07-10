import json

# fr = open('book_store.json', 'r', encoding='utf-8')
# json_str = fr.read()
# fr.close()
# json_obj = json.loads(json_str)

#以上步骤可以简化如下
import jsonpath

json_obj = json.load(open('book_store.json', 'r', encoding='utf-8'))
# print(json_obj)
# print(type(json_obj))

#获取所有作者

result = jsonpath.jsonpath(json_obj, '$.store.book[*].author')

print(result[1])