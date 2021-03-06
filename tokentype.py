#Definir todos los tokens y enumerarlos

import enum
class TokenType(enum.Enum):
    #End Of File
    EOF=-1
    NEWLINE=0
    NUMBER=1
    IDENT=2
    STRING=3
    #KEYWORDS
    LABEL=101
    GOTO=102
    PRINT=103
    INPUT=104
    LET=105
    IF=106
    THEN=107
    ENDIF=108
    WHILE=109
    REPEAT=110
    ENDWHILE=111
    ##Acciones acompañadas tambien con las keyword
    DECLARA=112
    BORRAR=113
    INSERTAR=114
    ELIMINAR=115
    ##Auxiliares igual que arriba de las keywords
    COMO=116
    Y=117
    EN=118
    DE=119
    DEL=120
    LA=121
    DE_LA=122
    POR=123
    PARA=124
    ##datatype Entero, flotante, cadena, botón

    ##devices
    TV=131
    PC=132
    ESTUFA=133
    LAVADORA=134
    FOCO=135
    CALENTON=136
    AIRE_ACONDICIONADO=137
    MICROONDAS=138
    CONSOLA=139
    ##materials
    PINTURA=141
    LAMINA=142
    ARENA=143
    CEMENTO=144
    MADERA=145
    VENTANAS=146
    CERAMICA=147
    GRANITO=148
    YESO=149
    ##tools
    PINZAS=151
    SERRUCHO=152
    PALA=153
    MEZCLADORA=154
    TALADRO=155
    LLANA=156
    BROCHA=157
    MONTACARGAS=158
    AMOLADORA=159
    ##heavy machinery
    TRACTOR_BULLDOZER=161
    RETROEXCAVADORA=162
    EXCAVADORA=163
    CAMION_HORMIGONERA=164
    RODILLO_COMPACTADOR=165
    GRUA=166
    MOTONIVELADORA=167
    MANIPULADOR_TELESCOPICO=168
    CARGADOR_FRONTAL=169
    ##ground y land
    LUGAR_ROCOSO=171
    TIERRA=172
    LUGAR_MONTANOSO=173
    LUGAR_DESERTICO=174
    PLAYA=175
    SUELO=176
    PAIS=177
    REGION=178
    TERRENO=179
    ##house
    CASA_PEQUENA=181
    CASA_NORMAL=182
    CASA_GRANDE=183
    RESIDENCIA=184
    MANSION=185
    CUARTO=186
    COCINA=187
    COMEDOR=188
    RECAMARA=189
    ##house y services
    PARED=191
    INTERIOR=192
    EXTERIOR=193
    DRENAJE=194
    AGUA_POTABLE=195
    ELECTRICIDAD=196
    ##
    #OPERADORES
    EQ=201
    PLUS=202
    MINUS=203
    ASTERISC=204
    SLASH=205
    EQEQ=206
    NOTEQ=207
    LT=208
    LTEQ=209
    GT=210
    GTEQ=211
