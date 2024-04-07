from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
from PIL import Image, ImageDraw, ImageFont
import time
import requests

app = Flask(__name__)

# Folder to store uploaded and generated images
UPLOAD_FOLDER = 'static/images'
GENERATED_FOLDER = 'static/generated'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['GENERATED_FOLDER'] = GENERATED_FOLDER

@app.route('/')
def home():
    # List images in the upload folder to display in the gallery
    images = os.listdir(app.config['GENERATED_FOLDER'])
    images = [img for img in images if img.endswith(".jpg")]
    return render_template('index.html', images=images)

@app.route('/generate', methods=['GET', 'POST'])
def generate():
    if request.method == 'POST':
        image_path = ""
        # Handle image upload or selection
        if 'file' in request.files:
            file = request.files['file']
            if file.filename != '':
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                file.save(filepath)
                image_path = filepath
            else:
                image_path = os.path.join(app.config['UPLOAD_FOLDER'], request.form.get('backdrop'))
        else:
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], request.form.get('backdrop'))

        # Add text to image
        image = Image.open(image_path)
        draw = ImageDraw.Draw(image)
        toptext = request.form.get('toptext', '')

        font = ImageFont.truetype("/app/static/FreeMono.ttf", 50)

        ascent, descent = font.getmetrics()
        toptextwidth = font.getmask(toptext).getbbox()[2]
        toptextheight = font.getmask(toptext).getbbox()[3] + descent

        width, height = image.size
        x = (width - toptextwidth) / 2
        y = 10
        draw.text((x, y), toptext, font=font, fill="white")

        bottomtext = request.form.get('bottomtext', '')
        ascent, descent = font.getmetrics()
        bottomtextwidth = font.getmask(bottomtext).getbbox()[2]
        bottomtextheight = font.getmask(bottomtext).getbbox()[3] + descent

        width, height = image.size
        x = (width - bottomtextwidth) / 2
        y = height - bottomtextheight - 20
        draw.text((x, y), bottomtext, font=font, fill="white")

        # Save the edited image
        output_path = os.path.join(app.config['GENERATED_FOLDER'], '%s.jpg'%time.time_ns())
        image.save(output_path)
        return redirect(url_for('home'))

    # Display form to upload or select an image and add text
    backdrops = os.listdir(app.config['UPLOAD_FOLDER'])
    backdrops = [img for img in backdrops if img.endswith(".jpg")]
    return render_template('generate.html', backdrops=backdrops)

@app.route('/loadImage', methods=['POST'])
def loadImage():
    # Ensure that the request contains a JSON body
    if not request.is_json:
        return "Error: Request must be JSON", 400

    data = request.get_json()
    image_url = data.get('imageURL', '')

    if not image_url:
        return "Error: No imageURL provided", 400

    try:
        blacklist = ["localhost", "127.0.0.1", "admin"]

        for b in blacklist:
            if b in image_url:
                return "Error: Your request was blocked for security reasons"

        # Make a GET request to the imageURL
        response = requests.get(image_url)

        # Check if the request was successful
        if response.status_code == 200:
            return response.text
        else:
            return "Error: Failed to download the image", 500

    except requests.exceptions.RequestException as e:
        # Handle any exceptions that occur during the request to the image URL
        return str(e), 500
        #return "Error", 500

@app.route('/admin')
def admin():
    if request.remote_addr != '127.0.0.1':
        return "Error: Access denied", 403
    return "swampCTF{SSRF_15_n0_Jok3!!1}"

@app.route('/uploads/<filename>')
def upload(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
