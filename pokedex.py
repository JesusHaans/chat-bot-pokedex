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
            'tipo': ['planta','veneno'],
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
        },
        #////////////////////////////////////////////////Ivysaur.
        {
            'pokemon': 'ivysaur',
            'num': '002',
            'tipo': ['planta','veneno'],
            'peso': '13 kg',
            'altura': '1 m',
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
            'descripcion': 'Ivysaur es un Pokémon de tipo planta/veneno introducido en la primera generación. Es la evolución de Bulbasaur. Es uno de los Pokémon iniciales que puede elegir el jugador al comenzar la aventura en las regiones Kanto y Johto.'
        },
        #////////////////////////////////////////////////Venusaur.
        {
            'pokemon': 'venusaur',
            'num': '003',
            'tipo': ['planta','veneno'],
            'peso': '100 kg',
            'altura': '2 m',
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
            'descripcion': 'Venusaur es un Pokémon de tipo planta/veneno introducido en la primera generación. Es la evolución de Ivysaur. Es uno de los Pokémon iniciales que puede elegir el jugador al comenzar la aventura en las regiones Kanto y Johto.'
        },
        #////////////////////////////////////////////////Charmander.
        {
            'pokemon': 'charmander',
            'num': '004',
            'tipo': ['fuego'],
            'peso': '8.5 kg',
            'altura': '0.6 m',
            'debilidad': [
                'agua',
                'tierra',
                'roca'
            ],
            'fortaleza': [
                'planta',
                'hielo',
                'bicho',
                'acero'
            ],
            'descripcion': 'Charmander es un Pokémon de tipo fuego introducido en la primera generación. Es uno de los Pokémon iniciales que puede elegir el jugador al comenzar la aventura en las regiones Kanto y Johto.'
        },
        #////////////////////////////////////////////////Charmeleon.
        {
            'pokemon': 'charmeleon',
            'num': '005',
            'tipo': ['fuego'],
            'peso': '19 kg',
            'altura': '1.1 m',
            'debilidad': [
                'agua',
                'tierra',
                'roca'
            ],
            'fortaleza': [
                'planta',
                'hielo',
                'bicho',
                'acero'
            ],
            'descripcion': 'Charmeleon es un Pokémon de tipo fuego introducido en la primera generación. Es la evolución de Charmander. Es uno de los Pokémon iniciales que puede elegir el jugador al comenzar la aventura en las regiones Kanto y Johto.'
        },
        #////////////////////////////////////////////////Charizard.
        {
            'pokemon': 'charizard',
            'num': '006',
            'tipo': ['fuego','volador'],
            'peso': '90.5 kg',
            'altura': '1.7 m',
            'debilidad': [
                'agua',
                'electrico',
                'roca'
            ],
            'fortaleza': [
                'planta',
                'bicho',
                'hielo',
                'acero'
            ],
            'descripcion': 'Charizard es un Pokémon de tipo fuego/volador introducido en la primera generación. Es la evolución de Charmeleon. Es uno de los Pokémon iniciales que puede elegir el jugador al comenzar la aventura en las regiones Kanto y Johto.'
        },
        #////////////////////////////////////////////////Squirtle.
        {
            'pokemon': 'squirtle',
            'num': '007',
            'tipo': ['agua'],
            'peso': '9 kg',
            'altura': '0.5 m',
            'debilidad': [
                'electrico',
                'planta'
            ],
            'fortaleza': [
                'fuego',
                'tierra',
                'roca'
            ],
            'descripcion': 'Squirtle es un Pokémon de tipo agua introducido en la primera generación. Es uno de los Pokémon iniciales que puede elegir el jugador al comenzar la aventura en las regiones Kanto y Johto.'
        },
        #////////////////////////////////////////////////Wartortle.
        {
            'pokemon': 'wartortle',
            'num': '008',
            'tipo': ['agua'],
            'peso': '22.5 kg',
            'altura': '1 m',
            'debilidad': [
                'electrico',
                'planta'
            ],
            'fortaleza': [
                'fuego',
                'tierra',
                'roca'
            ],
            'descripcion': 'Wartortle es un Pokémon de tipo agua introducido en la primera generación. Es la evolución de Squirtle.'
        },
        #////////////////////////////////////////////////Blastoise.
        {
            'pokemon': 'blastoise',
            'num': '009',
            'tipo': ['agua'],
            'peso': '85.5 kg',
            'altura': '1.6 m',
            'debilidad': [
                'electrico',
                'planta'
            ],
            'fortaleza': [
                'fuego',
                'tierra',
                'roca'
            ],
            'descripcion': 'Blastoise es un Pokémon de tipo agua introducido en la primera generación. Es la evolución de Wartortle.'
        },
        #////////////////////////////////////////////////Caterpie.
        {
            'pokemon': 'caterpie',
            'num': '010',
            'tipo': ['bicho'],
            'peso': '2.9 kg',
            'altura': '0.3 m',
            'debilidad': [
                'fuego',
                'volador',
                'roca'
            ],
            'fortaleza': [
                'planta',
                'psiquico'
            ],
            'descripcion': 'Caterpie es un Pokémon de tipo bicho introducido en la primera generación. Es uno de los Pokémon iniciales que puede elegir el jugador al comenzar la aventura en las regiones Kanto y Johto.'
        },
        #////////////////////////////////////////////////Metapod.
        {
            'pokemon': 'metapod',
            'num': '011',
            'tipo': ['bicho'],
            'peso': '9.9 kg',
            'altura': '0.7 m',
            'debilidad': [
                'fuego',
                'volador',
                'roca'
            ],
            'fortaleza': [
                'planta',
                'psiquico'
            ],
            'descripcion': 'Metapod es un Pokémon de tipo bicho introducido en la primera generación. Es la evolución de Caterpie.'
        },
        #////////////////////////////////////////////////Butterfree.
        {
            'pokemon': 'butterfree',
            'num': '012',
            'tipo': ['bicho','volador'],
            'peso': '32 kg',
            'altura': '1.1 m',
            'debilidad': [
                'fuego',
                'electrico',
                'hielo',
                'roca'
            ],
            'fortaleza': [
                'planta',
                'lucha',
                'bicho'
            ],
            'descripcion': 'Butterfree es un Pokémon de tipo bicho/volador introducido en la primera generación. Es la evolución de Metapod.'
        },
        #////////////////////////////////////////////////Weedle.
        {
            'pokemon': 'weedle',
            'num': '013',
            'tipo': ['bicho','veneno'],
            'peso': '3.2 kg',
            'altura': '0.3 m',
            'debilidad': [
                'fuego',
                'volador',
                'psiquico',
                'roca'
            ],
            'fortaleza': [
                'planta',
                'lucha',
                'bicho'
            ],
            'descripcion': 'Weedle es un Pokémon de tipo bicho/veneno introducido en la primera generación. De las regiones Kanto y Johto.'
        },
        #////////////////////////////////////////////////Kakuna.
        {
            'pokemon': 'kakuna',
            'num': '014',
            'tipo': ['bicho','veneno'],
            'peso': '10 kg',
            'altura': '0.6 m',
            'debilidad': [
                'fuego',
                'volador',
                'psiquico',
                'roca'
            ],
            'fortaleza': [
                'planta',
                'lucha',
                'bicho'
            ],
            'descripcion': 'Kakuna es un Pokémon de tipo bicho/veneno introducido en la primera generación. Es la evolución de Weedle.'
        },
        #////////////////////////////////////////////////Beedrill.
        {
            'pokemon': 'beedrill',
            'num': '015',
            'tipo': ['bicho','veneno'],
            'peso': '29.5 kg',
            'altura': '1 m',
            'debilidad': [
                'fuego',
                'volador',
                'psiquico',
                'roca'
            ],
            'fortaleza': [
                'planta',
                'lucha',
                'bicho'
            ],
            'descripcion': 'Beedrill es un Pokémon de tipo bicho/veneno introducido en la primera generación. Es la evolución de Kakuna.'
        },
        #////////////////////////////////////////////////Pidgey.
        {
            'pokemon': 'pidgey',
            'num': '016',
            'tipo': ['normal','volador'],
            'peso': '1.8 kg',
            'altura': '0.3 m',
            'debilidad': [
                'electrico',
                'hielo',
                'roca'
            ],
            'fortaleza': [
                'planta',
                'lucha',
                'bicho'
            ],
            'descripcion': 'Pidgey es un Pokémon de tipo normal/volador introducido en la primera generación. De las regiones Kanto y Johto.'
        },
        #////////////////////////////////////////////////Pidgeotto.
        {
            'pokemon': 'pidgeotto',
            'num': '017',
            'tipo': ['normal','volador'],
            'peso': '30 kg',
            'altura': '1.1 m',
            'debilidad': [
                'electrico',
                'hielo',
                'roca'
            ],
            'fortaleza': [
                'planta',
                'lucha',
                'bicho'
            ],
            'descripcion': 'Pidgeotto es un Pokémon de tipo normal/volador introducido en la primera generación. Es la evolución de Pidgey.'
        },
        #////////////////////////////////////////////////Pidgeot.
        {
            'pokemon': 'pidgeot',
            'num': '018',
            'tipo': ['normal','volador'],
            'peso': '39.5 kg',
            'altura': '1.5 m',
            'debilidad': [
                'electrico',
                'hielo',
                'roca'
            ],
            'fortaleza': [
                'planta',
                'lucha',
                'bicho'
            ],
            'descripcion': 'Pidgeot es un Pokémon de tipo normal/volador introducido en la primera generación. Es la evolución de Pidgeotto.'
        },
        #////////////////////////////////////////////////Rattata.
        {
            'pokemon': 'rattata',
            'num': '019',
            'tipo': ['normal'],
            'peso': '3.5 kg',
            'altura': '0.3 m',
            'debilidad': [
                'lucha'
            ],
            'fortaleza': [
                'fantasma'
            ],
            'descripcion': 'Rattata es un Pokémon de tipo normal introducido en la primera generación. De las regiones Kanto y Johto.'
        },
        #////////////////////////////////////////////////Raticate.
        {
            'pokemon': 'raticate',
            'num': '020',
            'tipo': ['normal'],
            'peso': '18.5 kg',
            'altura': '0.7 m',
            'debilidad': [
                'lucha'
            ],
            'fortaleza': [
                'fantasma'
            ],
            'descripcion': 'Raticate es un Pokémon de tipo normal introducido en la primera generación. Es la evolución de Rattata.'
        },
        #////////////////////////////////////////////////Spearow.
        {
            'pokemon': 'spearow',
            'num': '021',
            'tipo': ['normal','volador'],
            'peso': '2 kg',
            'altura': '0.3 m',
            'debilidad': [
                'electrico',
                'hielo',
                'roca'
            ],
            'fortaleza': [
                'planta',
                'lucha',
                'bicho'
            ],
            'descripcion': 'Spearow es un Pokémon de tipo normal/volador introducido en la primera generación. De las regiones Kanto y Johto.'
        },
        #////////////////////////////////////////////////Fearow.
        {
            'pokemon': 'fearow',
            'num': '022',
            'tipo': ['normal','volador'],
            'peso': '38 kg',
            'altura': '1.2 m',
            'debilidad': [
                'electrico',
                'hielo',
                'roca'
            ],
            'fortaleza': [
                'planta',
                'lucha',
                'bicho'
            ],
            'descripcion': 'Fearow es un Pokémon de tipo normal/volador introducido en la primera generación. Es la evolución de Spearow.'
        },
        #////////////////////////////////////////////////Ekans.
        {
            'pokemon': 'ekans',
            'num': '023',
            'tipo': ['veneno'],
            'peso': '6.9 kg',
            'altura': '2 m',
            'debilidad': [
                'tierra',
                'psiquico'
            ],
            'fortaleza': [
                'planta',
                'lucha',
                'bicho'
            ],
            'descripcion': 'Ekans es un Pokémon de tipo veneno introducido en la primera generación. De las regiones Kanto y Johto.'
        },
        #////////////////////////////////////////////////Arbok.
        {
            'pokemon': 'arbok',
            'num': '024',
            'tipo': ['veneno'],
            'peso': '65 kg',
            'altura': '3.5 m',
            'debilidad': [
                'tierra',
                'psiquico'
            ],
            'fortaleza': [
                'planta',
                'lucha',
                'bicho'
            ],
            'descripcion': 'Arbok es un Pokémon de tipo veneno introducido en la primera generación. Es la evolución de Ekans.'
        },
        #////////////////////////////////////////////////Pikachu.
        {
            'pokemon': 'pikachu',
            'num': '025',
            'tipo': ['electrico'],
            'peso': '6 kg',
            'altura': '0.4 m',
            'debilidad': [
                'tierra'
            ],
            'fortaleza': [
                'volador',
                'agua'
            ],
            'descripcion': 'Pikachu es un Pokémon de tipo eléctrico introducido en la primera generación. Es la forma evolucionada de Pichu.'
        },
        #////////////////////////////////////////////////Raichu.
        {
            'pokemon': 'raichu',
            'num': '026',
            'tipo': ['electrico'],
            'peso': '30 kg',
            'altura': '0.8 m',
            'debilidad': [
                'tierra'
            ],
            'fortaleza': [
                'volador',
                'agua'
            ],
            'descripcion': 'Raichu es un Pokémon de tipo eléctrico introducido en la primera generación. Es la forma evolucionada de Pikachu.'
        },
        #////////////////////////////////////////////////Sandshrew.
        {
            'pokemon': 'sandshrew',
            'num': '027',
            'tipo': ['tierra'],
            'peso': '12 kg',
            'altura': '0.6 m',
            'debilidad': [
                'agua',
                'planta',
                'hielo'
            ],
            'fortaleza': [
                'electrico',
                'veneno',
                'roca'
            ],
            'descripcion': 'Sandshrew es un Pokémon de tipo tierra introducido en la primera generación. De las regiones Kanto y Johto.'
        },
        #////////////////////////////////////////////////Sandslash.
        {
            'pokemon': 'sandslash',
            'num': '028',
            'tipo': ['tierra'],
            'peso': '29.5 kg',
            'altura': '1 m',
            'debilidad': [
                'agua',
                'planta',
                'hielo'
            ],
            'fortaleza': [
                'electrico',
                'veneno',
                'roca'
            ],
            'descripcion': 'Sandslash es un Pokémon de tipo tierra introducido en la primera generación. Es la evolución de Sandshrew.'
        },
        #////////////////////////////////////////////////Nidoran.
        {
            'pokemon': 'nidoran',
            'num': '029',
            'tipo': ['veneno'],
            'peso': '7 kg',
            'altura': '0.4 m',
            'debilidad': [
                'tierra',
                'psiquico'
            ],
            'fortaleza': [
                'planta',
                'lucha',
                'bicho'
            ],
            'descripcion': 'Nidoran es un Pokémon de tipo veneno introducido en la primera generación. De las regiones Kanto y Johto.'
        },
        #////////////////////////////////////////////////Nidorina.
        {
            'pokemon': 'nidorina',
            'num': '030',
            'tipo': ['veneno'],
            'peso': '20 kg',
            'altura': '0.8 m',
            'debilidad': [
                'tierra',
                'psiquico'
            ],
            'fortaleza': [
                'planta',
                'lucha',
                'bicho'
            ],
            'descripcion': 'Nidorina es un Pokémon de tipo veneno introducido en la primera generación. Es la evolución de Nidoran.'
        },
        #////////////////////////////////////////////////Nidoqueen.
        {
            'pokemon': 'nidoqueen',
            'num': '031',
            'tipo': ['veneno','tierra'],
            'peso': '60 kg',
            'altura': '1.3 m',
            'debilidad': [
                'agua',
                'hielo',
                'planta',
                'tierra'
            ],
            'fortaleza': [
                'veneno',
                'roca'
            ],
            'descripcion': 'Nidoqueen es un Pokémon de tipo veneno/tierra introducido en la primera generación. Es la evolución de Nidorina.'
        },
        #////////////////////////////////////////////////Nidoran.
        {
            'pokemon': 'nidoran',
            'num': '032',
            'tipo': ['veneno'],
            'peso': '9 kg',
            'altura': '0.5 m',
            'debilidad': [
                'tierra',
                'psiquico'
            ],
            'fortaleza': [
                'planta',
                'lucha',
                'bicho'
            ],
            'descripcion': 'Nidoran es un Pokémon de tipo veneno introducido en la primera generación. De las regiones Kanto y Johto.'
        },
        #////////////////////////////////////////////////Nidorino.
        {
            'pokemon': 'nidorino',
            'num': '033',
            'tipo': ['veneno'],
            'peso': '19.5 kg',
            'altura': '0.9 m',
            'debilidad': [
                'tierra',
                'psiquico'
            ],
            'fortaleza': [
                'planta',
                'lucha',
                'bicho'
            ],
            'descripcion': 'Nidorino es un Pokémon de tipo veneno introducido en la primera generación. Es la evolución de Nidoran.'
        },
        #////////////////////////////////////////////////Nidoking.
        {
            'pokemon': 'nidoking',
            'num': '034',
            'tipo': ['veneno','tierra'],
            'peso': '62 kg',
            'altura': '1.4 m',
            'debilidad': [
                'agua',
                'hielo',
                'planta',
                'tierra'
            ],
            'fortaleza': [
                'veneno',
                'roca'
            ],
            'descripcion': 'Nidoking es un Pokémon de tipo veneno/tierra introducido en la primera generación. Es la evolución de Nidorino.'
        },
        #////////////////////////////////////////////////Clefairy.
        {
            'pokemon': 'clefairy',
            'num': '035',
            'tipo': ['normal'],
            'peso': '7.5 kg',
            'altura': '0.6 m',
            'debilidad': [
                'lucha'
            ],
            'fortaleza': [
                'fantasma'
            ],
            'descripcion': 'Clefairy es un Pokémon de tipo normal introducido en la primera generación. De las regiones Kanto y Johto.'
        },
        #////////////////////////////////////////////////Clefable.
        {
            'pokemon': 'clefable',
            'num': '036',
            'tipo': ['normal'],
            'peso': '40 kg',
            'altura': '1.3 m',
            'debilidad': [
                'lucha'
            ],
            'fortaleza': [
                'fantasma'
            ],
            'descripcion': 'Clefable es un Pokémon de tipo normal introducido en la primera generación. Es la evolución de Clefairy.'
        },
        #////////////////////////////////////////////////Vulpix.
        {
            'pokemon': 'vulpix',
            'num': '037',
            'tipo': ['fuego'],
            'peso': '9.9 kg',
            'altura': '0.6 m',
            'debilidad': [
                'agua',
                'tierra',
                'roca'
            ],
            'fortaleza': [
                'planta',
                'hielo',
                'bicho',
                'acero'
            ],
            'descripcion': 'Vulpix es un Pokémon de tipo fuego introducido en la primera generación. De las regiones Kanto y Johto.'
        },
        #////////////////////////////////////////////////Ninetales.
        {
            'pokemon': 'ninetales',
            'num': '038',
            'tipo': ['fuego'],
            'peso': '19.9 kg',
            'altura': '1.1 m',
            'debilidad': [
                'agua',
                'tierra',
                'roca'
            ],
            'fortaleza': [
                'planta',
                'hielo',
                'bicho',
                'acero'
            ],
            'descripcion': 'Ninetales es un Pokémon de tipo fuego introducido en la primera generación. Es la evolución de Vulpix.'
        },
        #////////////////////////////////////////////////Jigglypuff.
        {
            'pokemon': 'jigglypuff',
            'num': '039',
            'tipo': ['normal'],
            'peso': '5.5 kg',
            'altura': '0.5 m',
            'debilidad': [
                'lucha'
            ],
            'fortaleza': [
                'fantasma'
            ],
            'descripcion': 'Jigglypuff es un Pokémon de tipo normal introducido en la primera generación. De las regiones Kanto y Johto.'
        },
        #////////////////////////////////////////////////Wigglytuff.
        {
            'pokemon': 'wigglytuff',
            'num': '040',
            'tipo': ['normal'],
            'peso': '12 kg',
            'altura': '1 m',
            'debilidad': [
                'lucha'
            ],
            'fortaleza': [
                'fantasma'
            ],
            'descripcion': 'Wigglytuff es un Pokémon de tipo normal introducido en la primera generación. Es la evolución de Jigglypuff.'
        },
        #////////////////////////////////////////////////Zubat.
        {
            'pokemon': 'zubat',
            'num': '041',
            'tipo': ['veneno','volador'],
            'peso': '7.5 kg',
            'altura': '0.8 m',
            'debilidad': [
                'electrico',
                'hielo',
                'psiquico',
                'roca'
            ],
            'fortaleza': [
                'planta',
                'lucha',
                'bicho'
            ],
            'descripcion': 'Zubat es un Pokémon de tipo veneno/volador introducido en la primera generación. De las regiones Kanto y Johto.'
        },
        #////////////////////////////////////////////////Golbat.
        {
            'pokemon': 'golbat',
            'num': '042',
            'tipo': ['veneno','volador'],
            'peso': '55 kg',
            'altura': '1.6 m',
            'debilidad': [
                'electrico',
                'hielo',
                'psiquico',
                'roca'
            ],
            'fortaleza': [
                'planta',
                'lucha',
                'bicho'
            ],
            'descripcion': 'Golbat es un Pokémon de tipo veneno/volador introducido en la primera generación. Es la evolución de Zubat.'
        },
        #////////////////////////////////////////////////Oddish.
        {
            'pokemon': 'oddish',
            'num': '043',
            'tipo': ['planta','veneno'],
            'peso': '5.4 kg',
            'altura': '0.5 m',
            'debilidad': [
                'fuego',
                'hielo',
                'volador',
                'psiquico'
            ],
            'fortaleza': [
                'agua',
                'tierra',
                'roca'
            ],
            'descripcion': 'Oddish es un Pokémon de tipo planta/veneno introducido en la primera generación. De las regiones Kanto y Johto.'
        },
        #////////////////////////////////////////////////Gloom.
        {
            'pokemon': 'gloom',
            'num': '044',
            'tipo': ['planta','veneno'],
            'peso': '8.6 kg',
            'altura': '0.8 m',
            'debilidad': [
                'fuego',
                'hielo',
                'volador',
                'psiquico'
            ],
            'fortaleza': [
                'agua',
                'tierra',
                'roca'
            ],
            'descripcion': 'Gloom es un Pokémon de tipo planta/veneno introducido en la primera generación. Es la evolución de Oddish.'
        },
        #////////////////////////////////////////////////Vileplume.
        {
            'pokemon': 'vileplume',
            'num': '045',
            'tipo': ['planta','veneno'],
            'peso': '18.6 kg',
            'altura': '1.2 m',
            'debilidad': [
                'fuego',
                'hielo',
                'volador',
                'psiquico'
            ],
            'fortaleza': [
                'agua',
                'tierra',
                'roca'
            ],
            'descripcion': 'Vileplume es un Pokémon de tipo planta/veneno introducido en la primera generación. Es la evolución de Gloom.'
        },
        #////////////////////////////////////////////////Paras.
        {
            'pokemon': 'paras',
            'num': '046',
            'tipo': ['bicho','planta'],
            'peso': '5.4 kg',
            'altura': '0.3 m',
            'debilidad': [
                'fuego',
                'hielo',
                'volador',
                'veneno',
                'roca',
                'bicho'
            ],
            'fortaleza': [
                'agua',
                'tierra',
                'lucha',
                'planta'
            ],
            'descripcion': 'Paras es un Pokémon de tipo bicho/planta introducido en la primera generación. De las regiones Kanto y Johto.'
        },
        #////////////////////////////////////////////////Parasect.
        {
            'pokemon': 'parasect',
            'num': '047',
            'tipo': ['bicho','planta'],
            'peso': '29.5 kg',
            'altura': '1 m',
            'debilidad': [
                'fuego',
                'hielo',
                'volador',
                'veneno',
                'roca',
                'bicho'
            ],
            'fortaleza': [
                'agua',
                'tierra',
                'lucha',
                'planta'
            ],
            'descripcion': 'Parasect es un Pokémon de tipo bicho/planta introducido en la primera generación. Es la evolución de Paras.'
        },
        #////////////////////////////////////////////////Venonat.
        {
            'pokemon': 'venonat',
            'num': '048',
            'tipo': ['bicho','veneno'],
            'peso': '30 kg',
            'altura': '1 m',
            'debilidad': [
                'fuego',
                'volador',
                'psiquico',
                'roca'
            ],
            'fortaleza': [
                'planta',
                'lucha',
                'bicho'
            ],
            'descripcion': 'Venonat es un Pokémon de tipo bicho/veneno introducido en la primera generación. De las regiones Kanto y Johto.'
        },
        #////////////////////////////////////////////////Venomoth.
        {
            'pokemon': 'venomoth',
            'num': '049',
            'tipo': ['bicho','veneno'],
            'peso': '12.5 kg',
            'altura': '1.5 m',
            'debilidad': [
                'fuego',
                'volador',
                'psiquico',
                'roca'
            ],
            'fortaleza': [
                'planta',
                'lucha',
                'bicho'
            ],
            'descripcion': 'Venomoth es un Pokémon de tipo bicho/veneno introducido en la primera generación. Es la evolución de Venonat.'
        },
        #////////////////////////////////////////////////Diglett.
        {
            'pokemon': 'diglett',
            'num': '050',
            'tipo': ['tierra'],
            'peso': '0.8 kg',
            'altura': '0.2 m',
            'debilidad': [
                'agua',
                'planta',
                'hielo'
            ],
            'fortaleza': [
                'electrico',
                'veneno',
                'roca'
            ],
            'descripcion': 'Diglett es un Pokémon de tipo tierra introducido en la primera generación. De las regiones Kanto y Johto.'
        },
        #////////////////////////////////////////////////Dugtrio.
        {
            'pokemon': 'dugtrio',
            'num': '051',
            'tipo': ['tierra'],
            'peso': '33.3 kg',
            'altura': '0.7 m',
            'debilidad': [
                'agua',
                'planta',
                'hielo'
            ],
            'fortaleza': [
                'electrico',
                'veneno',
                'roca'
            ],
            'descripcion': 'Dugtrio es un Pokémon de tipo tierra introducido en la primera generación. Es la evolución de Diglett.'
        },
        #////////////////////////////////////////////////Meowth.
        {
            'pokemon': 'meowth',
            'num': '052',
            'tipo': ['normal'],
            'peso': '4.2 kg',
            'altura': '0.4 m',
            'debilidad': [
                'lucha'
            ],
            'fortaleza': [
                'fantasma'
            ],
            'descripcion': 'Meowth es un Pokémon de tipo normal introducido en la primera generación. De las regiones Kanto y Alola.'
        },
        #////////////////////////////////////////////////Persian.
        {
            'pokemon': 'persian',
            'num': '053',
            'tipo': ['normal'],
            'peso': '32 kg',
            'altura': '1 m',
            'debilidad': [
                'lucha'
            ],
            'fortaleza': [
                'fantasma'
            ],
            'descripcion': 'Persian es un Pokémon de tipo normal introducido en la primera generación. Es la evolución de Meowth.'
        },
        #////////////////////////////////////////////////Psyduck.
        {
            'pokemon': 'psyduck',
            'num': '054',
            'tipo': ['agua'],
            'peso': '19.6 kg',
            'altura': '0.8 m',
            'debilidad': [
                'electrico',
                'planta'
            ],
            'fortaleza': [
                'fuego',
                'tierra',
                'roca'
            ],
            'descripcion': 'Psyduck es un Pokémon de tipo agua introducido en la primera generación. De las regiones Kanto y Johto.'
        },
        #////////////////////////////////////////////////Golduck.
        {
            'pokemon': 'golduck',
            'num': '055',
            'tipo': ['agua'],
            'peso': '76.6 kg',
            'altura': '1.7 m',
            'debilidad': [
                'electrico',
                'planta'
            ],
            'fortaleza': [
                'fuego',
                'tierra',
                'roca'
            ],
            'descripcion': 'Golduck es un Pokémon de tipo agua introducido en la primera generación. Es la evolución de Psyduck.'
        },
        #////////////////////////////////////////////////Mankey.
        {
            'pokemon': 'mankey',
            'num': '056',
            'tipo': ['lucha'],
            'peso': '28 kg',
            'altura': '0.5 m',
            'debilidad': [
                'volador',
                'psiquico',
                'hada'
            ],
            'fortaleza': [
                'normal',
                'hielo',
                'roca',
                'siniestro',
                'acero'
            ],
            'descripcion': 'Mankey es un Pokémon de tipo lucha introducido en la primera generación. De las regiones Kanto y Alola.'
        },
        #////////////////////////////////////////////////Primeape.
        {
            'pokemon': 'primeape',
            'num': '057',
            'tipo': ['lucha'],
            'peso': '32 kg',
            'altura': '1 m',
            'debilidad': [
                'volador',
                'psiquico',
                'hada'
            ],
            'fortaleza': [
                'normal',
                'hielo',
                'roca',
                'siniestro',
                'acero'
            ],
            'descripcion': 'Primeape es un Pokémon de tipo lucha introducido en la primera generación. Es la evolución de Mankey.'
        },
        #////////////////////////////////////////////////Growlithe.
        {
            'pokemon': 'growlithe',
            'num': '058',
            'tipo': ['fuego'],
            'peso': '19 kg',
            'altura': '0.7 m',
            'debilidad': [
                'agua',
                'tierra',
                'roca'
            ],
            'fortaleza': [
                'planta',
                'hielo',
                'bicho',
                'acero',
                'hada'
            ],
            'descripcion': 'Growlithe es un Pokémon de tipo fuego introducido en la primera generación. De las regiones Kanto y Johto.'
        },
        #////////////////////////////////////////////////Arcanine.
        {
            'pokemon': 'arcanine',
            'num': '059',
            'tipo': ['fuego'],
            'peso': '155 kg',
            'altura': '1.9 m',
            'debilidad': [
                'agua',
                'tierra',
                'roca'
            ],
            'fortaleza': [
                'planta',
                'hielo',
                'bicho',
                'acero',
                'hada'
            ],
            'descripcion': 'Arcanine es un Pokémon de tipo fuego introducido en la primera generación. Es la evolución de Growlithe.'
        },
        #////////////////////////////////////////////////Poliwag.
        {
            'pokemon': 'poliwag',
            'num': '060',
            'tipo': ['agua'],
            'peso': '12.4 kg',
            'altura': '0.6 m',
            'debilidad': [
                'electrico',
                'planta'
            ],
            'fortaleza': [
                'fuego',
                'tierra',
                'roca'
            ],
            'descripcion': 'Poliwag es un Pokémon de tipo agua introducido en la primera generación. De las regiones Kanto y Johto.'
        },
        #////////////////////////////////////////////////Poliwhirl.
        {
            'pokemon': 'poliwhirl',
            'num': '061',
            'tipo': ['agua'],
            'peso': '20 kg',
            'altura': '1 m',
            'debilidad': [
                'electrico',
                'planta'
            ],
            'fortaleza': [
                'fuego',
                'tierra',
                'roca'
            ],
            'descripcion': 'Poliwhirl es un Pokémon de tipo agua introducido en la primera generación. Es la evolución de Poliwag.'
        },
        #////////////////////////////////////////////////Poliwrath.
        {
            'pokemon': 'poliwrath',
            'num': '062',
            'tipo': [
                'agua',
                'lucha'
            ],
            'peso': '54 kg',
            'altura': '1.3 m',
            'debilidad': [
                'electrico',
                'volador',
                'psiquico',
                'hada',
                'planta'
            ],
            'fortaleza': [
                'fuego',
                'tierra',
                'roca',
                'normal',
                'hielo',
                'roca',
                'siniestro',
                'acero'
            ],
            'descripcion': 'Poliwrath es un Pokémon de tipo agua/lucha introducido en la primera generación. Es la evolución de Poliwhirl.'
        },
        #////////////////////////////////////////////////Abra.
        {
            'pokemon': 'abra',
            'num': '063',
            'tipo': ['psiquico'],
            'peso': '19.5 kg',
            'altura': '0.9 m',
            'debilidad': [
                'bicho',
                'fantasma',
                'oscuro'
            ],
            'fortaleza': [
                'lucha',
                'veneno'
            ],
            'descripcion': 'Abra es un Pokémon de tipo psíquico introducido en la primera generación. De las regiones Kanto y Johto.'
        },
        #////////////////////////////////////////////////Kadabra.
        {
            'pokemon': 'kadabra',
            'num': '064',
            'tipo': ['psiquico'],
            'peso': '56.5 kg',
            'altura': '1.3 m',
            'debilidad': [
                'bicho',
                'fantasma',
                'oscuro'
            ],
            'fortaleza': [
                'lucha',
                'veneno'
            ],
            'descripcion': 'Kadabra es un Pokémon de tipo psíquico introducido en la primera generación. Es la evolución de Abra.'
        },
        #////////////////////////////////////////////////Alakazam.
        {
            'pokemon': 'alakazam',
            'num': '065',
            'tipo': ['psiquico'],
            'peso': '48 kg',
            'altura': '1.5 m',
            'debilidad': [
                'bicho',
                'fantasma',
                'oscuro'
            ],
            'fortaleza': [
                'lucha',
                'veneno'
            ],
            'descripcion': 'Alakazam es un Pokémon de tipo psíquico introducido en la primera generación. Es la evolución de Kadabra.'
        },
        #////////////////////////////////////////////////Machop.
        {
            'pokemon': 'machop',
            'num': '066',
            'tipo': ['lucha'],
            'peso': '19.5 kg',
            'altura': '0.8 m',
            'debilidad': [
                'psiquico',
                'volador',
                'fairy'
            ],
            'fortaleza': [
                'normal',
                'hielo',
                'roca',
                'siniestro',
                'acero'
            ],
            'descripcion': 'Machop es un Pokémon de tipo lucha introducido en la primera generación. De las regiones Kanto y Johto.'
        },
        #////////////////////////////////////////////////Machoke.
        {
            'pokemon': 'machoke',
            'num': '067',
            'tipo': ['lucha'],
            'peso': '70.5 kg',
            'altura': '1.5 m',
            'debilidad': [
                'psiquico',
                'volador',
                'hada'
            ],
            'fortaleza': [
                'normal',
                'hielo',
                'roca',
                'siniestro',
                'acero'
            ],
            'descripcion': 'Machoke es un Pokémon de tipo lucha introducido en la primera generación. Es la evolución de Machop.'   
        },
        #////////////////////////////////////////////////Machamp.
        {
            'pokemon': 'machamp',
            'num': '068',
            'tipo': ['lucha'],
            'peso': '130 kg',
            'altura': '1.6 m',
            'debilidad': [
                'psiquico',
                'volador',
                'hada'
            ],
            'fortaleza': [
                'normal',
                'hielo',
                'roca',
                'siniestro',
                'acero'
            ],
            'descripcion': 'Machamp es un Pokémon de tipo lucha introducido en la primera generación. Es la evolución de Machoke.'
        },
        #////////////////////////////////////////////////Bellsprout.
        {
            'pokemon': 'bellsprout',
            'num': '069',
            'tipo': [
                'planta',
                'veneno'
            ],
            'peso': '4 kg',
            'altura': '0.7 m',
            'debilidad': [
                'fuego',
                'hielo',
                'volador',
                'psiquico'
            ],
            'fortaleza': [
                'agua',
                'tierra',
                'roca',
                'planta'
            ],
            'descripcion': 'Bellsprout es un Pokémon de tipo planta/veneno introducido en la primera generación. De las regiones Kanto y Johto.'
        },
        #////////////////////////////////////////////////Weepinbell.
        {
            'pokemon': 'weepinbell',
            'num': '070',
            'tipo': [
                'planta',
                'veneno'
            ],
            'peso': '6.4 kg',
            'altura': '1 m',
            'debilidad': [
                'fuego',
                'hielo',
                'volador',
                'psiquico'
            ],
            'fortaleza': [
                'agua',
                'tierra',
                'roca',
                'planta'
            ],
            'descripcion': 'Weepinbell es un Pokémon de tipo planta/veneno introducido en la primera generación. Es la evolución de Bellsprout.'
        },
        #////////////////////////////////////////////////Victreebel.
        {
            'pokemon': 'victreebel',
            'num': '071',
            'tipo': [
                'planta',
                'veneno'
            ],
            'peso': '15.5 kg',
            'altura': '1.7 m',
            'debilidad': [
                'fuego',
                'hielo',
                'volador',
                'psiquico'
            ],
            'fortaleza': [
                'agua',
                'tierra',
                'roca',
                'planta'
            ],
            'descripcion': 'Victreebel es un Pokémon de tipo planta/veneno introducido en la primera generación. Es la evolución de Weepinbell.'
        },
        #////////////////////////////////////////////////Tentacool.
        {
            'pokemon': 'tentacool',
            'num': '072',
            'tipo': [
                'agua',
                'veneno'
            ],
            'peso': '45.5 kg',
            'altura': '0.9 m',
            'debilidad': [
                'electrico',
                'tierra',
                'psiquico'
            ],
            'fortaleza': [
                'planta',
                'lucha'
            ],
            'descripcion': 'Tentacool es un Pokémon de tipo agua/veneno introducido en la primera generación. De las regiones Kanto y Johto.'
        },
        #////////////////////////////////////////////////Tentacruel.
        {
            'pokemon': 'tentacruel',
            'num': '073',
            'tipo': [
                'agua',
                'veneno'
            ],
            'peso': '55 kg',
            'altura': '1.6 m',
            'debilidad': [
                'electrico',
                'tierra',
                'psiquico'
            ],
            'fortaleza': [
                'planta',
                'lucha'
            ],
            'descripcion': 'Tentacruel es un Pokémon de tipo agua/veneno introducido en la primera generación. Es la evolución de Tentacool.'
        },
        #////////////////////////////////////////////////Geodude.
        {
            'pokemon': 'geodude',
            'num': '074',
            'tipo': [
                'roca',
                'tierra'
            ],
            'peso': '20 kg',
            'altura': '0.4 m',
            'debilidad': [
                'agua',
                'planta',
                'lucha',
                'tierra',
                'acero'
            ],
            'fortaleza': [
                'fuego',
                'electrico',
                'volador',
                'bicho'
            ],
            'descripcion': 'Geodude es un Pokémon de tipo roca/tierra introducido en la primera generación. De las regiones Kanto y Johto.'
        },
        #////////////////////////////////////////////////Graveler.
        {
            'pokemon': 'graveler',
            'num': '075',
            'tipo': [
                'roca',
                'tierra'
            ],
            'peso': '105 kg',
            'altura': '1 m',
            'debilidad': [
                'agua',
                'planta',
                'lucha',
                'tierra',
                'acero'
            ],
            'fortaleza': [
                'fuego',
                'electrico',
                'volador',
                'bicho'
            ],
            'descripcion': 'Graveler es un Pokémon de tipo roca/tierra introducido en la primera generación. Es la evolución de Geodude.'
        },
        #////////////////////////////////////////////////Golem.
        {
            'pokemon': 'golem',
            'num': '076',
            'tipo': [
                'roca',
                'tierra'
            ],
            'peso': '300 kg',
            'altura': '1.4 m',
            'debilidad': [
                'agua',
                'planta',
                'lucha',
                'tierra',
                'acero'
            ],
            'fortaleza': [
                'fuego',
                'electrico',
                'volador',
                'bicho'
            ],
            'descripcion': 'Golem es un Pokémon de tipo roca/tierra introducido en la primera generación. Es la evolución de Graveler.'
        },
        #////////////////////////////////////////////////Ponyta.
        {
            'pokemon': 'ponyta',
            'num': '077',
            'tipo': [
                'fuego'
            ],
            'peso': '30 kg',
            'altura': '1 m',
            'debilidad': [
                'agua',
                'tierra',
                'roca'
            ], 
            'fortaleza': [
                'planta',
                'hielo',
                'bicho',
                'acero'
            ],
            'descripcion': 'Ponyta es un Pokémon de tipo fuego introducido en la primera generación. De las regiones Kanto y Johto.'
        },
        #////////////////////////////////////////////////Rapidash.
        {
            'pokemon': 'rapidash',
            'num': '078',
            'tipo': [
                'fuego'
            ],
            'peso': '95 kg',
            'altura': '1.7 m',
            'debilidad': [
                'agua',
                'tierra',
                'roca'
            ],
            'fortaleza': [
                'planta',
                'hielo',
                'bicho',
                'acero'
            ],
            'descripcion': 'Rapidash es un Pokémon de tipo fuego introducido en la primera generación. Es la evolución de Ponyta.'
        },
        #////////////////////////////////////////////////Slowpoke.
        {
            'pokemon': 'slowpoke',
            'num': '079',
            'tipo': [
                'agua',
                'psiquico'
            ],
            'peso': '36 kg',
            'altura': '1.2 m',
            'debilidad': [
                'electrico',
                'bicho',
                'fantasma',
                'oscuro'
            ],
            'fortaleza': [
                'fuego',
                'agua',
                'lucha',
                'veneno',
                'tierra'
            ],
            'descripcion': 'Slowpoke es un Pokémon de tipo agua/psíquico introducido en la primera generación. De las regiones Kanto y Johto.'
        },
        #////////////////////////////////////////////////Slowbro.
        {
            'pokemon': 'slowbro',
            'num': '080',
            'tipo': [
                'agua',
                'psiquico'
            ],
            'peso': '78.5 kg',
            'altura': '1.6 m',
            'debilidad': [
                'electrico',
                'bicho',
                'fantasma',
                'oscuro'
            ],
            'fortaleza': [
                'fuego',
                'agua',
                'lucha',
                'veneno',
                'tierra'
            ],
            'descripcion': 'Slowbro es un Pokémon de tipo agua/psíquico introducido en la primera generación. Es la evolución de Slowpoke.'
        },
        #////////////////////////////////////////////////Magnemite.
        {
            'pokemon': 'magnemite',
            'num': '081',
            'tipo': [
                'electrico',
                'acero'
            ],
            'peso': '6 kg',
            'altura': '0.3 m',
            'debilidad': [
                'fuego',
                'lucha',
                'tierra'
            ],
            'fortaleza': [
                'hielo',
                'roca',
                'bicho',
                'planta',
                'psiquico',
                'dragon',
                'hada',
                'volador'
            ],
            'descripcion': 'Magnemite es un Pokémon de tipo eléctrico/acero introducido en la primera generación. De las regiones Kanto y Johto.'
        },
        #////////////////////////////////////////////////Magneton.
        {
            'pokemon': 'magneton',
            'num': '082',
            'tipo': [
                'electrico',
                'acero'
            ],
            'peso': '60 kg',
            'altura': '1 m',
            'debilidad': [
                'fuego',
                'lucha',
                'tierra'
            ],
            'fortaleza': [
                'hielo',
                'roca',
                'bicho',
                'planta',
                'psiquico',
                'dragon',
                'hada',
                'volador'
            ],
            'descripcion': 'Magneton es un Pokémon de tipo eléctrico/acero introducido en la primera generación. Es la evolución de Magnemite.'
        },
        #////////////////////////////////////////////////Farfetchd.
        {
            'pokemon': 'farfetchd',
            'num': '083',
            'tipo': [
                'normal',
                'volador'
            ],
            'peso': '15 kg',
            'altura': '0.8 m',
            'debilidad': [
                'electrico',
                'hielo',
                'roca'
            ],
            'fortaleza': [
                'planta',
                'bicho',
                'lucha',
                'tierra'
            ],
            'descripcion': 'Farfetch\'d es un Pokémon de tipo normal/volador introducido en la primera generación. De las regiones Kanto y Galar.'
        },
        #////////////////////////////////////////////////Doduo.
        {
            'pokemon': 'doduo',
            'num': '084',
            'tipo': [
                'normal',
                'volador'
            ],
            'peso': '39.2 kg',
            'altura': '1.4 m',
            'debilidad': [
                'electrico',
                'hielo',
                'roca'
            ],
            'fortaleza': [
                'planta',
                'bicho',
                'lucha',
                'tierra'
            ],
            'descripcion': 'Doduo es un Pokémon de tipo normal/volador introducido en la primera generación. De las regiones Kanto y Galar.'
        },
        #////////////////////////////////////////////////Dodrio.
        {
            'pokemon': 'dodrio',
            'num': '085',
            'tipo': [
                'normal',
                'volador'
            ],
            'peso': '85.2 kg',
            'altura': '1.8 m',
            'debilidad': [
                'electrico',
                'hielo',
                'roca'
            ],
            'fortaleza': [
                'planta',
                'bicho',
                'lucha',
                'tierra'
            ],
            'descripcion': 'Dodrio es un Pokémon de tipo normal/volador introducido en la primera generación. Es la evolución de Doduo.'
        },
        #////////////////////////////////////////////////Seel.
        {
            'pokemon': 'seel',
            'num': '086',
            'tipo': [
                'agua'
            ],
            'peso': '90 kg',
            'altura': '1.1 m',
            'debilidad': [
                'electrico',
                'planta'
            ],
            'fortaleza': [
                'fuego',
                'tierra',
                'roca'
            ],
            'descripcion': 'Seel es un Pokémon de tipo agua introducido en la primera generación. De las regiones Kanto y Alola.'
        },
        #////////////////////////////////////////////////Dewgong.
        {
            'pokemon': 'dewgong',
            'num': '087',
            'tipo': [
                'agua',
                'hielo'
            ],
            'peso': '120 kg',
            'altura': '1.7 m',
            'debilidad': [
                'electrico',
                'lucha',
                'roca',
                'planta'
            ],
            'fortaleza': [
                'fuego',
                'tierra',
                'bicho',
                'volador',
                'planta',
                'dragon'
            ],
            'descripcion': 'Dewgong es un Pokémon de tipo agua/hielo introducido en la primera generación. Es la evolución de Seel.'
        },
        #////////////////////////////////////////////////Grimer.
        {
            'pokemon': 'grimer',
            'num': '088',
            'tipo': [
                'veneno'
            ],
            'peso': '30 kg',
            'altura': '0.9 m',
            'debilidad': [
                'tierra',
                'psiquico'
            ],
            'fortaleza': [
                'planta',
                'lucha',
                'bicho',
                'hada'
            ],
            'descripcion': 'Grimer es un Pokémon de tipo veneno introducido en la primera generación. De las regiones Kanto y Alola.'
        },
        #////////////////////////////////////////////////Muk.
        {
            'pokemon': 'muk',
            'num': '089',
            'tipo': [
                'veneno'
            ],
            'peso': '30 kg',
            'altura': '1.2 m',
            'debilidad': [
                'tierra',
                'psiquico'
            ],
            'fortaleza': [
                'planta',
                'lucha',
                'bicho',
                'hada'
            ],
            'descripcion': 'Muk es un Pokémon de tipo veneno introducido en la primera generación. Es la evolución de Grimer.'
        },
        #////////////////////////////////////////////////Shellder.
        {
            'pokemon': 'shellder',
            'num': '090',
            'tipo': [
                'agua'
            ],
            'peso': '4 kg',
            'altura': '0.3 m',
            'debilidad': [
                'electrico',
                'planta'
            ],
            'fortaleza': [
                'fuego',
                'tierra',
                'roca'
            ],
            'descripcion': 'Shellder es un Pokémon de tipo agua introducido en la primera generación. De las regiones Kanto y Galar.'
        },
        #////////////////////////////////////////////////Cloyster.
        {
            'pokemon': 'cloyster',
            'num': '091',
            'tipo': [
                'agua',
                'hielo'
            ],
            'peso': '132.5 kg',
            'altura': '1.5 m',
            'debilidad': [
                'electrico',
                'lucha',
                'roca',
                'planta'
            ],
            'fortaleza': [
                'fuego',
                'tierra',
                'bicho',
                'volador',
                'planta',
                'dragon'
            ],
            'descripcion': 'Cloyster es un Pokémon de tipo agua/hielo introducido en la primera generación. Es la evolución de Shellder.'
        },
        #////////////////////////////////////////////////Gastly.
        {
            'pokemon': 'gastly',
            'num': '092',
            'tipo': [
                'fantasma',
                'veneno'
            ],
            'peso': '0.1 kg',
            'altura': '1.3 m',
            'debilidad': [
                'tierra',
                'psiquico',
                'fantasma',
                'oscuro'
            ],
            'fortaleza': [
                'planta',
                'lucha',
                'bicho',
                'hada',
                'veneno'
            ],
            'descripcion': 'Gastly es un Pokémon de tipo fantasma/veneno introducido en la primera generación. De las regiones Kanto y Galar.'
        },
        #////////////////////////////////////////////////Haunter.
        {
            'pokemon': 'haunter',
            'num': '093',
            'tipo': [
                'fantasma',
                'veneno'
            ],
            'peso': '0.1 kg',
            'altura': '1.6 m',
            'debilidad': [
                'tierra',
                'psiquico',
                'fantasma',
                'oscuro'
            ],
            'fortaleza': [
                'planta',
                'lucha',
                'bicho',
                'hada',
                'veneno'
            ],
            'descripcion': 'Haunter es un Pokémon de tipo fantasma/veneno introducido en la primera generación. Es la evolución de Gastly.'
        },
        #////////////////////////////////////////////////Gengar.
        {
            'pokemon': 'gengar',
            'num': '094',
            'tipo': [
                'fantasma',
                'veneno'
            ],
            'peso': '40.5 kg',
            'altura': '1.5 m',
            'debilidad': [
                'tierra',
                'psiquico',
                'fantasma',
                'oscuro'
            ],
            'fortaleza': [
                'planta',
                'lucha',
                'bicho',
                'hada',
                'veneno'
            ],
            'descripcion': 'Gengar es un Pokémon de tipo fantasma/veneno introducido en la primera generación. Es la evolución de Haunter.'
        },
        #////////////////////////////////////////////////Onix.
        {
            'pokemon': 'onix',
            'num': '095',
            'tipo': [
                'roca',
                'tierra'
            ],
            'peso': '210 kg',
            'altura': '8.8 m',
            'debilidad': [
                'agua',
                'planta',
                'lucha',
                'tierra',
                'acero'
            ],
            'fortaleza': [
                'fuego',
                'volador',
                'bicho',
                'veneno',
                'roca'
            ],
            'descripcion': 'Onix es un Pokémon de tipo roca/tierra introducido en la primera generación. De las regiones Kanto y Galar.'
        },
        #////////////////////////////////////////////////Drowzee.
        {
            'pokemon': 'drowzee',
            'num': '096',
            'tipo': [
                'psiquico'
            ],
            'peso': '32.4 kg',
            'altura': '1 m',
            'debilidad': [
                'bicho',
                'oscuro',
                'fantasma'
            ],
            'fortaleza': [
                'lucha',
                'psiquico'
            ],
            'descripcion': 'Drowzee es un Pokémon de tipo psíquico introducido en la primera generación. De las regiones Kanto y Galar.'
        },
        #////////////////////////////////////////////////Hypno.
        {
            'pokemon': 'hypno',
            'num': '097',
            'tipo': [
                'psiquico'
            ],
            'peso': '75.6 kg',
            'altura': '1.6 m',
            'debilidad': [
                'bicho',
                'oscuro',
                'fantasma'
            ],
            'fortaleza': [
                'lucha',
                'psiquico'
            ],
            'descripcion': 'Hypno es un Pokémon de tipo psíquico introducido en la primera generación. Es la evolución de Drowzee.'
        },
        #////////////////////////////////////////////////Krabby.
        {
            'pokemon': 'krabby',
            'num': '098',
            'tipo': [
                'agua'
            ],
            'peso': '6.5 kg',
            'altura': '0.4 m',
            'debilidad': [
                'electrico',
                'planta'
            ],
            'fortaleza': [
                'fuego',
                'tierra',
                'roca'
            ],
            'descripcion': 'Krabby es un Pokémon de tipo agua introducido en la primera generación. De las regiones Kanto y Galar.'
        },
        #////////////////////////////////////////////////Kingler.
        {
            'pokemon': 'kingler',
            'num': '099',
            'tipo': [
                'agua'
            ],
            'peso': '60 kg',
            'altura': '1.3 m',
            'debilidad': [
                'electrico',
                'planta'
            ],
            'fortaleza': [
                'fuego',
                'tierra',
                'roca'
            ],
            'descripcion': 'Kingler es un Pokémon de tipo agua introducido en la primera generación. Es la evolución de Krabby.'
        },
        #////////////////////////////////////////////////Voltorb.
        {
            'pokemon': 'voltorb',
            'num': '100',
            'tipo': [
                'electrico'
            ],
            'peso': '10.4 kg',
            'altura': '0.5 m',
            'debilidad': [
                'tierra'
            ],
            'fortaleza': [
                'agua',
                'volador',
                'acero'
            ],
            'descripcion': 'Voltorb es un Pokémon de tipo eléctrico introducido en la primera generación. De las regiones Kanto y Galar.'
        },
        #////////////////////////////////////////////////Electrode.
        {
            'pokemon': 'electrode',
            'num': '101',
            'tipo': [
                'electrico'
            ],
            'peso': '66.6 kg',
            'altura': '1.2 m',
            'debilidad': [
                'tierra'
            ],
            'fortaleza': [
                'agua',
                'volador',
                'acero'
            ],
            'descripcion': 'Electrode es un Pokémon de tipo eléctrico introducido en la primera generación. Es la evolución de Voltorb.'
        },
        #////////////////////////////////////////////////Exeggcute.
        {
            'pokemon': 'exeggcute',
            'num': '102',
            'tipo': [
                'planta',
                'psiquico'
            ],
            'peso': '2.5 kg',
            'altura': '0.4 m',
            'debilidad': [
                'fuego',
                'hielo',
                'veneno',
                'volador',
                'bicho',
                'fantasma',
                'oscuro'
            ],  
            'fortaleza': [
                'agua',
                'tierra',
                'lucha',
                'planta',
                'electrico',
                'psiquico'
            ],
            'descripcion': 'Exeggcute es un Pokémon de tipo planta/psíquico introducido en la primera generación. De las regiones Kanto y Galar.'
        },
        #////////////////////////////////////////////////Exeggutor.
        {
            'pokemon': 'exeggutor',
            'num': '103',
            'tipo': [
                'planta',
                'psiquico'
            ],
            'peso': '120 kg',
            'altura': '2 m',
            'debilidad': [
                'fuego',
                'hielo',
                'veneno',
                'volador',
                'bicho',
                'fantasma',
                'oscuro'
            ],
            'fortaleza': [
                'agua',
                'tierra',
                'lucha',
                'planta',
                'electrico',
                'psiquico'
            ],
            'descripcion': 'Exeggutor es un Pokémon de tipo planta/psíquico introducido en la primera generación. Es la evolución de Exeggcute.'
        },
        #////////////////////////////////////////////////Cubone.
        {
            'pokemon': 'cubone',
            'num': '104',
            'tipo': [
                'tierra'
            ],
            'peso': '6.5 kg',
            'altura': '0.4 m',
            'debilidad': [
                'agua',
                'planta',
                'hielo'
            ],
            'fortaleza': [
                'fuego',
                'electrico',
                'veneno',
                'roca'
            ],
            'descripcion': 'Cubone es un Pokémon de tipo tierra introducido en la primera generación. De las regiones Kanto y Alola.'
        },
        #////////////////////////////////////////////////Marowak.
        {
            'pokemon': 'marowak',
            'num': '105',
            'tipo': [
                'tierra'
            ],
            'peso': '45 kg',
            'altura': '1 m',
            'debilidad': [
                'agua',
                'planta',
                'hielo'
            ],
            'fortaleza': [
                'fuego',
                'electrico',
                'veneno',
                'roca'
            ],
            'descripcion': 'Marowak es un Pokémon de tipo tierra introducido en la primera generación. Es la evolución de Cubone.'
        },
        #////////////////////////////////////////////////Hitmonlee.
        {
            'pokemon': 'hitmonlee',
            'num': '106',
            'tipo': [
                'lucha'
            ],
            'peso': '49.8 kg',
            'altura': '1.5 m',
            'debilidad': [
                'volador',
                'psiquico',
                'hadap'
            ],
            'fortaleza': [
                'normal',
                'hielo',
                'roca',
                'oscuro',
                'acero'
            ],
            'descripcion': 'Hitmonlee es un Pokémon de tipo lucha introducido en la primera generación. Es uno de los dos posibles resultados de la evolución de Tyrogue.'
        },
        #////////////////////////////////////////////////Hitmonchan.
        {
            'pokemon': 'hitmonchan',
            'num': '107',
            'tipo': [
                'lucha'
            ],
            'peso': '50.2 kg',
            'altura': '1.4 m',
            'debilidad': [
                'volador',
                'psiquico',
                'hadap'
            ],
            'fortaleza': [
                'normal',
                'hielo',
                'roca',
                'oscuro',
                'acero'
            ],
            'descripcion': 'Hitmonchan es un Pokémon de tipo lucha introducido en la primera generación. Es uno de los dos posibles resultados de la evolución de Tyrogue.'
        },
        #////////////////////////////////////////////////Lickitung.
        {
            'pokemon': 'lickitung',
            'num': '108',
            'tipo': [
                'normal'
            ],
            'peso': '65.5 kg',
            'altura': '1.2 m',
            'debilidad': [
                'lucha'
            ],
            'fortaleza': [
                'fantasma'
            ],
            'descripcion': 'Lickitung es un Pokémon de tipo normal introducido en la primera generación. De las regiones Kanto y Galar.'
        },
        #////////////////////////////////////////////////Koffing.
        {
            'pokemon': 'koffing',
            'num': '109',
            'tipo': [
                'veneno'
            ],
            'peso': '1 kg',
            'altura': '0.6 m',
            'debilidad': [
                'tierra',
                'psiquico'
            ],
            'fortaleza': [
                'planta',
                'lucha',
                'bicho',
                'hada'
            ],
            'descripcion': 'Koffing es un Pokémon de tipo veneno introducido en la primera generación. De las regiones Kanto y Galar.'
        },
        #////////////////////////////////////////////////Weezing.
        {
            'pokemon': 'weezing',
            'num': '110',
            'tipo': [
                'veneno'
            ],
            'peso': '9.5 kg',
            'altura': '1.2 m',
            'debilidad': [
                'tierra',
                'psiquico'
            ],
            'fortaleza': [
                'planta',
                'lucha',
                'bicho',
                'hada'
            ],
            'descripcion': 'Weezing es un Pokémon de tipo veneno introducido en la primera generación. Es la evolución de Koffing.'
        },
        #////////////////////////////////////////////////Rhyhorn.
        {
            'pokemon': 'rhyhorn',
            'num': '111',
            'tipo': [
                'tierra',
                'roca'
            ],
            'peso': '115 kg',
            'altura': '1 m',
            'debilidad': [
                'agua',
                'planta',
                'hielo',
                'lucha',
                'tierra'
            ],
            'fortaleza': [
                'fuego',
                'electrico',
                'volador',
                'bicho',
                'normal',
                'veneno'
            ],
            'descripcion': 'Rhyhorn es un Pokémon de tipo tierra/roca introducido en la primera generación. Es la evolución de Rhydon.'
        },
        #////////////////////////////////////////////////Rhydon.
        {
            'pokemon': 'rhydon',
            'num': '112',
            'tipo': [
                'tierra',
                'roca'
            ],
            'peso': '120 kg',
            'altura': '1.9 m',
            'debilidad': [
                'agua',
                'planta',
                'hielo',
                'lucha',
                'tierra'
            ],
            'fortaleza': [
                'fuego',
                'electrico',
                'volador',
                'bicho',
                'normal',
                'veneno'
            ],
            'descripcion': 'Rhydon es un Pokémon de tipo tierra/roca introducido en la primera generación. Es la evolución de Rhyhorn.'
        },
        #////////////////////////////////////////////////Chansey.
        {
            'pokemon': 'chansey',
            'num': '113',
            'tipo': [
                'normal'
            ],
            'peso': '34.6 kg',
            'altura': '1.1 m',
            'debilidad': [
                'lucha'
            ],
            'fortaleza': [
                'fantasma'
            ],
            'descripcion': 'Chansey es un Pokémon de tipo normal introducido en la primera generación. Es la evolución de Happiny.'
        },
        #////////////////////////////////////////////////Tangela.
        {
            'pokemon': 'tangela',
            'num': '114',
            'tipo': [
                'planta'
            ],
            'peso': '35 kg',
            'altura': '1 m',
            'debilidad': [
                'fuego',
                'hielo',
                'veneno',
                'volador',
                'bicho'
            ],
            'fortaleza': [
                'agua',
                'tierra',
                'electrico',
                'planta'
            ],
            'descripcion': 'Tangela es un Pokémon de tipo planta introducido en la primera generación. Es la evolución de Tangrowth.'
        },
        #////////////////////////////////////////////////Kangaskhan.
        {
            'pokemon': 'kangaskhan',
            'num': '115',
            'tipo': [
                'normal'
            ],
            'peso': '80 kg',
            'altura': '2.2 m',
            'debilidad': [
                'lucha'
            ],
            'fortaleza': [
                'fantasma'
            ],
            'descripcion': 'Kangaskhan es un Pokémon de tipo normal introducido en la primera generación. Es la evolución de Cubone.'
        },
        #////////////////////////////////////////////////Horsea.
        {
            'pokemon': 'horsea',
            'num': '116',
            'tipo': [
                'agua'
            ],
            'peso': '8 kg',
            'altura': '0.4 m',
            'debilidad': [
                'electrico',
                'planta'
            ],
            'fortaleza': [
                'fuego',
                'agua',
                'hielo',
                'tierra'
            ],
            'descripcion': 'Horsea es un Pokémon de tipo agua introducido en la primera generación. Es la evolución de Seadra.'
        },
        #////////////////////////////////////////////////Seadra.
        {
            'pokemon': 'seadra',
            'num': '117',
            'tipo': [
                'agua'
            ],
            'peso': '25 kg',
            'altura': '1.2 m',
            'debilidad': [
                'electrico',
                'planta'
            ],
            'fortaleza': [
                'fuego',
                'agua',
                'hielo',
                'tierra'
            ],
            'descripcion': 'Seadra es un Pokémon de tipo agua introducido en la primera generación. Es la evolución de Horsea.'
        },
        #////////////////////////////////////////////////Goldeen.
        {
            'pokemon': 'goldeen',
            'num': '118',
            'tipo': [
                'agua'
            ],
            'peso': '15 kg',
            'altura': '0.6 m',
            'debilidad': [
                'electrico',
                'planta'
            ],
            'fortaleza': [
                'fuego',
                'agua',
                'hielo',
                'tierra'
            ],
            'descripcion': 'Goldeen es un Pokémon de tipo agua introducido en la primera generación.'
        },
        #////////////////////////////////////////////////Seaking.
        {
            'pokemon': 'seaking',
            'num': '119',
            'tipo': [
                'agua'
            ],
            'peso': '39 kg',
            'altura': '1.3 m',
            'debilidad': [
                'electrico',
                'planta'
            ],
            'fortaleza': [
                'fuego',
                'agua',
                'hielo',
                'tierra'
            ],
            'descripcion': 'Seaking es un Pokémon de tipo agua introducido en la primera generación. Es la evolución de Goldeen.'
        },
        #////////////////////////////////////////////////Staryu.
        {
            'pokemon': 'staryu',
            'num': '120',
            'tipo': [
                'agua'
            ],
            'peso': '34.5 kg',
            'altura': '0.8 m',
            'debilidad': [
                'electrico',
                'planta'
            ],
            'fortaleza': [
                'fuego',
                'agua',
                'hielo',
                'tierra'
            ],
            'descripcion': 'Staryu es un Pokémon de tipo agua introducido en la primera generación.'
        },
        #////////////////////////////////////////////////Starmie.
        {
            'pokemon': 'starmie',
            'num': '121',
            'tipo': [
                'agua',
                'psiquico'
            ],
            'peso': '80 kg',
            'altura': '1.1 m',
            'debilidad': [
                'fantasma',
                'bicho',
                'electrico',
                'hielo',
                'planta'
            ],
            'fortaleza': [
                'lucha',
                'veneno',
                'fuego',
                'agua',
                'tierra'
            ],
            'descripcion': 'Starmie es un Pokémon de tipo agua/psíquico introducido en la primera generación. Es la evolución de Staryu.'
        },
        #////////////////////////////////////////////////Mr. Mime.
        {
            'pokemon': 'mr. mime',
            'num': '122',
            'tipo': [
                'psiquico',
                'hada'
            ],
            'peso': '54.5 kg',
            'altura': '1.3 m',
            'debilidad': [
                'acero',
                'veneno'
            ],
            'fortaleza': [
                'lucha',
                'psiquico',
                'dragon'
            ],
            'descripcion': 'Mr. Mime es un Pokémon de tipo psíquico/hada introducido en la primera generación.'
        },
        #////////////////////////////////////////////////Scyther.
        {
            'pokemon': 'scyther',
            'num': '123',
            'tipo': [
                'bicho',
                'volador'
            ],
            'peso': '56 kg',
            'altura': '1.5 m',
            'debilidad': [
                'roca',
                'electrico',
                'hielo'
            ],
            'fortaleza': [
                'lucha',
                'bicho',
                'planta'
            ],
            'descripcion': 'Scyther es un Pokémon de tipo bicho/volador introducido en la primera generación.'
        },
        #////////////////////////////////////////////////Jynx.
        {
            'pokemon': 'jynx',
            'num': '124',
            'tipo': [
                'hielo',
                'psiquico'
            ],
            'peso': '40.6 kg',
            'altura': '1.4 m',
            'debilidad': [
                'bicho',
                'fantasma',
                'acero',
                'fuego',
                'roca'
            ],
            'fortaleza': [
                'lucha',
                'tierra',
                'planta',
                'dragon'
            ],
            'descripcion': 'Jynx es un Pokémon de tipo hielo/psíquico introducido en la primera generación.'
        },
        #////////////////////////////////////////////////Electabuzz.
        {
            'pokemon': 'electabuzz',
            'num': '125',
            'tipo': [
                'electrico'
            ],
            'peso': '30 kg',
            'altura': '1.1 m',
            'debilidad': [
                'tierra'
            ],
            'fortaleza': [
                'volador',
                'acero',
                'electrico'
            ],
            'descripcion': 'Electabuzz es un Pokémon de tipo eléctrico introducido en la primera generación.'
        },
        #////////////////////////////////////////////////Magmar.
        {
            'pokemon': 'magmar',
            'num': '126',
            'tipo': [
                'fuego'
            ],
            'peso': '44.5 kg',
            'altura': '1.3 m',
            'debilidad': [
                'tierra',
                'roca',
                'agua'
            ],
            'fortaleza': [
                'bicho',
                'planta',
                'hielo',
                'acero'
            ],
            'descripcion': 'Magmar es un Pokémon de tipo fuego introducido en la primera generación.'
        },
        #////////////////////////////////////////////////Pinsir.
        {
            'pokemon': 'pinsir',
            'num': '127',
            'tipo': [
                'bicho'
            ],
            'peso': '55 kg',
            'altura': '1.5 m',
            'debilidad': [
                'fuego',
                'volador',
                'roca'
            ],
            'fortaleza': [
                'lucha',
                'bicho',
                'planta'
            ],
            'descripcion': 'Pinsir es un Pokémon de tipo bicho introducido en la primera generación.'
        },
        #////////////////////////////////////////////////Tauros.
        {
            'pokemon': 'tauros',
            'num': '128',
            'tipo': [
                'normal'
            ],
            'peso': '88.4 kg',
            'altura': '1.4 m',
            'debilidad': [
                'lucha'
            ],
            'fortaleza': [
                'fantasma'
            ],
            'descripcion': 'Tauros es un Pokémon de tipo normal introducido en la primera generación.'
        },
        #////////////////////////////////////////////////Magikarp.
        {
            'pokemon': 'magikarp',
            'num': '129',
            'tipo': [
                'agua'
            ],
            'peso': '10 kg',
            'altura': '0.9 m',
            'debilidad': [
                'electrico',
                'planta'
            ],
            'fortaleza': [
                'fuego',
                'tierra',
                'roca'
            ],
            'descripcion': 'Magikarp es un Pokémon de tipo agua introducido en la primera generación.'
        },
        #////////////////////////////////////////////////Gyarados.
        {
            'pokemon': 'gyarados',
            'num': '130',
            'tipo': [
                'agua',
                'volador'
            ],
            'peso': '235 kg',
            'altura': '6.5 m',
            'debilidad': [
                'electrico',
                'roca'
            ],
            'fortaleza': [
                'fuego',
                'tierra',
                'lucha',
                'bicho',
                'planta'
            ],
            'descripcion': 'Gyarados es un Pokémon de tipo agua/volador introducido en la primera generación. Es la evolución de Magikarp.'
        },
        #////////////////////////////////////////////////Lapras.
        {
            'pokemon': 'lapras',
            'num': '131',
            'tipo': [
                'agua',
                'hielo'
            ],
            'peso': '220 kg',
            'altura': '2.5 m',
            'debilidad': [
                'electrico',
                'lucha',
                'roca',
                'planta'
            ],
            'fortaleza': [
                'fuego',
                'tierra',
                'agua',
                'hielo'
            ],
            'descripcion': 'Lapras es un Pokémon de tipo agua/hielo introducido en la primera generación.'
        },
        #////////////////////////////////////////////////Ditto.
        {
            'pokemon': 'ditto',
            'num': '132',
            'tipo': [
                'normal'
            ],
            'peso': '4 kg',
            'altura': '0.3 m',
            'debilidad': [
                'lucha'
            ],
            'fortaleza': [
                'fantasma'
            ],
            'descripcion': 'Ditto es un Pokémon de tipo normal introducido en la primera generación.'
        },
        #////////////////////////////////////////////////Eevee.
        {
            'pokemon': 'eevee',
            'num': '133',
            'tipo': [
                'normal'
            ],
            'peso': '6.5 kg',
            'altura': '0.3 m',
            'debilidad': [
                'lucha'
            ],
            'fortaleza': [
                'fantasma'
            ],
            'descripcion': 'Eevee es un Pokémon de tipo normal introducido en la primera generación.'
        },
        #////////////////////////////////////////////////Vaporeon.
        {
            'pokemon': 'vaporeon',
            'num': '134',
            'tipo': [
                'agua'
            ],
            'peso': '29 kg',
            'altura': '1 m',
            'debilidad': [
                'electrico',
                'planta'
            ],
            'fortaleza': [
                'fuego',
                'tierra',
                'roca'
            ],
            'descripcion': 'Vaporeon es un Pokémon de tipo agua introducido en la primera generación. Es una de las evoluciones de Eevee. Algunos dicen que es el pokémon más compatible con los humanos 7u7.'
        },
        #////////////////////////////////////////////////Jolteon.
        {
            'pokemon': 'jolteon',
            'num': '135',
            'tipo': [
                'electrico'
            ],
            'peso': '24.5 kg',
            'altura': '0.8 m',
            'debilidad': [
                'tierra'
            ],
            'fortaleza': [
                'agua',
                'volador'
            ],
            'descripcion': 'Jolteon es un Pokémon de tipo eléctrico introducido en la primera generación. Es una de las evoluciones de Eevee.'
        },
        #////////////////////////////////////////////////Flareon.
        {
            'pokemon': 'flareon',
            'num': '136',
            'tipo': [
                'fuego'
            ],
            'peso': '25 kg',
            'altura': '0.9 m',
            'debilidad': [
                'agua',
                'tierra',
                'roca'
            ],
            'fortaleza': [
                'bicho',
                'planta',
                'hielo',
                'acero'
            ],
            'descripcion': 'Flareon es un Pokémon de tipo fuego introducido en la primera generación. Es una de las evoluciones de Eevee.'
        },
        #////////////////////////////////////////////////Porygon.
        {
            'pokemon': 'porygon',
            'num': '137',
            'tipo': [
                'normal'
            ],
            'peso': '36.5 kg',
            'altura': '0.8 m',
            'debilidad': [
                'lucha'
            ],
            'fortaleza': [
                'fantasma'
            ],
            'descripcion': 'Porygon es un Pokémon de tipo normal introducido en la primera generación.'
        },
        #////////////////////////////////////////////////Omanyte.
        {
            'pokemon': 'omanyte',
            'num': '138',
            'tipo': [
                'roca',
                'agua'
            ],
            'peso': '7.5 kg',
            'altura': '0.4 m',
            'debilidad': [
                'electrico',
                'lucha',
                'planta',
                'tierra',
                'bicho'
            ],
            'fortaleza': [
                'fuego',
                'hielo',
                'volador',
                'normal',
                'fuego',
                'veneno',
                'volador'
            ],
            'descripcion': 'Omanyte es un Pokémon de tipo roca/agua introducido en la primera generación. Es uno de los fósiles regenerados a partir de un Helix Fossil.'
        },
        #////////////////////////////////////////////////Omastar.
        {
            'pokemon': 'omastar',
            'num': '139',
            'tipo': [
                'roca',
                'agua'
            ],
            'peso': '35 kg',
            'altura': '1 m',
            'debilidad': [
                'electrico',
                'lucha',
                'planta',
                'tierra',
                'bicho'
            ],
            'fortaleza': [
                'fuego',
                'hielo',
                'volador',
                'normal',
                'fuego',
                'veneno',
                'volador'
            ],
            'descripcion': 'Omastar es un Pokémon de tipo roca/agua introducido en la primera generación. Es uno de los fósiles regenerados a partir de un Helix Fossil.'
        },
        #////////////////////////////////////////////////Kabuto.
        {
            'pokemon': 'kabuto',
            'num': '140',
            'tipo': [
                'roca',
                'agua'
            ],
            'peso': '11.5 kg',
            'altura': '0.5 m',
            'debilidad': [
                'electrico',
                'lucha',
                'planta',
                'tierra',
                'bicho'
            ],
            'fortaleza': [
                'fuego',
                'hielo',
                'volador',
                'normal',
                'fuego',
                'veneno',
                'volador'
            ],
            'descripcion': 'Kabuto es un Pokémon de tipo roca/agua introducido en la primera generación. Es uno de los fósiles regenerados a partir de un Dome Fossil.'
        },
        #////////////////////////////////////////////////Kabutops.
        {
            'pokemon': 'kabutops',
            'num': '141',
            'tipo': [
                'roca',
                'agua'
            ],
            'peso': '40.5 kg',
            'altura': '1.3 m',
            'debilidad': [
                'electrico',
                'lucha',
                'planta',
                'tierra',
                'bicho'
            ],
            'fortaleza': [
                'fuego',
                'hielo',
                'volador',
                'normal',
                'fuego',
                'veneno',
                'volador'
            ],
            'descripcion': 'Kabutops es un Pokémon de tipo roca/agua introducido en la primera generación. Es uno de los fósiles regenerados a partir de un Dome Fossil.'
        },
        #////////////////////////////////////////////////Aerodactyl.
        {
            'pokemon': 'aerodactyl',
            'num': '142',
            'tipo': [
                'roca',
                'volador'
            ],
            'peso': '59 kg',
            'altura': '1.8 m',
            'debilidad': [
                'electrico',
                'hielo',
                'roca',
                'acero',
                'agua'
            ],
            'fortaleza': [
                'bicho',
                'planta',
                'lucha',
                'volador'
            ],
            'descripcion': 'Aerodactyl es un Pokémon de tipo roca/volador introducido en la primera generación. Es uno de los fósiles regenerados a partir de un Old Amber.'
        },
        #////////////////////////////////////////////////Snorlax.
        {
            'pokemon': 'snorlax',
            'num': '143',
            'tipo': [
                'normal'
            ],
            'peso': '460 kg',
            'altura': '2.1 m',
            'debilidad': [
                'lucha'
            ],
            'fortaleza': [
                'fantasma'
            ],
            'descripcion': 'Snorlax es un Pokémon de tipo normal introducido en la primera generación. Es la evolución de Munchlax.'
        },
        #////////////////////////////////////////////////Articuno.
        {
            'pokemon': 'articuno',
            'num': '144',
            'tipo': [
                'hielo',
                'volador'
            ],
            'peso': '55.4 kg',
            'altura': '1.7 m',
            'debilidad': [
                'electrico',
                'fuego',
                'roca',
                'acero'
            ],
            'fortaleza': [
                'bicho',
                'planta',
                'lucha',
                'volador'
            ],
            'descripcion': 'Articuno es un Pokémon de tipo hielo/volador introducido en la primera generación. Es uno de los Pokémon legendarios de Kanto.'
        },
        #////////////////////////////////////////////////Zapdos.
        {
            'pokemon': 'zapdos',
            'num': '145',
            'tipo': [
                'electrico',
                'volador'
            ],
            'peso': '52.6 kg',
            'altura': '1.6 m',
            'debilidad': [
                'hielo',
                'roca'
            ],
            'fortaleza': [
                'bicho',
                'planta',
                'lucha',
                'volador'
            ],
            'descripcion': 'Zapdos es un Pokémon de tipo eléctrico/volador introducido en la primera generación. Es uno de los Pokémon legendarios de Kanto.'
        },
        #////////////////////////////////////////////////Moltres.
        {
            'pokemon': 'moltres',
            'num': '146',
            'tipo': [
                'fuego',
                'volador'
            ],
            'peso': '60 kg',
            'altura': '2 m',
            'debilidad': [
                'electrico',
                'hielo',
                'roca',
                'acero',
                'agua'
            ],
            'fortaleza': [
                'bicho',
                'planta',
                'lucha',
                'volador'
            ],
            'descripcion': 'Moltres es un Pokémon de tipo fuego/volador introducido en la primera generación. Es uno de los Pokémon legendarios de Kanto.'
        },
        #////////////////////////////////////////////////Dratini.
        {
            'pokemon': 'dratini',
            'num': '147',
            'tipo': [
                'dragon'
            ],
            'peso': '3.3 kg',
            'altura': '1.8 m',
            'debilidad': [
                'dragon',
                'hielo',
                'hada'
            ],
            'fortaleza': [
                'fuego',
                'agua',
                'planta',
                'electrico'
            ],
            'descripcion': 'Dratini es un Pokémon de tipo dragón introducido en la primera generación. Es la forma evolucionada de Bagon.'
        },
        #////////////////////////////////////////////////Dragonair.
        {
            'pokemon': 'dragonair',
            'num': '148',
            'tipo': [
                'dragon'
            ],
            'peso': '16.5 kg',
            'altura': '4 m',
            'debilidad': [
                'dragon',
                'hielo',
                'hada'
            ],
            'fortaleza': [
                'fuego',
                'agua',
                'planta',
                'electrico'
            ],
            'descripcion': 'Dragonair es un Pokémon de tipo dragón introducido en la primera generación. Es la forma evolucionada de Dratini.'
        },
        #////////////////////////////////////////////////Dragonite.
        {
            'pokemon': 'dragonite',
            'num': '149',
            'tipo': [
                'dragon',
                'volador'
            ],
            'peso': '210 kg',
            'altura': '2.2 m',
            'debilidad': [
                'hielo',
                'roca',
                'dragon',
                'hada'
            ],
            'fortaleza': [
                'bicho',
                'planta',
                'lucha',
                'dragon',
                'volador'
            ],
            'descripcion': 'Dragonite es un Pokémon de tipo dragón/volador introducido en la primera generación. Es la forma evolucionada de Dragonair.'
        },
        #////////////////////////////////////////////////Mewtwo.
        {
            'pokemon': 'mewtwo',
            'num': '150',
            'tipo': [
                'psiquico'
            ],
            'peso': '122 kg',
            'altura': '2 m',
            'debilidad': [
                'bicho',
                'fantasma',
                'siniestro'
            ],
            'fortaleza': [
                'lucha',
                'psiquico'
            ],
            'descripcion': 'Mewtwo es un Pokémon de tipo psíquico introducido en la primera generación. Es uno de los Pokémon legendarios de Kanto.'
        },
        #////////////////////////////////////////////////Mew.
        {
            'pokemon': 'mew',
            'num': '151',
            'tipo': [
                'psiquico'
            ],
            'peso': '4 kg',
            'altura': '0.4 m',
            'debilidad': [
                'bicho',
                'fantasma',
                'siniestro'
            ],
            'fortaleza': [
                'lucha',
                'psiquico'
            ],
            'descripcion': 'Mew es un Pokémon de tipo psíquico introducido en la primera generación. Es uno de los Pokémon legendarios de Kanto.'
        }

    ]
    return pokedex


#----------------------------------------------------------------------
# Base de pokémon
# La base de pokemones representa una lista de todos los pokemon.
#----------------------------------------------------------------------
def pokemonesC():
    # Lista de los 151 Pokémon originales
    pokemones = [
        "bulbasaur", "ivysaur", "venusaur", "charmander", "charmeleon",
        "charizard", "squirtle", "wartortle", "blastoise", "caterpie",
        "metapod", "butterfree", "weedle", "kakuna", "beedrill",
        "pidgey", "pidgeotto", "pidgeot", "rattata", "raticate",
        "spearow", "fearow", "ekans", "arbok", "pikachu",
        "raichu", "sandshrew", "sandslash", "nidoran", "nidorina",
        "nidoqueen", "nidoran", "nidorino", "nidoking", "clefairy",
        "clefable", "vulpix", "ninetales", "jigglypuff", "wigglytuff",
        "zubat", "golbat", "oddish", "gloom", "vileplume",
        "paras", "parasect", "venonat", "venomoth", "diglett",
        "dugtrio", "meowth", "persian", "psyduck", "golduck",
        "mankey", "primeape", "growlithe", "arcanine", "poliwag",
        "poliwhirl", "poliwrath", "abra", "kadabra", "alakazam",
        "machop", "machoke", "machamp", "bellsprout", "weepinbell",
        "victreebel", "tentacool", "tentacruel", "geodude", "graveler",
        "golem", "ponyta", "rapidash", "slowpoke", "slowbro",
        "magnemite", "magneton", "farfetchd", "doduo", "dodrio",
        "seel", "dewgong", "grimer", "muk", "shellder",
        "cloyster", "gastly", "haunter", "gengar", "onix",
        "drowzee", "hypno", "krabby", "kingler", "voltorb",
        "electrode", "exeggcute", "exeggutor", "cubone", "marowak",
        "hitmonlee", "hitmonchan", "lickitung", "koffing", "weezing",
        "rhyhorn", "rhydon", "chansey", "tangela", "kangaskhan",
        "horsea", "seadra", "goldeen", "seaking", "staryu",
        "starmie", "mr-mime", "scyther", "jynx", "electabuzz",
        "magmar", "pinsir", "tauros", "magikarp", "gyarados",
        "lapras", "ditto", "eevee", "vaporeon", "jolteon",
        "flareon", "porygon", "omanyte", "omastar", "kabuto",
        "kabutops", "aerodactyl", "snorlax", "articuno", "zapdos",
        "moltres", "dratini", "dragonair", "dragonite", "mewtwo",
        "mew"]
    return pokemones