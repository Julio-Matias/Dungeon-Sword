# DungeonSword
Sinopse:
> Dungeon Sword é um jogo de visão top-down desenvolvido utilizando a biblioteca Pygame, inspirado em jogos como Zelda, Enter The Gungeon e Soul Knight, de onde foram tiradas algumas mecânicas e sprites. O nosso herói Chico, comerciante de espadas, entra numa masmorra onde enfrenta os irmãos Bob, bolinhas de gosma aparentemente dóceis, porém extremamente tóxicas. Ao matar um inimigo, este pode deixar espadas ou escudos que podem ser coletados por Chico, para aumentar o alcance de seu ataque e aumentar sua vida, respectivamente. Inicialmente, Chico tem 3 vidas, que podem aumentar ou diminuir durante o combate, com a colisão com os inimigos e a coleta de escudos, caso o número de vidas de Chico chegue a 0, significa que ele morreu e o jogo se encerra. O objetivo do jogo é conseguir sempre a maior pontuação possível que é contabilizada ao abater um inimigo. O número de inimigos aumenta conforme o nível aumenta, correspondente ao número de fases, representadas pelas portas.


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
|  **mvsl2**|   |
|  **jmps2** e **vgls** | Criação dos coletáveis, imagens e efeitos sonoros.  |
|  **pvmc** |   |
|  **gpg** |   |
|  **fbms** |  Criação da tela de menu/pause, botões e efeitos sonoros.  |


## Como Rodar o Jogo:
> 1º - Basta Ter o Python e o Pygame instalados em sua Máquina.
>
> 
> 2º - Clonar este repositório ou baixar o aquivo zip.
>
>3º - Rodar o arquivo main.py.
>


## Controles:

Jogador      |     Teclas    |
| ------------------- | ------------------- |
|  **Movimentação**|  W , A , S , D ou &#8592; , &#8593; , &#8594; , &#8595; |
|  **Ataque** | Barra de espaço |
|  **Menu/Pause** | M |


## Itens:

Interável      |     Ação    |
| ------------------- | ------------------- |
|  **Espada**|  Aumenta o alcance do ataque durante um breve período. |
|  **Escudo** | Ganha uma vida. |
|  **Porta** | Passa de fase. |
|  **Inimigos** | Ao colidir com herói, tira uma vida dele. |


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


## Desafios/Experiência:


## Imagens do jogo:

<img src="/projeto/assets/gameover.png">
<img src="/projeto/assets/menu.png">
<img src="/projeto/assets/game.png">
<img src="/projeto/assets/telainicial.png">
