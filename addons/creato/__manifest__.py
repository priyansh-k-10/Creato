{
    'name': 'Creato',
    'version': '1.0',
    'depends': ['base'],
    'summary': 'Core models and shared backend logic for Creato',
    'description': """
Creato Core
===========

This module provides the foundational backend models, views,
and shared logic for the Creato platform.

It is designed as a technical base module that can be extended
by other Creato modules such as website, operations, and integrations.
""",
    'author': 'Priyansh Khatri',
    'license': 'LGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'views/menus.xml',
    ],
    'application': True,
    'installable': True,
}
