from odoo import models, fields

class CreatoInfluencer(models.Model):
    _name = 'creato.influencer'
    _description = 'Influencer'

    name = fields.Char(string="Name", required=True)
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    active = fields.Boolean(string="Active", default=True)