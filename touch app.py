from flask import Flask, render_template, request, send_file
import os
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)
UPLOAD_FOLDER = 'static/images'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    images = [f for f in os.listdir(UPLOAD_FOLDER) if allowed_file(f)]
    return render_template('index.html', images=images)

@app.route('/generate_meme', methods=['POST'])
def generate_meme():
    image_name = request.form['image']
    text = request.form['text']
    top_text = request.form.get('top_text', '')
    bottom_text = request.form.get('bottom_text', '')

    image_path = os.path.join(UPLOAD_FOLDER, image_name)
    image = Image.open(image_path).convert('RGB')
    draw = ImageDraw.Draw(image)
    try:
        font = ImageFont.truetype("arial.ttf", 40)  # Fontu belirtin
    except IOError:
        font = ImageFont.load_default()

    def draw_text(text, position):
        width, height = draw.textsize(text, font=font)
        x, y = position
        draw.rectangle([x, y, x + width, y + height], fill=(0, 0, 0))
        draw.text((x, y), text, font=font, fill=(255, 255, 255))

    if top_text:
        draw_text(top_text, (10, 10))
    if bottom_text:
        draw_text(bottom_text, (10, image.height - 50))

    output_path = os.path.join(UPLOAD_FOLDER, f'meme_{image_name}')
    image.save(output_path)
    return send_file(output_path, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)
