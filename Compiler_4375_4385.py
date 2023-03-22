#KARAGIANNIDIS CHRISTOS     4375    cse84375
#KATSILEROU NEFELI-ELENI    4385    cse84385


import sys;
import os;

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z'
            ,'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z',
            ]

numbers=['0','1','2','3','4','5','6','7','8','9']

keywords = ['program' ,'declare','if','else','while','switchcase','forcase','incase','case','default',
            'not','and','or','function','procedure','call','return','in','inout','input','print']

#Used to convert the numbers to family types in order to match the examples of a proper run that were given
conversionToFamily = ['identifier','number','addOperator','addOperator','mulOperator','mulOperator','relOperator',
                      'relOperator','relOperator','assignment','groupSymbol','groupSymbol','delimiter','delimiter',
                      'groupSymbol','groupSymbol','eof','delimiter','groupSymbol','groupSymbol','relOperator',
                      'assignment','relOperator','relOperator','keyword','keyword','keyword','keyword',
                      'keyword','keyword','keyword','keyword','keyword','keyword','keyword',
                      'keyword','keyword','keyword','keyword','keyword','keyword','keyword',
                      'keyword','keyword','keyword']
last = 0


white_character = 0
letter = 1
digit = 2
plus = 3
minus = 4
multiplication_operator = 5
division_operator = 6
equal_sign = 7
less = 8
greater = 9
colon = 10
left_angle_bracket = 11
right_angle_bracket = 12
comma = 13
semicolon = 14
right_parenthesis = 15
left_parenthesis = 16
eof = 17
wrong_symbol = 18
full_stop = 19
left_square_bracket = 20
right_square_bracket = 21
hashtag = 22
newline = 23


token_identifier = 50
token_number = 51
token_plus = 52
token_minus = 53
token_multiply = 54
token_divide = 55
token_equal = 56
token_less = 57
token_greater = 58
token_colon = 59
token_left_angle_bracket = 60
token_right_angle_bracket = 61
token_comma = 62
token_semicolon = 63
token_right_parenthesis = 64
token_left_parenthesis = 65
token_eof = 66
token_full_stop = 67
token_left_square_bracket = 68
token_right_square_bracket = 69
token_different_than = 70
token_assignment = 71
token_less_or_equal = 72
token_greater_or_equal = 73
token_program = 74
token_declare = 75
token_if = 76
token_else = 77
token_while = 78
token_switchcase = 79
token_forcase = 80
token_incase = 81
token_case = 82
token_default = 83
token_not = 84
token_and = 85
token_or = 86
token_function = 87
token_procedure = 88
token_call = 89
token_return = 90
token_in = 91
token_inout = 92
token_input = 93
token_print = 94


state_start = 0
state_letter_or_digit = 1
state_digits = 2
state_less = 3
state_greater = 4
state_assignment = 5
state_comment = 6
state_error_wrong_sym = -1
state_error_wrong_assignment = -2
state_error_letter_after_digit = -3
state_error_never_closing_comment = -4
state_error_out_of_bounds_number = -5
state_error_more_than_30_characters = -6


transitions = [
    # state_start
    [state_start, state_letter_or_digit, state_digits, token_plus, token_minus, token_multiply, token_divide,
     token_equal, state_less, state_greater, state_assignment, token_left_angle_bracket,token_right_angle_bracket, token_comma, token_semicolon, token_right_parenthesis, token_left_parenthesis, token_eof,
     state_error_wrong_sym, token_full_stop, token_left_square_bracket, token_right_square_bracket , state_comment, state_start],

    # state_letter_or_digit
    [token_identifier, state_letter_or_digit, state_letter_or_digit, token_identifier, token_identifier, token_identifier, token_identifier, token_identifier, token_identifier, token_identifier, token_identifier,
     token_identifier, token_identifier, token_identifier, token_identifier, token_identifier, token_identifier, token_identifier, state_error_wrong_sym, token_identifier, token_identifier, token_identifier, token_identifier, token_identifier],

    # state_digits
    [token_number, state_error_letter_after_digit, state_digits, token_number, token_number, token_number,
     token_number, token_number, token_number, token_number, token_number, token_number, token_number, token_number, token_number, token_number, token_number, token_number, state_error_wrong_sym, token_number,
     token_number, token_number, token_number, token_number],

    # state_less
    [token_less, token_less, token_less, token_less, token_less, token_less,token_less, token_less_or_equal, token_less, token_different_than, token_less, token_less,
     token_less, token_less, token_less, token_less, token_less, token_less, state_error_wrong_sym, token_less,
     token_less, token_less, token_less, token_less],

    # state_greater
    [token_greater, token_greater, token_greater, token_greater, token_greater, token_greater,token_greater, token_greater_or_equal, token_greater, token_greater, token_greater, token_greater,
     token_greater, token_greater, token_greater, token_greater, token_greater, token_greater, state_error_wrong_sym,
     token_greater, token_greater, token_greater, token_greater, token_greater],

    # state_assignment
    [state_error_wrong_assignment, state_error_wrong_assignment, state_error_wrong_assignment, state_error_wrong_assignment, state_error_wrong_assignment,
     state_error_wrong_assignment,state_error_wrong_assignment, token_assignment, state_error_wrong_assignment, state_error_wrong_assignment, state_error_wrong_assignment,
     state_error_wrong_assignment, state_error_wrong_assignment, state_error_wrong_assignment, state_error_wrong_assignment, state_error_wrong_assignment, state_error_wrong_assignment,
     state_error_wrong_assignment, state_error_wrong_sym, state_error_wrong_assignment,state_error_wrong_assignment, state_error_wrong_assignment, state_error_wrong_assignment, state_error_wrong_assignment],

    # state_comment
    [state_comment, state_comment, state_comment, state_comment, state_comment, state_comment,
     state_comment, state_comment, state_comment, state_comment, state_comment,state_comment,state_comment, state_comment, state_comment, state_comment, state_comment, state_error_never_closing_comment,
     state_comment, state_comment, state_comment, state_comment, state_start, state_comment]
]

current_line = 1


def lex_analyzer():
        global current_line
        global line_number
        recognised_string = ''
        current_state = state_start
        line_counter = current_line

        def print_error():
            if (current_state == state_error_wrong_sym):
                print("ERROR: SYMBOL NOT RECOGNISED")
                exit(1)
            elif (current_state == state_error_never_closing_comment):
                print("ERROR: EXPECTED # BEFORE EOF ")
                exit(1)
            elif (current_state == state_error_letter_after_digit):
                print("ERROR: LETTER GIVEN AFTER A DIGIT")
                exit(1)
            elif (current_state == state_error_out_of_bounds_number):
                print("ERROR: A NUMBER IS OUT OF BOUNDS")
                exit(1)
            elif (current_state == state_error_wrong_assignment):
                print("ERROR: EXPECTED '=' AFTER ':' ")
                exit(1)
            elif (current_state == state_error_more_than_30_characters):
                print("ERROR: A WORD HAS MORE THAN 30 CHARACTERS")
                exit(1)

        while (current_state >= 0 and current_state <= 6):
            char_from_file = file.read(1)

            if (char_from_file == '\t' or char_from_file == ' '):
                token_character_read = white_character
            elif (char_from_file in alphabet):
                token_character_read = letter
            elif (char_from_file in numbers):
                token_character_read = digit
            elif (char_from_file == '+'):
                token_character_read = plus
            elif (char_from_file == '-'):
                token_character_read = minus
            elif (char_from_file == '*'):
                token_character_read = multiplication_operator
            elif (char_from_file == '/'):
                token_character_read = division_operator
            elif (char_from_file == '='):
                token_character_read = equal_sign
            elif (char_from_file == '<'):
                token_character_read = less
            elif (char_from_file == '>'):
                token_character_read = greater
            elif (char_from_file == ':'):
                token_character_read = colon
            elif (char_from_file == '{'):
                token_character_read = left_angle_bracket
            elif (char_from_file == '}'):
                token_character_read = right_angle_bracket
            elif (char_from_file == ','):
                token_character_read = comma
            elif (char_from_file == ';'):
                token_character_read = semicolon
            elif (char_from_file == ')'):
                token_character_read = right_parenthesis
            elif (char_from_file == '('):
                token_character_read = left_parenthesis
            elif (char_from_file == ''):
                token_character_read = eof
            elif (char_from_file == '.'):
                token_character_read = full_stop
            elif (char_from_file == '['):
                token_character_read = left_square_bracket
            elif (char_from_file == ']'):
                token_character_read = right_square_bracket
            elif (char_from_file == '#'):
                token_character_read = hashtag
            elif (char_from_file == '\n'):
                line_counter = line_counter + 1
                token_character_read = newline
            else:
                token_character_read = wrong_symbol

            current_state = transitions[current_state][token_character_read]

            if (len(recognised_string) < 30): #checks that word character count <30
                if (current_state != state_start and current_state != state_comment):
                    recognised_string += char_from_file
            else:
                current_state = state_error_more_than_30_characters

        if (current_state == token_identifier or current_state == token_number or current_state == token_less or current_state == token_greater):
            if (char_from_file == '\n'):
                line_counter -= 1
            file.seek(file.tell() - 1, 0)                   #goes back one character if we had "peeked" in order to verify the token
            recognised_string = recognised_string[:-1]      #delete last char from recognized string

        if (current_state == token_identifier):
            if (recognised_string in keywords):
                if (recognised_string == 'program'):
                    current_state = token_program
                elif (recognised_string == 'declare'):
                    current_state = token_declare
                elif (recognised_string == 'if'):
                    current_state = token_if
                elif (recognised_string == 'else'):
                    current_state = token_else
                elif (recognised_string == 'while'):
                    current_state = token_while
                elif (recognised_string == 'switchcase'):
                    current_state = token_switchcase
                elif (recognised_string == 'forcase'):
                    current_state = token_forcase
                elif (recognised_string == 'incase'):
                    current_state = token_incase
                elif (recognised_string == 'case'):
                    current_state = token_case
                elif (recognised_string == 'default'):
                    current_state = token_default
                elif (recognised_string == 'procedure'):
                    current_state = token_procedure
                elif (recognised_string == 'function'):
                    current_state = token_function
                elif (recognised_string == 'call'):
                    current_state = token_call
                elif (recognised_string == 'return'):
                    current_state = token_return
                elif (recognised_string == 'in'):
                    current_state = token_in
                elif (recognised_string == 'inout'):
                    current_state = token_inout
                elif (recognised_string == 'and'):
                    current_state = token_and
                elif (recognised_string == 'or'):
                    current_state = token_or
                elif (recognised_string == 'not'):
                    current_state = token_not
                elif (recognised_string == 'input'):
                    current_state = token_input
                elif (recognised_string == 'print'):
                    current_state = token_print

        if (current_state == token_number and recognised_string.isdigit() == True):         #check if num is between (-2^32,2^32)
            if(int(recognised_string) >= 4294967296 or int(recognised_string) <= -4294967296):
                current_state = state_error_out_of_bounds_number

        print_error()

        token = [current_state, line_counter, recognised_string]
        family = conversionToFamily[token[0]-50]    #Subtructs 50 from the token number in order to go to the proper position of the matrix (because tokens start from 50)
        #print(token[2],"\t \tfamily: \"",family,"\"", "line = ",token[1])
        current_line = line_counter

        return token


class Argument():

    def __init__(self,name):
        self.name = name
        self.type = 0
        self.parMode = -1 # 0 CV   1 REF


class Entity():


    def __init__(self,name,type):
        self.name = name
        self.type = type # 0 = 'VAR' or 1= 'SUBPR' or 2= 'PARAM' or 3= 'TEMP'

        self.variable = self.Variable()
        self.subprogram = self.SubProgram()
        self.parameter = self.Parameter()
        self.tempVariable = self.TempVariable()

    class Variable:
        def __init__(self):
            self.type = 0 # integer
            self.offset = 0

    class SubProgram:
        def __init__(self):
            self.type = -1     # 0 ='Procedure' 1 = 'Function' .
            self.startingQuad = 0
            self.argumentList = []
            self.frameLength = 0

    class Parameter:
        def __init__(self):
            self.parMode = -1  # 0='CV', 1='REF'
            self.offset = 0

    class TempVariable:
        def __init__(self):
            self.type = 0
            self.offset = 0


class Scope():

    def __init__(self,name):
        self.name = name
        self.entityList = []
        self.nestingLevel = 0
        self.enclosingScope = None


def new_argument(object):
    global topScope

    topScope.entityList[-1].subprogram.argumentList.append(object)


def new_entity(object):

    global topScope

    topScope.entityList.append(object)





def newScope(name):
    global topScope

    nextScope = Scope(name)
    nextScope.enclosingScope = topScope

    if (topScope == None):
        nextScope.nestingLevel = 0
    else:
        nextScope.nestingLevel = topScope.nestingLevel + 1

    topScope = nextScope


def deleteScope():
    global topScope

    topScope = topScope.enclosingScope

def addScopeToListOfAllScopes():
    global topScope
    global AllScopes

    AllScopes.append(topScope)


def calcStartingQuad():
    global topScope

    topScope.enclosingScope.entityList[-1].subprogram.startingQuad = nextquad()


def calculateOffset():
    global topScope

    offset = 12
    if (topScope.entityList is not []):
        for entity in (topScope.entityList):
            if (entity.type == 0 or entity.type == 2 or entity.type == 3):
                offset += 4

    return offset

def calcFramelength():
    global topScope

    topScope.enclosingScope.entityList[-1].subprogram.frameLength = calculateOffset()


def addParameters():

    global topScope

    for arg in topScope.enclosingScope.entityList[-1].subprogram.argumentList:
        entity = Entity(arg.name,2)
        entity.parameter.parMode = arg.parMode
        entity.parameter.offset = calculateOffset()
        new_entity(entity)


def printSymbTable(symbFile):
    global topScope
    print("\n\n")
    print("__________________________________________________________________________")
    print("__________________________________________________________________________")
    print("\n\n")
    symbFile.write("\n\n")
    symbFile.write("__________________________________________________________________________\n")
    symbFile.write("__________________________________________________________________________\n")
    symbFile.write("\n\n")

    sco = topScope
    while sco != None:
        print("SCOPE: " + "name:" + str(sco.name) + " nestingLevel:" + str(sco.nestingLevel))
        symbFile.write("SCOPE: " + "name:" + str(sco.name) + " nestingLevel:" + str(sco.nestingLevel)+"\n")
        print("\tENTITIES:")
        symbFile.write("\tENTITIES:"+"\n")
        for ent in sco.entityList:
            if (ent.type == 0):#VAR
                print("\t " + " name:" + str(ent.name) + "\t type:" + str(ent.type) +"(=Variable)"+ "\t variable-type:" + str(ent.variable.type)+"(=int)" + "\t offset:" + str(ent.variable.offset))
                symbFile.write("\t " + " name:" + str(ent.name) + "\t type:" + str(ent.type) +"(=Variable)"+ "\t variable-type:" + str(ent.variable.type) +"(=int)"+ "\t offset:" + str(ent.variable.offset)+"\n")
            elif (ent.type == 3):#TEMP
                print("\t " + " name:" + str(ent.name) + "\t type:" + str(ent.type) +"(=Temp)"+ "\t temp-type:" + str(ent.tempVariable.type) +"(=int)"+ "\t offset:" + str(ent.tempVariable.offset))
                symbFile.write("\t " + " name:" + str(ent.name) + "\t type:" + str(ent.type)+"(=Temp)" + "\t temp-type:" + str(ent.tempVariable.type) +"(=int)"+ "\t offset:" + str(ent.tempVariable.offset)+"\n")
            elif (ent.type == 1):#SUBPROGRAM
                if (ent.subprogram.type == 1):#Function
                    print("\t " + " name:" + str(ent.name) + "\t type:" + str(ent.type) +"(=Function/Procedure)"+ "\t function-type:" + str(ent.subprogram.type) + "\t startingQuad:" + str(ent.subprogram.startingQuad) + "\t frameLength:" + str(ent.subprogram.frameLength))
                    symbFile.write("\t " + " name:" + str(ent.name) + "\t type:" + str(ent.type) +"(=Function/Procedure)"+ "\t function-type:" + str(ent.subprogram.type) + "\t startingQuad:" + str(ent.subprogram.startingQuad) + "\t frameLength:" + str(ent.subprogram.frameLength)+"\n")
                    print("\t\tARGUMENTS:")
                    symbFile.write("\t\tARGUMENTS:"+"\n")
                    for arg in ent.subprogram.argumentList:
                        Result = 'REF'
                        if arg.parMode == 0:
                            Result  = 'CV'
                        print("\t\tARGUMENT: " + " name:" + str(arg.name) + "\t type:" + str(arg.type) + "\t parMode:" + str(arg.parMode)+"(="+Result+")")
                        symbFile.write("\t\tARGUMENT: " + " name:" + str(arg.name) + "\t type:" + str(arg.type) + "\t parMode:" + str(arg.parMode)+"(="+Result+")"+"\n")
                elif (ent.subprogram.type == 0):#Procedure
                    print("\t " + " name:" + str(ent.name) + "\t type:" + str(ent.type)+"(=Subprogram)" + "\t procedure-type:" + str(ent.subprogram.type)+"(=Procedure)" + "\t startingQuad:" + str(ent.subprogram.startingQuad) + "\t frameLength:" + str(ent.subprogram.frameLength))
                    symbFile.write("\t " + " name:" + str(ent.name) + "\t type:" + str(ent.type) +"(=Subprogram)"+ "\t procedure-type:" + str(ent.subprogram.type) +"(=Procedure)"+ "\t startingQuad:" + str(ent.subprogram.startingQuad) + "\t frameLength:" + str(ent.subprogram.frameLength)+"\n")
                    print("\t\tARGUMENTS:")
                    symbFile.write("\t\tARGUMENTS:"+"\n")
                    for arg in ent.subprogram.argumentList:
                        Result = 'REF'
                        if arg.parMode == 0:
                            Result  = 'CV'
                        print("\t\tARGUMENT: " + " name:" + str(arg.name) + "\t type:" + str(arg.type) + "\t parMode:" + str(arg.parMode)+"(="+Result+")")
                        symbFile.write("\t\tARGUMENT: " + " name:" + str(arg.name) + "\t type:" + str(arg.type) + "\t parMode:" + str(arg.parMode)+"(="+Result+")"+"\n")
            elif (ent.type == 2):#PARAM
                Result = 'REF'
                if ent.parameter.parMode ==0:
                    Result = 'CV'
                print("\t " + " name:" + str(ent.name) + "\t type:" + str(ent.type)+"(=Parameter)" + "\t mode:" + str(ent.parameter.parMode) +"(="+Result+")"+ "\t offset:" + str(ent.parameter.offset))
                symbFile.write("\t " + " name:" + str(ent.name) + "\t type:" + str(ent.type) +"(=Parameter)"+ "\t mode:" + str(ent.parameter.parMode) +"(="+Result+")"+ "\t offset:" + str(ent.parameter.offset)+"\n")
        sco = sco.enclosingScope

    print("\n\n")
    print("__________________________________________________________________________")
    print("__________________________________________________________________________")
    print("\n\n\n\n\n")
    symbFile.write("\n\n")
    symbFile.write("__________________________________________________________________________\n")
    symbFile.write("__________________________________________________________________________\n")
    symbFile.write("\n\n\n\n\n")


def syntax_analyzer():
        global lexical_analyzer
        global line_number
        global last
        global cFile

        def get_token(): #Calls lex_analyzer and saves the token it returns to the variable lexical_analyzer. It also saves the current line number
            global lexical_analyzer
            global line_number
            lexical_analyzer = lex_analyzer()
            line_number = lexical_analyzer[1]

        def error(position,LINENUM):
            error_names=[" : IDENTIFIER EXPECTED",
                         " : ASSIGNMENT SYMBOL EXPECTED",
                         " : RIGHT SQUARE BRACKET EXPECTED ",
                         " : LEFT SQUARE BRACKET EXPECTED ",
                         " : RIGHT PARENTHESIS EXPECTED ",
                         " : LEFT PARENTHESIS EXPECTED ",
                         " : INVALID DEFINITION OF 'CALL' ",
                         " : SEMICOLON EXPECTED",
                         " : CONSTANT EXRPESSION OR VARIABLE EXPECTED ",
                         " : INVALID DEFINITION OF 'DEFAULT' IN 'FORCASE'",
                         " : INVALID DEFINITION OF 'FORCASE' ",
                         " : VARIABLE NAME EXPECTED ",
                         " : IF CAN'T OPEN",
                         " : INVALID DEFINITION OF 'INCASE' ",
                         " : INPUT ERROR ",
                         " : PRINT ERROR ",
                         " : FULL STOP EXPECTED TO END PROGRAM",
                         " : NAME OF PROGRAM NOT FOUND",
                         " : WORD PROGRAM EXPECTED",
                         " : RELATIONAL OPERATOR EXPECTED ",
                         " : RIGHT ANGLE BRACKET EXPECTED ",
                         " : INVALID DEFINITION OF 'DEFAULT' IN 'SWITCHCASE' ",
                         " : INVALID DEFINITION OF 'SWITCHCASE'  ",
                         " : EXPECTED COMMA BETWEEN TWO IDENTIFIERS ",
                         " : INVALID DEFINITION OF 'WHILE' ",
                         " : UNEXPECTED CALL OF 'EXIT' "]
            error_start  = ' ERROR AT LINE'
            print(error_start, LINENUM,error_names[position] )
            exit(-1)

            return

        def actualparitem():
            global lexical_analyzer
            global line_number
            if(lexical_analyzer[0]==token_in):
                get_token()
                E = expression()
                genquad("par",E,"CV","_")
            elif(lexical_analyzer[0] == token_inout):
                get_token()
                if(lexical_analyzer[0]==token_identifier):
                    id = lexical_analyzer[2]
                    genquad("par", id, "REF", "_")
                    get_token()

                else:
                    error(11,line_number)
            return

        def actualparlist():
            global lexical_analyzer
            global line_number
            actualparitem()
            while(lexical_analyzer[0] == token_comma):
                get_token()
                actualparitem()
            return

        def addoperator():
            global lexical_analyzer
            global line_number
            if (lexical_analyzer[0] == token_minus):
                temp_add_op = lexical_analyzer[2]
                get_token()
            elif (lexical_analyzer[0] == token_plus):
                temp_add_op = lexical_analyzer[2]
                get_token()
            return temp_add_op

        def assignStat():
            global lexical_analyzer

            if(lexical_analyzer[0]==token_identifier):
                idplace = lexical_analyzer[2]
                get_token()
                if(lexical_analyzer[0]==token_assignment):
                    get_token()
                    Eplace = expression()
                    genquad(':=',Eplace,'_',idplace)
                    return
                else:
                    error(1, line_number)
            else:
                error(0, line_number)

        def programblock(name, BlockFlag):
            global lexical_analyzer
            global line_number
            global last
            global symb


            if(lexical_analyzer[0] == token_left_angle_bracket):
                get_token()
                newScope(name)
                if(BlockFlag!=1):
                    addParameters()
                if(lexical_analyzer[0]==token_declare):
                    declarations()

                subprograms()
                genquad('begin_block',name,'_','_')
                if(BlockFlag!=1):
                    calcStartingQuad()

                block()




                if(lexical_analyzer[0] == token_right_angle_bracket):
                    get_token()
                    if BlockFlag == 1:
                        genquad('halt', '_', '_', '_')
                    else:
                        calcFramelength()
                    genquad('end_block', name, '_', '_')
                    printSymbTable(symb)
                    addScopeToListOfAllScopes()
                    deleteScope()
                    print("Last scope deleted.")
                    return
                elif(line_number==last and lexical_analyzer[0] != token_right_angle_bracket):
                    error(20,line_number)
                elif(lexical_analyzer[0] != token_semicolon):
                    error(7,line_number-1)

        def block():
            global lexical_analyzer
            global line_number
            statement()
            while(lexical_analyzer[0] == token_semicolon):
                get_token()
                statement()
            return

        def boolfactor():
            global lexical_analyzer
            global line_number
            Rtrue = []
            Rfalse = []
            if(lexical_analyzer[0]==token_not):
                get_token()
                if(lexical_analyzer[0]==token_left_square_bracket):
                    get_token()
                    cond = condition()
                    if(lexical_analyzer[0]==token_right_square_bracket):
                        get_token()
                        Rtrue = cond[1]
                        Rfalse = cond[0]

                    else:
                        error(2, line_number)
                else:
                    error(3, line_number)
            elif(lexical_analyzer[0] == token_left_square_bracket):
                 get_token()
                 cond = condition()
                 if(lexical_analyzer[0]==token_right_square_bracket):
                    get_token()
                    Rtrue = cond[0]
                    Rfalse = cond[1]
                 else:
                     error(2, line_number)
            else:
                E1place = expression()
                relop = reloperator()
                E2place = expression()
                Rtrue = makelist(nextquad())
                genquad(relop,E1place,E2place,"_")
                Rfalse = makelist(nextquad())
                genquad("jump","_","_","_")
            return Rtrue,Rfalse

        def boolterm():
            global lexical_analyzer
            global line_number

            R1 = boolfactor()
            Qtrue = R1[0]
            Qfalse = R1[1]
            while(lexical_analyzer[0] == token_and):
                get_token()
                backpatch(Qtrue,nextquad())
                R2 = boolfactor()
                Qfalse = merge(Qfalse,R2[1])
                Qtrue = R2[0]
            return Qtrue,Qfalse

        def callStat():
            global lexical_analyzer
            global line_number

            if (lexical_analyzer[0] == token_call):
                get_token()
                id = lexical_analyzer[2]
                if(lexical_analyzer[0]==token_identifier):
                    get_token()
                    if (lexical_analyzer[0] == token_left_parenthesis):
                        get_token()
                        actualparlist()
                        genquad("call",id,"_","_")
                        if (lexical_analyzer[0] == token_right_parenthesis):
                            get_token()
                            return
                        else:
                            error(4, line_number)
                    else:
                        error(5, line_number)
                else:
                    error(0, line_number)
            else:
                error(6, line_number)
            return

        def condition():
            global lexical_analyzer
            global line_number

            Q1 = boolterm()
            Btrue = Q1[0]
            Bfalse = Q1[1]
            while(lexical_analyzer[0] == token_or):
                get_token()
                backpatch(Bfalse,nextquad())
                Q2 = boolterm()
                Btrue = merge(Btrue,Q2[0])
                Bfalse = Q2[1]
            return Btrue,Bfalse

        def declarations():
            global lexical_analyzer
            global cFile
            global declarationCounter


            while(lexical_analyzer[0] == token_declare):
                get_token()
                varlist()
                declarationCounter+=1;
                if(lexical_analyzer[0] == token_semicolon):
                    get_token()
                else:
                    error(7, line_number-1)
            return

        def elsepart():
            global lexical_analyzer
            global line_number

            if(lexical_analyzer[0]==token_else):
                get_token()
                statements()
            return

        def expression():
            global lexical_analyzer
            global line_number
            optionalsign()
            T1place = term()

            while(lexical_analyzer[0] == token_minus or lexical_analyzer[0] == token_plus):
                temp_add_op = addoperator()
                T2place = term()
                w = newtemp()
                genquad(temp_add_op,T1place,T2place,w)
                T1place = w

            Eplace = T1place
            return Eplace

        def factor():
            global lexical_analyzer
            global line_number
            if(lexical_analyzer[0]==token_number):
                fact = lexical_analyzer[2]
                get_token()
            elif(lexical_analyzer[0] == token_left_parenthesis):
                get_token()
                Eplace = expression()
                fact  = Eplace
                if(lexical_analyzer[0]==token_right_parenthesis):
                    get_token()
                else:
                    error(4, line_number)
            elif(lexical_analyzer[0] == token_identifier):
                fact = lexical_analyzer[2]
                get_token()
                fact = idtail(fact)
            else:
                error(8, line_number)
            return fact

        def forcaseStat():
            global lexical_analyzer
            global line_number
            if (lexical_analyzer[0] == token_forcase):
                get_token()
                firstCondQuad = nextquad()
                while (lexical_analyzer[0] == token_case):
                    get_token()
                    if (lexical_analyzer[0] == token_left_parenthesis):
                        get_token()
                        Condition = condition()
                        CondTrue = Condition[0]
                        CondFalse = Condition[1]
                        backpatch(CondTrue,nextquad())

                        if (lexical_analyzer[0] == token_right_parenthesis):
                            get_token()
                            statements()
                            genquad('jump','_','_',firstCondQuad)
                            backpatch(CondFalse,nextquad())

                        else:
                            error(4, line_number)
                    else:
                        error(5, line_number)
                if (lexical_analyzer[0] == token_default):
                    get_token()
                    statements()
                else:
                    error(9, line_number)
            else:
                error(10, line_number)
            return

        def formalparitem():
            global lexical_analyzer
            global line_number

            if(lexical_analyzer[0]==token_in):
                get_token()
                if(lexical_analyzer[0]==token_identifier):
                    argument = Argument(lexical_analyzer[2])
                    argument.parMode = 0
                    new_argument(argument)

                    get_token()
                else:
                    error(11, line_number)
            elif(lexical_analyzer[0] == token_inout):
                get_token()
                if(lexical_analyzer[0]==token_identifier):
                    argument = Argument()
                    argument.name = lexical_analyzer[2]
                    argument.parMode = 1
                    new_argument(argument)

                    get_token()
                else:
                    error(0, line_number)
            while(lexical_analyzer[0] == token_comma):
                get_token()
                if (lexical_analyzer[0] == token_in):
                    get_token()
                    if (lexical_analyzer[0] == token_identifier):
                        argument = Argument(lexical_analyzer[2])
                        argument.parMode = 0
                        new_argument(argument)
                        get_token()
                    else:
                        error(11, line_number)
                elif (lexical_analyzer[0] == token_inout):
                    get_token()
                    if (lexical_analyzer[0] == token_identifier):
                        argument = Argument(lexical_analyzer[2])
                        argument.parMode = 1
                        new_argument(argument)
                        get_token()
                    else:
                        error(0, line_number)
            return

        def idtail(id):
            global lexical_analyzer
            global line_number
            if(lexical_analyzer[0]==token_left_parenthesis):
                get_token()
                actualparlist()
                w = newtemp()
                genquad("par",w,"RET","_")
                genquad("call", id, "_", "_")
                if(lexical_analyzer[0]==token_right_parenthesis):
                    get_token()
                    return w
                else:
                    error(4,line_number)
            else:
                return id
            return

        def ifStat():
            global lexical_analyzer
            global line_number

            if(lexical_analyzer[0]==token_if):
                get_token()
                if(lexical_analyzer[0]==token_left_parenthesis):
                    get_token()
                    B = condition()
                    Btrue = B[0]
                    Bfalse = B[1]
                    backpatch(Btrue, nextquad())
                    if(lexical_analyzer[0]==token_right_parenthesis):
                        get_token()
                        S1 = statements()
                        ifList = makelist(nextquad())
                        genquad("jump","_","_","_")
                        backpatch(Bfalse,nextquad())
                        TAIL = elsepart()
                        backpatch(ifList,nextquad())
                        return
                    else:
                        error(4, line_number)
                else:
                    error(5, line_number)
            else:
                error(12, line_number)

        def incaseStat():
            global lexical_analyzer
            global line_number
            if (lexical_analyzer[0] == token_incase):
                get_token()
                firstCondQuad = nextquad()
                flag = newtemp()
                genquad(':=','0','_',flag)
                while (lexical_analyzer[0] == token_case):
                    get_token()
                    if (lexical_analyzer[0] == token_left_parenthesis):
                        get_token()
                        Condition  = condition()
                        CondTrue = Condition[0]
                        CondFalse = Condition[1]
                        backpatch(CondTrue,nextquad())
                        if (lexical_analyzer[0] == token_right_parenthesis):
                            get_token()
                            statements()
                            genquad(':=','1','_',flag)
                            backpatch(CondFalse,nextquad())
                        else:
                            error(4, line_number)
                    else:
                        error(5, line_number)
                genquad('=',flag,'1',firstCondQuad)
            else:
                error(13, line_number)
            return

        def inputStat():
            global lexical_analyzer
            global line_number
            if (lexical_analyzer[0] == token_input):
                get_token()
                if (lexical_analyzer[0] == token_left_parenthesis):
                    get_token()
                    if (lexical_analyzer[0] == token_identifier):
                        get_token()
                        idplace = lexical_analyzer[2]
                        genquad("inp",idplace,"_","_")
                        if (lexical_analyzer[0] == token_right_parenthesis):
                            get_token()
                            return
                        else:
                            error(4, line_number)
                    else:
                        error(0, line_number)
                else:
                    error(5, line_number)
            else:
                error(14, line_number)

        def muloperator():
            global lexical_analyzer
            global line_number
            if(lexical_analyzer[0]==token_divide):
                temp_mul_op = lexical_analyzer[2]
                get_token()
            elif(lexical_analyzer[0] == token_multiply):
                temp_mul_op = lexical_analyzer[2]
                get_token()
            return temp_mul_op

        def optionalsign():
            global lexical_analyzer
            global line_number
            if(lexical_analyzer[0]==token_plus or lexical_analyzer[0]==token_minus):
                addoperator()
            return

        def printStat():
            global lexical_analyzer
            global line_number
            if (lexical_analyzer[0] == token_print):
                get_token()
                if (lexical_analyzer[0] == token_left_parenthesis):
                    get_token()
                    Eplace = expression()
                    genquad("out",Eplace,"_","_")
                    if (lexical_analyzer[0] == token_right_parenthesis):
                         get_token()
                    else:
                        error(4, line_number)
                else:
                    error(5, line_number)
            else:
                error(15, line_number)
            return

        def program():
            global lexical_analyzer
            global line_number
            get_token()

            if(lexical_analyzer[0] == token_program):
                get_token()
                if(lexical_analyzer[0] == token_identifier):
                    id = lexical_analyzer[2]
                    get_token()
                    programblock(id,1)
                    if(lexical_analyzer[0] == token_full_stop):
                        get_token()
                        return
                    else:
                        error(16, line_number)
                else:
                    error(17, line_number)
            else:
                error(18, line_number)

        def reloperator():
            global lexical_analyzer
            global line_number
            if(lexical_analyzer[0]==token_equal):
                relop = lexical_analyzer[2]
                get_token()
            elif (lexical_analyzer[0] == token_greater_or_equal):
                relop = lexical_analyzer[2]
                get_token()
            elif(lexical_analyzer[0] == token_different_than):
                relop = lexical_analyzer[2]
                get_token()
            elif (lexical_analyzer[0] == token_greater):
                relop = lexical_analyzer[2]
                get_token()
            elif (lexical_analyzer[0] == token_less_or_equal):
                relop = lexical_analyzer[2]
                get_token()
            elif (lexical_analyzer[0] == token_less):
                relop = lexical_analyzer[2]
                get_token()

            else:
                error(19, line_number)
            return relop

        def returnStat():
            global lexical_analyzer
            global line_number
            if (lexical_analyzer[0] == token_return):
                get_token()

                if(lexical_analyzer[0] == token_left_parenthesis):
                    get_token()
                    Eplace = expression()
                    genquad("retv",Eplace,"_","_")
                    if (lexical_analyzer[0] == token_right_parenthesis):
                         get_token()
                         return
                    else:
                        error(4, line_number)
                else:
                    error(5, line_number)

        def statement():
            global lexical_analyzer

            if(lexical_analyzer[0]==token_identifier):
                assignStat()
            elif(lexical_analyzer[0] == token_while):
                whileStat()
            elif (lexical_analyzer[0] == token_switchcase):
                switchcaseStat()
            elif (lexical_analyzer[0] == token_input):
                inputStat()
            elif (lexical_analyzer[0] == token_forcase):
                forcaseStat()
            elif (lexical_analyzer[0] == token_incase):
                incaseStat()
            elif (lexical_analyzer[0] == token_call):
                callStat()
            elif (lexical_analyzer[0] == token_return):
                returnStat()
            elif (lexical_analyzer[0] == token_if):
                ifStat()
            elif (lexical_analyzer[0] == token_print):
                printStat()

            return

        def statements():
            global lexical_analyzer
            global line_number

            if(lexical_analyzer[0]==token_left_angle_bracket):
                get_token()
                statement()
                while(lexical_analyzer[0] == token_semicolon):
                    get_token()
                    statement()
                if(lexical_analyzer[0]==token_right_angle_bracket):
                    get_token()
                    return
                else:
                    error(20, line_number)
            else:
                statement()
                if(lexical_analyzer[0]==token_semicolon):
                    get_token()
                    return
                else:
                    error(7, line_number-1)

        def subprogram():
            global lexical_analyzer

            if (lexical_analyzer[0] == token_function):
                get_token()

                if (lexical_analyzer[0] == token_identifier):
                    id = lexical_analyzer[2]

                    entity = Entity(lexical_analyzer[2],1)
                    entity.subprogram.type = 1
                    new_entity(entity)

                    get_token()
                    if (lexical_analyzer[0] == token_left_parenthesis):
                        get_token()
                        formalparitem()
                        if (lexical_analyzer[0] == token_right_parenthesis):
                            get_token()
                            programblock(id,0)
                            return
                        else:
                            error(4, line_number)
                    else:
                        error(5, line_number)
                else:
                    error(0, line_number)
            elif(lexical_analyzer[0] == token_procedure):
                get_token()
                if(lexical_analyzer[0]==token_identifier):
                    id = lexical_analyzer[2]
                    entity = Entity(lexical_analyzer[2],1)
                    entity.subprogram.type = 0
                    new_entity(entity)
                    get_token()
                    if(lexical_analyzer[0]==token_left_parenthesis):
                        get_token()
                        formalparitem()
                        if(lexical_analyzer[0]==token_right_parenthesis):
                            get_token()
                            programblock(id,0)
                            return
                        else:
                            error(4, line_number)
                    else:
                        error(5, line_number)
                else:
                    error(0, line_number)

        def subprograms():
            global lexical_analyzer

            while(lexical_analyzer[0] == token_function or lexical_analyzer[0] == token_procedure):
                subprogram()
            return

        def switchcaseStat():
            global lexical_analyzer
            global line_number
            if(lexical_analyzer[0]==token_switchcase):
                get_token()
                ExitList = emptylist()
                while(lexical_analyzer[0] == token_case):
                    get_token()
                    if(lexical_analyzer[0]==token_left_parenthesis):
                        get_token()
                        Condition = condition()
                        CondTrue = Condition[0]
                        CondFalse = Condition[1]
                        backpatch(CondTrue,nextquad())
                        if(lexical_analyzer[0]==token_right_parenthesis):
                            get_token()
                            statements()
                            t = makelist(nextquad())
                            genquad('jump','_','_','_')
                            ExitList = merge(ExitList,t)
                            backpatch(CondFalse,nextquad())
                        else:
                            error(4, line_number)
                    else:
                        error(5, line_number)
                if(lexical_analyzer[0]==token_default):
                    get_token()
                    statements()
                    backpatch(ExitList,nextquad())
                else:
                    error(21, line_number)
            else:
                error(22, line_number)

        def term():
            global lexical_analyzer
            global line_number
            F1place = factor()
            while(lexical_analyzer[0] == token_divide or lexical_analyzer[0] == token_multiply):
                temp_mul_op = muloperator()
                F2place = factor()
                w = newtemp()
                genquad(temp_mul_op, F1place, F2place, w)
                F1place = w
            Tplace = F1place
            return Tplace

        def varlist():
            global lexical_analyzer
            global declarationCounter
            global listOfDeclarations
            tempListOfDeclarations =[]
            if(lexical_analyzer[0] == token_identifier):
                tempListOfDeclarations.append(lexical_analyzer[2])
                entity = Entity(lexical_analyzer[2],0)
                entity.variable.offset = calculateOffset()
                new_entity(entity)
                get_token()
                while(lexical_analyzer[0] == token_comma):
                    get_token()
                    if(lexical_analyzer[0] == token_identifier):
                        tempListOfDeclarations.append(lexical_analyzer[2])
                        entity = Entity(lexical_analyzer[2],0)
                        entity.variable.offset = calculateOffset()
                        new_entity(entity)
                        get_token()
                    else:
                        error(23, line_number)
            listOfDeclarations.append(tempListOfDeclarations)
            return

        def whileStat():
            global lexical_analyzer
            global line_number
            if(lexical_analyzer[0]==token_while):
                get_token()
                Bquad = nextquad()
                if(lexical_analyzer[0]==token_left_parenthesis):
                    get_token()
                    B = condition()
                    Btrue = B[0]
                    Bfalse = B[1]
                    backpatch(Btrue,nextquad())
                    if(lexical_analyzer[0]==token_right_parenthesis):
                        get_token()
                        statements()
                        genquad("jump","_","_",Bquad)
                        backpatch(Bfalse,nextquad())
                        return
                    else:
                        error(4, line_number)
                else:
                    error(5, line_number)
            else:
                error(24, line_number)

        program()
        return



global unique_num
global all_quads
global temp_vars
global listOfTempVars
global cFile
global listOfDeclarations
global declarationCounter
topScope = None
listOfDeclarations = []
declarationCounter = 0
listOfTempVars = []
all_quads =[]
unique_num = 1
temp_vars = 0

def nextquad():
    global unique_num
    return unique_num

def genquad(op, x,y,z):
    global all_quads
    global unique_num
    quad = []


    quad = [nextquad()]
    quad.append(op)
    quad.append(x)
    quad.append(y)
    quad.append(z)
    unique_num+=1
    all_quads += [quad]
    return quad

def newtemp():
    global temp_vars
    global listOfTempVars
    temp_vars+=1
    myTuple = ("T",str(temp_vars))
    mySeparator = "_"
    temp = mySeparator.join(myTuple)
    listOfTempVars +=[temp]

    entity = Entity(temp,3)
    entity.tempVariable.offset = calculateOffset()
    new_entity(entity)

    return temp

def emptylist():
    emptyList = []
    return emptyList

def makelist(x):
    myList = []
    myList.append(x)
    return myList

def merge(list1,list2):
    mergedList = list1
    mergedList.extend(list2)
    return mergedList

def backpatch(list,z):
    global all_quads
    for i in range(len(list)):
        for j in range(len(all_quads)):
            if (list[i] == all_quads[j][0]):
                all_quads[j][4] = z
    return

def print_listOfAllQuads():
    global all_quads

    intFile = open('test.int','w')
    for i in range(len(all_quads)):
        print(str(all_quads[i][0])+": ["+str(all_quads[i][1])+"\t\t"+str(all_quads[i][2])+"\t\t"+ str(all_quads[i][3])+"\t\t"+str(all_quads[i][4])+"]")
        intFile.write(str(all_quads[i][0]) + ": " + str(all_quads[i][1]) + " " + str(all_quads[i][2]) + " " + str(all_quads[i][3]) + " " + str(all_quads[i][4]) + "\n")
    intFile.close()

def c(cFile):
    global listOfTempVars
    global all_quads
    global listOfDeclarations
    global declarationCounter

    def printSemicolon(cF,newlines,tabs):
        cF.write(";")
        for i in range(newlines):
            cF.write("\n")
        for i in range(tabs):
            cF.write("\t")

    def printLine(cF,num):
        cF.write("L_"+str(num)+": ")

    for i in range(len(listOfDeclarations)):
        QuantityOfDeclarations = len(listOfDeclarations[i])
        if QuantityOfDeclarations != 0:
            cFile.write("int ")
            for j in range(QuantityOfDeclarations):
                cFile.write(listOfDeclarations[i][j])
                if QuantityOfDeclarations != j + 1:
                    cFile.write(",")
                else:
                    printSemicolon(cFile,1,1)

    QuantityOfTemps = len(listOfTempVars)
    if QuantityOfTemps!=0:
        cFile.write("int ")
    for i in range(QuantityOfTemps):
        cFile.write(listOfTempVars[i])
        if(QuantityOfTemps != i+1):
            cFile.write(",")
        else:
            printSemicolon(cFile,2,1)

    for i in range(len(all_quads)):
        if (all_quads[i][1] == 'begin_block'):
            printLine(cFile,i+1)
            cFile.write("\n\t")
        elif (all_quads[i][1] == "out"):
            printLine(cFile, i + 1)
            cFile.write("printf(\"" + all_quads[i][2] + "= %d\", " + all_quads[i][2] + ")")
            printSemicolon(cFile, 1, 1)
        elif (all_quads[i][1] == ":="):
            printLine(cFile, i + 1)
            cFile.write(all_quads[i][4] + "=" + all_quads[i][2])
            printSemicolon(cFile,1,1)
        elif (all_quads[i][1] == "+"):
            printLine(cFile, i + 1)
            cFile.write(all_quads[i][4] + "=" + all_quads[i][2] + "+" + all_quads[i][3])
            printSemicolon(cFile, 1, 1)
        elif (all_quads[i][1] == "-"):
            printLine(cFile, i + 1)
            cFile.write(all_quads[i][4] + "=" + all_quads[i][2] + "-" + all_quads[i][3])
            printSemicolon(cFile, 1, 1)
        elif (all_quads[i][1] == "*"):
            printLine(cFile, i + 1)
            cFile.write(all_quads[i][4] + "=" + all_quads[i][2] + "*" + all_quads[i][3])
            printSemicolon(cFile, 1, 1)
        elif (all_quads[i][1] == "/"):
            printLine(cFile, i + 1)
            cFile.write(all_quads[i][4] + "=" + all_quads[i][2] + "/" + all_quads[i][3])
            printSemicolon(cFile, 1, 1)
        elif (all_quads[i][1] == "="):
            printLine(cFile, i + 1)
            cFile.write("if (" + all_quads[i][2] + "==" + all_quads[i][3] + ") goto L_" + str(all_quads[i][4]))
            printSemicolon(cFile, 1, 1)
        elif (all_quads[i][1] == "<>"):
            printLine(cFile, i + 1)
            cFile.write("if (" + str(all_quads[i][2]) + "!=" + str(all_quads[i][3]) + ") goto L_" + str(all_quads[i][4]))
            printSemicolon(cFile, 1, 1)
        elif (all_quads[i][1] == "<"):
            printLine(cFile, i + 1)
            cFile.write("if (" + all_quads[i][2] + "<" + all_quads[i][3] + ") goto L_" + str(all_quads[i][4]))
            printSemicolon(cFile, 1, 1)
        elif (all_quads[i][1] == "<="):
            printLine(cFile, i + 1)
            cFile.write("if (" + all_quads[i][2] + "<=" + all_quads[i][3] + ") goto L_" + str(all_quads[i][4]))
            printSemicolon(cFile, 1, 1)
        elif (all_quads[i][1] == ">"):
            printLine(cFile, i + 1)
            cFile.write("if (" + all_quads[i][2] + ">" + all_quads[i][3] + ") goto L_" + str(all_quads[i][4]))
            printSemicolon(cFile, 1, 1)
        elif (all_quads[i][1] == ">="):
            printLine(cFile, i + 1)
            cFile.write("if (" + all_quads[i][2] + ">=" + all_quads[i][3] + ") goto L_" + str(all_quads[i][4]))
            printSemicolon(cFile, 1, 1)
        elif (all_quads[i][1] == "jump"):
            printLine(cFile, i + 1)
            cFile.write("goto L_" + str(all_quads[i][4]))
            printSemicolon(cFile, 1, 1)
        elif (all_quads[i][1] == 'halt'):
            printLine(cFile, i + 1)
            cFile.write(": {}\n\t")

def CreateCFile():
    global cFile
    cFile = open('test.c','w')
    cFile.write("int main(int argc ,char* argv[]){\n\t")

    syntax_analyzer()
    print_listOfAllQuads()
    c(cFile)
    cFile.write("\n}")
    cFile.close()


def countFileLines():  # counts how many lines a file has. We use the value 'last' in syntax_analyzer() -> programblock() to catch a wrong error report in some cases
    global last
    global file
    for line in file:
        if line != "\n":
            last += 1
    file.close()
    file = open(filename, 'r')
    return

def FinalCode():
    global ASMfile
    global topScope
    global AllScopes
    i=0
    ASMfile = open('test.asm', 'w')


    def loadvr(v,reg):
        global topScope
        global ASMfile
        global AllScopes

        if v is int: #1.2.2.6 Constant integer
            ASMfile.write('li t'+str(reg)+','+str(v)+'\n')
        else:

            level = 0
            offset = 0
            mode = 0
            for i in range(len(AllScopes)):
                currentScope = AllScopes[i]
                while(currentScope!=None):
                    for e in currentScope.entityList:
                        if e.name == v:
                            type = e.type
                            level = currentScope.nestingLevel
                            if e.type == 0: #var
                                offset = e.variable.offset
                            elif e.type == 2:#parameter
                                offset = e.parameter.offset
                                mode = e.parameter.parMode
                            elif e.type == 3: #temp
                                offset = e.tempVariable.offset
                    currentScope = currentScope.enclosingScope


            if level==0: #1.2.2.5 Global variable
                ASMfile.write('lw t'+str(reg)+',-'+str(offset)+'(gp)\n')
            elif type==3 or (type==2 and mode==0) or (type==0 and level==1000):#1.2.2.1 #opou 1000 mpainei to topScope.nestingLevel
                ASMfile.write('lw t'+str(reg)+',-'+str(offset)+'(sp)\n')
            elif (type==2 and mode==1):#1.2.2.2 param by reference
                ASMfile.write('lw t0,-'+str(offset)+'(sp)\n')
                ASMfile.write('lw t'+str(reg)+',(t0)\n')
            elif (type==0 or (type==2 and mode ==0)) and 1000>level:#1.2.2.3   #opou 1000 mpainei to topScope.nestingLevel
                #DEN KSEROUME PWS NA VROUME POIA SYNARTISI KALESE TIN SYGKEKRIMENI GRAMMI STON ENDIAMESO KWDIKA AFOU TO TOP SCOPE EINAI NONE LOGW TOU DELETE
                gnlvcode(v)
                ASMfile.write('lw t'+str(reg)+',(t0)\n')
            elif (type==2 and mode==1)and level<1000:#1.2.2.4  #opou 1000 mpainei to topScope.nestingLevel
                gnlvcode(v)
                ASMfile.write('lw t0,(t0)')
                ASMfile.write('lw t'+str(reg)+',(t0)')

    def storerv(reg,v):
        global topScope
        global ASMfile
        global AllScopes
        if v is int:  # 1.2.3.6 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            loadvr(1,0)#fortwsi tis aithmitikis statheras se enan register
            storerv(0,v)#topothetisi stin metavliti stoxo
        else:

            level =0
            offset =0
            mode =0
            for i in range(len(AllScopes)):
                currentScope = AllScopes[i]
                while (currentScope != None):
                    for e in currentScope.entityList:
                        if e.name == str(v):
                            type = e.type
                            level = currentScope.nestingLevel
                            if e.type == 0:  # var
                                offset = e.variable.offset
                            elif e.type == 2: #parameter
                                offset = e.parameter.offset
                                mode = e.parameter.parMode
                            elif e.type == 3:  # temp
                                offset = e.tempVariable.offset
                    currentScope = currentScope.enclosingScope
            if level==0:#1.2.3.5
                ASMfile.write('sw t'+str(reg)+'-'+str(offset)+'(gp)\n')
            elif (type==2 and mode==1) and level<1000:#1.2.3.4  #opou 1000 mpainei to topScope.nestingLevel
                gnlvcode(v)
                ASMfile.write('lw t0,(t0)\n')
                ASMfile.write('sw t'+str(reg)+'(t0)\n')
                ASMfile.write('sw t'+str(reg)+'(t0)\n')
            elif (type==0 or (type==2 and mode==0)) and level<1000:#1.2.3.3  #opou 1000 mpainei to topScope.nestingLevel
                gnlvcode(v)
                ASMfile.write('sw t'+str(reg)+',(t0)\n')
            elif type==2 and mode==1:#1.2.3.2
                ASMfile.write('lw t0,-'+str(offset)+'(sp)\n')
                ASMfile.write('sw t'+str(reg)+',(t0)\n')
            elif type==3 or (type==2 and mode==0) or (type==0 and level==1000):#1.2.3.1  #opou 1000 mpainei to topScope.nestingLevel
                ASMfile.write('sw t'+str(reg)+',-'+str(offset)+'(sp)\n')

    def gnlvcode(v):
        global topScope
        global ASMfile
        global AllScopes
        #idk an pairnei to swsto scope
        foundEntity =0
        levelOnWhichGnlvWasCalled = 1
        if topScope!=None:
            levelOnWhichGnlvWasCalled = 1#anti gia 1 tha eprepe topScope.nestingLevel
        for i in range(len(AllScopes)):
            currentScope = AllScopes[i]
            while(currentScope!= None):
                for entity in currentScope.entityList:
                    if entity.name == v:
                        foundEntity =1
                        levelOnWhichEntityWasFound = currentScope.nestingLevel
                        levelDiff = levelOnWhichGnlvWasCalled-levelOnWhichEntityWasFound #+++++++++++++++++++++++++++++++++++
                        ASMfile.write('lw t0,-8(sp)\n')
                        for i in range(levelDiff):
                            ASMfile.write('lw t0,-8(0)\n')
                        if entity.type ==0:
                            offset = entity.variable.offset
                        else:
                            offset = entity.parameter.offset
                        ASMfile.write('addi t0,t0,'+str(offset)+'\n')
                currentScope = currentScope.enclosingScope

        if(foundEntity==0):
            print('No variable with the name "' + str(v) + '" was found')
            exit(-1)


    for current_quad in all_quads:
        ASMfile.write('L'+str(current_quad[0])+':\n')
        if current_quad[1] == 'jump':
            ASMfile.write('J '+str(current_quad[4])+'\n')
        elif current_quad[1] == ':=':
            loadvr(current_quad[2],1)
            storerv(1,current_quad[4])
        elif current_quad[1] == '<':
            loadvr(current_quad[2],1)
            loadvr(current_quad[3],2)
            ASMfile.write('blt t1,t2,'+str(current_quad[4])+'\n')
        elif current_quad[1] == '<=':
            loadvr(current_quad[2],1)
            loadvr(current_quad[3],2)
            ASMfile.write('ble t1,t2,'+str(current_quad[4])+'\n')
        elif current_quad[1] == '>':
            loadvr(current_quad[2], 1)
            loadvr(current_quad[3], 2)
            ASMfile.write('bgt t1,t2,' + str(current_quad[4])+'\n')
        elif current_quad[1] == '>=':
            loadvr(current_quad[2], 1)
            loadvr(current_quad[3], 2)
            ASMfile.write('bge t1,t2,' + str(current_quad[4])+'\n')
        elif current_quad[1] == '<>':
            loadvr(current_quad[2], 1)
            loadvr(current_quad[3], 2)
            ASMfile.write('bne t1,t2,' + str(current_quad[4])+'\n')
        elif current_quad[1] == '==':
            loadvr(current_quad[2],1)
            loadvr(current_quad[3],2)
            ASMfile.write('beq t1,t2,'+str(current_quad[4])+'\n')
        elif current_quad[1] == '=':
            loadvr(current_quad[2], 1)
            loadvr(current_quad[3], 2)
            ASMfile.write('beq t1,t2,' + str(current_quad[4])+'\n')
        elif current_quad[1] == '+':
            loadvr(current_quad[2],1)
            loadvr(current_quad[3],2)
            ASMfile.write('add t1,t1,t2\n')
            storerv(1,current_quad[4])
        elif current_quad[1] == '-':
            loadvr(current_quad[2],1)
            loadvr(current_quad[3],2)
            ASMfile.write('sub t1,t1,t2\n')
            storerv(1,current_quad[4])
        elif current_quad[1] == '*':
            loadvr(current_quad[2],1)
            loadvr(current_quad[3],2)
            ASMfile.write('mul t1,t1,t2\n')
            storerv(1,current_quad[4])
        elif current_quad[1] == '/':
            loadvr(current_quad[2],1)
            loadvr(current_quad[3],2)
            ASMfile.write('div t1,t1,t2\n')
            storerv(1,current_quad[4])
        elif current_quad[1]=='retv':
            loadvr(current_quad[4],1)
            ASMfile.write('lw t0,-8(sp)\n')
            ASMfile.write('sw t1,(t0)\n')
        elif current_quad[1]=='par':
            nestingLevel = 1
            currentLevel = 0
            if current_quad[3]=='CV':
                loadvr(current_quad[2],0)
                res = 12+4*i;
                ASMfile.write('sw t0,-'+str(res)+'(fp)\n')
            elif current_quad[3]=='REF':
                if nestingLevel == currentLevel:
                    offset=0
                    ASMfile.write('addi t0,sp,-'+str(offset)+'\n')
                    res = 12+4*i
                    ASMfile.write('sw t0,-'+str(res)+'(fp)\n')
                else:
                    gnlvcode(current_quad[2])
                    ASMfile.write('lw t0,(t0)\n')
                    res = 12+4*i
                    ASMfile.write('sw t0,-'+str(res)+'(fp)\n')
                    offset = 0
                    ASMfile.write('addi t0,sp,-'+str(offset)+'\n')
                    ASMfile.write('sw t0,-8(fp)\n')
        elif current_quad[1]=='call':
            nestingLevel =1
            currentLevel =0
            if nestingLevel==currentLevel:
                ASMfile.write('lw t0,-4(sp)\n')
                ASMfile.write('sw t0,-4(fp)\n')
            else:
                ASMfile.write('sw sp,-4(fp)\n')
                framelength = 8;
                ASMfile.write('addi sp,sp,'+str(framelength)+'\n')
                ASMfile.write('jal '+str(current_quad[2])+'\n')
                ASMfile.write('addi sp,sp,-'+str(framelength)+'\n')
        elif current_quad[1]=='begin_block':
            if current_quad[2]!='main':
                ASMfile.write('j main\n')
                ASMfile.write('sw ra,-0(sp)\n')
            else:
                ASMfile.write('main:\n')#den mpainei edw . pws na katalvw oti einai i prwti grammi tis main
                framelength = 24
                ASMfile.write('addi sp,sp,'+str(framelength)+'\n')
                ASMfile.write('mv gp,sp')
        elif current_quad[1]=='end_block':
            ASMfile.write('lw ra,-0(sp)\n')
            ASMfile.write('jr ra\n')








global ASMfile
global symb
global AllScopes
AllScopes = []
ASMfile = open('test.asm', 'w')
symb = open('test.symb','w')
filename = sys.argv[1]
file= open(filename, 'r')
countFileLines()
CreateCFile()
FinalCode()
ASMfile.close()
file.close()