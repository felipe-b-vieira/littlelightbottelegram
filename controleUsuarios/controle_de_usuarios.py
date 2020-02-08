from mongoengine import *

	
class Usuarios(Document):
    idTelegram = IntField(required=True, max_length=200, primary_key=True)
    is_bot = BooleanField(required=True, default = False)
    username = StringField( max_length=200)
    full_name = StringField(required=True, max_length=200)

#função responsável por salvar o usuário no banco de dados(AINDA SEM PROTEÇÂO DE QUANTIDADE)
def salva_usuario(update, context):
	usuarioAtual = update.message.from_user
	if not Usuarios.objects(idTelegram=usuarioAtual.id):
		usuarioDB = Usuarios(idTelegram =usuarioAtual.id)
		usuarioDB.is_bot = usuarioAtual.is_bot
		usuarioDB.username = usuarioAtual.username
		usuarioDB.full_name = usuarioAtual.full_name
		usuarioDB.save()