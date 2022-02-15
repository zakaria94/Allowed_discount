{
    'name': 'Allowed Discount',
    'summary': """ 
       My Allowed Discount Module addons
    """,
    'depends': ['sale_management', 'account_accountant', 'purchase'],
    'description': 'Allowed Discount module',
    'author': 'zakariya',
    'data': [
        'views/account_view.xml',
        'views/res_partner_view.xml',
        'views/purchase_order_form_view.xml',
        'views/my_order_sale_view.xml',
        'views/account_move.xml'

    ],
    'installable': True,
    'auto_install': False,
    'licence': 'LGPL-3'
}