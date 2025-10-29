from odoo import models, fields, api
import unicodedata
import re

class CoffeeOrigin(models.Model):
    _name = 'coffee.origin'
    _description = 'Coffee Origin'
    _order = 'name'

    name = fields.Char(string='Country', required=True)
    code = fields.Char(string='Code', readonly=True, copy=False)

    _sql_constraints = [
        ('code_unique', 'UNIQUE(code)', 'Origin code must be unique!')
    ]

    @api.model
    def create(self, vals):
        """Auto-generate a code if user created the record from a Many2one field"""
        if not vals.get('code') and vals.get('name'):
            # Remove accents and make uppercase
            name_clean = self._remove_accents(vals['name']).upper()
            name_clean = re.sub(r'[^A-Z]', '', name_clean)
            vals['code'] = name_clean[:3]  # Use first 3 letters as code
        return super().create(vals)

    def _remove_accents(self, text):
        if not text:
            return ""
        text = unicodedata.normalize('NFKD', text)
        return ''.join([c for c in text if not unicodedata.combining(c)])
