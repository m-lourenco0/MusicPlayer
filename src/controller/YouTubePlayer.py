from flask_classy import FlaskView, route
import json
from src.appservice.YouTubePlayerAppService import YouTubePlayerAppService


class YouTubePlayer(FlaskView):

    @route('/add/<yt_id>')
    def yt_player(self, yt_id):
        try:
            yt_player = YouTubePlayerAppService.yt_player(yt_id)
            return json.dumps(yt_player, default=str), 200
        except Exception as e:
            msg = {'msg': 'Exception error from Keypress.'}
            return json.dumps(msg), 500

    @route('/play')
    def player_start(self):
        try:
            yt_player = YouTubePlayerAppService.player_start()
            return json.dumps(yt_player, default=str), 200
        except Exception as e:
            msg = {'msg': 'Exception error from Keypress.'}
            return json.dumps(msg), 500

    @route('/stop')
    def player_stop(self):
        try:
            yt_player = YouTubePlayerAppService.player_stop()
            return json.dumps(yt_player, default=str), 200
        except Exception as e:
            msg = {'msg': 'Exception error from Keypress.'}
            return json.dumps(msg), 500

    @route('/next')
    def player_next(self):
        try:
            yt_player = YouTubePlayerAppService.player_next()
            return json.dumps(yt_player, default=str), 200
        except Exception as e:
            msg = {'msg': 'Exception error from Keypress.'}
            return json.dumps(msg), 500

    @route('/playlist')
    def playlist(self):
        try:
            yt_player = YouTubePlayerAppService.get_playlist()
            return json.dumps(yt_player, default=str), 200
        except Exception as e:
            msg = {'msg': 'Exception error from Keypress.'}
            return json.dumps(msg), 500

    @route('/current')
    def current(self):
        try:
            yt_player = YouTubePlayerAppService.get_current_playing()
            return json.dumps(yt_player, default=str), 200
        except Exception as e:
            msg = {'msg': 'Exception error from Keypress.'}
            return json.dumps(msg), 500

    @route('/start')
    def current(self):
        try:
            yt_player = YouTubePlayerAppService.player_engine()
            return json.dumps(yt_player, default=str), 200
        except Exception as e:
            msg = {'msg': 'Exception error from Keypress.'}
            return json.dumps(msg), 500