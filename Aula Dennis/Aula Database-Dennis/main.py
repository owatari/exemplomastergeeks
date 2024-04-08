from database import db

def criar(nome_pessoa,telefone_pessoa,email_pessoa):
    novo_contato = db.Contato(nome=nome_pessoa, telefone=telefone_pessoa, email=email_pessoa)
    db.session.add(novo_contato)
    db.session.commit()

def deletar(id):
    pessoa_deletada = db.session.get(db.Contato, id)
    db.session.delete(pessoa_deletada)
    db.session.commit()

def atualizar(id,nome_pessoa="",telefone_pessoa="",email_pessoa=""):
    pessoa_atualizada = db.session.get(db.Contato,id)

    if nome_pessoa:
        pessoa_atualizada.nome = nome_pessoa

    if telefone_pessoa:
        pessoa_atualizada.telefone = telefone_pessoa

    if email_pessoa:
        pessoa_atualizada.email = email_pessoa

    if nome_pessoa or telefone_pessoa or email_pessoa:
        db.session.commit()


def buscar(id=''):
    if id:
        return db.session.get(db.Contato, id)
    else: 
        return db.session.query(db.Contato).all()

#deletar(4)
#for pessoa in buscar():
#    print(pessoa)
    
atualizar(4, 'Lucas', "123123123", "lucas@example.com")
    
#criar("Rafael", "4899999999", "example@gmail.com")