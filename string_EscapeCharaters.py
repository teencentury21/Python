"""
Multi comment is not suit for escape character
"""

# \n	New Line
# \"    Double Quote
txt = "we are the so-called \"vikings\" from the north."
print (txt, "\n")

#this example erases one character (backspace):
txt = "hello \bworld!"
print (txt, "\n") 

txt = "Hello\r\nWorld!"
print (txt) 

# \'	Single Quote
# \\	Backslash

# \r	Carriage Return
# \t	Tab
# \b	Backspace
# \f	Form Feed

#A backslash followed by three integers will result in a octal value:
# \ooo	Octal value

#A backslash followed by an 'x' and a hex number represents a hex value:
# \xhh	Hex value
