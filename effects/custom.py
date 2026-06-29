from flask import request

def custom():
    return {
        'w': request.args.get('w', default=100, type=int),
        'h': request.args.get('h', default=100, type=int),
        'x': request.args.get('x', default=0, type=int),
        'y': request.args.get('y', default=0, type=int),
        
        'content': request.args.get('content', default=''),
        'linespace': request.args.get('linespace', default=10, type=int),

        'color': request.args.get('color', default='black'),
        'bgcolor': request.args.get('bgcolor', default='white'),

        'border': request.args.get('border', default='#000'), # border color
        'border_width': request.args.get('border-width', default=0, type=int),
        'border_radius': request.args.get('border-radius', default=0, type=int),
    }
