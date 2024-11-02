import numpy as np

data_type = [('name', 'S15'), ('class', int), ('heet', float)]
students_details = [('jimmy', 33, 348.5), ('jam', 36, 352.5),('jonssun', 35, 342.10), ('Pit', 115, 40.11)]


sut = np.array(students_details, dtype=data_type)   
print("oginal array:")
print(students_details)
print("sort by heet")
print(np.sort(sut, order='heet'))