#language: pt
Funcionalidade: Listar jogos

	Como visitante e usuario
	Afim de conferir determinados jogos
	Devo ser capaz de listar os jogos a minha escolha

    Contexto:
        Dado que existem os seguintes jogos cadastrados no sistema:
            |  LIGA                      |  TIME CASA  |  TIME FORA   |  CASA   |  EMPATE   |  FORA   |  DATA                 |
            |  UEFA                      |  Barcelona  |  Real Madri  |  2.10   |  1.90     |  4.30   |  14/03/2017 às 18:30  |
            |  Campeonato Internacional  |  São Paulo  |  Chelsea     |  9.20   |  3.50     |  2.10   |  12/03/2017 às 21:00  |
            |  Copa do Mundo             |  Brasil     |  Portugal    |  4.50   |  5.30     |  1.90   |  13/03/2017 às 16:30  |
            |  Campeonato Brasileiro     |  Vasco      |  Flamengo    |  2.00   |  1.90     |  8.33   |  14/03/2017 às 18:30  |

    @wip
	Cenário: Listar todos os jogos
        Dado que acesso a página inicial
        Quando que acesso como visitante
        Então verei os seguintes jogos na tela:
            |  TIME CASA  |  TIME FORA   |  CASA   |  EMPATE   |  FORA   |  DATA                 |
            |  Barcelona  |  Real Madri  |  2.10   |  1.90     |  4.30   |  14/03/2017 às 18:30  |
            |  São Paulo  |  Chelsea     |  9.20   |  3.50     |  2.10   |  12/03/2017 às 21:00  |
            |  Brasil     |  Portugal    |  4.50   |  5.30     |  1.90   |  13/03/2017 às 16:30  |
            |  Vasco      |  Flamengo    |  2.00   |  1.90     |  8.33   |  14/03/2017 às 18:30  |
