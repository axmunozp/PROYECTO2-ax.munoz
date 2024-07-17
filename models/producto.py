from abc import ABC, abstractmethod
from db import db
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base



Base = declarative_base()

class Productos(db.Model, Base):
    __tablename__ = 'productos'

    id = db.Column(Integer, primary_key=True)
    tipo = db.Column(String(50), nullable=False)
    nombre = db.Column(String(100), nullable=False)
    precio_publico = db.Column(Integer, nullable=False)
    tipo_vaso = db.Column(String(50))
    volumen = db.Column(Integer)
    
    # Definición de las relaciones con los ingredientes
    ingrediente1_id = db.Column(db.Integer, db.ForeignKey('ingredientes.id'), nullable=False)
    ingrediente2_id = db.Column(db.Integer, db.ForeignKey('ingredientes.id'), nullable=False)
    ingrediente3_id = db.Column(db.Integer, db.ForeignKey('ingredientes.id'), nullable=False)
    
    # Relaciones con la clase Ingrediente
    ingrediente1 = db.relationship("Ingredientes", foreign_keys=[ingrediente1_id])
    ingrediente2 = db.relationship("Ingredientes", foreign_keys=[ingrediente2_id])
    ingrediente3 = db.relationship("Ingredientes", foreign_keys=[ingrediente3_id])

    def calcular_costo(self) -> str:
        precios = 0
        for ingrediente in self.ingredientes:
            precios += ingrediente.get_precio()
        return ("Costo del producto: $" + str(precios))

    def calcular_calorias(self)->str:
        calorias = 0
        for ingrediente in self.ingredientes:
            calorias += ingrediente.get_calorias()
        return("Calorias totales: ") + str(round(calorias * 0.95,2))

    
    def calcular_rentabilidad(self)->str:
        precios_ingredientes = 0
        for ingrediente in self.ingredientes:
            precios_ingredientes += ingrediente.get_precio()
        rentabilidad = self.precio_publico - precios_ingredientes
        return ("Rentabilidad: $" + str(rentabilidad))
    
    ## Getters y Setters:

    def get_nombre(self) -> str:
        return self.nombre

    def set_nombre(self, nombre: str) -> None:
        self.nombre = nombre

    def get_precio_publico(self) -> int:
        return self.precio_publico

    def set_precio_publico(self, precio_publico: int) -> None:
        self.precio_publico = precio_publico

    def get_tipo_vaso(self) -> int:
        return self.tipo_vaso

    def set_tipo_vaso(self, tipo_vaso: int) -> None:
        self.tipo_vaso = tipo_vaso
    
    def get_ingredientes(self)->list:
        return [
        self.ingrediente1.nombre if self.ingrediente1 else None,
        self.ingrediente2.nombre if self.ingrediente2 else None,
        self.ingrediente3.nombre if self.ingrediente3 else None,
        ]

    def set_ingredientes(self, ingredientes: list) -> None:
        self.ingredientes = ingredientes
    

    
    
