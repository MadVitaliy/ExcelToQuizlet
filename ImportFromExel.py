from openpyxl import load_workbook


def FirstNotEmptyRow(sheet):
  for i, row in enumerate(sheet):
    if not all(cell.value is None for cell in row):
      return i + 1
  return -1
  
  
def LastNotEmptyRow(sheet):
  for i, row in reversed(list(enumerate(sheet))):
    if not all(cell.value is None for cell in row):
      return i + 1
  return -1
  
def NumberOfNotEmptyRow(sheet):
  counter = int(0);
  for i, row in enumerate(sheet):
    if not all(cell.value is None for cell in row):
      counter += 1
  return counter
  

wb = load_workbook('./test_data/words.xlsx')
ws = wb.active


first_row_ind = FirstNotEmptyRow(ws)
last_row_ind = LastNotEmptyRow(ws)
number_of_not_empt = NumberOfNotEmptyRow(ws)
print(first_row_ind)
print(last_row_ind)
print(number_of_not_empt)

#reading table header
for i, cell in enumerate(ws[first_row_ind]): #indices starting from 1 suck
  print(f'{i}:{cell.value}')

titles_inds = [i for i, cell in enumerate(ws[first_row_ind]) if cell.value is not None]
print(titles_inds)

for cell in ws[]

