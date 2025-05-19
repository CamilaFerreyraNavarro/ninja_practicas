{
    'name': 'Ninja Quiz',
    'version': '1.0',
    'category': 'Survey',
    'summary': 'Clon de Kahoot basado en Survey',
    'depends': ['survey'],
    'data': [
        'views/ninja_quiz_views.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'ninja_quiz/static/src/css/ninja_quiz.css',
            'ninja_quiz/static/src/xml/ninja_quiz_templates.xml',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}


