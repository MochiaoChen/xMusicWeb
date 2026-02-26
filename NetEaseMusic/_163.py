# coding=utf-8
'''
@author: comwrg
@license: MIT
@time : 2017/05/25 14:12
@desc : 
'''
import requests, json

def getList(url):
    '''

    :param url: 
    :return: [(歌名, 歌手, 专辑), ...]
    '''
    id_start = url.find('id=')
    if id_start == -1:
        # Try to find id in path if it's like /playlist/123
        # But for now assume id parameter exists as per original code assumption
        return []

    id = url[id_start+len('id='):]
    if '&' in id:
        id = id.split('&')[0]

    url = 'https://music.163.com/api/v6/playlist/detail'
    data = {'id': id, 'n': 1000, 's': 8}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Referer': 'https://music.163.com/',
        'Cookie': 'os=pc'
    }

    r = requests.post(url, data=data, headers=headers)
    data = json.loads(r.text)

    l = []
    if 'playlist' in data and 'tracks' in data['playlist']:
        for track in data['playlist']['tracks']:
            songname = track['name']

            artistsname = ''
            for artist in track['ar']:
                artistsname += artist['name'] + '/'
            artistsname = artistsname[:-1]
            # print artistsname

            albumname = track['al']['name']
            l.append((songname, artistsname, albumname))
    return l



if __name__ == '__main__':
    l = getList('http://music.163.com/#/playlist?id=98176052')
    print(len(l))
    if len(l) > 0:
        print(l[0])
