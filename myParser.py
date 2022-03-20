import ply.yacc as yacc
from myLexer import MyLexer
import sys
variables = {}

class MyParser:
    
    def __init__(self,lexer):
        print("Parser constructor called")
        self.parser = yacc.yacc(module=self)
        self.lexer = lexer

    tokens = MyLexer().tokens
 
    precedence = (
     ('nonassoc', 'if', 'while'),  # Nonassociative operators
     ('left', 'addition', 'soustraction'),
     ('left', 'multiplication', 'division'),
     ('left', 'superieur', 'inferieur'),
     ('left', 'superieur_egale', 'inferieur_egale'),
     #('right', 'UMINUS'),            # Unary minus operator
 )
 

    def p_command(self,p):
            '''
            expression :  if  ouvrir_parenthese expression  fermer_parenthese ouvrir_accolade expression fermer_accolade
            '''
            #print("if statements")
            if p[3] is not None:
                p[0] = p[6]
            else :   #p[1] is None and p[2] is None
                p[0] = None
           

    def p_expression_relationnel(self,p):
        '''
        expression : expression_arithmetique operation_relationnel expression_arithmetique
                        | chaine_de_caractere operation_relationnel expression_arithmetique
                        | expression_arithmetique operation_relationnel chaine_de_caractere
                        | chaine_de_caractere operation_relationnel chaine_de_caractere
        '''
        for i in variables :
            if i == p[1]:
                p[1]=variables[p[1]]
            if i == p[3]:
                p[3]=variables[p[3]]
        
        if p[2] == '>=':
            if p[1] >= p[3]:
                p[0]=True
            else:
                p[0]=False
        elif p[2] == '<=':
            if p[1] <= p[3]:
                p[0]=True
            else:
                p[0]=False
        elif p[2] == '<':
            if p[1] < p[3]:
                p[0]=True
            else:
                p[0]=False
        elif p[2] == '>':
            if p[1] > p[3]:
                p[0]=True
            else:
                p[0]=False 
        
                
    def p_egal(self,p):
        '''
        expression : expression egalite expression
                        | chaine_de_caractere egalite expression
                        | chaine_de_caractere egalite chaine_de_caractere
        '''
        #print('comparaison accepte')
        for i in variables :
            if i == p[1]:
                p[1]=variables[p[1]]
            if i == p[3]:
                p[3]=variables[p[3]]
        if p[1] == p[3]:
            p[0]=True
        else:
            p[0]=False 
            
    def p_diff(self,p):
        '''
        expression : expression different expression
                        | chaine_de_caractere different expression
                        | chaine_de_caractere different chaine_de_caractere
        '''
        for i in variables :
            if i == p[1]:
                p[1]=variables[p[1]]
            if i == p[3]:
                p[3]=variables[p[3]]
        #print('difference accepte')
        if p[1] == p[3]:
            p[0]=False
        else:
            p[0]=True 
        
    
    def p_expression_affectation(self,p):
         'expression : term'
         p[0] = p[1]
     
    
    
    def p_term_factor(self,p):
         'term : factor'
         p[0] = p[1]
     
    def p_factor_entier(self,p):
         'factor : entier'
         p[0] = p[1]
     
    def p_factor_expression(self,p):
         'factor : ouvrir_parenthese expression fermer_parenthese'
         p[0] = p[2]
    
    def p_expressions_add(self,p):
         '''
         expression : expression addition expression
                       | addition expression
                       | chaine_de_caractere addition expression
                       | expression addition chaine_de_caractere 
                       | chaine_de_caractere addition chaine_de_caractere
        '''
         #print("addition done")
         for i in variables :
             if i == p[1]:
                 p[1]=variables[p[1]]
             if i == p[3]:
                 p[3]=variables[p[3]]
         if (len(p) == 4):
             p[0] = p[1] + p[3]
         elif (len(p) == 3):
             p[0] = +p[2]
         
             
    def p_expressions_sous(self,p):
           '''
           expression : expression soustraction expression
                         | soustraction expression
                         | chaine_de_caractere soustraction expression
                         | expression soustraction chaine_de_caractere 
                         | chaine_de_caractere soustraction chaine_de_caractere
          '''
           #print("soustraction done")
           for i in variables :
               if i == p[1]:
                   p[1]=variables[p[1]]
               if i == p[3]:
                   p[3]=variables[p[3]]
           if (len(p) == 4):
               p[0] = p[1] - p[3]
           elif (len(p) == 3):
               p[0] = -p[2]
           print('res',p[0])
         
    def p_print(self,p):
        '''
        expression : printf expression
                        | printf chaine_de_caractere
        '''
        for i in variables :
            if i == p[2]:
                p[0]=variables[p[2]]
            else:
                p[0] = p[2]
       
    
    
   
    def p_declaration_chaine(self,p):
        '''
        expression :  chaine_de_caractere affectation  chaine_de_caractere 
        '''
        #print('declaration chaine')
        res = False
        for i in variables:
            if i == p[1]:
                res = True
                break
        if res == True:
            variables.update({p[1] : p[3]})
        else :
            variables[p[1]] =p[3] 
    def p_declaration_entier(self,p):
        '''
        expression :  chaine_de_caractere affectation entier
        '''
        res = False
        for i in variables:
            if i == p[1]:
                res = True
                break
        if res == True:
            variables.update({p[1] : p[3]})
        else :
            variables[p[1]] =p[3] 
        #print('declaration entier')
        p[0] = p[1]
    def p_declaration_char(self,p):
         '''
         expression :  identificateur affectation caractere
         '''
         #print('declaration char')
         
    def p_size(self,p):
        '''
        expression : size_of ouvrir_parenthese chaine_de_caractere fermer_parenthese
        '''
        p[0] = len(p[3])
        
    def p_operation_superieur(self,p):
        'operation_relationnel : superieur'
        p[0] = p[1] 
    def p_operation_inferieur(self,p):
        'operation_relationnel : inferieur'
        p[0] = p[1] 
    def p_operation_superieur_egal(self,p):
        'operation_relationnel : superieur_egale'
        p[0] = p[1] 
    def p_operation_inferieur_egal(self,p):
        'operation_relationnel : inferieur_egale'
        p[0] = p[1] 
                
    
        
    def p_term_multiplication(self,p):
             '''
             expression : expression multiplication expression
                         | chaine_de_caractere multiplication expression
                         | expression multiplication chaine_de_caractere 
                         | chaine_de_caractere multiplication chaine_de_caractere
             '''
             
             for i in variables :
                 if i == p[1]:
                     p[1]=variables[p[1]]
                 if i == p[3]:
                     p[3]=variables[p[3]]
             p[0] = p[1] * p[3]
    def p_term_division(self,p):
             '''
             expression : expression division expression
                         | chaine_de_caractere division expression
                         | expression division chaine_de_caractere 
                         | chaine_de_caractere division chaine_de_caractere
             '''
             for i in variables :
                 if i == p[1]:
                     p[1]=variables[p[1]]
                 if i == p[3]:
                     p[3]=variables[p[3]]
             p[0] = p[1] / p[3]
        
        
        
        
    def p_expression_arit(self,p):
            '''expression_arithmetique : term 
                                        | expression'''
            p[0] = p[1]    
    def p_expression_addition(self,p):
       '''
       expression : expression_arithmetique addition term
       '''

       p[0] = p[1] + p[2]
            
            
    def p_expression_soustraction(self,p):
             '''
             expression : expression_arithmetique soustraction term
             '''
             p[0] = p[1] - p[3]
             
    def p_factor_expr(self,p):
            'factor : ouvrir_parenthese expression_arithmetique fermer_parenthese'
            p[0] = p[2]
        
        
    def p_factor_integer(self,p):
            'factor : inti'
            p[0] = p[1]
        
    def p_factor_float(self,p):
            'factor : floati'
            p[0] = p[1]
        
    def p_factor_id(self,p):
            '''
            factor : identificateur
            '''
            p[0] = p[1]
        
    def p_factor_char(self,p):
            'factor : char'
            p[0] = p[1]
                 
    def p_command_basic_command(self,p):
            'command : basic_command'
            p[0] = p[1] 
    def p_command_iteration(self,p):
            'command : iteration'
            p[0] = p[1] 
#### if, else  statement #######
    def p_statement_if(self,p):
             '''
             expression : if ouvrir_parenthese expression fermer_parenthese ouvrir_accolade  expression fermer_accolade else ouvrir_accolade expression fermer_accolade
             '''
             #print("boule if ")
             if p[3] :
                 p[0] = p[6]
             else :   #p[1] is None and p[2] is None
                 p[0] = p[10]
###### for statement ##########
    def p_for(self,p):
        '''
        loop_while : for ouvrir_parenthese entier fermer_parenthese ouvrir_accolade expression fermer_accolade
        '''
        ret = []
        for i in range(p[3]):
            ret.append(p[6])
        p[0]=ret
    
    def p_assignment(self,p):
            'assignment : identificateur affectation expression_arithmetique '
            p[0] = p[1]     
            
    def p_basic_command_affectation(self,p):
            'basic_command : affectation'
            p[0] = p[1] 
    def p_basic_command_block(self,p):
            'basic_command : block'
            p[0] = p[1] 
            
    def p_statement_while(self,p):
        'statement : loop_while'
        p[0]=p[1]
    def p_condLoop_while(self,p):
        'condLoop : ouvrir_parenthese expression fermer_parenthese'
        p[0]=p[2]
####### commentaire ######
    def p_comment(self,p):
        'comment : hashtag expression '
        print("#"+p[2])
        
    def p_loop_while(self,p):
        'loop_while : while ouvrir_parenthese condLoop fermer_parenthese ouvrir_accolade expression  fermer_accolade'

        i=0
        ret=[]
        while (p[2]):
            ret.append(p[4])
            i=i+1
            if (i == 100):
                print("ereur : boucle infini")
                print(variables)
                break
        p[0] = ret
            
   
    def p_iteration_DO(self,p):
            'iteration : do command while ouvrir_parenthese expression fermer_parenthese point_virgule'
            p[0] = p[1]
        
            
    def p_block(self,p):
            'block : ouvrir_accolade expression command fermer_accolade'
            p[0] = p[1]
            
         # Error rule for syntax errors
    def p_error(self,p):
             if p:
                  print("Syntax error at token", p.type)
                  # Just discard the token and tell the parser it's okay.



