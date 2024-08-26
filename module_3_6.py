# Дополнительное практическое задание по модулю: "Подробнее о функциях."

def counter(elem):
  if isinstance(elem, int):
    return elem
  elif isinstance(elem, str):
    return len(elem)


def calculate_structure_sum(object):
  global count
  if isinstance(object, list | tuple | set):
    for elem in object:
      if isinstance(elem, int):
        count += elem
      else:
        calculate_structure_sum(elem)
  elif isinstance(object, dict):
    for key, values in object.items():
        count += counter(key)
        count += counter(values)
  else:
    count += counter(object)
  return count


count = 0
data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)




