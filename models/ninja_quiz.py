from odoo import models, fields, api
import random, string

class SurveySurvey(models.Model):
    _inherit = 'survey.survey'

    kahoot_code = fields.Char(string='Kahoot Code', copy=False, readonly=True, default='')

    @api.model
    def create(self, vals):
        # generar un código PIN de 6 dígitos 
        if not vals.get('kahoot_code'):
            vals['kahoot_code'] = ''.join(random.choices(string.digits, k=6))
        return super().create(vals)


class SurveyQuestion(models.Model):
    _inherit = 'survey.question'

    kahoot_timer = fields.Integer(string='Kahoot Timer (segundos)', default=30)
    score_points = fields.Integer(string='Puntos por respuesta', default=1000)
