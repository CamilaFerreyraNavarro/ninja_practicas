{
    'name': 'Ninja Quiz',
    'version': '1.0',
    'category': 'Survey',
    'summary': 'Clon de Kahoot basado en Survey',
    'depends': ['survey', 'website'],
    'data': [
        'views/ninja_quiz_views.xml',
        'static/src/xml/ninja_quiz_templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'ninja_quiz/static/src/css/ninja_quiz.css',
            'ninja_quiz/static/src/xml/ninja_quiz_templates.xml',
            'ninja_quiz/static/src/js/ninja_timer.js',
            'ninja_quiz/static/src/js/ninja_chart.js'
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}


