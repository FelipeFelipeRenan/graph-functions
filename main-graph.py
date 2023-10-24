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

    def EVertice(self, v):
        return v in self.adjacencias


    def AddAresta(self, vi, vj, peso):
        if vi in self.adjacencias and vj in self.adjacencias:
            self.adicionar_aresta(vi, vj, peso)
            self.m += 1
        else:
            print(f"Vi ou Vj não pertencem ao grafo, a operação não pode ser efetuada.")


    def RemoveAresta(self, vi, vj, peso):
        if vi in self.adjacencias and vj in self.adjacencias:
            if (vj, peso) in self.adjacencias[vi]:
                self.adjacencias[vi].remove((vj, peso))
                self.m -= 1
            else:
                print(f"A aresta entre {vi} e {vj} com peso {peso} não existe.")
        else:
            print(f"Vi ou Vj não pertencem ao grafo, a operação não pode ser efetuada.")


    def ExisteAresta(self, vi, vj, peso):
        if vi in self.adjacencias and vj in self.adjacencias:
            for aresta in self.adjacencias[vi]:
                if aresta[0] == vj and aresta[1] == peso:
                    return True
        return False
    

    def MudaPeso(self, vi, vj, peso_original, novo_peso):
        if vi in self.adjacencias and vj in self.adjacencias:
            arestas_vi = self.adjacencias[vi]
            for i in range(len(arestas_vi)):
                if arestas_vi[i][0] == vj and arestas_vi[i][1] == peso_original:
                    arestas_vi[i] = (vj, novo_peso)
                    return
            print(f"A aresta entre {vi} e {vj} com peso {peso_original} não foi encontrada.")
        else:
            print(f"Vi ou Vj não pertencem ao grafo, a operação não pode ser efetuada.")

        
    def ImprimeGrafo(self):
        print("Vértices:")
        for u in self.adjacencias:
            print(f"Vértice {u}")
        
        print("Arestas:")
        for u, vizinhos in self.adjacencias.items():
            for v, peso in vizinhos:
                print(f"Aresta ({u}, {v}) - Peso: {peso}")

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

    # Exemplo de uso da função EVertice
    v = 55
    if grafo.EVertice(v):
        print(f"O vértice {v} pertence ao grafo.")
    else:
        print(f"O vértice {v} não pertence ao grafo.")