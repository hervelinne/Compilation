import ply.lex as lex
import ply.yacc as yacc
import sys
from myLexer import MyLexer
from myParser import MyParser

# create objects MY LEXER and MY PARSER
myLex = MyLexer()
lex = myLex.lexer
myPars = MyParser(myLex)
parser = myPars.parser

#reading INPUT FILE
path = 'projet.txt'
file = open(path, 'r')
data = file.readlines()
for line in data:
    #print(line)
    r=parser.parse(line)
    print(r)
file.close()
#Build the parser
# while True:
#     try:
#         s = input('input > ')
#     except EOFError:
#         break
#     if not s: continue
#     result = parser.parse(s)
#     if result != None :
#         print(result)

