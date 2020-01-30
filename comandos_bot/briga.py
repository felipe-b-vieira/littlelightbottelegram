
#função responsável por gerar a briga
def briga(update, context):
	entidadesMensagem = update.message.parse_entities(types='mention')
	print(entidadesMensagem)
	
	membrosDaBriga = []
	
	for nomes in entidadesMensagem.values():
		print(nomes)
		membrosDaBriga.append(nomes)
		
	update.message.reply_text(membrosDaBriga[0]+" bateu em "+membrosDaBriga[1])