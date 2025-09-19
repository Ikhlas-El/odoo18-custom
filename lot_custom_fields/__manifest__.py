{
    'name': "Stock Lot Custom Fields",
    'version': '1.0',
    'depends': ['base', 'stock'],
    'author': "Ikhlas",
    'category': 'Inventory',
    'description': """
        Adds custom fields to stock.production.lot.
    """,
    'data': [
        'views/stock_lot_views.xml',
        'views/report_lot_label_inherit.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}