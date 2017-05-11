#language: pt
Funcionalidade: Cadastro no sistema

	Como visitante
	Afim de criar uma conta no sistema
	Devo ser capaz de preencher meus dados e possuir uma conta

	Cenário: Criar uma conta de usuário
		Dado que acesso a página inicial
		E que acesso como visitante
		Quando clico no link "Registre-se"
		E preencho um formulário de cadastro de usuário conforme abaixo:
			|  NOME             |  USERNAME  |  EMAIL               |  SENHA     |
			|  Anderson Carlos  |  anderson  |  anderson@gmail.com  |  senha123  |
		E clico no botão "Cadastrar"
		Então estárei na página "Usuário cadastrado com sucesso!"
		E terei um usuário "anderson" cadastrado

	Cenário: Não é possivel criar uma conta de usuário com username já existente
		Dado possuo uma conta cadastrada com dados conforme abaixo:
			|  NOME        |  USERNAME  |  EMAIL                |
			|  Paulo João  |  anderson  |  paulojoao@gmail.com  |
		E que acesso a página inicial
		E que acesso como visitante
		Quando clico no link "Registre-se"
		E preencho um formulário de cadastro de usuário conforme abaixo:
			|  NOME             |  USERNAME  |  EMAIL               |  SENHA     |
			|  Anderson Carlos  |  anderson  |  anderson@gmail.com  |  senha123  |
		E clico no botão "Cadastrar"
		Então estárei na página "Um usuário com este nome de usuário já existe."
		E não terei usuário chamado "Anderson Carlos"
