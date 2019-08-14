vector1 = [2, 4, 3]
vector2 = [8, 10, 97]
#add vector
def add_vector(vec1, vec2):
  return [v1+v2 for v1, v2 in zip(vec1, vec2)]

added_vector = add_vector(vector1, vector2)
print(added_vector)
