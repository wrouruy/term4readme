from flask import request
import svgwrite

def mk_svg(body):
    dwg = svgwrite.Drawing(size=(body['w'], body['h']))

    dwg.embed_font(name="JetBrainsMono", filename="assets/font/JetBrainsMono.ttf")

    dwg.add(
        dwg.rect(
            insert=(body['border_width'] / 2, body['border_width'] / 2),
            rx=body['border_radius'], ry=body['border_radius'],
            size=(body['w'] - body['border_width'], body['h'] - body['border_width']),
            fill=body['bgcolor'],
            stroke=body['border'],
            stroke_width=body['border_width']))

    for i, e in enumerate(body['content'].split('\n')):
        dwg.add(
            dwg.text(
                e,
                font_family="JetBrainsMono",
                insert=(body['x'], body['linespace'] * i + body['y']),
                fill=body['color'],
                style='white-space: pre;',
                **{'xml:space': 'preserve'}))
    return dwg.tostring()

