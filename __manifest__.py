{
    'name': 'Azentra Delivery Line Weights',
    'version': '19.0.1.0.0',
    'category': 'Inventory/Delivery',
    'summary': 'Adds G.W and N.W to Delivery Lines and PDF',
    'description': """
        Custom module developed by Azentra Consulting.
        Adds Gross and Net weight to stock.move operations and the Delivery Slip PDF.
    """,
    'author': 'Azentra Consulting',
    'depends': ['stock'],
    'data': [
        'views/stock_picking_views.xml',
        'reports/delivery_slip_report.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}