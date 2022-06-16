from dataclasses import field, fields
import string
from odoo import models, fields

#creando un modelo (tabl ade la base de datos) a partir de una clase
class Libros(models.Model):
    _name = 'libros' #nombre de la tabla aque se va a generar 
    
    name = fields.Char(string="nombre del libro") #nombre del campo que es de tipo cadena