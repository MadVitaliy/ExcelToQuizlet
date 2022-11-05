
from ExportToQuizlet import *


def main():
  quizlet_login, quizlet_pasword = GetAutorisationCredits()  
  print(f"login is '{quizlet_login}'")
  print(f"password is '{quizlet_pasword}'")
      
if __name__ == '__main__':
  main()