
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ACOR ALLAVE AND APAR ARROBA BOOLEAN BOOLEANOEXPRESION BREAK CADENAEXPRESION CCOR CLLAVE COMA COMDOBLE COMENTARIOMULTILINEA COMENTARIOSIMPLE COMPARETO COMSIMPLE CONTAINS CPAR DIVISION DOSPUNTOS DOWNTO ELSE ENTEROEXPRESION F FALSE FLOAT FOR FUN GET GETINDEX HASHCODE ID IF IGUAL IGUALIGUAL IN INDICES INICIOCOMENTARIO INT ISEMPTY LIST LISTOF MAYOR MAYORIGUAL MENOR MENORIGUAL MODULO MULT NEGACION NOIGUAL OR PAIR PREGUNTA PRINT PRINTLN PUNTO PUNTOCOMA PUNTOPUNTO RESTA SET SETOF SIGNODOLAR SIZE SLICE STEP STRING SUMA TOLIST TOSTRING TRIPLE TRIPLEIGUAL TRUE UNTIL VAL VAR WHILE WITHINDEXsentencia : asignacion\n                | valor\n                | metodo\n                | control\n                | condicion\n                | atributo\n    asignacion : VAL ID tipoAsignacion\n                  | VAR ID tipoAsignacion\n                  | ID inicializacion\n    tipoAsignacion : declaracion\n                      | inicializacion\n                      | declaracion inicializaciondeclaracion : DOSPUNTOS tipoDatoinicializacion : IGUAL valortipoDato : INT\n                | FLOAT\n                | BOOLEAN\n                | STRING\n                | LIST MENOR tipoDato MAYOR\n                | SET MENOR tipoDato MAYOR\n                | PAIR MENOR tipoDato COMA tipoDato MAYOR\n                | TRIPLE MENOR tipoDato COMA tipoDato COMA tipoDato MAYOR valor : ENTEROEXPRESION\n             | flotante\n             | BOOLEANOEXPRESION\n             | CADENAEXPRESION\n             | list\n             | set\n             | pair\n             | triple\n             | expresion\n             | IDflotante : ENTEROEXPRESION F\n                | ENTEROEXPRESION PUNTO ENTEROEXPRESION Flist : LISTOF APAR contenido CPARset : SETOF APAR contenido CPARpair : PAIR APAR factorEspecial COMA factorEspecial CPARtriple : TRIPLE APAR factorEspecial COMA factorEspecial COMA factorEspecial CPARcontenido : factorEspecial\n                 | factorEspecial COMA contenidoexpresion : expresion SUMA terminoexpresion : expresion RESTA terminoexpresion : expresion DIVISION terminoexpresion : expresion MULT terminoexpresion : expresion MODULO terminoexpresion : terminotermino : termino SUMA factorEspecialtermino : termino RESTA factortermino : termino MULT factortermino : termino DIVISION factortermino : termino MODULO factortermino : factortermino : ENTEROEXPRESION\n               | flotante\n               | CADENAEXPRESION\n               | list\n               | set\n               | IDfactor : ENTEROEXPRESIONfactor : flotantefactor : IDfactorEspecial : factor\n               | CADENAEXPRESION\n               | list\n               | setfactor : APAR expresion CPARfuncion : WITHINDEX\n                | GET\n                | SLICE\n                | COMPARETO\n                | GETINDEX\n                | HASHCODE\n                | CONTAINS\n                | SIZE\n                | ISEMPTY\n                | TOSTRING\n                | TOLIST\n                | PRINT\n                | PRINTLN\n                | INDICES\n    metodo : ID PUNTO ID APAR CPAR\n            | ID PUNTO ID APAR ID CPAR\n            | atributo PUNTO ID APAR CPAR\n            | atributo PUNTO ID APAR ID CPAR\n            | ID PUNTO funcion APAR CPAR\n            | ID PUNTO funcion APAR ID CPAR\n            | atributo PUNTO funcion APAR CPAR\n            | atributo PUNTO funcion APAR ID CPAR\n    atributo : ID PUNTO IDcomparador : IGUALIGUAL \n                | TRIPLEIGUAL \n                | NOIGUAL \n                | MAYOR \n                | MENOR \n                | MAYORIGUAL \n                | MENORIGUAL\n    conector : AND \n                | OR\n    compmiembro : ID\n                    | ENTEROEXPRESION\n                    | metodo\n                    | atributo\n                    | asignacion\n    condicion : compmiembro comparador compmiembro\n                | compmiembro comparador compmiembro conector compmiembro comparador compmiembro\n    control : if\n                | for\n                | while\n    cuerpo : sentencia\n                | ALLAVE sentencia CLLAVE\n    if : IF APAR condicion CPAR cuerpo\n        | IF APAR condicion CPAR cuerpo ELSE cuerpo\n    for : FOR APAR ID IN ID CPAR cuerpo\n        | FOR APAR ID DOSPUNTOS INT IN ID CPAR cuerpo\n        | FOR APAR ID IN ENTEROEXPRESION PUNTOPUNTO ENTEROEXPRESION CPAR cuerpo\n        | FOR APAR ID IN ENTEROEXPRESION UNTIL ENTEROEXPRESION CPAR cuerpo\n        | FOR APAR ID IN ENTEROEXPRESION UNTIL ENTEROEXPRESION STEP ENTEROEXPRESION CPAR cuerpo\n        | FOR APAR ID IN ENTEROEXPRESION DOWNTO ENTEROEXPRESION STEP ENTEROEXPRESION CPAR cuerpo\n        | FOR APAR ID IN ID PUNTO INDICES CPAR cuerpo\n        | FOR APAR ID IN ID PUNTO ID CPAR cuerpo\n        | FOR APAR APAR ID COMA ID CPAR IN ID PUNTO WITHINDEX APAR CPAR CPAR cuerpo\n        | FOR APAR APAR ID COMA ID CPAR IN ID CPAR cuerpo\n    while : WHILE APAR condicion CPAR cuerpo\n    '
    
_lr_action_items = {'VAL':([0,54,55,56,57,58,59,60,61,71,73,149,150,151,157,161,180,194,197,200,226,227,228,229,232,244,246,247,255,],[8,8,-90,-91,-92,-93,-94,-95,-96,8,8,8,-97,-98,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'VAR':([0,54,55,56,57,58,59,60,61,71,73,149,150,151,157,161,180,194,197,200,226,227,228,229,232,244,246,247,255,],[10,10,-90,-91,-92,-93,-94,-95,-96,10,10,10,-97,-98,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'ID':([0,8,10,20,34,37,38,42,43,44,45,46,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,131,134,135,146,147,149,150,151,153,155,156,157,159,161,180,181,194,196,197,200,201,205,225,226,227,228,229,232,244,246,247,255,],[9,35,39,53,74,94,98,53,53,53,53,53,108,-90,-91,-92,-93,-94,-95,-96,121,121,121,121,121,121,121,121,121,108,132,108,158,162,165,170,172,108,-97,-98,121,121,121,9,182,9,9,199,108,121,9,9,216,221,235,9,9,9,9,9,9,9,9,9,]),'ENTEROEXPRESION':([0,20,38,41,42,43,44,45,46,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,73,149,150,151,153,155,156,157,159,161,180,194,196,197,200,202,203,204,226,227,228,229,230,231,232,244,246,247,255,],[11,48,97,100,48,48,48,48,48,109,-90,-91,-92,-93,-94,-95,-96,119,119,119,119,119,119,119,119,119,109,109,109,-97,-98,119,119,119,11,183,11,11,109,119,11,11,218,219,220,11,11,11,11,240,241,11,11,11,11,11,]),'BOOLEANOEXPRESION':([0,38,157,161,180,197,200,226,227,228,229,232,244,246,247,255,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'CADENAEXPRESION':([0,20,38,42,43,44,45,46,62,63,64,65,66,153,155,156,157,161,180,196,197,200,226,227,228,229,232,244,246,247,255,],[14,50,14,50,50,50,50,50,116,116,116,116,116,116,116,116,14,14,14,116,14,14,14,14,14,14,14,14,14,14,14,]),'LISTOF':([0,20,38,42,43,44,45,46,62,63,64,65,66,153,155,156,157,161,180,196,197,200,226,227,228,229,232,244,246,247,255,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'SETOF':([0,20,38,42,43,44,45,46,62,63,64,65,66,153,155,156,157,161,180,196,197,200,226,227,228,229,232,244,246,247,255,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'PAIR':([0,38,93,157,161,166,167,168,169,180,197,200,208,209,226,227,228,229,232,234,244,246,247,255,],[27,27,144,27,27,144,144,144,144,27,27,27,144,144,27,27,27,27,27,144,27,27,27,27,]),'TRIPLE':([0,38,93,157,161,166,167,168,169,180,197,200,208,209,226,227,228,229,232,234,244,246,247,255,],[28,28,145,28,28,145,145,145,145,28,28,28,145,145,28,28,28,28,28,145,28,28,28,28,]),'IF':([0,157,161,180,197,200,226,227,228,229,232,244,246,247,255,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'FOR':([0,157,161,180,197,200,226,227,228,229,232,244,246,247,255,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'WHILE':([0,157,161,180,197,200,226,227,228,229,232,244,246,247,255,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'APAR':([0,20,25,26,27,28,30,31,32,38,42,43,44,45,46,62,63,64,65,66,67,68,69,70,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,94,95,153,155,156,157,161,180,196,197,200,226,227,228,229,232,244,246,247,250,255,],[20,20,62,63,64,65,71,72,73,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,131,134,135,-67,-68,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-80,146,147,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,253,20,]),'$end':([1,2,3,4,5,6,7,9,11,12,13,14,15,16,17,18,19,21,22,23,29,33,36,40,48,49,50,51,52,53,90,91,92,94,96,97,98,99,101,102,103,104,105,106,107,108,109,110,111,112,115,116,117,118,119,120,121,125,126,127,128,129,136,137,138,139,140,141,148,152,154,163,164,171,173,178,179,185,186,187,192,193,195,206,207,210,212,213,215,224,233,236,237,238,239,242,248,249,251,252,256,],[0,-1,-2,-3,-4,-5,-6,-32,-23,-24,-25,-26,-27,-28,-29,-30,-31,-106,-107,-108,-46,-52,-9,-33,-53,-54,-55,-56,-57,-58,-7,-10,-11,-89,-14,-23,-32,-8,-41,-42,-43,-44,-45,-66,-104,-99,-100,-101,-102,-103,-62,-63,-64,-65,-59,-60,-61,-47,-48,-49,-50,-51,-12,-13,-15,-16,-17,-18,-34,-35,-36,-83,-87,-81,-85,-111,-109,-123,-84,-88,-82,-86,-37,-19,-20,-105,-112,-110,-113,-38,-21,-120,-119,-115,-116,-114,-22,-122,-117,-118,-121,]),'ELSE':([2,3,4,5,6,7,9,11,12,13,14,15,16,17,18,19,21,22,23,29,33,36,40,48,49,50,51,52,53,90,91,92,94,96,97,98,99,101,102,103,104,105,106,107,108,109,110,111,112,115,116,117,118,119,120,121,125,126,127,128,129,136,137,138,139,140,141,148,152,154,163,164,171,173,178,179,185,186,187,192,193,195,206,207,210,212,213,215,224,233,236,237,238,239,242,248,249,251,252,256,],[-1,-2,-3,-4,-5,-6,-32,-23,-24,-25,-26,-27,-28,-29,-30,-31,-106,-107,-108,-46,-52,-9,-33,-53,-54,-55,-56,-57,-58,-7,-10,-11,-89,-14,-23,-32,-8,-41,-42,-43,-44,-45,-66,-104,-99,-100,-101,-102,-103,-62,-63,-64,-65,-59,-60,-61,-47,-48,-49,-50,-51,-12,-13,-15,-16,-17,-18,-34,-35,-36,-83,-87,-81,-85,197,-109,-123,-84,-88,-82,-86,-37,-19,-20,-105,-112,-110,-113,-38,-21,-120,-119,-115,-116,-114,-22,-122,-117,-118,-121,]),'CLLAVE':([2,3,4,5,6,7,9,11,12,13,14,15,16,17,18,19,21,22,23,29,33,36,40,48,49,50,51,52,53,90,91,92,94,96,97,98,99,101,102,103,104,105,106,107,108,109,110,111,112,115,116,117,118,119,120,121,125,126,127,128,129,136,137,138,139,140,141,148,152,154,163,164,171,173,178,179,185,186,187,192,193,195,198,206,207,210,212,213,215,224,233,236,237,238,239,242,248,249,251,252,256,],[-1,-2,-3,-4,-5,-6,-32,-23,-24,-25,-26,-27,-28,-29,-30,-31,-106,-107,-108,-46,-52,-9,-33,-53,-54,-55,-56,-57,-58,-7,-10,-11,-89,-14,-23,-32,-8,-41,-42,-43,-44,-45,-66,-104,-99,-100,-101,-102,-103,-62,-63,-64,-65,-59,-60,-61,-47,-48,-49,-50,-51,-12,-13,-15,-16,-17,-18,-34,-35,-36,-83,-87,-81,-85,-111,-109,-123,-84,-88,-82,-86,-37,213,-19,-20,-105,-112,-110,-113,-38,-21,-120,-119,-115,-116,-114,-22,-122,-117,-118,-121,]),'IGUALIGUAL':([2,4,7,9,11,12,13,14,15,16,17,18,19,24,29,33,36,40,48,49,50,51,52,53,90,91,92,94,96,97,98,99,101,102,103,104,105,106,108,109,110,111,112,115,116,117,118,119,120,121,125,126,127,128,129,136,137,138,139,140,141,148,152,154,163,164,171,173,174,186,187,192,193,195,206,207,224,233,248,],[-103,-101,-102,-99,-100,-24,-25,-26,-27,-28,-29,-30,-31,55,-46,-52,-9,-33,-53,-54,-55,-56,-57,-58,-7,-10,-11,-89,-14,-23,-32,-8,-41,-42,-43,-44,-45,-66,-99,-100,-101,-102,-103,-62,-63,-64,-65,-59,-60,-61,-47,-48,-49,-50,-51,-12,-13,-15,-16,-17,-18,-34,-35,-36,-83,-87,-81,-85,55,-84,-88,-82,-86,-37,-19,-20,-38,-21,-22,]),'TRIPLEIGUAL':([2,4,7,9,11,12,13,14,15,16,17,18,19,24,29,33,36,40,48,49,50,51,52,53,90,91,92,94,96,97,98,99,101,102,103,104,105,106,108,109,110,111,112,115,116,117,118,119,120,121,125,126,127,128,129,136,137,138,139,140,141,148,152,154,163,164,171,173,174,186,187,192,193,195,206,207,224,233,248,],[-103,-101,-102,-99,-100,-24,-25,-26,-27,-28,-29,-30,-31,56,-46,-52,-9,-33,-53,-54,-55,-56,-57,-58,-7,-10,-11,-89,-14,-23,-32,-8,-41,-42,-43,-44,-45,-66,-99,-100,-101,-102,-103,-62,-63,-64,-65,-59,-60,-61,-47,-48,-49,-50,-51,-12,-13,-15,-16,-17,-18,-34,-35,-36,-83,-87,-81,-85,56,-84,-88,-82,-86,-37,-19,-20,-38,-21,-22,]),'NOIGUAL':([2,4,7,9,11,12,13,14,15,16,17,18,19,24,29,33,36,40,48,49,50,51,52,53,90,91,92,94,96,97,98,99,101,102,103,104,105,106,108,109,110,111,112,115,116,117,118,119,120,121,125,126,127,128,129,136,137,138,139,140,141,148,152,154,163,164,171,173,174,186,187,192,193,195,206,207,224,233,248,],[-103,-101,-102,-99,-100,-24,-25,-26,-27,-28,-29,-30,-31,57,-46,-52,-9,-33,-53,-54,-55,-56,-57,-58,-7,-10,-11,-89,-14,-23,-32,-8,-41,-42,-43,-44,-45,-66,-99,-100,-101,-102,-103,-62,-63,-64,-65,-59,-60,-61,-47,-48,-49,-50,-51,-12,-13,-15,-16,-17,-18,-34,-35,-36,-83,-87,-81,-85,57,-84,-88,-82,-86,-37,-19,-20,-38,-21,-22,]),'MAYOR':([2,4,7,9,11,12,13,14,15,16,17,18,19,24,29,33,36,40,48,49,50,51,52,53,90,91,92,94,96,97,98,99,101,102,103,104,105,106,108,109,110,111,112,115,116,117,118,119,120,121,125,126,127,128,129,136,137,138,139,140,141,148,152,154,163,164,171,173,174,186,187,188,189,192,193,195,206,207,222,224,233,243,248,],[-103,-101,-102,-99,-100,-24,-25,-26,-27,-28,-29,-30,-31,58,-46,-52,-9,-33,-53,-54,-55,-56,-57,-58,-7,-10,-11,-89,-14,-23,-32,-8,-41,-42,-43,-44,-45,-66,-99,-100,-101,-102,-103,-62,-63,-64,-65,-59,-60,-61,-47,-48,-49,-50,-51,-12,-13,-15,-16,-17,-18,-34,-35,-36,-83,-87,-81,-85,58,-84,-88,206,207,-82,-86,-37,-19,-20,233,-38,-21,248,-22,]),'MENOR':([2,4,7,9,11,12,13,14,15,16,17,18,19,24,29,33,36,40,48,49,50,51,52,53,90,91,92,94,96,97,98,99,101,102,103,104,105,106,108,109,110,111,112,115,116,117,118,119,120,121,125,126,127,128,129,136,137,138,139,140,141,142,143,144,145,148,152,154,163,164,171,173,174,186,187,192,193,195,206,207,224,233,248,],[-103,-101,-102,-99,-100,-24,-25,-26,-27,-28,-29,-30,-31,59,-46,-52,-9,-33,-53,-54,-55,-56,-57,-58,-7,-10,-11,-89,-14,-23,-32,-8,-41,-42,-43,-44,-45,-66,-99,-100,-101,-102,-103,-62,-63,-64,-65,-59,-60,-61,-47,-48,-49,-50,-51,-12,-13,-15,-16,-17,-18,166,167,168,169,-34,-35,-36,-83,-87,-81,-85,59,-84,-88,-82,-86,-37,-19,-20,-38,-21,-22,]),'MAYORIGUAL':([2,4,7,9,11,12,13,14,15,16,17,18,19,24,29,33,36,40,48,49,50,51,52,53,90,91,92,94,96,97,98,99,101,102,103,104,105,106,108,109,110,111,112,115,116,117,118,119,120,121,125,126,127,128,129,136,137,138,139,140,141,148,152,154,163,164,171,173,174,186,187,192,193,195,206,207,224,233,248,],[-103,-101,-102,-99,-100,-24,-25,-26,-27,-28,-29,-30,-31,60,-46,-52,-9,-33,-53,-54,-55,-56,-57,-58,-7,-10,-11,-89,-14,-23,-32,-8,-41,-42,-43,-44,-45,-66,-99,-100,-101,-102,-103,-62,-63,-64,-65,-59,-60,-61,-47,-48,-49,-50,-51,-12,-13,-15,-16,-17,-18,-34,-35,-36,-83,-87,-81,-85,60,-84,-88,-82,-86,-37,-19,-20,-38,-21,-22,]),'MENORIGUAL':([2,4,7,9,11,12,13,14,15,16,17,18,19,24,29,33,36,40,48,49,50,51,52,53,90,91,92,94,96,97,98,99,101,102,103,104,105,106,108,109,110,111,112,115,116,117,118,119,120,121,125,126,127,128,129,136,137,138,139,140,141,148,152,154,163,164,171,173,174,186,187,192,193,195,206,207,224,233,248,],[-103,-101,-102,-99,-100,-24,-25,-26,-27,-28,-29,-30,-31,61,-46,-52,-9,-33,-53,-54,-55,-56,-57,-58,-7,-10,-11,-89,-14,-23,-32,-8,-41,-42,-43,-44,-45,-66,-99,-100,-101,-102,-103,-62,-63,-64,-65,-59,-60,-61,-47,-48,-49,-50,-51,-12,-13,-15,-16,-17,-18,-34,-35,-36,-83,-87,-81,-85,61,-84,-88,-82,-86,-37,-19,-20,-38,-21,-22,]),'PUNTO':([7,9,11,48,94,97,108,111,119,182,235,],[34,37,41,41,-89,41,37,34,41,201,245,]),'SUMA':([9,11,12,14,15,16,19,29,33,40,47,48,49,50,51,52,53,97,98,101,102,103,104,105,106,115,116,117,118,119,120,121,125,126,127,128,129,148,152,154,],[-58,-53,-54,-55,-56,-57,42,66,-52,-33,42,-53,-54,-55,-56,-57,-58,-53,-58,66,66,66,66,66,-66,-62,-63,-64,-65,-59,-60,-61,-47,-48,-49,-50,-51,-34,-35,-36,]),'RESTA':([9,11,12,14,15,16,19,29,33,40,47,48,49,50,51,52,53,97,98,101,102,103,104,105,106,115,116,117,118,119,120,121,125,126,127,128,129,148,152,154,],[-58,-53,-54,-55,-56,-57,43,67,-52,-33,43,-53,-54,-55,-56,-57,-58,-53,-58,67,67,67,67,67,-66,-62,-63,-64,-65,-59,-60,-61,-47,-48,-49,-50,-51,-34,-35,-36,]),'MULT':([9,11,12,14,15,16,19,29,33,40,47,48,49,50,51,52,53,97,98,101,102,103,104,105,106,115,116,117,118,119,120,121,125,126,127,128,129,148,152,154,],[-58,-53,-54,-55,-56,-57,45,68,-52,-33,45,-53,-54,-55,-56,-57,-58,-53,-58,68,68,68,68,68,-66,-62,-63,-64,-65,-59,-60,-61,-47,-48,-49,-50,-51,-34,-35,-36,]),'DIVISION':([9,11,12,14,15,16,19,29,33,40,47,48,49,50,51,52,53,97,98,101,102,103,104,105,106,115,116,117,118,119,120,121,125,126,127,128,129,148,152,154,],[-58,-53,-54,-55,-56,-57,44,69,-52,-33,44,-53,-54,-55,-56,-57,-58,-53,-58,69,69,69,69,69,-66,-62,-63,-64,-65,-59,-60,-61,-47,-48,-49,-50,-51,-34,-35,-36,]),'MODULO':([9,11,12,14,15,16,19,29,33,40,47,48,49,50,51,52,53,97,98,101,102,103,104,105,106,115,116,117,118,119,120,121,125,126,127,128,129,148,152,154,],[-58,-53,-54,-55,-56,-57,46,70,-52,-33,46,-53,-54,-55,-56,-57,-58,-53,-58,70,70,70,70,70,-66,-62,-63,-64,-65,-59,-60,-61,-47,-48,-49,-50,-51,-34,-35,-36,]),'IGUAL':([9,35,39,91,108,137,138,139,140,141,206,207,233,248,],[38,38,38,38,38,-13,-15,-16,-17,-18,-19,-20,-21,-22,]),'F':([11,48,97,100,119,],[40,40,40,148,40,]),'AND':([12,13,14,15,16,17,18,19,29,33,36,40,48,49,50,51,52,53,90,91,92,94,96,97,98,99,101,102,103,104,105,106,107,108,109,110,111,112,115,116,117,118,119,120,121,125,126,127,128,129,136,137,138,139,140,141,148,152,154,163,164,171,173,186,187,192,193,195,206,207,224,233,248,],[-24,-25,-26,-27,-28,-29,-30,-31,-46,-52,-9,-33,-53,-54,-55,-56,-57,-58,-7,-10,-11,-89,-14,-23,-32,-8,-41,-42,-43,-44,-45,-66,150,-99,-100,-101,-102,-103,-62,-63,-64,-65,-59,-60,-61,-47,-48,-49,-50,-51,-12,-13,-15,-16,-17,-18,-34,-35,-36,-83,-87,-81,-85,-84,-88,-82,-86,-37,-19,-20,-38,-21,-22,]),'OR':([12,13,14,15,16,17,18,19,29,33,36,40,48,49,50,51,52,53,90,91,92,94,96,97,98,99,101,102,103,104,105,106,107,108,109,110,111,112,115,116,117,118,119,120,121,125,126,127,128,129,136,137,138,139,140,141,148,152,154,163,164,171,173,186,187,192,193,195,206,207,224,233,248,],[-24,-25,-26,-27,-28,-29,-30,-31,-46,-52,-9,-33,-53,-54,-55,-56,-57,-58,-7,-10,-11,-89,-14,-23,-32,-8,-41,-42,-43,-44,-45,-66,151,-99,-100,-101,-102,-103,-62,-63,-64,-65,-59,-60,-61,-47,-48,-49,-50,-51,-12,-13,-15,-16,-17,-18,-34,-35,-36,-83,-87,-81,-85,-84,-88,-82,-86,-37,-19,-20,-38,-21,-22,]),'CPAR':([12,13,14,15,16,17,18,19,29,33,36,40,47,48,49,50,51,52,53,90,91,92,94,96,97,98,99,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,125,126,127,128,129,130,133,134,135,136,137,138,139,140,141,146,147,148,152,154,162,163,164,165,170,171,172,173,175,176,182,186,187,192,193,195,199,206,207,210,211,216,217,218,219,221,224,233,235,240,241,248,253,254,],[-24,-25,-26,-27,-28,-29,-30,-31,-46,-52,-9,-33,106,-53,-54,-55,-56,-57,-58,-7,-10,-11,-89,-14,-23,-32,-8,-41,-42,-43,-44,-45,-66,-104,-99,-100,-101,-102,-103,152,-39,-62,-63,-64,-65,-59,-60,-61,154,-47,-48,-49,-50,-51,157,161,163,164,-12,-13,-15,-16,-17,-18,171,173,-34,-35,-36,186,-83,-87,187,192,-81,193,-85,-40,195,200,-84,-88,-82,-86,-37,214,-19,-20,-105,224,226,227,228,229,232,-38,-21,244,246,247,-22,254,255,]),'WITHINDEX':([34,37,245,],[76,76,250,]),'GET':([34,37,],[77,77,]),'SLICE':([34,37,],[78,78,]),'COMPARETO':([34,37,],[79,79,]),'GETINDEX':([34,37,],[80,80,]),'HASHCODE':([34,37,],[81,81,]),'CONTAINS':([34,37,],[82,82,]),'SIZE':([34,37,],[83,83,]),'ISEMPTY':([34,37,],[84,84,]),'TOSTRING':([34,37,],[85,85,]),'TOLIST':([34,37,],[86,86,]),'PRINT':([34,37,],[87,87,]),'PRINTLN':([34,37,],[88,88,]),'INDICES':([34,37,201,],[89,89,217,]),'DOSPUNTOS':([35,39,132,],[93,93,160,]),'COMA':([40,106,114,115,116,117,118,119,120,121,123,124,138,139,140,141,148,152,154,158,177,190,191,206,207,223,233,248,],[-33,-66,153,-62,-63,-64,-65,-59,-60,-61,155,156,-15,-16,-17,-18,-34,-35,-36,181,196,208,209,-19,-20,234,-21,-22,]),'INT':([93,160,166,167,168,169,208,209,234,],[138,184,138,138,138,138,138,138,138,]),'FLOAT':([93,166,167,168,169,208,209,234,],[139,139,139,139,139,139,139,139,]),'BOOLEAN':([93,166,167,168,169,208,209,234,],[140,140,140,140,140,140,140,140,]),'STRING':([93,166,167,168,169,208,209,234,],[141,141,141,141,141,141,141,141,]),'LIST':([93,166,167,168,169,208,209,234,],[142,142,142,142,142,142,142,142,]),'SET':([93,166,167,168,169,208,209,234,],[143,143,143,143,143,143,143,143,]),'IN':([132,184,214,],[159,205,225,]),'ALLAVE':([157,161,197,200,226,227,228,229,232,244,246,247,255,],[180,180,180,180,180,180,180,180,180,180,180,180,180,]),'PUNTOPUNTO':([183,],[202,]),'UNTIL':([183,],[203,]),'DOWNTO':([183,],[204,]),'STEP':([219,220,],[230,231,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'sentencia':([0,157,161,180,197,200,226,227,228,229,232,244,246,247,255,],[1,179,179,198,179,179,179,179,179,179,179,179,179,179,179,]),'asignacion':([0,54,71,73,149,157,161,180,194,197,200,226,227,228,229,232,244,246,247,255,],[2,112,112,112,112,2,2,2,112,2,2,2,2,2,2,2,2,2,2,2,]),'valor':([0,38,157,161,180,197,200,226,227,228,229,232,244,246,247,255,],[3,96,3,3,3,3,3,3,3,3,3,3,3,3,3,3,]),'metodo':([0,54,71,73,149,157,161,180,194,197,200,226,227,228,229,232,244,246,247,255,],[4,110,110,110,110,4,4,4,110,4,4,4,4,4,4,4,4,4,4,4,]),'control':([0,157,161,180,197,200,226,227,228,229,232,244,246,247,255,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'condicion':([0,71,73,157,161,180,197,200,226,227,228,229,232,244,246,247,255,],[6,130,133,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'atributo':([0,54,71,73,149,157,161,180,194,197,200,226,227,228,229,232,244,246,247,255,],[7,111,111,111,111,7,7,7,111,7,7,7,7,7,7,7,7,7,7,7,]),'flotante':([0,20,38,42,43,44,45,46,62,63,64,65,66,67,68,69,70,153,155,156,157,161,180,196,197,200,226,227,228,229,232,244,246,247,255,],[12,49,12,49,49,49,49,49,120,120,120,120,120,120,120,120,120,120,120,120,12,12,12,120,12,12,12,12,12,12,12,12,12,12,12,]),'list':([0,20,38,42,43,44,45,46,62,63,64,65,66,153,155,156,157,161,180,196,197,200,226,227,228,229,232,244,246,247,255,],[15,51,15,51,51,51,51,51,117,117,117,117,117,117,117,117,15,15,15,117,15,15,15,15,15,15,15,15,15,15,15,]),'set':([0,20,38,42,43,44,45,46,62,63,64,65,66,153,155,156,157,161,180,196,197,200,226,227,228,229,232,244,246,247,255,],[16,52,16,52,52,52,52,52,118,118,118,118,118,118,118,118,16,16,16,118,16,16,16,16,16,16,16,16,16,16,16,]),'pair':([0,38,157,161,180,197,200,226,227,228,229,232,244,246,247,255,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'triple':([0,38,157,161,180,197,200,226,227,228,229,232,244,246,247,255,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'expresion':([0,20,38,157,161,180,197,200,226,227,228,229,232,244,246,247,255,],[19,47,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'if':([0,157,161,180,197,200,226,227,228,229,232,244,246,247,255,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'for':([0,157,161,180,197,200,226,227,228,229,232,244,246,247,255,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'while':([0,157,161,180,197,200,226,227,228,229,232,244,246,247,255,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'compmiembro':([0,54,71,73,149,157,161,180,194,197,200,226,227,228,229,232,244,246,247,255,],[24,107,24,24,174,24,24,24,210,24,24,24,24,24,24,24,24,24,24,24,]),'termino':([0,20,38,42,43,44,45,46,157,161,180,197,200,226,227,228,229,232,244,246,247,255,],[29,29,29,101,102,103,104,105,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'factor':([0,20,38,42,43,44,45,46,62,63,64,65,66,67,68,69,70,153,155,156,157,161,180,196,197,200,226,227,228,229,232,244,246,247,255,],[33,33,33,33,33,33,33,33,115,115,115,115,115,126,127,128,129,115,115,115,33,33,33,115,33,33,33,33,33,33,33,33,33,33,33,]),'inicializacion':([9,35,39,91,108,],[36,92,92,136,36,]),'comparador':([24,174,],[54,194,]),'funcion':([34,37,],[75,95,]),'tipoAsignacion':([35,39,],[90,99,]),'declaracion':([35,39,],[91,91,]),'contenido':([62,63,153,],[113,122,175,]),'factorEspecial':([62,63,64,65,66,153,155,156,196,],[114,114,123,124,125,114,176,177,211,]),'tipoDato':([93,166,167,168,169,208,209,234,],[137,188,189,190,191,222,223,243,]),'conector':([107,],[149,]),'cuerpo':([157,161,197,200,226,227,228,229,232,244,246,247,255,],[178,185,212,215,236,237,238,239,242,249,251,252,256,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> sentencia","S'",1,None,None,None),
  ('sentencia -> asignacion','sentencia',1,'p_sentencia','analizador_sintactico.py',9),
  ('sentencia -> valor','sentencia',1,'p_sentencia','analizador_sintactico.py',10),
  ('sentencia -> metodo','sentencia',1,'p_sentencia','analizador_sintactico.py',11),
  ('sentencia -> control','sentencia',1,'p_sentencia','analizador_sintactico.py',12),
  ('sentencia -> condicion','sentencia',1,'p_sentencia','analizador_sintactico.py',13),
  ('sentencia -> atributo','sentencia',1,'p_sentencia','analizador_sintactico.py',14),
  ('asignacion -> VAL ID tipoAsignacion','asignacion',3,'p_asignacion','analizador_sintactico.py',19),
  ('asignacion -> VAR ID tipoAsignacion','asignacion',3,'p_asignacion','analizador_sintactico.py',20),
  ('asignacion -> ID inicializacion','asignacion',2,'p_asignacion','analizador_sintactico.py',21),
  ('tipoAsignacion -> declaracion','tipoAsignacion',1,'p_tipoAsignacion','analizador_sintactico.py',26),
  ('tipoAsignacion -> inicializacion','tipoAsignacion',1,'p_tipoAsignacion','analizador_sintactico.py',27),
  ('tipoAsignacion -> declaracion inicializacion','tipoAsignacion',2,'p_tipoAsignacion','analizador_sintactico.py',28),
  ('declaracion -> DOSPUNTOS tipoDato','declaracion',2,'p_declaracion','analizador_sintactico.py',31),
  ('inicializacion -> IGUAL valor','inicializacion',2,'p_inicializacion','analizador_sintactico.py',34),
  ('tipoDato -> INT','tipoDato',1,'p_tipoDato','analizador_sintactico.py',37),
  ('tipoDato -> FLOAT','tipoDato',1,'p_tipoDato','analizador_sintactico.py',38),
  ('tipoDato -> BOOLEAN','tipoDato',1,'p_tipoDato','analizador_sintactico.py',39),
  ('tipoDato -> STRING','tipoDato',1,'p_tipoDato','analizador_sintactico.py',40),
  ('tipoDato -> LIST MENOR tipoDato MAYOR','tipoDato',4,'p_tipoDato','analizador_sintactico.py',41),
  ('tipoDato -> SET MENOR tipoDato MAYOR','tipoDato',4,'p_tipoDato','analizador_sintactico.py',42),
  ('tipoDato -> PAIR MENOR tipoDato COMA tipoDato MAYOR','tipoDato',6,'p_tipoDato','analizador_sintactico.py',43),
  ('tipoDato -> TRIPLE MENOR tipoDato COMA tipoDato COMA tipoDato MAYOR','tipoDato',8,'p_tipoDato','analizador_sintactico.py',44),
  ('valor -> ENTEROEXPRESION','valor',1,'p_valor','analizador_sintactico.py',47),
  ('valor -> flotante','valor',1,'p_valor','analizador_sintactico.py',48),
  ('valor -> BOOLEANOEXPRESION','valor',1,'p_valor','analizador_sintactico.py',49),
  ('valor -> CADENAEXPRESION','valor',1,'p_valor','analizador_sintactico.py',50),
  ('valor -> list','valor',1,'p_valor','analizador_sintactico.py',51),
  ('valor -> set','valor',1,'p_valor','analizador_sintactico.py',52),
  ('valor -> pair','valor',1,'p_valor','analizador_sintactico.py',53),
  ('valor -> triple','valor',1,'p_valor','analizador_sintactico.py',54),
  ('valor -> expresion','valor',1,'p_valor','analizador_sintactico.py',55),
  ('valor -> ID','valor',1,'p_valor','analizador_sintactico.py',56),
  ('flotante -> ENTEROEXPRESION F','flotante',2,'p_flotante','analizador_sintactico.py',59),
  ('flotante -> ENTEROEXPRESION PUNTO ENTEROEXPRESION F','flotante',4,'p_flotante','analizador_sintactico.py',60),
  ('list -> LISTOF APAR contenido CPAR','list',4,'p_list','analizador_sintactico.py',63),
  ('set -> SETOF APAR contenido CPAR','set',4,'p_set','analizador_sintactico.py',66),
  ('pair -> PAIR APAR factorEspecial COMA factorEspecial CPAR','pair',6,'p_pair','analizador_sintactico.py',69),
  ('triple -> TRIPLE APAR factorEspecial COMA factorEspecial COMA factorEspecial CPAR','triple',8,'p_triple','analizador_sintactico.py',72),
  ('contenido -> factorEspecial','contenido',1,'p_contenido','analizador_sintactico.py',75),
  ('contenido -> factorEspecial COMA contenido','contenido',3,'p_contenido','analizador_sintactico.py',76),
  ('expresion -> expresion SUMA termino','expresion',3,'p_expresion_suma','analizador_sintactico.py',79),
  ('expresion -> expresion RESTA termino','expresion',3,'p_expresion_resta','analizador_sintactico.py',82),
  ('expresion -> expresion DIVISION termino','expresion',3,'p_expresion_division','analizador_sintactico.py',85),
  ('expresion -> expresion MULT termino','expresion',3,'p_expresion_mult','analizador_sintactico.py',88),
  ('expresion -> expresion MODULO termino','expresion',3,'p_expresion_modulo','analizador_sintactico.py',91),
  ('expresion -> termino','expresion',1,'p_expresion_termino','analizador_sintactico.py',94),
  ('termino -> termino SUMA factorEspecial','termino',3,'p_termino_suma','analizador_sintactico.py',97),
  ('termino -> termino RESTA factor','termino',3,'p_termino_resta','analizador_sintactico.py',100),
  ('termino -> termino MULT factor','termino',3,'p_termino_mult','analizador_sintactico.py',103),
  ('termino -> termino DIVISION factor','termino',3,'p_termino_division','analizador_sintactico.py',106),
  ('termino -> termino MODULO factor','termino',3,'p_termino_modulo','analizador_sintactico.py',109),
  ('termino -> factor','termino',1,'p_termino_factor','analizador_sintactico.py',112),
  ('termino -> ENTEROEXPRESION','termino',1,'p_termino_factorEspecial','analizador_sintactico.py',115),
  ('termino -> flotante','termino',1,'p_termino_factorEspecial','analizador_sintactico.py',116),
  ('termino -> CADENAEXPRESION','termino',1,'p_termino_factorEspecial','analizador_sintactico.py',117),
  ('termino -> list','termino',1,'p_termino_factorEspecial','analizador_sintactico.py',118),
  ('termino -> set','termino',1,'p_termino_factorEspecial','analizador_sintactico.py',119),
  ('termino -> ID','termino',1,'p_termino_factorEspecial','analizador_sintactico.py',120),
  ('factor -> ENTEROEXPRESION','factor',1,'p_factor_num','analizador_sintactico.py',123),
  ('factor -> flotante','factor',1,'p_factor_float','analizador_sintactico.py',126),
  ('factor -> ID','factor',1,'p_factor_id','analizador_sintactico.py',129),
  ('factorEspecial -> factor','factorEspecial',1,'p_factorEspecial','analizador_sintactico.py',132),
  ('factorEspecial -> CADENAEXPRESION','factorEspecial',1,'p_factorEspecial','analizador_sintactico.py',133),
  ('factorEspecial -> list','factorEspecial',1,'p_factorEspecial','analizador_sintactico.py',134),
  ('factorEspecial -> set','factorEspecial',1,'p_factorEspecial','analizador_sintactico.py',135),
  ('factor -> APAR expresion CPAR','factor',3,'p_factor_expr','analizador_sintactico.py',138),
  ('funcion -> WITHINDEX','funcion',1,'p_funcion','analizador_sintactico.py',141),
  ('funcion -> GET','funcion',1,'p_funcion','analizador_sintactico.py',142),
  ('funcion -> SLICE','funcion',1,'p_funcion','analizador_sintactico.py',143),
  ('funcion -> COMPARETO','funcion',1,'p_funcion','analizador_sintactico.py',144),
  ('funcion -> GETINDEX','funcion',1,'p_funcion','analizador_sintactico.py',145),
  ('funcion -> HASHCODE','funcion',1,'p_funcion','analizador_sintactico.py',146),
  ('funcion -> CONTAINS','funcion',1,'p_funcion','analizador_sintactico.py',147),
  ('funcion -> SIZE','funcion',1,'p_funcion','analizador_sintactico.py',148),
  ('funcion -> ISEMPTY','funcion',1,'p_funcion','analizador_sintactico.py',149),
  ('funcion -> TOSTRING','funcion',1,'p_funcion','analizador_sintactico.py',150),
  ('funcion -> TOLIST','funcion',1,'p_funcion','analizador_sintactico.py',151),
  ('funcion -> PRINT','funcion',1,'p_funcion','analizador_sintactico.py',152),
  ('funcion -> PRINTLN','funcion',1,'p_funcion','analizador_sintactico.py',153),
  ('funcion -> INDICES','funcion',1,'p_funcion','analizador_sintactico.py',154),
  ('metodo -> ID PUNTO ID APAR CPAR','metodo',5,'p_metodo','analizador_sintactico.py',159),
  ('metodo -> ID PUNTO ID APAR ID CPAR','metodo',6,'p_metodo','analizador_sintactico.py',160),
  ('metodo -> atributo PUNTO ID APAR CPAR','metodo',5,'p_metodo','analizador_sintactico.py',161),
  ('metodo -> atributo PUNTO ID APAR ID CPAR','metodo',6,'p_metodo','analizador_sintactico.py',162),
  ('metodo -> ID PUNTO funcion APAR CPAR','metodo',5,'p_metodo','analizador_sintactico.py',163),
  ('metodo -> ID PUNTO funcion APAR ID CPAR','metodo',6,'p_metodo','analizador_sintactico.py',164),
  ('metodo -> atributo PUNTO funcion APAR CPAR','metodo',5,'p_metodo','analizador_sintactico.py',165),
  ('metodo -> atributo PUNTO funcion APAR ID CPAR','metodo',6,'p_metodo','analizador_sintactico.py',166),
  ('atributo -> ID PUNTO ID','atributo',3,'p_atributo','analizador_sintactico.py',172),
  ('comparador -> IGUALIGUAL','comparador',1,'p_comparador','analizador_sintactico.py',177),
  ('comparador -> TRIPLEIGUAL','comparador',1,'p_comparador','analizador_sintactico.py',178),
  ('comparador -> NOIGUAL','comparador',1,'p_comparador','analizador_sintactico.py',179),
  ('comparador -> MAYOR','comparador',1,'p_comparador','analizador_sintactico.py',180),
  ('comparador -> MENOR','comparador',1,'p_comparador','analizador_sintactico.py',181),
  ('comparador -> MAYORIGUAL','comparador',1,'p_comparador','analizador_sintactico.py',182),
  ('comparador -> MENORIGUAL','comparador',1,'p_comparador','analizador_sintactico.py',183),
  ('conector -> AND','conector',1,'p_conector','analizador_sintactico.py',187),
  ('conector -> OR','conector',1,'p_conector','analizador_sintactico.py',188),
  ('compmiembro -> ID','compmiembro',1,'p_compmiembro','analizador_sintactico.py',192),
  ('compmiembro -> ENTEROEXPRESION','compmiembro',1,'p_compmiembro','analizador_sintactico.py',193),
  ('compmiembro -> metodo','compmiembro',1,'p_compmiembro','analizador_sintactico.py',194),
  ('compmiembro -> atributo','compmiembro',1,'p_compmiembro','analizador_sintactico.py',195),
  ('compmiembro -> asignacion','compmiembro',1,'p_compmiembro','analizador_sintactico.py',196),
  ('condicion -> compmiembro comparador compmiembro','condicion',3,'p_condicion','analizador_sintactico.py',200),
  ('condicion -> compmiembro comparador compmiembro conector compmiembro comparador compmiembro','condicion',7,'p_condicion','analizador_sintactico.py',201),
  ('control -> if','control',1,'p_control','analizador_sintactico.py',206),
  ('control -> for','control',1,'p_control','analizador_sintactico.py',207),
  ('control -> while','control',1,'p_control','analizador_sintactico.py',208),
  ('cuerpo -> sentencia','cuerpo',1,'p_cuerpo','analizador_sintactico.py',213),
  ('cuerpo -> ALLAVE sentencia CLLAVE','cuerpo',3,'p_cuerpo','analizador_sintactico.py',214),
  ('if -> IF APAR condicion CPAR cuerpo','if',5,'p_if','analizador_sintactico.py',219),
  ('if -> IF APAR condicion CPAR cuerpo ELSE cuerpo','if',7,'p_if','analizador_sintactico.py',220),
  ('for -> FOR APAR ID IN ID CPAR cuerpo','for',7,'p_for','analizador_sintactico.py',226),
  ('for -> FOR APAR ID DOSPUNTOS INT IN ID CPAR cuerpo','for',9,'p_for','analizador_sintactico.py',227),
  ('for -> FOR APAR ID IN ENTEROEXPRESION PUNTOPUNTO ENTEROEXPRESION CPAR cuerpo','for',9,'p_for','analizador_sintactico.py',228),
  ('for -> FOR APAR ID IN ENTEROEXPRESION UNTIL ENTEROEXPRESION CPAR cuerpo','for',9,'p_for','analizador_sintactico.py',229),
  ('for -> FOR APAR ID IN ENTEROEXPRESION UNTIL ENTEROEXPRESION STEP ENTEROEXPRESION CPAR cuerpo','for',11,'p_for','analizador_sintactico.py',230),
  ('for -> FOR APAR ID IN ENTEROEXPRESION DOWNTO ENTEROEXPRESION STEP ENTEROEXPRESION CPAR cuerpo','for',11,'p_for','analizador_sintactico.py',231),
  ('for -> FOR APAR ID IN ID PUNTO INDICES CPAR cuerpo','for',9,'p_for','analizador_sintactico.py',232),
  ('for -> FOR APAR ID IN ID PUNTO ID CPAR cuerpo','for',9,'p_for','analizador_sintactico.py',233),
  ('for -> FOR APAR APAR ID COMA ID CPAR IN ID PUNTO WITHINDEX APAR CPAR CPAR cuerpo','for',15,'p_for','analizador_sintactico.py',234),
  ('for -> FOR APAR APAR ID COMA ID CPAR IN ID CPAR cuerpo','for',11,'p_for','analizador_sintactico.py',235),
  ('while -> WHILE APAR condicion CPAR cuerpo','while',5,'p_while','analizador_sintactico.py',241),
]
