from mongoengine import *

	
class Usuario(Document):
    id = IntField(required=True, max_length=200)
    is_bot = BooleanField(required=True, default = False)
    username = StringField( max_length=200)
    full_name = StringField(required=True, max_length=200)

#função responsável por salvar o usuário no banco de dados(AINDA SEM PROTEÇÂO DE QUANTIDADE)
def salva_usuario(update, context):
	console.log(update.message.from_user)
	console.log(update.message.from_user())
	usuarioAtual = update.message.from_user
	
	usuarioDB = Usuario(id=usuarioAtual.id)
	usuarioDB.is_bot = usuarioAtual.is_bot
	usuarioDB.username = usuarioAtual.username
	usuarioDB.full_name = usuarioAtual.full_name
	usuarioDB.save()