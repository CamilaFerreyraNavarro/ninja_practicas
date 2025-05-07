from odoo import models, fields

class NinjaQuiz(models.Model):
    _name = 'ninja.quiz'
    _description = 'Ninja Quiz'

    name = fields.Char(string='Quiz Name', required=True)
    description = fields.Text(string='Description')
    is_ninja_quiz = fields.Boolean(string="¿Es un Quiz?", default=False) 
    survey_id = fields.Many2one('survey.survey', string="Survey", required=True) 
