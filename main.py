 # Faça o donwload dos dados
# "https://www.kaggle.com/leonardopena/top-spotify-songs-from-20102019-by-year/download" -O top10s.csv

from csv import reader
from unidecode import unidecode #pega todo caractere que nao é asci e tenta passar para ascii (ex á à ã â -> a)
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from unidecode import unidecode
import re
import uuid


class SpotData(object):

    def __init__(self):#, CLIENT_ID, CLIENT_SECRET):
        #self.client_id = CLIENT_ID
        #self.client_secret = CLIENT_SECRET
        self.feats = {}
        self.artists = []



    def get_csv_data(self):
        #------------------------------------------------------CODIGO NOJENTO ARRUMAR DPS-------------
        # Abre arquivo para leitura.
        with open('top10s.csv') as file:
            file.readline()
            for i, row in enumerate(reader(file), 2):


                
                title = unidecode(row[1])
                artist = unidecode(row[2])
                

                if artist not in self.artists:
                    self.artists.append(artist)


                try:
                    s = len("(feat. ")
                    a = title.index("(feat.")
                    b = title[a:].index(")")                    
                    feat = unidecode(title[a+s:b+a])
                    feat = re.split(" & |, ", feat)

                    if artist not in self.feats:
                        self.feats[artist] = feat
                    else:
                        for f in feat:
                            if f not in self.feats[artist]:
                               self.feats[artist].append(f)
                    for f in feat:                       
                        if f not in self.artists:
                            self.artists.append(f)
 
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

            for n in self.artists:
                file.write('  node [\n')
                file.write('    id "{}"\n'.format(n))
                file.write('  ]\n')

            for source in self.feats.keys():
                for target in self.feats[source]:
                    file.write('  edge [\n')
                    file.write('    source "{}"\n'.format(source))
                    file.write('    target "{}"\n'.format(target))
                    file.write('  ]\n')

                

        # Última linha, que fecha os colchetes da rede.
            file.write(']\n')

    def drawPrint(self):
        print("{")
        for i in self.feats.keys():
            print('\t"',str(i), '": [')
            for j in self.feats[i]:
                print('\t\t "', str(j), '",')
            print("],")
        print("}")

    def start(self):
        self.get_csv_data()


if __name__ == '__main__':
    spot = SpotData(); #CLIENT_ID, CLIENT_SECRET)
    spot.get_csv_data();
    spot.writeGML();
    