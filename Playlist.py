import time

class Sistema:
    def __init__(self):
        self.playlists = {} # Dicionário para armazenar as playlists, onde a key é o nome da playlist e o valor é um objeto Playlist
        self.ids = {}       # Dicionário para armazenar os IDs das playlists

    def ad_playlist(self):
        playlist = input("Digite sua playlist: ")
        if playlist in self.playlists:
            print("Playlist já existente")
            return
        
        self.playlists[playlist] = Playlist(playlist)

        ult_chave = max(self.ids.keys(), default = 0)
        self.ids[ult_chave + 1] = playlist

        print(f"Playlist adicionada: {playlist}")

    def rem_playlist(self):
        self.ver_playlists()

        try:
            id = int(input("Digite o ID da playlist: "))
        except ValueError:
            print("ID inválido!")
            return
        
        playlist = None

        for playlist_id, n in self.ids.items():
            if playlist_id == id:
                playlist = n
                break

        if playlist in self.playlists:
            self.playlists.pop(playlist)
            self.ids.pop(id)
            print(f"Playlist removida: {playlist}")

        else:
            print("Playlist não existente!")

    def ver_playlists(self):
        if self.playlists:
            print("=====Playlists=====")
            for i, playlist in self.ids.items():
                print(f"{i}) - {playlist}")
            print("===================")

        else:
            print("Nenhuma playlist criada!")

class Playlist:
    def __init__(self, nome):
        self.nome = nome    # Nome da playlist
        self.musicas = []   # Lista para armazenar as músicas da playlist
        self.ids = {}       # Dicionário para armazenar os IDs das músicas

    def ad_musica(self):
        musica = input("Digite a música: ")
        if musica in self.musicas:
            print("Musica já existente")
            return
        
        self.musicas.append(musica)
        
        ult_chave = max(self.ids.keys(), default = 0)
        self.ids[ult_chave + 1] = musica

        print(f"Adicionado: {musica}")

    def rem_musica(self):
        self.ver_musicas()
        try:
            id = int(input("Digite o ID da música: "))
        except ValueError:
            print("ID inválido!")
            return
        
        musica = None
        for musica_id, n in self.ids.items():
            if musica_id == id:
                musica = n
                break

        if musica in self.musicas:
            self.musicas.remove(musica)
            self.ids.pop(id)
            print(f"Removido: {musica}")

        else:
            print("Musica não existente!")

    def ver_musicas(self):
        if self.musicas:
            print(f"Playlist '{self.nome}':")
            print("=====Músicas=====")
            for i, musica in self.ids.items():
                print(f"{i}) - {musica}")   
            print("=================")

        else:
            print("Nenhuma musica na playlist!")

sistema = Sistema()

def escolhe_playlist():
    sistema.ver_playlists()
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
        print("1. Adicionar playlist")
        print("2. Remover playlist")
        print("3. Ver playlists")
        print("4. Adicionar música a playlist")
        print("5. Remover música de playlist")
        print("6. Ver músicas de playlist")
        print("7. Sair")
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
