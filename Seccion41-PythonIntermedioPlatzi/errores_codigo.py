# verificaicones de las excepciones

# execepcion con try
def palindrome(string):
    return string == string[::-1]

try:
    print(palindrome(1))
except TypeError:
    print("Solo se pueden ingresar strings")

# execepcion con rise
def palindrome(string):
  try:
    if len(string) == 0:
      raise ValueError("No se puede ingresar una cadena vacia")
    return string == string[::-1]
  except ValueError as ve:
    print(ve)
    return False

try:
  print(palindrome(**))
except TypeError:
  print("Solo se puede ingresar strings")
  
#execepcion con  finally
try:
  f = open("archivo.txt")
  #hacer cualquier cosa con nuestro 
finally:
  f.close()