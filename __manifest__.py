{
    'name': 'Azentra Operations and Invoice Weights',
    'version': '19.0.2',
    'category': 'Inventory/Accounting',
    'summary': 'Adds Gross and Net weight flow to Deliveries and Invoices',
    'author': 'Azentra Consulting',
    'depends': ['stock', 'account'],
    'data': [
        'views/stock_picking_views.xml',
        'views/account_move_views.xml',
        'reports/delivery_slip_report.xml',
        'reports/invoice_report.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}