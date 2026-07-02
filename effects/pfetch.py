from flask import request
import json

def pfetch():
    query = request.args.get

    username = query('username', default='undefined')
    hostname = query('hostname', default='localhost')

    osname = query('os', default='')
    host = query('host', default='undefined')
    kernel = query('kernel', default='undefined')
    uptime = query('uptime', default='0m')
    pkgs = query('pkgs', default=0)
    memory = query('memory', default='undefined')

    fetched = (f'{username}@{hostname}', f'os     {osname}', f'host   {host}', f'kernel {kernel}', f'uptime {uptime}', f'pkgs   {pkgs}', f'memory {memory}')

    prompt = query('prompt', default='')

    with open("assets/pfetch.json") as f:
        logos = json.load(f)

    content = f'{prompt}\n' if prompt else ''
    if not osname in logos:
        content += 'invalid os name'
    else:
        logo = logos["arch"]
        for i in range(0, max(len(logo), len(fetched))):
            content += f'{logo[i] or ''}   {fetched[i] or ''}\n' 
    

    return {
        'w': query('w', default=100, type=int),
        'h': query('h', default=100, type=int),
        'x': query('x', default=0, type=int),
        'y': query('y', default=0, type=int),
        
        'content': content,
        'linespace': query('linespace', default=20, type=int),

        'color': query('color', default='black'),
        'bgcolor': query('bgcolor', default='white'),

        'border': query('border', default='#000'), # border color
        'border_width': query('border-width', default=0, type=int),
        'border_radius': query('border-radius', default=0, type=int),
    }