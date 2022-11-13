# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class schrute_bucks(models.Model):
    _inherit = 'purchase.order'

    schrute_bucks = fields.Char("Value in schrute bucks", required=True)

    @api.model
    def create(self, vals):
        if 'schrute_bucks' in vals:
            try:
                int(vals.get("schrute_bucks"))
            except ValueError as verr:
                raise ValidationError(f'Unable to convert {vals.get("schrute_bucks")}. Error: {verr}')
        return super().create(vals)
