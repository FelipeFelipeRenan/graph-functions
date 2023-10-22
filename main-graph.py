class Grafo:
    def __init__(self, nome, n, m):
        self.nome = nome
        self.n = n
        self.m = m
        self.adjacencias = {}
    
    @classmethod
    def NovoGrafo(cls):
        novo_grafo = cls("G", 1, 0)
        return novo_grafo

    def adicionar_aresta(self, u, v, peso):
        if u not in self.adjacencias:
            self.adjacencias[u] = []
        self.adjacencias[u].append((v, peso))

    def ler_grafo_do_arquivo(self, nome_arquivo):
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()

            # Lê a primeira linha para obter o nome, número de vértices e número de arestas
            nome, n, m = linhas[0].strip().split()
            self.nome = nome
            self.n = int(n)
            self.m = int(m)

            # Processa as linhas seguintes para ler as arestas
            for linha in linhas[2:]:
                u, v, peso = linha.strip().split()
                u = int(u)
                v = int(v)
                peso = float(peso)  # Converte o peso para float
                self.adicionar_aresta(u, v, peso)

    def mostrar_grafo(self):
        print(f"Nome do grafo: {self.nome}")
        print(f"Número de vértices: {self.n}")
        print(f"Número de arestas: {self.m}")
        print("Arestas:")
        for u, vizinhos in self.adjacencias.items():
            for v, peso in vizinhos:
                print(f"({u}, {v}) - Peso: {peso}")
    
    def mostrar_lista_de_adjacencias(self):
        print("Lista de Adjacências:")
        for u, vizinhos in self.adjacencias.items():
            print(f"Vértice {u} -> {', '.join([f'({v}, {peso})' for v, peso in vizinhos])}")



if __name__ == "__main__":
    nome_arquivo = "graph.txt"  # Substitua pelo nome do arquivo de entrada
    grafo = Grafo("", 0, 0)
    grafo.ler_grafo_do_arquivo(nome_arquivo)
    grafo.mostrar_grafo()
    grafo.mostrar_lista_de_adjacencias()

    # Novo grafo vazio
    novo_grafo = Grafo.NovoGrafo()
    print("\nGrafo Novo:")
    novo_grafo.mostrar_grafo()
    novo_grafo.mostrar_lista_de_adjacencias()
