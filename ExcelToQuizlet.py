
from ExportToQuizlet import *
from ImportFromExel import *

class QuizletCard:

  def __init__(self):
    self._term = ''
    self._definition = ''

  @property
  def term(self):
    return self._term
  
  @term.setter  
  def term(self,i_term):
    self._term = i_term
    
  @property
  def definition(self):
    return self._definition

  @definition.setter  
  def definition(self,i_definition):
    self._definition = i_definition
    
  def AddExample(self, i_example):
    i_example = i_example.replace(self._term, "**")
    self._definition += ":\n\n" + i_example

  def print(self):
    print(f'term:{self._term}')
    print(f'definition:{self._definition}')
    
def main():
  path = './test_data/words.xlsx'
  titles, data = ReadExcel(path)
  print(titles)
  print(data)
  
  for data_for_card in data:
    card = QuizletCard()
    card.term = data_for_card['word']
    card.definition = data_for_card['definition']
    card.AddExample(data_for_card['example'])
    card.print()
    print('\n\n')
  
      
if __name__ == '__main__':
  main()