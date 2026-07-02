from flask import request

def custom():
    query = request.args.get

    return {
        'w': query('w', default=100, type=int),
        'h': query('h', default=100, type=int),
        'x': query('x', default=0, type=int),
        'y': query('y', default=0, type=int),
        
        'content': query('content', default=''),
        'linespace': query('linespace', default=20, type=int),

        'color': query('color', default='black'),
        'bgcolor': query('bgcolor', default='white'),

        'border': query('border', default='#000'), # border color
        'border_width': query('border-width', default=0, type=int),
        'border_radius': query('border-radius', default=0, type=int),
    }
