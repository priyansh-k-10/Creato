from odoo import models, fields


class CreatoBrand(models.Model):
    _name = 'creato.brand'
    _description = 'Brand'

    name = fields.Char(string="Name", required=True)
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    active = fields.Boolean(string="Active", default=True)
