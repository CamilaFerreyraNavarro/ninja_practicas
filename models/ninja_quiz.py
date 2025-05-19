from odoo import models, fields

class SurveySurvey(models.Model):
    _inherit = 'survey.survey'

    kahoot_code = fields.Char(string='Kahoot Code')

class SurveyQuestion(models.Model):
    _inherit = 'survey.question'

    kahoot_timer = fields.Integer(string='Kahoot Timer (segundos)', default=30)
