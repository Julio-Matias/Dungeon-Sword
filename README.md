# DungeonSword
Sinopse:
> Dungeon Sword é um jogo de visão top-down desenvolvido utilizando a biblioteca Pygame, inspirado em jogos como Zelda, Enter The Gungeon e Soul Knight, de onde foram tiradas algumas mecânicas e sprites. O nosso herói Chico, comerciante de espadas, entra numa masmorra onde enfrenta os irmãos Bob, bolinhas de gosma aparentemente dóceis, porém extremamente tóxicas, ou os fantasmas Ghostavo, que são mais rápidos e atravessam paredes. Ao matar um inimigo, este pode deixar espadas e escudos que podem ser coletados por Chico, para aumentar o alcance de seu ataque e aumentar sua vida, respectivamente. Inicialmente, Chico tem 3 vidas, que podem aumentar ou diminuir durante o combate, com a colisão com os inimigos e a coleta de escudos, caso o número de vidas de Chico chegue a 0, significa que ele morreu e o jogo se encerra. O objetivo do jogo é conseguir sempre a maior pontuação possível que é contabilizada ao abater um inimigo. O número de inimigos aumenta conforme o nível aumenta, correspondente ao número de fases, representadas pelas portas.




## Equipe:


- Marcus Vinícius (mvsl2)
- Júlio Matias (jmps2)
- Pedro Vasconcelos (pvmc)
- Gabriel Pimentel (gpg)
- Vinícius Lopes (vgls)
- Filipe Bezerra (fbms)




## Divisão de tarefas:


|      Equipes      |     Atribuições     |
| ------------------- | ------------------- |
|  **mvsl2**| Criação dos mapas a partir de matrizes, animações do jogador e do inimigo, criação de sprites |
|  **jmps2** e **vgls** | Criação dos coletáveis, imagens e efeitos sonoros.  |
|  **gpg** e **pvmc** |  Criação dos inimigos e vetores para seguir o player, criação do player, movimentação e colisão, sprite do jogador, ataque do jogador, interação com o ataque, coleta dos objetos, múltiplos inimigos, e mudança de mapas ao passar de nível  |
|  **fbms** |  Criação da tela de menu/pause, botões e efeitos sonoros.  |




## Como Rodar o Jogo:
> 1º - Basta Ter o Python e o Pygame instalados em sua Máquina.
>
> 2º - Clonar este repositório ou baixar o arquivo zip.
>
> 3º - Abrir a pasta Dungeon-Sword ou Dungeon-Sword-Main em um editor de código como VS CODE ou PyCharm
>
> 4º - Rodar o arquivo main.py.
>




## Controles:


Jogador      |     Teclas    |
| ------------------- | ------------------- |
|  **Movimentação**|  W , A , S , D ou &#8592; , &#8593; , &#8594; , &#8595; |
|  **Ataque** | Barra de espaço |
|  **Menu/Pause** | M |




## Itens:


Obj. Interativo     |     Ação    |
| ------------------- | ------------------- |
|  **Espada**|  Aumenta o alcance do ataque durante um breve período. |
|  **Escudo** | Aumenta a vida do jogador em 1. |
|  **Porta** | Passa de fase. |
|  **Inimigos** | Ao colidir com herói, tira uma vida dele, e ao colidir com o ataque do herói, perde uma de suas vidas. |




## Bibliotecas e Ferramentas:


|      Biblioteca, Ferramentas e Frameworks      |     Aplicação     |
| ------------------- | ------------------- |
|  PyGame  |  A biblioteca pygame é a principal de nosso projeto, pois ela tem funções específicas que facilitam na criação do jogo, principalmente na questão da renderização de objetos e as interações entre eles. |
|  Random  | A biblioteca "Random" foi utilizada em três partes do código, utilizando a função "Randint", que sorteia um número inteiro dentro de um intervalo definido, fizemos as mecânicas da chance de "dropar" itens dos inimigos, o lugar onde nascem os inimigos e a quantidade de inimigos em cada fase. |
|  Sys |  Da biblioteca "Sys", foi utilizada a função "exit", que serve para encerrar o processo do programa. |
|  Piskel |  O site "Piskel" foi muito utilizado para criação e manutenção dos sprites do jogo, do player, do mapa, do inimigo... |




## Conceitos e Aplicação:
> É possível ver ao longo do código, aplicações de diversos conceitos ensinados durante o semestre. Nota-se com uma certa frequência o uso de Comandos condicionais, Laços de repetição, Listas, Tuplas, Dicionários, Funções e principalmente, programação orientada a objeto.
>
> Sendo assim, a utilização de laços de repetição torna-se evidente logo no arquivo principal, "main.py", aquele que executa o jogo, que por sua vez, ocorre dentro de um laço "while", e dentro desse laço, há vários laços do tipo "for", testando se ocorre algum evento durante o jogo, assim como um Comando condicional "if", dentro do loop principal, que checa se o jogo está pausado ou não, e assim mostrando a respectiva tela.
>
>  As listas também estão muito presentes, podendo ser encontradas no gerenciamento dos inimigos, coletáveis e também nas criações dos mapas, que são listas de strings, formando uma matriz e a partir disso, renderizando as imagens. As tuplas cumprem um papel essencial em algumas partes do código, armazenando informações imutáveis utilizadas em várias partes do projeto.
>
> E por fim, a parte mais importante do projeto, a utilização da programação orientada à objeto. Utilizamos os conceitos de módulos, classes, objetos, métodos e atributos em quase todo o código. A utilização de classes e programação orientada a objetos se tornou essencial para o projeto, visto que esse conceito foi utilizado extensivamente durante todo o código. As classes foram muito úteis para a organização dos métodos e seus atributos, além de facilitar a importação dos mesmos. Além disso, a criação de objetos utilizando classes foi usada para a criação do jogador, dos inimigos, dos coletáveis e dos mapas. Sem classes isso se tornaria inviável, pois todos esses objetos eram criados e atualizados durante toda a criação do jogo.


 
## Organização do código:
O código foi estruturado Orientado à objetos e utilizou o recurso de loop para a lógica do jogo acontecer. As classes e funções importantes foram:


- *Player()*:
> Player é o personagem jogável, e é responsável por receber os inputs de locomoção  e ataque, também derrota do jogador, atualização quando o jogador perde e também sua colisão com as paredes
- *Coletaveis()*:
> A classe Coletaveis se da aos itens que o player pode pegar durante sua jogatina que influenciam, que são as espadas e os escudos
- *Portal()*:
> Gera o coletável que serve para o jogador passar para o próximo nível. Ele funcionava de forma diferente aos outros coletáveis, então fizemos uma classe separada para isso.
- *HUD()*:
> Mostra na tela as pontuações, vida e itens coletados pelo player além de mudar quando o player ganha um buff
- *Button()*:
> Faz com que seja possível interagir com os botões visíveis na tela
- *Mapa()*:
> Essa classe escolhe um mapa aleatoriamente, monta o mapa escolhido e cria os inimigos a cada nível como mostrado a seguir.
- *def montar_mapa()*
> Essa função analisa a matriz de construção do mapa, e utiliza uma outra classe chamada Tile, que gera imagens e retângulos utilizando o PyGame na uma posição relativa da matriz baseada em seu índice e com um tipo definido pelo elemento analisado da matriz, que irá definir a imagem desse objeto e se esse objeto será um obstáculo (impedindo o jogador e inimigos comuns de o atravessarem), um lugar onde inimigos poderão aparecer ou apenas visual.
- *def proxima_fase()*
> Após todos os inimigos de um nível serem derrotados e o jogador entrar na porta que é criada, essa função escolhe um mapa diferente aleatoriamente entre os 11 mapas que existem no jogo, e gera novos inimigos em posições aleatórias do mapa.
- *Game()*:
> Cria o loop de jogo e define onde cada elemento do jogo vai ser colocado e a cada tick ele analisa onde os inimigos estão e timer
- *Enemy()*:
> Define o tipo de inimigo que vai ser gerado a partir do parâmetro "tipo" que define qual dos dois inimigos será: O Slime, que é o inimigo mais comum, ou o Ghost, que é aparece em um número menor, mas é mais rápido que o Slime e consegue atravessar paredes.
- *Superficie()*:
> Carrega as imagens do Chão, da Parede, dos Menus, e as fontes que podem ser utilizadas para criar mensagens
- *Audios()*:
> Carrega os áudios do jogo e define seu volume


## Desafios/Experiência:
O principal desafio que sentimos durante a realização desse projeto foi aprender a utilizar ferramentas e conceitos nunca antes vistos, como a biblioteca do PyGame e programação orientada a objeto. Contudo, foi muito útil aprender como usar essas funcionalidades, porque elas permitem realizar tarefas muito mais avançadas que não imaginávamos no começo do curso.


Além disso, tivemos outros desafios menores durante a realização do projeto, mas que foram resolvidos na medida em que aprendemos mais como o PyGame funciona, como impedir que o jogador e os inimigos atravessassem obstáculos, desenvolver uma forma do inimigo seguir o jogador, programar animações, e organizar os menus.


## Imagens do jogo:


<img src="/projeto/assets/relatorio/gameover.png">
<img src="/projeto/assets/relatorio/menu.png">
<img src="/projeto/assets/relatorio/game.png">
<img src="/projeto/assets/relatorio/telainicial.png">
