from gtts import gTTS
import os

text = input('Enter Your text here: ')
lang = 'en'
slow_or_fast = input('(S)low Or (F)ast: ').lower()

if slow_or_fast == 's' or slow_or_fast == 'slow':
    slowmode = True
elif slow_or_fast == 'f' or slow_or_fast == 'fast':
    slowmode = False

output = gTTS(text=text, lang=lang, slow=slowmode)

output.save('output.mp3')

os.system('start output.mp3')