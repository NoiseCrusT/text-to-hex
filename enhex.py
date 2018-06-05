print """
TEXT To HEX Converter

Coded By Afrizal F.A
"""
a = raw_input ('Masukkan Text = ').rstrip()
def hexcape(stri):
   f = ""
   for x in stri:
      f += "\\x"+x.encode('hex')
   return f
print(hexcape(a))
