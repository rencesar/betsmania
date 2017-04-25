#language: pt
Funcionalidade: Login no sistema
	
	Como visitante
	Afim de fazer login no sistema
	Devo ser capaz de entrar na minha conta

	Contexto: Conta cadastrada
		Dado que possuo uma conta cadastrada com dados conforme abaixo:
			|  NOME             |  USERNAME |  EMAIL               |  SENHA     |
			|  Anderson Carlos  |  anderson |  anderson@gmail.com  |  senha123  |


	Cenário: Fazer login com dados corretos
		Dado que acesso a página inicial
		E que acesso como visitante
		E preencho os dados de login conforme abaixo:
			|  USERNAME  |  SENHA     |
			|  anderson  |  senha123  |
		Quando clico no botão "Entrar"
		Então estárei na página "Login efetuado com sucesso!"


	Cenário: Fazer login com dados incorretos
		Dado que acesso a página inicial
		E que acesso como visitante
		E preencho os dados de login conforme abaixo:
			|  USERNAME  |  SENHA      |
			|  anderson  |  senha1233  |
		Quando clico no botão "Entrar"
		Então estárei na página "Por favor, entre com um usuário e senha corretos."
