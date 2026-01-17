# sistemas de gestión empresarial.

##  Modelos practica 602
### #### Modelo socio.

```python 
# -*- coding: utf-8 -*-

from odoo import models, fields, api
 
class socio(models.Model):
    _name = 'library.socio'
    _description = 'library.socio'
    nombre_socio = fields.Char(string = "nombre_socio", required = True)        
    apellidos_socio = fields.Char(string ="apellidos_socio", required = True)
 
    fecha_nac = fields.Date()
    libros = fields.Many2many(
        comodel_name = 'library.libro',
        string='Libros'
    )
    ```


#### Modelo autor: 

```python 
# -*- coding: utf-8 -*-

from odoo import models, fields, api
 
class autor(models.Model):
    _name = 'library.autor'
    _description = 'library.autor'
 
    nombre_autor = fields.Char()
 
    fecha_nac = fields.Date()
 
 
    libros = fields.Char()
 
    biografia = fields.Char()
    ```

#### Modelo libro:  

```python 
# -*- coding: utf-8 -*-

from odoo import models, fields, api
 
class libro(models.Model):
    #nombre modulo nombre modelo
    _name = 'library.libro'
    _description = 'library.libro'
 

# Nombre
# Autor, nuevamente, este campo debería estar relacionado con el tro modelo. Por ahora lo dejaremos de tipo char
# Fecha de publicación
# ISBN
# Sinopsis
    nombre_libro = fields.Char( string = "titulo", required=True)     
    autor_id = fields.Many2one(
        comodel_name="library.author",
        string="Autor",
        ondelete="restrict",
        required=True,
    )#el genero del libro.
    genero = fields.Selection(
        selection=[
            ("novela", "Novela"),
            ("drama", "Drama"),
            ("ciencia_ficcion", "Ciencia ficción"),
            ("misterio", "Misterio"),
            ("terror", "Terror"),
            ("historico", "Histórico"),
        ],
        string="Género",
        required=True,
    )#el socio que lo tiene 
    id_socio  = fields.Many2many(
        comodel_name="library.socio",
        relation="prestamos_realizados",
        column1="titulo_libro",
        column2="id_socio",
        string="Socios que lo tienen prestado",
    )

```