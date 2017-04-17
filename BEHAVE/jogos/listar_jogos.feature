#language: pt
Funcionalidade: Listar jogos

	Como visitante e usuario
	Afim de conferir determinados jogos
	Devo ser capaz de listar os jogos a minha escolha

    Contexto:
        Dado que existem os seguintes jogos cadastrados no sistema:
            |  TIME CASA  |  TIME FORA   |  CASA  |  EMPATE  |  FORA  |  DATA                 |
            |  Barcelona  |  Real Madri  |  2.1   |  1.9     |  4.3   |  14/03/2017 às 18:30  |
            |  São Paulo  |  Chelsea     |  9.2   |  3.5     |  2.1   |  12/03/2017 às 21:00  |
            |  Brasil     |  Portugal    |  4.5   |  5.3     |  1.9   |  13/03/2017 às 16:30  |
            |  Vasco      |  Flamengo    |  2.0   |  1.9     |  8.33  |  14/03/2017 às 18:30  |

    @wip
	Cenário: Listar todos os jogos
        Dado que acesso a página inicial
        Quando que acesso como visitante
        Então verei os seguintes jogos na tela:
            |  TIME CASA  |  TIME FORA   |  CASA  |  EMPATE  |  FORA  |  DATA                 |
            |  Barcelona  |  Real Madri  |  2.1   |  1.9     |  4.3   |  14/03/2017 às 18:30  |
            |  São Paulo  |  Chelsea     |  9.2   |  3.5     |  2.1   |  12/03/2017 às 21:00  |
            |  Brasil     |  Portugal    |  4.5   |  5.3     |  1.9   |  13/03/2017 às 16:30  |
            |  Vasco      |  Flamengo    |  2.0   |  1.9     |  8.33  |  14/03/2017 às 18:30  |
