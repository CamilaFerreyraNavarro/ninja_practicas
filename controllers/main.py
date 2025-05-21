from odoo import http
from odoo.http import request

class NinjaQuizController(http.Controller):

    # resultados
    @http.route('/ninja_quiz/results/<int:user_input_id>', auth='public', website=True)
    def show_results(self, user_input_id):
        user_input = request.env['survey.user_input'].sudo().browse(user_input_id)
        if not user_input:
            return request.not_found()

        players = request.env['ninja_quiz.player'].sudo().search([
            ('session_id.survey_id', '=', user_input.survey_id.id)
        ], order='points desc')

        return request.render('ninja_quiz.template_results', {
            'players': players,
            'survey_title': user_input.survey_id.title
        })

    # unirse a una partida
    @http.route('/ninja_quiz/join', type='http', auth='public', website=True, methods=['POST'], csrf=False)
    def join_quiz(self, **post):
        pin = post.get('pin')
        name = post.get('player_name')

        # buscar encuesta por código
        survey = request.env['survey.survey'].sudo().search([('kahoot_code', '=', pin)], limit=1)
        if not survey:
            return request.render("website.404")  # O podrías hacer tu propia pantalla de "Código inválido"

        # crear entrada
        user_input = request.env['survey.user_input'].sudo().create({
            'survey_id': survey.id,
            'state': 'new',
        })

        # crear jugador
        request.env['ninja_quiz.player'].sudo().create({
            'name': name,
            'session_id': user_input.id,
            'points': 0,
        })

        # mandar a jugar
        return request.redirect(f"/survey/start/{survey.id}?user_input_id={user_input.id}")

    # lobby 

    @http.route('/ninja_quiz/lobby', auth='public', website=True)
    def show_lobby(self):
        return request.render('ninja_quiz.template_lobby')


    @http.route('/ninja_quiz/wait/<int:survey_id>', auth='public', website=True)
    def wait_quiz(self, survey_id):
        Survey = request.env['survey.survey'].sudo()
        Player = request.env['ninja_quiz.player'].sudo()
        survey = Survey.browse(survey_id)
        if not survey.exists():
            return request.not_found()
        # jugadores que hicieron login
        players = Player.search([('session_id.survey_id', '=', survey_id)])
        base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url')
        return request.render('ninja_quiz.template_wait', {
            'survey': survey,
            'players': players,
            'base_url': base_url,
        })