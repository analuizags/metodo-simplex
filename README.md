# Método Simplex

O método Simplex é uma técnica desenvolvida  pelo matemático George Dantzig, com o intuito de calcular, a solução ótima de um modelo de programação linear. 

## Este algoritmo

Desenvolvido com python3 para, inicialmente resolver problemas de programação linear, na forma padrão, obedecendo as seguintes características:

1. Todas as variáveis são não-negativas;
2. Todos os b são não-negativos;
3. Todas as equações iniciais do sistema são do tipo “ ≤ “.

## Para inserção da equação

Deve-se inserir nas variáveis, dentro do arquivo ```variaveis.txt```, seguinto exatamente a ordem dos fatores. Sendo primeiro a função objetivo e posteriormente as restrições do problema, um em cada linha do arquivo. De acordo com o exemplo abaixo:

#### Equações do problema:
```
   z = 3x + 5x 
   2x + 4x <= 10
   6x + 1x <= 20
   1x - 1x <= 30
```
#### Inserção no codigo:
```
   fo = [1, -3.0, -5.0, 0] 
   r = [[0, 2.0, 4.0, 10.0], [0, 6.0, 1.0, 20.0], [0, 1.0, -1.0, 30.0]] 
   b = [0, 10.0, 20.0, 30.0] 
   qtde = 3
 ```
