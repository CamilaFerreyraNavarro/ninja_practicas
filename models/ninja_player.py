from odoo import models, fields

class SurveyPlayer(models.Model):
    _name = 'ninja_quiz.player'
    _description = 'Jugador de Ninja Quiz'

    name = fields.Char(string="Nombre del jugador", required=True)
    session_id = fields.Many2one('survey.user_input', string="Sesión", required=True)
    points = fields.Integer(string="Puntos", default=0)
