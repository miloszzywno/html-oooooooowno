# class Duzy_String:
#     def get_String(self): 
#         self.text = input("Daj mi parę liter: ")

#     def print_String(self): 
#         print(self.text.upper())

# Ds = Duzy_String()
# Ds.get_String()
# Ds.print_String()

# class OdracaczString:
#     def odwroc_string(self):
#         ciąg = input("Podaj ciąg liter: ")
#         odwrocony_ciag = ''.join(reversed(ciąg))
#         print("Odwrócony ciąg:", odwrocony_ciag)

# odra = OdracaczString()
# odra.odwroc_string()

# class Notebook:
#     def __init__(self):
#         self.notes = {}  
    
#     def __getitem__(self, page_number):
#         return self.notes.get(page_number, "Brak notatki na podanejj stronie")
    
#     def __setitem__(self, page_number, content):
#         self.notes[page_number] = content  
    
#     def __delitem__(self, page_number):
#         if page_number in self.notes:
#             del self.notes[page_number] 


# notebook = Notebook()
# notebook[1] = "Pierwszaa"
# notebook[2] = "Druga"

# print(notebook[1])
# print(notebook[3]) 

# del notebook[1]
# print(notebook[1]) 

# class BinaryConverter:
#     def __init__(self, filename):
#         with open(filename, 'r') as file:
#             self.binaries = [line.strip() for line in file if line.strip()]
    
#     def __getitem__(self, index):
#         return int(self.binaries[index], 2)
    
#     def __len__(self):
#         return len(self.binaries)
    
#     def convert_all(self):
#         return list(map(lambda x: int(x, 2), self.binaries))

# converter = BinaryConverter('binaries.txt')

# print(len(converter))
# print(converter[0])
# print(converter.convert_all())

class Multiplier:
    def __init__(self, number):
        self.number = number
    
    def __call__(self, other_number):
        return self.number * other_number

multiplier = Multiplier(5)
print(multiplier(3)) 
