from flask import Flask, render_template, request
import this, conexao

db_connection = conexao.conexao()
con = db_connection.cursor()

App = Flask(__name__)  #Representando uma variável do tipo flask

def cadastrar(cpf,nome,senha,telefone,endereco,dataDeNascimento):
    try:
        sql = "insert into cliente(cpf,nome,senha,telefone,endereco,dataDeNascimento) values('{}', '{}','{}', '{}', '{}', '{}')".format(cpf,nome,senha,telefone,endereco,dataDeNascimento)
        con.execute(sql)
        db_connection.commit()
        return con.rowcount, "Inserido"
    except Exception as erro:
        return erro
def consultar(CPF):
    try:
        sql = "select * from cliente where CPF = '{}'".format(CPF)
        con.execute(sql)

        this.msg = ""
        this.msg = "Nenhum dado Encontrado!"
        for(CPF, nome, senha, telefone, endereco, dataDeNascimento) in con:
            if int(CPF) == int(CPF):
                this.msg = "Código: {}, Nome: {}, Senha: {}, Telefone: {}, Endereço: {}, Data de Nascimento: {}".format(CPF, nome, senha, telefone, endereco, dataDeNascimento)
                return this.msg
        return this.msg
    except Exception as erro:
        return erro
def atualizar(CPF, campo, novoDado):
    try:
        sql = "update cliente set {} = '{}' where CPF = '{}'".format(campo, novoDado, CPF)
        con.execute(sql)
        db_connection.commit()
        return "".format(con.rowcount)
    except Exception as erro:
        return erro
def excluir(CPF):
    try:
        sql = "delete from cliente where CPF = '{}'".format(CPF)
        con.execute(sql)
        db_connection.commit()
        return "".format(con.rowcount)
    except Exception as erro:
        return erro