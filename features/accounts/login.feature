#language: pt
Funcionalidade: Login no sistema
	
	Como visitante
	Afim de fazer login no sistema
	Devo ser capaz de entrar na minha conta preenchendo corretamente meus dados

	@wip
	Cenário: Fazer login com dados corretamente
		Dado que acesso a página inicial
		E que acesso como visitante
		E possuo uma conta cadastrada com dados conforme abaixo:
			|  NOME             |  USERNAME |  EMAIL               |  SENHA     |
			|  Anderson Carlos  |  anderson |  anderson@gmail.com  |  senha123  |
		Quando clico no link "Login"
		E preencho os dados de login conforme abaixo:
			|  USERNAME  |  SENHA     |
			|  anderson  |  senha123  |
		E clico no botão "Acessar"
		Então estárei na pagina "Login efetuado com sucesso!"