from odoo import models, fields 

class Survey(models.Model):
    _inherit = 'survey.survey'

    is_ninja_quiz = fields.Boolean(string="¿Es un Quiz?", default=False)