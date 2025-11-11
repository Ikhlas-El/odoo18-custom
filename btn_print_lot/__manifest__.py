{
    'name': 'Lot Label Print',
    'version': '1.0',
    'category': 'Manufacturing',
    'summary': 'Print lot labels directly from Manufacturing Orders',
    'depends': [
        'mrp',
        'stock',
        'lot_custom_fields',
    ],
    'data': [
        'views/mrp_production_views.xml',
    ],
    'installable': True,
    'application': False,
}