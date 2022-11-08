import time

def GetValue(param_string):
  eq_ind = param_string.find("=")
  return param_string[eq_ind+1:].strip()

def GetAutorisationCredits():
  try:
    with open('../LoginPassword.txt') as f:
      lines = f.readlines()
      for line in lines:
        line = line.strip()
        if line.startswith('login'):
          login = GetValue(line)
        elif line.startswith('password'):
          password = GetValue(line)
  finally:     
    return login, password
  
def FillStudySet(dictionary):
       
  from selenium import webdriver
  from selenium.webdriver.common.keys import Keys
  from selenium.webdriver.common.by import By
  from selenium.webdriver.firefox.options import Options

  options = Options()
  options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

  try:
    driver = webdriver.Firefox(options=options)
    driver.get("https://quizlet.com")
    print(f"driver.title{driver.title}")
    assert "Quizlet" in driver.title
    footer = driver.find_element(By.TAG_NAME, 'footer')
    print(footer)
    lenguage_selector = footer.find_element(By.TAG_NAME, 'select')
    all_options = lenguage_selector.find_elements(By.TAG_NAME, "option")
    
    for option in all_options[:-2]:
      if option.get_attribute("value") == 'en-us':
        print("Value is: en-us")
        option.click()
        break
    
    #omelchenko.vitalik1@gmail.com
    time.sleep(5)
    # try:
      # google_cont = driver.find_element(By.ID, 'credential_picker_container')
      # print(F"google_cont{google_cont}")
      # close_element = google_cont.find_element(By.ID, 'close')
      # print(F"close_element{close_element}")
      # close_element.click()
      # print('Goodbay google')
    # finally:
      # print('ok')
    
    input("Login and Press Enter to continue...") 


    #actual function body
    rows_div = driver.find_element(By.CLASS_NAME, 'TermRows')
    term_rows = rows_div.find_elements(By.CLASS_NAME, "TermRows-termRowWrap")
    
    number_of_words_to_add = len(dictionary)
    number_of_words_placeholders = len(term_rows)-1
    
    #insert empty quizlet cards
    print(f'number_of_words_to_add:{number_of_words_to_add}')
    print(f'number_of_words_placeholders:{number_of_words_placeholders}')
    
    number_of_additional_placeholders = number_of_words_to_add - number_of_words_placeholders
    if number_of_additional_placeholders > 0:
      for i in range(number_of_additional_placeholders):
        print(f'i:{i}')
        add_button = rows_div.find_element(By.CLASS_NAME, "TermContent-addRow")
        print(f'add_button:{add_button}')
        add_button.click()
      term_rows = rows_div.find_elements(By.CLASS_NAME, "TermRows-termRowWrap")
    
    
    for ind, word in enumerate(dictionary):
      print (f'ind:{ind}, word:{word}, def:{dictionary[word]}')
      term_row = term_rows[ind]
      
      word_div = term_row.find_element(By.CLASS_NAME, 'TermContent-side--word')
      word_text_field = word_div.find_element(By.CLASS_NAME, 'ProseMirror')
      word_text_field.click()
      word_text_field.send_keys(word)
      
      
      definition_div = term_row.find_element(By.CLASS_NAME, 'TermContent-side--definition')
      definition_text_field = definition_div.find_element(By.CLASS_NAME, 'ProseMirror')
      definition_text_field.click()
      definition_text_field.send_keys(dictionary[word])
      
      
    create_button_div = driver.find_element(By.CLASS_NAME, 'CreateSetPage-publishButton')
    create_button = create_button_div.find_element(By.TAG_NAME, 'button')
    create_button.click()
    
    
    #<div class="CreateSetPage-publishButton"><button type="button" aria-label="Create" class="AssemblyButtonBase AssemblyPrimaryButton--default AssemblyButtonBase--xlarge AssemblyButtonBase--padding"><span>Create</span></button></div>
    
    # for term_row in term_rows:
      # print(term_row.get_attribute('data-term-luid'))
      # word_div = term_row.find_element(By.CLASS_NAME, 'TermContent-side--word')
      # word_text_field = word_div.find_element(By.CLASS_NAME, 'ProseMirror')
      # word_text_field.click()
      # word_text_field.send_keys('Word from set')
      
      
      # definition_div = term_row.find_element(By.CLASS_NAME, 'TermContent-side--definition')
      # definition_text_field = definition_div.find_element(By.CLASS_NAME, 'ProseMirror')
      # definition_text_field.click()
      # definition_text_field.send_keys('Definition from set')
      
      #<div class="TermContent-side TermContent-side--word"><div class="WordSide is-active"><div class="RichTextEditor" data-testid="RichTextEditor"><div class="PMEditor pc1cm7j notranslate" data-testid="PMEditor"><div tabindex="7" role="textbox" aria-multiline="true" aria-labelledby="editor-term-side" class="ProseMirror" contenteditable="true"><p>test1vbcvbcb</p></div></div><div class="PMEditor-border"></div><span></span><span class="RichTextEditor-label"><div class="RichTextEditor-labelText">TERM</div><div class="LanguageBarSide"><button class="UILink is-Popover is-Tooltip UIOverlayTrigger-target" tabindex="-1" type="button">CHOOSE LANGUAGE</button></div></span></div></div><span></span></div>
      
    
   
  finally:
    input("Press to exit...") 
    driver.close()
  
  
#words_to_add = dict({'Beauty': 'the thing only Liia has', 'Love': 'Liia', 'Hugs, cuddles, talks, sex, ect': 'what I want with Liia'})
#FillStudySet(words_to_add) 
  