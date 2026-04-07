import time
import os

class Sistema:

    """
    Classe para representar o sistema de gerenciamento de playlists, contendo métodos para CRUD
    simples de playlists, bem como um dicionário para armazenar as playlists e seus IDs.
    """

    def __init__(self):
        self.playlists = {} # Dicionário para armazenar as playlists, onde a key é o nome da playlist e o valor é um objeto Playlist. Estrutura: {nome_da_playlist(str): Playlist}
        self.ids = {}       # Dicionário para armazenar os IDs das playlists. Estrutura: {id(int): playlist(str)}

        with open("playlists.txt", "a") as f:
            pass
        self.atualiza_playlists()

    def atualiza_playlists(self):
        self.playlists.clear()
        self.ids.clear()

        if os.path.exists("playlists.txt"):
            with open("playlists.txt", "r") as f:
                for line in f:
                    playlist = line.strip()
                    self.playlists[playlist] = Playlist(playlist)
                    ult_chave = max(self.ids.keys(), default = 0)
                    self.ids[ult_chave + 1] = playlist

    def ad_playlist(self):
        playlist = input("Digite sua playlist: ")
        if playlist in self.playlists:
            print("Playlist já existente")
            return
        
        with open("playlists.txt", "a") as f:
            f.write(playlist + "\n")

        self.atualiza_playlists()
        print(f"Playlist adicionada: {playlist}")

    def rem_playlist(self):
        if not self.ver_playlists():
            return

        try:
            id = int(input("Digite o ID da playlist: "))
        except ValueError:
            print("ID inválido!")
            return
        
        playlist = None
        playlist = self.ids.get(id)

        if playlist in self.playlists and os.path.exists("playlists.txt"):
            with open("playlists.txt", "r") as f:
                linhas = f.readlines()

            with open("playlists.txt", "w") as f:
                for linha in linhas:
                    if linha.strip() != playlist:
                        f.write(linha)

            os.remove(f"{playlist}.txt")
            self.atualiza_playlists()
            print(f"Playlist removida: {playlist}")

        else:
            print("Playlist não existente!")

    def ver_playlists(self):
        if self.playlists:
            print("=====Playlists=====")
            for i, playlist in self.ids.items():
                print(f"{i}) {playlist}")
            print("===================")
            return True

        else:
            print("Nenhuma playlist criada!")
            return False

class Playlist:

    """
    Classe para representar uma playlist, contendo métodos para CRUD simples de músicas,
    bem como uma lista para armazenar as músicas e um dicionário para armazenar os IDs das músicas.
    """

    def __init__(self, nome):
        self.nome = nome    # Nome da playlist
        self.musicas = []   # Lista para armazenar as músicas da playlist
        self.ids = {}       # Dicionário para armazenar os IDs das músicas. Estrutura: {id(int): musica(str)}

        with open(f"{nome}.txt", "a") as f:
            pass
        
        self.atualiza_musicas()

    def atualiza_musicas(self):
        self.musicas.clear()
        self.ids.clear()

        if os.path.exists(f"{self.nome}.txt"):
            with open(f"{self.nome}.txt", "r") as f:
                for line in f:
                    musica = line.strip()
                    self.musicas.append(musica)
                    ult_chave = max(self.ids.keys(), default = 0)
                    self.ids[ult_chave + 1] = musica

    def ad_musica(self):
        musica = input("Digite a música: ")
        if musica in self.musicas:
            print("Musica já existente")
            return
        
        with open(f"{self.nome}.txt", "a") as f:
            f.write(musica + "\n")

        self.atualiza_musicas()
        print(f"Adicionado: {musica}")

    def rem_musica(self):
        self.ver_musicas()
        
        try:
            id = int(input("Digite o ID da música: "))
        except ValueError:
            print("ID inválido!")
            return
        
        musica = self.ids.get(id)

        if musica in self.musicas and os.path.exists(f"{self.nome}.txt"):
            with open(f"{self.nome}.txt", "r") as f:
                linhas = f.readlines()
            with open(f"{self.nome}.txt", "w") as f:
                for linha in linhas:
                    if linha.strip() != musica:
                        f.write(linha)

            self.atualiza_musicas()
            print(f"Removido: {musica}")

        else:
            print("Musica não existente!")

    def ver_musicas(self):
        if self.musicas:
            print(f"Playlist '{self.nome}':")
            print("=====Músicas=====")
            for i, musica in self.ids.items():
                print(f"{i}) {musica}")   
            print("=================")

        else:
            print("Nenhuma musica na playlist!")

sistema = Sistema()

def escolhe_playlist():
    if not sistema.ver_playlists():
        return None
    try:
        id = int(input("Escolha a playlist: "))
    except ValueError:
        print("ID inválido!")
        return None
    
    if id in sistema.ids:
        return id
    else:
        print("Playlist não existente!")
        return None

def main():
    while True:
        print("\nMenu:")
        print("====================")
        print("1) Adicionar playlist")
        print("2) Remover playlist")
        print("3) Ver playlists")
        print("4) Adicionar música a playlist")
        print("5) Remover música de playlist")
        print("6) Ver músicas de playlist")
        print("7) Sair")
        print("====================")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            sistema.ad_playlist()
        elif escolha == '2':
            sistema.rem_playlist()
        elif escolha == '3':
            sistema.ver_playlists()
        elif escolha == '4':
            id = escolhe_playlist()
            if id is not None:
                sistema.playlists[sistema.ids[id]].ad_musica()
        elif escolha == '5':
            id = escolhe_playlist()
            if id is not None:
                sistema.playlists[sistema.ids[id]].rem_musica()
        elif escolha == '6':
            id = escolhe_playlist()
            if id is not None:
                sistema.playlists[sistema.ids[id]].ver_musicas()
        elif escolha == '7':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")
        time.sleep(2)

if __name__ == "__main__":
    main()
