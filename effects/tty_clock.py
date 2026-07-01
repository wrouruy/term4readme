from flask import request
import requests

num2ascii = {
    '0': [
        '██████',
        '██  ██',
        '██  ██',
        '██  ██',
        '██████'
    ], '1': [
        '    ██',
        '    ██',
        '    ██',
        '    ██',
        '    ██'
    ], '2': [
        '██████',
        '    ██',
        '██████',
        '██    ',
        '██████'
    ], '3': [
        '██████',
        '    ██',
        '██████',
        '    ██',
        '██████',
    ], '4': [
        '██  ██',
        '██  ██',
        '██████',
        '    ██',
        '    ██'
    ], '5': [
        '██████',
        '██    ',
        '██████',
        '    ██',
        '██████'
    ], '6': [
        '██████',
        '██    ',
        '██████',
        '██  ██',
        '██████'
    ], '7': [
        '██████',
        '    ██',
        '    ██',
        '    ██',
        '    ██'
    ], '8': [
        '██████',
        '██  ██',
        '██████',
        '██  ██',
        '██████'
    ], '9': [
        '██████',
        '██  ██',
        '██████',
        '    ██',
        '██████'
    ], ':': [
        '    ',
        ' ██ ',
        '    ',
        ' ██ ',
        '    '
    ]
}

def tty_clock():
    query = request.args.get

    timezone = query('timezone', default='America/New_York')
    prompt = query('prompt', default='')

    try:
        response = requests.get(f'https://timeapi.io/api/time/current/zone?timeZone={timezone}', timeout=5)
        
        if response.ok:
            data = response.json()
            current_time = data['time']
            full_time = data['dateTime'][:data['dateTime'].find('T')] 

        else:
            current_time = None
            
    except requests.exceptions.RequestException:
        current_time = None

    
    content = f'{prompt}\n' if prompt else ''
    if current_time:
        for i in range(0, 5):
            for char in current_time:
                content += num2ascii[char][i] + ' '
            content += '\n'
        
        content += f'\n            {full_time}'
    else:
        content += 'invalid timeZone'

    return {
        'w': query('w', default=100, type=int),
        'h': query('h', default=100, type=int),
        'x': query('x', default=0, type=int),
        'y': query('y', default=0, type=int),

        'content': content,
        'linespace': query('linespace', default=10, type=int),

        'color': query('color', default='black'),
        'bgcolor': query('bgcolor', default='white'),

        'border': query('border', default='#000'), # border color
        'border_width': query('border-width', default=0, type=int),
        'border_radius': query('border-radius', default=0, type=int),
    }