from odoo import models, fields

class CreatoBrand(models.Model):
    _name = 'creato.brand'
    _description = 'Creato Brand' 

    name = fields.Char(string="Brand Name", required=True)
    description = fields.Text(string="Description")
