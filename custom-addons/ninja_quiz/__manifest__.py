{
    'name': 'Ninja Quiz',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Kahoot quiz game con Survey',
    'author': 'Camila',
    'license': 'LGPL-3',
    'depends': ['survey'],
    'data': [
        'security/ir.model.access.csv',
        'views/ninja_survey_quiz_views.xml',
        'views/ninja_quiz_menus.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
