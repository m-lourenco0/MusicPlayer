import pafy
import vlc
import time

player_list = []

class YouTubePlayerAppService():
    FLAG = True

    def yt_player(yt_id):
        try:
            s_url = 'https://www.youtube.com/watch?v=' + yt_id
            video = pafy.new(s_url)
            best = video.getbestaudio()
            YouTubePlayerAppService.player_queue({'Music': best.title, 'Url': best.url, 'Duration': video.duration})
            return {'Status': True, 'Video': f'{best.title}',  'message': 'Success adding music to playlist.'}
        except Exception as e:
            print(e)
    
    def player_queue(yt_id):
        player_list.append(yt_id)

    def player_stop():
        YouTubePlayerAppService.FLAG = 'Stop'
        return {'Status': True, 'Message': 'Stopped player.'}

    def player_next():
        YouTubePlayerAppService.FLAG = 'Next'
        return {'Status': True, 'Message': 'Next music player.'}

    def get_playlist():
        list = []
        for music in player_list:
            list.append({'Music': music['Music'], 'Duration': music['Duration']})
        return list

    def get_current_playing():
        return {'Music': player_list[0]['Music'], 'Duration': player_list[0]['Duration']}

    def player_start():
        YouTubePlayerAppService.FLAG = True
        return {'Status': True, 'Message': 'Music player started.'}

    def player_engine():
        try:
            while(True):
                time.sleep(2)
                if(YouTubePlayerAppService.FLAG == True):
                    if (len(player_list) > 0):
                        music, duration = player_list[0]['Music'], player_list[0]['Duration']
                        print(f'Music : {music} Duration: {duration}')

                        VLCMediaPlayer.player_start(player_list[0])
                        player_list.pop(0)

                        if(YouTubePlayerAppService.FLAG == 'Next'):
                            YouTubePlayerAppService.FLAG = True
                elif(YouTubePlayerAppService.FLAG == 'Stop'):
                    break
        except Exception as e:
            print(e, flush=True)

    # player_engine()

class VLCMediaPlayer():

    def player():
        player = vlc.MediaPlayer()
        player.play()

    def player_start(media):
        player = vlc.MediaPlayer(media['Url'])
        player.play()
        time.sleep(5)
        while(player.is_playing()):
            time.sleep(2)
            if((YouTubePlayerAppService.FLAG != True)):
                player.stop()
                break