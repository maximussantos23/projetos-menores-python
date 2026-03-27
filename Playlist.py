import time

class Playlist:
    def __init__(self, nome):
        self.nome = nome
        self.musicas = []

    def ad_musica(self, musica):
        if musica in self.musicas:
            print("Musica já existente")
        self.musicas.append(musica)
        print(f"Adicionado: {musica}")

    def rem_musica(self, musica):
        if musica in self.musicas:
            self.musicas.remove(musica)
            print(f"Removido: {musica}")
        else:
            print("Musica não existente!")

    def ver_musicas(self):
        if self.musicas:
            print(f"Playlist '{self.nome}':")
            for musica in self.musicas:
                print(f"- {musica}")
        else:
            print("Nenhuma musica na playlist!")

playlists = {}

while True:
    print("====================\n1) Nova playlist\n2) Selecionar playlist\n3) Ver playlists\n====================\n")
    x = int(input("Digite uma opção: "))

    if x not in (1, 2, 3):
        print("Valor invalido!")
  
    if x == 3:
        if playlists:
            for i in range(1, len(playlists) + 1):
                print(f"- {playlists[i]}")
        else:
            print("Nenhuma playlist adicionada!")
        time.sleep(2)

    if x == 1:

        # dict = {"1": "Playlist 1", "2": "Playlist 2"}
        # Lógica pra adicionar playlist associando a uma key no dict

        playlist = input("Digite sua playlist: ")

        i = max(playlists.keys(), default=0) + 1

        playlists[i] = playlist

        print("Playlist adicionada!")
        time.sleep(2)

    if x == 2:
        while True:
            if playlists:
                print("====================")
                for i in range(1, len(playlists) + 1):
                    print(f"{i} - {playlists[i]}")
                print("====================\n")
                playlist_esc = int(input("Escolha uma playlist: "))
            else:
                print("Nenhuma playlist adicionada!")
                break

            # Lógica pra playlist escolhida



