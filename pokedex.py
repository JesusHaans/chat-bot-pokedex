#----------------------------------------------------------------------
# Base de pokedex
# La base de pokedex representa una lista de todos los pokemon.
#
# Cada pokemon es un diccionario que incluye los siguientes keys (propiedades):
# - pokemon: Nombre para identificar el pokemon
# - num: Numero del pokemon
# - tipo: Lista de posibles tipos del pokemon
# - peso: Peso del pokemon
# - altura: Altura del pokemon
# - debilidad: Lista de posibles tipos a los cuales es debil el pokemon
# - fortaleza: Lista de posibles tipos a los cuales es fuerte el pokemon
# - descripcion: Descripcion del pokemon
#----------------------------------------------------------------------
def pokedexC():
    '''
    Define la base de datos de la pokedex
    rawtype de string
    :return el pokedex a mostrar
    :rtype str 
    '''
    pokedex = [
        #////////////////////////////////////////////////Bulbasaur.
        {
            'pokemon': 'bulbasaur',
            'num': '001',
            'tipo': [
                'planta',
                'veneno'
            ],
            'peso': '6.9 kg',
            'altura': '0.7 m',
            'debilidad': [
                'fuego',
                'volador',
                'hielo',
                'psiquico'
            ],
            'fortaleza': [
                'agua',
                'planta',
                'tierra',
                'electrico'
            ],  
            'descripcion': 'Bulbasaur es un Pokémon de tipo planta/veneno introducido en la primera generación. Es uno de los Pokémon iniciales que puede elegir el jugador al comenzar la aventura en las regiones Kanto y Johto.'
        }
    ]
    return pokedex