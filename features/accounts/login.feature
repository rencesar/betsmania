#language: pt
Funcionalidade: Login no sistema
	
	Como visitante
	Afim de fazer login no sistema
	Devo ser capaz de entrar na minha conta preenchendo corretamente meus dados

	@wip
	Cenário: Fazer login com dados corretamente
		Dado que acesso como visitante
		E que está na página inicial
		E possuo uma conta cadastrada com dados conforme abaixo:
			|  NOME             |  USERNAME |  EMAIL               |  SENHA        |
			|  Anderson Carlos  |  anderson |  anderson@gmail.com  |  anderson123  |
		Quando clico no botão "Login"
		E preencho os dados conforme abaixo:
			|  USERNAME |  SENHA     |
			|  paulo    |  paulo123  |
		Então estárei na pagina "Login efetuado com sucesso!"