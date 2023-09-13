# -*- coding: utf-8 -*-
{
    'name': "Customer Order",

    'summary': """
        Module Order Brocin""",

    'description': """
        Manajemen Order
    """,

    'author': "Nendi",
    'website': "https::/nendi.cnt.id",

    'category': 'Uncategorized',
    'version': '0.1',

		# Depencicy
    'depends': ['base'],

		# Include ALL XML Code in Here be mindful of order
    'data': [
        'security/ir.model.access.csv',
        'views/menuitems.views.xml',
        'views/customer.views.xml'
    ],

    'installable': True,
    'application': True,
    'auto_install': False

}