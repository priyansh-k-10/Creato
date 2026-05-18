from odoo import models, fields
class CreatoInfluencer(models.Model):
    _name = 'creato.influencer'
    _description = 'Influencer'

    name = fields.Char(string="Name", required=True)
    email = fields.Char(string="Email")
    insta_followers = fields.Char(string="instagram Followers")
    insta_username = fields.Char(string="instagram Username")
    active = fields.Boolean(string="Active", default=True)

class ResPartner(models.Model):
    _inherit = 'res.partner'

    customer_code = fields.Char(string="Customer Code")