{
    'name': 'Creato Core',
    'version': '1.0.0',
    'category': 'Custom',
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

    'depends': [
        'base',
    ],

    'data': [
        'security/ir.model.access.csv',
        'views/creato_base_views.xml',
        'models/models.py',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}
