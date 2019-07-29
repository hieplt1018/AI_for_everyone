def parameteric_rectified_linear_unit_fuc(data):
  result = []
  for d in data:
    if d < 0:
      result.append(0.1*d)
    else:
      result.append(d)
  return result

parameteric_rectified_linear_unit_fuc([1,5,-4,3,2])
