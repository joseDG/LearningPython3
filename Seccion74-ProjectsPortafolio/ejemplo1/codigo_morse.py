message = input('Message to be encoded to Morse? ').lower()
           
morse = ['·−' , '−···' ,'−·−·' ,'−··', '·' , '··−·', '−−·', '····', '··', '·−−−', '−·−', '·−··', '−.' ,'−−−', '·−−·','−−·−', '·−·' , '···', ' −' ,'··−', '···−', '·−−', '−··−','−·−−', ' −−··', '-.-.--']
plain_text = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '!']

def translate(message):
  morse_code = ' '
  for letter in message:
    if letter == ' ':
      index = None
      continue
    else: 
      index = plain_text.index(letter)
    if index > 12:
       index -= 1
    morse_code += ' ' + morse[index] 
  print(morse_code)  
  
#Copyright 2021 Corey Python , Created on Replit

#Callable from main 
translate(message)