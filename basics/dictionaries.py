"=============Словари=============="
# Словарь (dict) - изменяемый, итерируемый, неиндексируемый, неупорядоченный тип данных, в котором значения хранятся в
# парах (ключ : значение)

dict_ = {'a': 1, 'b': 2, 'c': 3}
# print(dict_['a']) # 1
# print(type(dict_['a'])) # type will be whatever value will be

print(dict_['a'])

# ключами в словаре могут являться все неизменяемые типы данных
# значениями в словаре могут являться любые типы данных
# ключи должны быть уникальными

dict_ = {
    1: 'hello',
    4.5: {'a': 5},
    # {'s': 5}: 44 # TypeError: unhashable type: 'dict'
    }
print (dict_[4.5]) # {'a': 5}
print (dict_[4.5['a']]) # 5
print (dict_['a']) # KeyError: 'a'

"====================Методы словаря================="

dict_.clear() # чистит словарь
print(dict_) # {}

dict_ = dict.fromkeys([1,2,4]) 
print(dict_) # {1:None, 2:None, 4:None}

dict_ = dict.fromkeys([1,2,4], "hello") 
print(dict_) # {1:"hello", 2:"hello", 4:"hello"}

dict_ = {"a":1, "b":2}
dict_["a"] # 1
dict_["c"] # KeyError

# метод get нужен только для получения значений
dict_.get("a") # 1
dict_.get("c") # None
dict_.get("c", 5) # 5
dict_.get("a", 5) # 1

dict_.keys() # dict_keys(['a', 'b'])
dict_.values() # dict_values([1, 2])
dict_.items() # dict_items([('a', 1), ('b', 2)])

dict1 = {1:"a", 2:"b", 3:"c"}
dict2 = {3:"d", 4:"e"}
# метод update добавляет пары из второго словаря в первый
dict1.update(dict2)
print(dict1) # {1:"a", 2:"b", 3:"d", 4:"e"}
print(dict2) # {3:"d", 4:"e"}

# метод pop удаляет пару по ключу и возвращает по значению
popped = dict1.pop(3) # вырезали ключ 3:'d'
print(dict1) # {1:"a", 2:"b", 4:"e"}
print(popped) # d

dict1.pop('несуществующий ключ') # KeyError
# del dict1['несуществующий ключ'] # KeyError

# метод popitem удаляет и возвращает последнюю пару
print(dict1.popitem()) # (4, 'e')
print(dict1) # {1: 'a', 2: 'b'}


