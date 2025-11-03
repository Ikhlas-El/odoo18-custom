from odoo import models, api


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    def _generate_finished_moves(self):
        """Override to add production context for lot inheritance"""
        moves = super(MrpProduction, self)._generate_finished_moves()

        for move in moves:
            move = move.with_context(default_production_id=self.id)

        return moves

    def button_mark_done(self):
        """Override to ensure lot inheritance when production is completed"""
        res = super(MrpProduction, self).button_mark_done()

        for production in self:
            for move in production.move_finished_ids:
                if move.lot_ids:
                    # Get the first parent lot from raw materials
                    parent_lot = self._get_first_parent_lot(production)

                    if parent_lot:
                        for finished_lot in move.lot_ids:
                            if not finished_lot.x_origine_id and not finished_lot.x_espece:
                                finished_lot.write({
                                    'parent_lot_id': parent_lot.id,
                                    'x_origine_id': parent_lot.x_origine_id.id if parent_lot.x_origine_id else False,
                                    'x_espece': parent_lot.x_espece,
                                    'x_screen_size': parent_lot.x_screen_size,
                                })

        return res

    def _get_first_parent_lot(self, production):
        """Get the first parent lot from production raw materials"""
        cafe_vert = self.env.ref('coffee_maturity.cafe-vert', raise_if_not_found=False)
        cafe_pese = self.env.ref('coffee_maturity.cafe-pese', raise_if_not_found=False)

        for raw_move in production.move_raw_ids:
            if raw_move.lot_ids:
                for consumed_lot in raw_move.lot_ids:
                    if (cafe_vert and consumed_lot.product_id.categ_id == cafe_vert) or \
                            (cafe_pese and consumed_lot.product_id.categ_id == cafe_pese):
                        return consumed_lot  # Return the first matching lot found
        return False