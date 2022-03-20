import ply.lex as lex

class MyLexer:
    
    def __init__(self):
       print('Lexer constructor called.')
       self.lexer = lex.lex(module=self)



    tokens = [
        
        'addition',  
        'soustraction',
        'multiplication',
        'division',
        'affectation',
        'inferieur',
        'superieur',
        'inferieur_egale',
        'superieur_egale',
        'egalite',
        'et',
        'ou',
        'hashtag', 
        'different',
        'ouvrir_parenthese',
        'fermer_parenthese',
        'ouvrir_accolade',
        'fermer_accolade',
        'entier',
        'reel',
        'caractere',
        'chaine_de_caractere',
        'for',
        'while',
        'do',
        'if',
        'else',
        'printf',
        'scanf',
        'class',
        'true',
        'false',
        'break',
        'continue',
        'switch', 
        'case',
        'dafault', 
        'enum',
        'new',
        'private',
        'protected', 
        'public',
        'return',
        'inti',
        'achari',
        'floati',
        'char',
        'awal',
        'this',
        'delete',
        'include',
        'negatif',
        'identificateur',
        'point_virgule',
        'bdo',
        'size_of'

    ]


   
    def t_newline(self,t):
        r'\n+'
        t.lexer.lineno += len(t.value)
     
    def t_size_of(self,t):
        r'toul'
        return t
    
    def t_entier(self,t):   
            r'\d+'
            t.value = int (t.value)
            return t
    def t_negatif(self,t):
            r'\-d+'
            return t
        
    def t_reel(self,t):
            r'\d+.d+[1-9]*'
            t.value = float(t.value)
            return t
    def t_inti(self,t):
            r'ra9m'
            return t
    def t_floati(self,t):
            r'a9i9i'
            return t
    def t_achari(self,t):
            r'achari'
            return t
    def t_char(self,t):
            r'amzwar'
            return t
    def t_awal(self,t):
            r'awal'
            return t
    def t_enum(self,t):
            r'7seb'
            return t
        
    def t_identificateur(self,t):
           # r'[a-zA-Z_][a-zA-Z0-9_]*'
            r'id'
            return t        
    def t_bdo(self,t):
            r'\bdo'
            return t
    def t_if(self,t):
            r'ikm'
            return t
    def t_for(self,t):
            r'ma7ed'
            return t
    def t_else(self,t):
            r'ighmla'
            return t
    def t_do(self,t):
            r'igh'
            return t
    def t_true(self,t):
            r'is7a'
            return t
    def t_false(self,t):
            r'oris7i'
            return t
    def t_new(self,t):
            r'ljdid'
            return t
    def t_return(self,t):
            r'aghol'
            return t
    def t_this(self,t):
            r'wad'
            return t
    def t_delete(self,t):
            r'mse7'
            return t
    def t_include(self,t):
            r'awid'
            return t
    def t_break(self,t):
            r'fegh'
            return t
    def t_continue(self,t):
            r'kmel'
            return t
    def t_printf(self,t):
            r'ari'
            return t
    def t_scanf(self,t):
            r'9ra'
            return t
    def t_while(self,t):
            r'skud'
            return t
    def t_case(self,t):
            r'tikfest'
            return t
    def t_private(self,t):
            r'uslig'
            return t
    def t_public(self,t):
            r'azayz'
            return t
    def t_taggayt(self,t):
            r'taggayt'
            return t
    def t_chaine_de_caractere(self, t) : 
            r'[a-zA-Z_][a-zA-Z0-9_]*'
            return t
    def t_error(self,t):
             
             print("Caractere non reconnu", t.value)
             line = t.lexer.lineno
             
             line=str(line)
             print(t.value+ "erreur lex" )
             t.lexer.skip(1)
    t_soustraction   = r'-'        
    t_addition = r'\+'
    t_hashtag = r'\#'
    
    t_multiplication   = r'\*'
    t_division  = r'/'
    t_affectation = r'\='
    t_inferieur=r'\<'
    t_superieur=r'\>'
    t_ouvrir_parenthese  = r'\('
    t_fermer_parenthese  = r'\)'
    t_ouvrir_accolade = r'\{'
    t_fermer_accolade = r'\}'
    t_caractere  = r'\[a-zA-Z]'
   
    t_inferieur_egale = r'\<='
    t_superieur_egale= r'\>='
    t_egalite= r'\=='
    t_et = r'\&&'

    """t_ou = r'||' """
    t_different = r'\!='
    t_point_virgule = r'\;'
    t_ignore  = ' \t'
         
#lexer = lex.lex()
    

""" Parser """




"""
printf :  ari
scanf: 9ra
for: 
if: ikm
else:
while:
do: igh
break: fegh
continue: kmel
switch: 
case:
default:
enum:
true: is7a
false:oris7i
new:  ljdid
private:
protected:
public:
return: aghol
int:
double:
float:
bool:
char:
string:
class:
this: wad
delete:mse7
include: awid .



+, -, /, *, =, ., <, <=, ==, >=, > &&, ||, &, |, !, ~, != ,

"""