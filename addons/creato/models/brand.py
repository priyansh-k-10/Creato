from odoo import models, fields


class CreatoBrand(models.Model):
    _name = 'creato.brand'
    _description = 'Brand'

    name = fields.Char(string="Name", required=True)
    product_name = fields.Char(string="Product Name")
    location = fields.Char(string="Location")
    email = fields.Char(string="Email")
    active = fields.Boolean(string="Active", default=True)
