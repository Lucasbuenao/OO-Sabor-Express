from modelos.restaurante import Restaurante

restaurante_brasileiro = Restaurante('Fogo de Chão', 'Comida Brasileira')
restaurante_brasileiro.receber_avaliacao('Lucas', 5)
restaurante_brasileiro.receber_avaliacao('Duda', 2)
restaurante_brasileiro.receber_avaliacao('Kiwi', 3)

# restaurante_italiano = Restaurante('Spoleto', 'Comida Italiana')
# restaurante_japones = Restaurante('Aska', 'Comida Japonesa')

# restaurante_japones.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()

# Vimos que surgiu uma nova pasta chamada '__pycache__', que é uma forma mais simples do Python interpretar aquele módulo que estamos importando. Ou seja, é um diretório que o Python cria para armazenar os arquivos compilados em bytecode. Que é uma forma que ele tem de interpretar aqueles códigos de uma maneira muito mais simples do que no arquivo original.