
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
		update.message.reply_text("Você bateu em si mesmo, bom trabalho")
	elif(quantidadeNaBriga==1):
		update.message.reply_text("Aqui vai ser feito um aleatório com outras pessoas, ainda não está pronto")
	elif(quantidadeNaBriga==2):
		update.message.reply_text(membrosDaBriga[0]+" bateu em "+membrosDaBriga[1])
	elif(quantidadeNaBriga==3):
		update.message.reply_text("Aqui vai ser porradaria em grupo, ainda não está pronto")