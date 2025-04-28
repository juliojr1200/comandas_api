import db
from sqlalchemy import Column, VARCHAR, CHAR, Integer, Float, LargeBinary

# ORM

class ProdutoDB(db.Base):
    __tablename__ = 'tb_produto'
    id_produto = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome_produto = Column(VARCHAR(100), nullable=False)
    descricao = Column(VARCHAR(300), nullable=False)
    foto = Column(LargeBinary, nullable=True)
    valor_unitario = Column(Float, nullable=True)
    def __init__(self, id_produto, nome_produto, descricao, foto, valor_unitario):
        self.id_produto = id_produto
        self.nome_produto = nome_produto
        self.descricao = descricao
        self.foto = foto
        self.valor_unitario = valor_unitario

from db import Base, engine