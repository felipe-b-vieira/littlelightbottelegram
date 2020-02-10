from mongoengine import *

	
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
	if(quantidadeNaBriga==0):
		brigaAtual = TextoBriga.objects.filter(quantUsuarios=0).aggregate( [ { $sample: { size: 1 } } ])
		if(not brigaAtual == None):
			update.message.reply_text(brigaAtual.acao)
		else:
			update.message.reply_text("Você bateu em si mesmo, bom trabalho")
	elif(quantidadeNaBriga==1):
		update.message.reply_text("Aqui vai ser feito um aleatório com outras pessoas, ainda não está pronto")
	elif(quantidadeNaBriga==2):
		brigaAtual = TextoBriga.objects.filter(quantUsuarios=2).aggregate( [ { $sample: { size: 1 } } ])
		if(not brigaAtual == None):
			textosBrigas = brigaAtual.acao.split("\X")
			update.message.reply_text(textosBrigas[0]+membrosDaBriga[0]+textosBrigas[1]+membrosDaBriga[1]+textosBrigas[2])
		else:
			update.message.reply_text(membrosDaBriga[0]+" bateu em "+membrosDaBriga[1])
	elif(quantidadeNaBriga>3):
		brigaAtual = TextoBriga.objects.filter(quantUsuarios=quantidadeNaBriga).aggregate( [ { $sample: { size: 1 } } ])
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
	textoDividido = texto.split("\X")
	tamTextoDividido = len(textoDividido)
	if(tamTextoDividido>0):
		brigaDB = TextoBriga(acao = textoAtual)
		brigaDB.quantUsuarios = tamTextoDividido-1
		brigaDB.save()
	else:
		update.message.reply_text("Mensagem inválida")