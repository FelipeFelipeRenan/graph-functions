from graph import Grafo


def main():
    nome_arquivo = "graph.txt"
    grafo = Grafo("", 0, 0)
    grafo.ler_grafo_do_arquivo(nome_arquivo)
    
    while True:
        print("\nMenu:")
        print("1. Exibir grafo")
        print("2. Exibir lista de adjacências")
        print("3. Verificar se o grafo é conexo")
        print("4. Calcular caminho mínimo")
        print("5. Calcular custos dos caminhos mínimos")
        print("6. Verificar se o grafo é simples")
        print("7. Verificar se o grafo é uma árvore")
        print("8. Verificar se o grafo é bipartido")
        print("9. Obter grafo complementar")
        print("10. Verificar existência de aresta entre vértices")
        print("11. Obter lista de adjacência de um vértice")
        print("12. Obter arestas incidentes a um vértice")
        print("13. Construir matriz de adjacência")
        print("14. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            grafo.mostrar_grafo()
        elif escolha == "2":
            grafo.mostrar_lista_de_adjacencias()
        elif escolha == "3":
            if grafo.Conexo():
                print("O grafo é conexo.")
            else:
                print("O grafo não é conexo.")
        elif escolha == "4":
            vi = int(input("Digite o vértice de origem (vi): "))
            vj = int(input("Digite o vértice de destino (vj): "))
            caminho_minimo = grafo.CaminhoMinimo1(vi, vj)
            if caminho_minimo:
                print(f"Caminho mínimo entre {vi} e {vj}: {caminho_minimo}")
            else:
                print(f"Não há caminho entre {vi} e {vj}.")
        elif escolha == "5":
            vi = int(input("Digite o vértice de origem (vi): "))
            custos_minimos = grafo.CustoMinimo(vi)
            if custos_minimos:
                for v, custo in custos_minimos.items():
                    if v != vi:
                        print(f"Custo mínimo de {vi} para {v}: {custo}")
            else:
                print(f"O vértice {vi} não pertence ao grafo.")
        elif escolha == "6":
            if grafo.GrafoSimples():
                print("O grafo é simples.")
            else:
                print("O grafo não é simples.")
        elif escolha == "7":
            if grafo.EArvore():
                print("O grafo é uma árvore.")
            else:
                print("O grafo não é uma árvore.")
        elif escolha == "8":
            if grafo.EBipartido():
                print("O grafo é bipartido.")
            else:
                print("O grafo não é bipartido.")
        elif escolha == "9":
            grafo_complementar = grafo.Complemento()
            print("Grafo complementar:")
            grafo_complementar.mostrar_grafo()
        elif escolha == "10":
            vi = int(input("Digite o vértice de origem (vi): "))
            vj = int(input("Digite o vértice de destino (vj): "))
            if grafo.EAdj(vi, vj):
                print(f"Existe uma aresta entre {vi} e {vj}.")
            else:
                print(f"Não existe uma aresta entre {vi} e {vj}.")
        elif escolha == "11":
            v = int(input("Digite o número do vértice: "))
            lista_adjacencia = grafo.Adjacencia(v)
            print(f"Lista de adjacência do vértice {v}: {lista_adjacencia}")
        elif escolha == "12":
            v = int(input("Digite o número do vértice: "))
            arestas_incidencia = grafo.Incidencia(v)
            print(f"Arestas incidentes ao vértice {v}: {arestas_incidencia}")
        elif escolha == "13":
            matriz_adjacencia = grafo.MatrizAdj()
            print("Matriz de adjacência:")
            for linha in matriz_adjacencia:
                print(linha)
        elif escolha == "14":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()