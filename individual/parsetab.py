
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABSTRACT ACTUAL ADD ANNOTATION APPEND ARRAYLIST ARRAYOF ARROW AS AS_SAFE AT_NO_WS BOOLEAN BREAK BY CATCH CHAR CLASS COLONCOLON COMMA COMMENT COMPANION CONJ CONST CONSTRUCTOR CONTINUE CROSSINLINE DATA DECR DECREMENTIN DECREMENTONE DISJ DIVIDE DIVIDEIN DO DOT DOTS DOUBLE_ARROW DOUBLE_SEMICOLON DYNAMIC ELSE ENUM EQEQ EQEQEQ EQUAL EXCL_EQ EXCL_EQEQ EXCL_NO_WS EXCL_WS EXPECT EXTERNAL FIELD FILE FINAL FINALLY FIRST FLOAT FOR FUN GE GET HASH ID IF IMPORT IN INCR INCREMENTIN INCREMENTONE INCREMENTTIMES INDICES INFIX INIT INLINE INNER INT INTERFACE INTERNAL IS ISEMPTY LANGLE LAST LATEINIT LCURL LE LINEBREAK LINKEDL LISTOF LONG LPAREN LSQUARE MARK_1 MARK_2 MINUS MOD MODIN NOINLINE OBJECT OPEN OPERATOR OUT OVERRIDE PACKAGE PARAM PEEK PLUS POLL POP PRINT PRINTLN PRIVATE PROPERTY PROTECTED PUBLIC PUSH QUEST_WS QUEUE RANGE RANGLE RCURL RECEIVER REIFIED REMOVE REMOVEI REMOVEL REMOVEN RETURN RPAREN RSQUARE SEALED SEMICOLON SET SETPARAM SINGLE_QUOTE SIZE STACK STRING_1 SUM SUPER SUSPEND TAILREC TBOOLEAN TCHAR TDOUBLE TEMPLATE TFLOAT THIS THREEDOTS THROW TIMES TINT TLONG TRY TSTRING TYPEOF TYPE_ALIAS VAL VALUE VAL_TIPO_1 VAR VARARG VAR_TIPO_1 WHEN WHERE WHILEline : impresion\n                | expression\n                | condicionL\n                | condicionR\n                | condicionN\n                | asignacion\n                | asignacion SEMICOLON\n                | for\n                | if\n                | stack\n                | stack_actuar\n                | instance_arraylist\n                | def_estruct_tipoDato\n                impresion : PRINT LPAREN term RPAREN\n                | PRINTLN LPAREN term RPARENfor : FOR LPAREN ID IN ID RPAREN LCURL line RCURLkeywordVariables : VAR\n                        | VALasignacion : keywordVariables asignacionSimple\n                    | asignacionSimpleasignacionSimple : ID DOTS tipoDato EQUAL valor\n                        | ID EQUAL valortipoDato : TINT\n                | TLONG\n                | TFLOAT\n                | TDOUBLE\n                | TBOOLEAN\n                | TCHAR\n                | TSTRINGvalor : expressionexpression : expression PLUS termexpression : expression MINUS termexpression : expression TIMES termexpression : expression DIVIDE termexpression : expression MOD termexpression : termterm : factorterm : LPAREN expression RPARENfactor : INT\n                | FLOAT\n                | LONG\n                | CHAR\n                | BOOLEAN\n                | ID\n                | STRING_1\n                if : IF LPAREN condicion RPAREN LCURL line RCURL\n            | IF LPAREN condicion RPAREN LCURL line RCURL else\n            else : ELSE LCURL line RCURLcondicion : condicionL\n                | condicionR\n                | condicionN\n                condicionL : BOOLEAN opL BOOLEAN\n                    | ID opL ID\n                    | ID opL BOOLEAN\n                    | BOOLEAN opL ID\n                    condicionR : INT opR INT\n                    | INT opR FLOAT\n                    | INT opR LONG\n                    | FLOAT opR FLOAT\n                    | FLOAT opR INT\n                    | FLOAT opR LONG\n                    | LONG opR LONG\n                    | LONG opR INT\n                    | LONG opR FLOAT\n                    | STRING_1 opR STRING_1\n                    | CHAR opR CHAR\n                    | ID opR ID\n                    condicionN : EXCL_WS BOOLEAN\n                    | EXCL_WS ID\n                    opL : CONJ\n            | DISJ\n            opR : LANGLE\n            | RANGLE\n            | LE\n            | GE\n            | EXCL_EQ\n            | EXCL_EQEQ\n            | AS_SAFE\n            | EQEQ\n            | EQEQEQ\n            stack : keywordVariables ID DOTS def_estruct_tipoDato EQUAL instance_arraylistdef_estruct_tipoDato : STACK LANGLE tipoDato RANGLEinstance_arraylist : ARRAYLIST LPAREN RPARENstack_actuar : ID DOT stack_funciones stack_funciones : stack_isEmpty\n                        | stack_push\n                        | stack_pop\n                        stack_isEmpty : ISEMPTY LPAREN RPARENstack_pop : POP LPAREN RPARENstack_push : PUSH LPAREN factor RPAREN'
    
_lr_action_items = {'PRINT':([0,153,158,164,],[14,14,14,14,]),'PRINTLN':([0,153,158,164,],[17,17,17,17,]),'BOOLEAN':([0,15,25,35,36,37,38,39,41,50,51,52,53,54,58,78,140,142,153,158,164,],[18,47,73,47,47,47,47,47,47,47,89,-70,-71,92,47,128,47,47,18,18,18,]),'ID':([0,15,25,26,33,34,35,36,37,38,39,41,50,51,52,53,54,55,58,59,60,61,62,63,64,65,66,67,77,78,140,142,144,153,158,164,],[19,48,74,76,-17,-18,48,48,48,48,48,48,48,90,-70,-71,91,93,48,-72,-73,-74,-75,-76,-77,-78,-79,-80,123,129,48,48,152,19,19,19,]),'INT':([0,15,35,36,37,38,39,41,50,58,59,60,61,62,63,64,65,66,67,68,69,70,78,140,142,153,158,164,],[20,43,43,43,43,43,43,43,43,43,-72,-73,-74,-75,-76,-77,-78,-79,-80,111,115,118,130,43,43,20,20,20,]),'FLOAT':([0,15,35,36,37,38,39,41,50,58,59,60,61,62,63,64,65,66,67,68,69,70,78,140,142,153,158,164,],[21,44,44,44,44,44,44,44,44,44,-72,-73,-74,-75,-76,-77,-78,-79,-80,112,114,119,131,44,44,21,21,21,]),'LONG':([0,15,35,36,37,38,39,41,50,58,59,60,61,62,63,64,65,66,67,68,69,70,78,140,142,153,158,164,],[22,45,45,45,45,45,45,45,45,45,-72,-73,-74,-75,-76,-77,-78,-79,-80,113,116,117,132,45,45,22,22,22,]),'STRING_1':([0,15,35,36,37,38,39,41,50,58,59,60,61,62,63,64,65,66,67,71,78,140,142,153,158,164,],[23,49,49,49,49,49,49,49,49,49,-72,-73,-74,-75,-76,-77,-78,-79,-80,120,133,49,49,23,23,23,]),'CHAR':([0,15,35,36,37,38,39,41,50,58,59,60,61,62,63,64,65,66,67,72,78,140,142,153,158,164,],[24,46,46,46,46,46,46,46,46,46,-72,-73,-74,-75,-76,-77,-78,-79,-80,121,134,46,46,24,24,24,]),'EXCL_WS':([0,78,153,158,164,],[25,25,25,25,25,]),'FOR':([0,153,158,164,],[28,28,28,28,]),'IF':([0,153,158,164,],[29,29,29,29,]),'ARRAYLIST':([0,151,153,158,164,],[30,30,30,30,30,]),'STACK':([0,122,153,158,164,],[31,31,31,31,31,]),'LPAREN':([0,14,15,17,28,29,30,35,36,37,38,39,41,50,58,98,99,100,142,153,158,164,],[15,41,15,50,77,78,79,15,15,15,15,15,15,15,15,139,140,141,15,15,15,15,]),'VAR':([0,153,158,164,],[33,33,33,33,]),'VAL':([0,153,158,164,],[34,34,34,34,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,16,18,19,20,21,22,23,24,27,32,40,43,44,45,46,47,48,49,73,74,75,81,82,83,84,85,87,89,90,91,92,93,94,95,96,97,109,110,111,112,113,114,115,116,117,118,119,120,121,135,137,138,146,147,149,150,154,155,159,161,163,166,],[0,-1,-2,-3,-4,-5,-6,-8,-9,-10,-11,-12,-13,-36,-43,-44,-39,-40,-41,-45,-42,-20,-37,-7,-39,-40,-41,-42,-43,-44,-45,-68,-69,-19,-31,-32,-33,-34,-35,-38,-52,-55,-53,-54,-67,-84,-85,-86,-87,-22,-30,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-83,-14,-15,-82,-88,-89,-21,-90,-81,-46,-47,-16,-48,]),'RCURL':([2,3,4,5,6,7,8,9,10,11,12,13,16,18,19,20,21,22,23,24,27,32,40,43,44,45,46,47,48,49,73,74,75,81,82,83,84,85,87,89,90,91,92,93,94,95,96,97,109,110,111,112,113,114,115,116,117,118,119,120,121,135,137,138,146,147,149,150,154,155,157,159,160,161,163,165,166,],[-1,-2,-3,-4,-5,-6,-8,-9,-10,-11,-12,-13,-36,-43,-44,-39,-40,-41,-45,-42,-20,-37,-7,-39,-40,-41,-42,-43,-44,-45,-68,-69,-19,-31,-32,-33,-34,-35,-38,-52,-55,-53,-54,-67,-84,-85,-86,-87,-22,-30,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-83,-14,-15,-82,-88,-89,-21,-90,-81,159,-46,163,-47,-16,166,-48,]),'PLUS':([3,16,18,19,20,21,22,23,24,32,42,43,44,45,46,47,48,49,81,82,83,84,85,87,110,],[35,-36,-43,-44,-39,-40,-41,-45,-42,-37,35,-39,-40,-41,-42,-43,-44,-45,-31,-32,-33,-34,-35,-38,35,]),'MINUS':([3,16,18,19,20,21,22,23,24,32,42,43,44,45,46,47,48,49,81,82,83,84,85,87,110,],[36,-36,-43,-44,-39,-40,-41,-45,-42,-37,36,-39,-40,-41,-42,-43,-44,-45,-31,-32,-33,-34,-35,-38,36,]),'TIMES':([3,16,18,19,20,21,22,23,24,32,42,43,44,45,46,47,48,49,81,82,83,84,85,87,110,],[37,-36,-43,-44,-39,-40,-41,-45,-42,-37,37,-39,-40,-41,-42,-43,-44,-45,-31,-32,-33,-34,-35,-38,37,]),'DIVIDE':([3,16,18,19,20,21,22,23,24,32,42,43,44,45,46,47,48,49,81,82,83,84,85,87,110,],[38,-36,-43,-44,-39,-40,-41,-45,-42,-37,38,-39,-40,-41,-42,-43,-44,-45,-31,-32,-33,-34,-35,-38,38,]),'MOD':([3,16,18,19,20,21,22,23,24,32,42,43,44,45,46,47,48,49,81,82,83,84,85,87,110,],[39,-36,-43,-44,-39,-40,-41,-45,-42,-37,39,-39,-40,-41,-42,-43,-44,-45,-31,-32,-33,-34,-35,-38,39,]),'SEMICOLON':([7,16,27,32,43,44,45,46,47,48,49,75,81,82,83,84,85,87,109,110,150,],[40,-36,-20,-37,-39,-40,-41,-42,-43,-44,-45,-19,-31,-32,-33,-34,-35,-38,-22,-30,-21,]),'RPAREN':([16,32,42,43,44,45,46,47,48,49,73,74,79,81,82,83,84,85,86,87,88,89,90,91,92,93,111,112,113,114,115,116,117,118,119,120,121,124,125,126,127,139,141,148,152,],[-36,-37,87,-39,-40,-41,-42,-43,-44,-45,-68,-69,135,-31,-32,-33,-34,-35,137,-38,138,-52,-55,-53,-54,-67,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,145,-49,-50,-51,147,149,154,156,]),'CONJ':([18,19,128,129,],[52,52,52,52,]),'DISJ':([18,19,128,129,],[53,53,53,53,]),'DOT':([19,],[56,]),'DOTS':([19,76,],[57,122,]),'EQUAL':([19,76,101,102,103,104,105,106,107,108,143,146,],[58,58,142,-23,-24,-25,-26,-27,-28,-29,151,-82,]),'LANGLE':([19,20,21,22,23,24,31,129,130,131,132,133,134,],[59,59,59,59,59,59,80,59,59,59,59,59,59,]),'RANGLE':([19,20,21,22,23,24,102,103,104,105,106,107,108,129,130,131,132,133,134,136,],[60,60,60,60,60,60,-23,-24,-25,-26,-27,-28,-29,60,60,60,60,60,60,146,]),'LE':([19,20,21,22,23,24,129,130,131,132,133,134,],[61,61,61,61,61,61,61,61,61,61,61,61,]),'GE':([19,20,21,22,23,24,129,130,131,132,133,134,],[62,62,62,62,62,62,62,62,62,62,62,62,]),'EXCL_EQ':([19,20,21,22,23,24,129,130,131,132,133,134,],[63,63,63,63,63,63,63,63,63,63,63,63,]),'EXCL_EQEQ':([19,20,21,22,23,24,129,130,131,132,133,134,],[64,64,64,64,64,64,64,64,64,64,64,64,]),'AS_SAFE':([19,20,21,22,23,24,129,130,131,132,133,134,],[65,65,65,65,65,65,65,65,65,65,65,65,]),'EQEQ':([19,20,21,22,23,24,129,130,131,132,133,134,],[66,66,66,66,66,66,66,66,66,66,66,66,]),'EQEQEQ':([19,20,21,22,23,24,129,130,131,132,133,134,],[67,67,67,67,67,67,67,67,67,67,67,67,]),'ISEMPTY':([56,],[98,]),'PUSH':([56,],[99,]),'POP':([56,],[100,]),'TINT':([57,80,122,],[102,102,102,]),'TLONG':([57,80,122,],[103,103,103,]),'TFLOAT':([57,80,122,],[104,104,104,]),'TDOUBLE':([57,80,122,],[105,105,105,]),'TBOOLEAN':([57,80,122,],[106,106,106,]),'TCHAR':([57,80,122,],[107,107,107,]),'TSTRING':([57,80,122,],[108,108,108,]),'IN':([123,],[144,]),'LCURL':([145,156,162,],[153,158,164,]),'ELSE':([159,],[162,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'line':([0,153,158,164,],[1,157,160,165,]),'impresion':([0,153,158,164,],[2,2,2,2,]),'expression':([0,15,58,142,153,158,164,],[3,42,110,110,3,3,3,]),'condicionL':([0,78,153,158,164,],[4,125,4,4,4,]),'condicionR':([0,78,153,158,164,],[5,126,5,5,5,]),'condicionN':([0,78,153,158,164,],[6,127,6,6,6,]),'asignacion':([0,153,158,164,],[7,7,7,7,]),'for':([0,153,158,164,],[8,8,8,8,]),'if':([0,153,158,164,],[9,9,9,9,]),'stack':([0,153,158,164,],[10,10,10,10,]),'stack_actuar':([0,153,158,164,],[11,11,11,11,]),'instance_arraylist':([0,151,153,158,164,],[12,155,12,12,12,]),'def_estruct_tipoDato':([0,122,153,158,164,],[13,143,13,13,13,]),'term':([0,15,35,36,37,38,39,41,50,58,142,153,158,164,],[16,16,81,82,83,84,85,86,88,16,16,16,16,16,]),'keywordVariables':([0,153,158,164,],[26,26,26,26,]),'asignacionSimple':([0,26,153,158,164,],[27,75,27,27,27,]),'factor':([0,15,35,36,37,38,39,41,50,58,140,142,153,158,164,],[32,32,32,32,32,32,32,32,32,32,148,32,32,32,32,]),'opL':([18,19,128,129,],[51,54,51,54,]),'opR':([19,20,21,22,23,24,129,130,131,132,133,134,],[55,68,69,70,71,72,55,68,69,70,71,72,]),'stack_funciones':([56,],[94,]),'stack_isEmpty':([56,],[95,]),'stack_push':([56,],[96,]),'stack_pop':([56,],[97,]),'tipoDato':([57,80,122,],[101,136,101,]),'valor':([58,142,],[109,150,]),'condicion':([78,],[124,]),'else':([159,],[161,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> line","S'",1,None,None,None),
  ('line -> impresion','line',1,'p_cuerpo','kotlin_sintactico_karla.py',10),
  ('line -> expression','line',1,'p_cuerpo','kotlin_sintactico_karla.py',11),
  ('line -> condicionL','line',1,'p_cuerpo','kotlin_sintactico_karla.py',12),
  ('line -> condicionR','line',1,'p_cuerpo','kotlin_sintactico_karla.py',13),
  ('line -> condicionN','line',1,'p_cuerpo','kotlin_sintactico_karla.py',14),
  ('line -> asignacion','line',1,'p_cuerpo','kotlin_sintactico_karla.py',15),
  ('line -> asignacion SEMICOLON','line',2,'p_cuerpo','kotlin_sintactico_karla.py',16),
  ('line -> for','line',1,'p_cuerpo','kotlin_sintactico_karla.py',17),
  ('line -> if','line',1,'p_cuerpo','kotlin_sintactico_karla.py',18),
  ('line -> stack','line',1,'p_cuerpo','kotlin_sintactico_karla.py',19),
  ('line -> stack_actuar','line',1,'p_cuerpo','kotlin_sintactico_karla.py',20),
  ('line -> instance_arraylist','line',1,'p_cuerpo','kotlin_sintactico_karla.py',21),
  ('line -> def_estruct_tipoDato','line',1,'p_cuerpo','kotlin_sintactico_karla.py',22),
  ('impresion -> PRINT LPAREN term RPAREN','impresion',4,'p_impresion','kotlin_sintactico_karla.py',26),
  ('impresion -> PRINTLN LPAREN term RPAREN','impresion',4,'p_impresion','kotlin_sintactico_karla.py',27),
  ('for -> FOR LPAREN ID IN ID RPAREN LCURL line RCURL','for',9,'p_for','kotlin_sintactico_karla.py',30),
  ('keywordVariables -> VAR','keywordVariables',1,'p_keywordVariables','kotlin_sintactico_karla.py',35),
  ('keywordVariables -> VAL','keywordVariables',1,'p_keywordVariables','kotlin_sintactico_karla.py',36),
  ('asignacion -> keywordVariables asignacionSimple','asignacion',2,'p_asignacion','kotlin_sintactico_karla.py',39),
  ('asignacion -> asignacionSimple','asignacion',1,'p_asignacion','kotlin_sintactico_karla.py',40),
  ('asignacionSimple -> ID DOTS tipoDato EQUAL valor','asignacionSimple',5,'p_asignacionS','kotlin_sintactico_karla.py',43),
  ('asignacionSimple -> ID EQUAL valor','asignacionSimple',3,'p_asignacionS','kotlin_sintactico_karla.py',44),
  ('tipoDato -> TINT','tipoDato',1,'p_tipoDato','kotlin_sintactico_karla.py',48),
  ('tipoDato -> TLONG','tipoDato',1,'p_tipoDato','kotlin_sintactico_karla.py',49),
  ('tipoDato -> TFLOAT','tipoDato',1,'p_tipoDato','kotlin_sintactico_karla.py',50),
  ('tipoDato -> TDOUBLE','tipoDato',1,'p_tipoDato','kotlin_sintactico_karla.py',51),
  ('tipoDato -> TBOOLEAN','tipoDato',1,'p_tipoDato','kotlin_sintactico_karla.py',52),
  ('tipoDato -> TCHAR','tipoDato',1,'p_tipoDato','kotlin_sintactico_karla.py',53),
  ('tipoDato -> TSTRING','tipoDato',1,'p_tipoDato','kotlin_sintactico_karla.py',54),
  ('valor -> expression','valor',1,'p_valor','kotlin_sintactico_karla.py',57),
  ('expression -> expression PLUS term','expression',3,'p_expression_plus','kotlin_sintactico_karla.py',60),
  ('expression -> expression MINUS term','expression',3,'p_expression_minus','kotlin_sintactico_karla.py',63),
  ('expression -> expression TIMES term','expression',3,'p_expression_times','kotlin_sintactico_karla.py',66),
  ('expression -> expression DIVIDE term','expression',3,'p_expression_divide','kotlin_sintactico_karla.py',69),
  ('expression -> expression MOD term','expression',3,'p_expression_mod','kotlin_sintactico_karla.py',72),
  ('expression -> term','expression',1,'p_expression_single','kotlin_sintactico_karla.py',75),
  ('term -> factor','term',1,'p_term_factor','kotlin_sintactico_karla.py',78),
  ('term -> LPAREN expression RPAREN','term',3,'p_term_Paren','kotlin_sintactico_karla.py',81),
  ('factor -> INT','factor',1,'p_factor','kotlin_sintactico_karla.py',84),
  ('factor -> FLOAT','factor',1,'p_factor','kotlin_sintactico_karla.py',85),
  ('factor -> LONG','factor',1,'p_factor','kotlin_sintactico_karla.py',86),
  ('factor -> CHAR','factor',1,'p_factor','kotlin_sintactico_karla.py',87),
  ('factor -> BOOLEAN','factor',1,'p_factor','kotlin_sintactico_karla.py',88),
  ('factor -> ID','factor',1,'p_factor','kotlin_sintactico_karla.py',89),
  ('factor -> STRING_1','factor',1,'p_factor','kotlin_sintactico_karla.py',90),
  ('if -> IF LPAREN condicion RPAREN LCURL line RCURL','if',7,'p_if','kotlin_sintactico_karla.py',96),
  ('if -> IF LPAREN condicion RPAREN LCURL line RCURL else','if',8,'p_if','kotlin_sintactico_karla.py',97),
  ('else -> ELSE LCURL line RCURL','else',4,'p_else','kotlin_sintactico_karla.py',101),
  ('condicion -> condicionL','condicion',1,'p_condicion','kotlin_sintactico_karla.py',111),
  ('condicion -> condicionR','condicion',1,'p_condicion','kotlin_sintactico_karla.py',112),
  ('condicion -> condicionN','condicion',1,'p_condicion','kotlin_sintactico_karla.py',113),
  ('condicionL -> BOOLEAN opL BOOLEAN','condicionL',3,'p_condicionL','kotlin_sintactico_karla.py',117),
  ('condicionL -> ID opL ID','condicionL',3,'p_condicionL','kotlin_sintactico_karla.py',118),
  ('condicionL -> ID opL BOOLEAN','condicionL',3,'p_condicionL','kotlin_sintactico_karla.py',119),
  ('condicionL -> BOOLEAN opL ID','condicionL',3,'p_condicionL','kotlin_sintactico_karla.py',120),
  ('condicionR -> INT opR INT','condicionR',3,'p_condicionR','kotlin_sintactico_karla.py',124),
  ('condicionR -> INT opR FLOAT','condicionR',3,'p_condicionR','kotlin_sintactico_karla.py',125),
  ('condicionR -> INT opR LONG','condicionR',3,'p_condicionR','kotlin_sintactico_karla.py',126),
  ('condicionR -> FLOAT opR FLOAT','condicionR',3,'p_condicionR','kotlin_sintactico_karla.py',127),
  ('condicionR -> FLOAT opR INT','condicionR',3,'p_condicionR','kotlin_sintactico_karla.py',128),
  ('condicionR -> FLOAT opR LONG','condicionR',3,'p_condicionR','kotlin_sintactico_karla.py',129),
  ('condicionR -> LONG opR LONG','condicionR',3,'p_condicionR','kotlin_sintactico_karla.py',130),
  ('condicionR -> LONG opR INT','condicionR',3,'p_condicionR','kotlin_sintactico_karla.py',131),
  ('condicionR -> LONG opR FLOAT','condicionR',3,'p_condicionR','kotlin_sintactico_karla.py',132),
  ('condicionR -> STRING_1 opR STRING_1','condicionR',3,'p_condicionR','kotlin_sintactico_karla.py',133),
  ('condicionR -> CHAR opR CHAR','condicionR',3,'p_condicionR','kotlin_sintactico_karla.py',134),
  ('condicionR -> ID opR ID','condicionR',3,'p_condicionR','kotlin_sintactico_karla.py',135),
  ('condicionN -> EXCL_WS BOOLEAN','condicionN',2,'p_condicionN','kotlin_sintactico_karla.py',139),
  ('condicionN -> EXCL_WS ID','condicionN',2,'p_condicionN','kotlin_sintactico_karla.py',140),
  ('opL -> CONJ','opL',1,'p_opL','kotlin_sintactico_karla.py',145),
  ('opL -> DISJ','opL',1,'p_opL','kotlin_sintactico_karla.py',146),
  ('opR -> LANGLE','opR',1,'p_opR','kotlin_sintactico_karla.py',150),
  ('opR -> RANGLE','opR',1,'p_opR','kotlin_sintactico_karla.py',151),
  ('opR -> LE','opR',1,'p_opR','kotlin_sintactico_karla.py',152),
  ('opR -> GE','opR',1,'p_opR','kotlin_sintactico_karla.py',153),
  ('opR -> EXCL_EQ','opR',1,'p_opR','kotlin_sintactico_karla.py',154),
  ('opR -> EXCL_EQEQ','opR',1,'p_opR','kotlin_sintactico_karla.py',155),
  ('opR -> AS_SAFE','opR',1,'p_opR','kotlin_sintactico_karla.py',156),
  ('opR -> EQEQ','opR',1,'p_opR','kotlin_sintactico_karla.py',157),
  ('opR -> EQEQEQ','opR',1,'p_opR','kotlin_sintactico_karla.py',158),
  ('stack -> keywordVariables ID DOTS def_estruct_tipoDato EQUAL instance_arraylist','stack',6,'p_stack','kotlin_sintactico_karla.py',164),
  ('def_estruct_tipoDato -> STACK LANGLE tipoDato RANGLE','def_estruct_tipoDato',4,'p_def_estruct_dato','kotlin_sintactico_karla.py',168),
  ('instance_arraylist -> ARRAYLIST LPAREN RPAREN','instance_arraylist',3,'p_instance_ArrayList','kotlin_sintactico_karla.py',172),
  ('stack_actuar -> ID DOT stack_funciones','stack_actuar',3,'p_stack_actuar','kotlin_sintactico_karla.py',176),
  ('stack_funciones -> stack_isEmpty','stack_funciones',1,'p_stack_funciones','kotlin_sintactico_karla.py',180),
  ('stack_funciones -> stack_push','stack_funciones',1,'p_stack_funciones','kotlin_sintactico_karla.py',181),
  ('stack_funciones -> stack_pop','stack_funciones',1,'p_stack_funciones','kotlin_sintactico_karla.py',182),
  ('stack_isEmpty -> ISEMPTY LPAREN RPAREN','stack_isEmpty',3,'p_stack_isEmpty','kotlin_sintactico_karla.py',186),
  ('stack_pop -> POP LPAREN RPAREN','stack_pop',3,'p_stack_pop','kotlin_sintactico_karla.py',189),
  ('stack_push -> PUSH LPAREN factor RPAREN','stack_push',4,'p_stack_push','kotlin_sintactico_karla.py',192),
]
