# Faça o donwload dos dados
# "https://www.kaggle.com/leonardopena/top-spotify-songs-from-20102019-by-year/download" -O top10s.csv

from csv import reader
from unidecode import unidecode #pega todo caractere que nao é asci e tenta passar para ascii (ex á à ã â -> a)
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from unidecode import unidecode


class SpotData(object):

    def __init__(self):#, CLIENT_ID, CLIENT_SECRET):
        #self.client_id = CLIENT_ID
        #self.client_secret = CLIENT_SECRET
        self.neighbors = {}
        self.titles = {}
        self.artists = {}



    def get_csv_data(self):
        # Abre arquivo para leitura.
        with open('top10s.csv') as file:
            file.readline()
            
            for i, row in enumerate(reader(file), 2):
                title = row [1]
                artist = row[2]
                pop = row[14]

                self.titles[i] = title

                try:
                    a = title.index("(feat.") 
                    print(unidecode(title[a:]))
                except ValueError:
                    continue                

                # primeiro pega tudo que esta dentro dos paranteses
                # se tiver "," ou "&"" tem mais que um no feat -> separa em substrigns

    
    def writeGML(self):
        with open('spotify.gml', 'w') as file:
                # Primeira linha, que abre os colchetes da rede.
            file.write('graph [\n')

            # Segunda linha, que indica se a rede é dirigida (1) ou não (0).
            file.write('  directed 1\n')

            # Colchetes de cada nó. Você sempre precisa colocar um id (inteiro
            # ou string) e depois pode colocar os atributos adicionais que
            # quiser, contanto que sejam inteiros, floats ou strings. Se forem   
            # strings, não esqueça as aspas duplas (isso vale para o id também).
            # Não esqueça também da indentação. Ela não é necessária mas ajuda
            # a deixar mais legível.
            #
            # O módulo unidecode converte todo caractere não-ASCII para o
            # caractere ASCII mais próximo. Isso é necessário porque a
            # especificação do formato gml exige que ele seja ASCII.
            for n in names.keys():
                file.write('  node [\n')
                file.write('    id "{}"\n'.format(n))
                file.write('    name "{}"\n'.format(unidecode(names[n])))
                file.write('  ]\n')

        # Colchetes de cada aresta. Você sempre precisa colocar um source
        # e um target (ids de nós) e depois pode colocar os atributos
        # adicionais que quiser, contanto que sejam inteiros, floats ou
        # strings. Se forem strings, não esqueça as aspas duplas (isso
        # vale para o source e o target também). Não esqueça também da
        # indentação. Ela não é necessária mas ajuda a deixar mais legível.
            for n in neighbors.keys():
                for m in neighbors[n]:
                    file.write('  edge [\n')
                    file.write('    source "{}"\n'.format(n))
                    file.write('    target "{}"\n'.format(m))
                    file.write('  ]\n')

        # Última linha, que fecha os colchetes da rede.
            file.write(']\n')

    def start(self):
        self.get_csv_data()


if __name__ == '__main__':
    spot = SpotData(); #CLIENT_ID, CLIENT_SECRET)
    spot.get_csv_data();