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
  