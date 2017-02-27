# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """Manage Trainings""",

    'description': """
        Open Academy modules for managing trainings:
            - training courses
            - training sessions
            - attendees registration
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','board'],

    # always loaded
    'data': [
        'views/session_board.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/openacademy.xml',
        'views/partner.xml',
        'views/session_workflow.xml',
        'reports.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

