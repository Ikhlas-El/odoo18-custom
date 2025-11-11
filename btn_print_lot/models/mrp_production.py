from odoo import models
from odoo.exceptions import UserError


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    def _get_report_base_filename(self):
        """Override filename for lot label printing"""
        self.ensure_one()
        if self.lot_producing_id:
            return f'Lot-{self.lot_producing_id.name}'

        # Raise error if trying to print lot label without a lot
        raise UserError(
            "Aucun lot assigné à cet ordre de fabrication. "
            "Veuillez d'abord définir un numéro de lot dans le champ 'Lot/Numéro de série' "
            "avant d'imprimer l'étiquette."
        )