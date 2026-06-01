from odoo import models, fields

class CreatoInfluencer(models.Model):
    _name = 'creato.influencer'
    _description = 'Influencer'

    name = fields.Char(string="Name", required=True)
    email = fields.Char(string="Email")
    insta_followers = fields.Char(string="Instagram Followers")
    insta_username = fields.Char(string="Instagram Username")
    active = fields.Boolean(string="Active", default=True)

    partner_id = fields.Many2one(
        'res.partner',
        string="Contact"
    )

    user_id = fields.Many2one(
        'res.users',
        string="User"
    )

class ResPartner(models.Model):
    _inherit = 'res.partner'

    customer_code = fields.Char(
        string="Customer Code"
    )