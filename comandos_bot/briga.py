from mongoengine import *
import os

#senha para verificar se pode adicionar
senha_admin = os.environ.get('SENHAADMINTELEGRAM', None)

	
class TextoBriga(Document):
	acao = StringField(required=True, max_length=300)
	quantUsuarios = IntField(required=True, max_length=20)
	
#função responsável por gerar a briga
def briga(update, context):
	entidadesMensagem = update.message.parse_entities(types='mention')
	
	
	#pega as menções e transforma em nomes
	membrosDaBriga = []
	for nomes in entidadesMensagem.values():
		membrosDaBriga.append(nomes)

	#verifica a quantidade de menções para poder decidir o que vai fazer
	quantidadeNaBriga = len(membrosDaBriga)
	#se a quantidade for 0, não marcou ninguem então a pessoa se bate, escolhe o que não marca ninguem e o que tem uma marcação no meio
	if(quantidadeNaBriga==1):
		brigaAtual = TextoBriga.objects.filter(quantUsuarios_lte=1).aggregate( [ { "$sample": { size: 1 } } ])
		if(not brigaAtual == None):
			update.message.reply_text(brigaAtual.acao)
		else:
			update.message.reply_text("Você bateu em si mesmo, bom trabalho")
	
	#marcou apenas uma pessoa, então tem que escolher outra aleatóriamente
	elif(quantidadeNaBriga==1):
		brigaAtual = TextoBriga.objects.filter(quantUsuarios=2).aggregate( [ { "$sample": { size: 1 } } ])
		usuarioAleatorio = Usuarios.objects.filter(username_ne=update.message.from_user.username).aggregate( [ { "$sample": { size: 1 } } ])
		if(not brigaAtual == None):
			textosBrigas = brigaAtual.acao.split("\X")
			update.message.reply_text(textosBrigas[0]+membrosDaBriga[0]+textosBrigas[1]+usuarioAleatorio+textosBrigas[2])
		else:
			update.message.reply_text("Aqui vai ser feito um aleatório com outras pessoas, ainda não está pronto")
			
	#aqui tem duas pessoas marcas, então escolhe as duas e mostra a mensagem
	elif(quantidadeNaBriga==2):
		brigaAtual = TextoBriga.objects.filter(quantUsuarios=2).aggregate( [ { "$sample": { size: 1 } } ])
		if(not brigaAtual == None):
			textosBrigas = brigaAtual.acao.split("\X")
			update.message.reply_text(textosBrigas[0]+membrosDaBriga[0]+textosBrigas[1]+membrosDaBriga[1]+textosBrigas[2])
		else:
			update.message.reply_text(membrosDaBriga[0]+" bateu em "+membrosDaBriga[1])
			
	#mais que três pessoas então é briga em grupo, escolhe a mensagem apropriada e usa um for para gerar a mensagem
	elif(quantidadeNaBriga>2):
		brigaAtual = TextoBriga.objects.filter(quantUsuarios=quantidadeNaBriga).aggregate( [ { "$sample": { size: 1 } } ])
		if(not brigaAtual == None):
			textosBrigas = brigaAtual.acao.split("\X")
			i=0
			textoFinal=""
			for texto in textosBrigas:
				textoFinal+=texto+membrosDaBriga[i]
				i+=1
			update.message.reply_text(textoFinal)
		else:
			update.message.reply_text("Aqui vai ser porradaria em grupo, ainda não está pronto")
		
		
#função responsável por adicionar uma nova briga
def adiciona_briga(update, context):
	textoAtual = update.message.text
	textoAtual = textoAtual.split(" ", 1)
	if(len(textoAtual)>1):
		textoAtual = textoAtual[1].split("@")
		senha = textoAtual[0]
		if(senha_admin==senha):
			textoDividido = textoAtual[1].split("\X")
			tamTextoDividido = len(textoDividido)
			if(tamTextoDividido>0):
				brigaDB = TextoBriga(acao = textoAtual[1])
				brigaDB.quantUsuarios = tamTextoDividido-1
				brigaDB.save()
				update.message.reply_text("Comando salvo")
			else:
				update.message.reply_text("Mensagem inválida")
		else:
			update.message.reply_text("Senha incorreta")
	else:
		update.message.reply_text("Mensagem inválida")