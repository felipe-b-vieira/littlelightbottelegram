
#função responsável por gerar a briga
def briga(update, context):
	entidadesMensagem = update.message.parse_entities(types='mention')
	print(entidadesMensagem)
	
	membrosDaBriga = []
	
	for entid in entidadesMensagem:
		print(entid)
		print(entid.user)
		membrosDaBriga.append(entid.user)
		
	update.message.reply_text(membrosDaBriga[0].username+" bateu em "+membrosDaBriga[1].username)