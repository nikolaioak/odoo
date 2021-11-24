# -*- coding: utf-8 -*-
# Custom extension for Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Estate',
    'depends': [
        'base',
    ],
    'data': [
    	'security/ir.model.access.csv',
    	
    	'views/estate_property_offer_views.xml',
        'views/estate_property_views.xml',
    	'views/estate_property_type_views.xml',
    	'views/estate_property_tag_views.xml',
    	'views/estate_menus.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3'
}
