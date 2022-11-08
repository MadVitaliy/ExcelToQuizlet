
from ExportToQuizlet import *
from ImportFromExel import *

def main():
  path = './test_data/words.xlsx'
  titles, data = ReadExcel(path)
  print(titles)
  print(data)
  
      
if __name__ == '__main__':
  main()