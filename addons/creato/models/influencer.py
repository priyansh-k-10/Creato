from odoo import models, fields

class CreatoInfluencer(models.Model):
    _name = 'creato.influencer'
    _description = 'Influencer'

    name = fields.Char(string="Name", required=True)
    email = fields.Char(string="Email")
    insta_followers = fields.Float(float="Instagram Followers")
    insta_username = fields.Char(string="Intagram Username")
    active = fields.Boolean(string="Active", default=True)