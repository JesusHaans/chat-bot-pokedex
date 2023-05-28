from pokedex import pokemonesC

#----------------------------------------------------------------------
# Base de conocimiento
# La base de conocimiento representa una lista de todos los casos o intents.
#
# Cada caso o intent es un diccionario que incluye los siguientes keys (propiedades):
# - intent: Nombre para identificar el intent
# - regex: Lista de posibles expresiones regulares asociadas al intent, donde los parámetros se obtienen del texto parentizado en la expresión regular
# - respuesta: Lista de posibles respuestas al usuario, indicando los parámetros obtenidos con la notación %1, %2, %3, etc para cada parámetro
#----------------------------------------------------------------------
def conocimientoT():
    '''
    Define la base de conocimiento de glados

    :return El conicimiento a mostrar
    :rtype str 
    '''
    conocimiento = [
        #////////////////////////////////////////////////Bienvenida.
        {
            'intent': 'bienvenida',
            'regex': [
                r'.*hola.*',
                r'.*buen(a|o)s (dias|tardes|noches).*',
            ],
            'respuesta': [
                'Hola, soy una pokédex.',
                'Hola, soy una IA de conversación sobre pokémones.',
                'Hola, ¿En que puedo ayudarte?'
            ]
        },
        #////////////////////////////////////////////////Tipo.
        {
            'intent': 'tipo',
            'regex': [
                # r'(.*)tipo (.*)$', -----esta no jala
                r'^.*tipo de (.*)$',
                r'^.*tipo es (.*)$',
            ],
            'respuesta': [
                'El tipo de %1 es '
            ]
        },
        #////////////////////////////////////////////////Peso.
        {
            'intent': 'peso',
            'regex': [
                r'^.*peso de (.*)$',
                r'^.*peso tiene (.*)$',
            ],
            'respuesta': [
                'El peso de %1 es '
            ]
        }, 
        #////////////////////////////////////////////////Altura.
        {
            'intent': 'altura',
            'regex': [
                r'^.*altura de (.*)$',
                r'^.*altura tiene (.*)$',
            ],
            'respuesta': [
                'La altura de %1 es '
            ]
        },
        #////////////////////////////////////////////////Debilidad.
        {
            'intent': 'debilidad',
            'regex': [
                r'^.*(debilidad|debilidades) de (.*)$',
                r'^.*(debilidad|debilidades) tiene (.*)$',
            ],
            'respuesta': [
                'La debilidad de %1 es '
            ]
        }, 
        #////////////////////////////////////////////////Fortaleza.
        {
            'intent': 'fortaleza',
            'regex': [
                r'^.*(fortaleza|fortalezas) de (.*)$',
                r'^.*(fortaleza|fortalezas) tiene (.*)$',
            ],
            'respuesta': [
                'La fortaleza de %1 es '
            ]
        },
        #////////////////////////////////////////////////Descripcion.
        {
            'intent': 'descripcion',
            'regex': [
                r'^.*descripcion de (.*)$',
                r'^.*descripcion tiene (.*)$',
            ],
            'respuesta': [
                'La descripcion de %1 es '
            ]
        }, 
        #////////////////////////////////////////////////Otro.
        {
            'intent': 'otro',
            'regex': [
                r"\b(" + "|".join(pokemones) + r")\b",
                r'[0-9][0-9][0-9]'
            ],
            'respuesta': [
                ''
            ]
        },
        #////////////////////////////////////////////////Fin.
        {
            'intent': 'terminar',
            'regex': [
                r'.*salir.*',
                r'.*adios.*',
                r'.*bye.*',
                r'.*hasta luego.*'
            ],
            'respuesta': [
                ''
            ]
        },
        #////////////////////////////////////////////////Cualquier caso no contemplado.
        {
            'intent': 'desconocido',
            'regex': [
                r'.*'
            ],
            'respuesta': [
                'No te entendí ¿Puedes repetirlo por favor?',
                'Creo que no tengo información al respecto; lo siento',
                'Disculpa, no comprendí lo que dices'
            ]
        }
        #////////////////////////////////////////////////
    ]
    return conocimiento



#---------------------------------------#
#  pokemones                            #
#---------------------------------------#
pokemones = pokemonesC()