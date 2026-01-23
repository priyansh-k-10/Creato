from odoo import models, fields, api


class CreatoBase(models.Model):
    _name = "creato.base"
    _description = "Creato Base Model"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "create_date desc"

    name = fields.Char(
        string="Name",
        required=True,
        tracking=True
    )

    active = fields.Boolean(
        default=True
    )

    description = fields.Text(
        string="Description"
    )

    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("active", "Active"),
            ("archived", "Archived"),
        ],
        string="Status",
        default="draft",
        tracking=True
    )

    create_uid = fields.Many2one(
        "res.users",
        string="Created By",
        readonly=True
    )

    create_date = fields.Datetime(
        string="Created On",
        readonly=True
    )

    write_uid = fields.Many2one(
        "res.users",
        string="Last Updated By",
        readonly=True
    )

    write_date = fields.Datetime(
        string="Last Updated On",
        readonly=True
    )

    def action_activate(self):
        for record in self:
            record.state = "active"

    def action_archive(self):
        for record in self:
            record.state = "archived"
