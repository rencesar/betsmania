#language: pt
Funcionalidade: Registrar no sistema
	
	Como visitante
	Afim de criar uma conta de usuário
	Devo ser capaz de me registrar no sistema

	Cenário: Registrar usuario na página inicial

		Dado que acesso como visitante
		E que está na página inicial
		Quando clico no botão "Cadastrar"
		E preencho os dados conforme abaixo:
			|  NOME            |  USERNAME |  EMAIL            |  SENHA     |
			|  Paulo Emanuel   |  paulo    |  paulo@gmail.com  |  paulo123  |
		Então estárei na pagina "Parabéns, Paulo conta cadastrada com sucesso."