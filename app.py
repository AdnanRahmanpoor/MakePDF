from flask import Flask, render_template, request, send_file
from flask_cors import CORS
from weasyprint import HTML
import os
import json

app = Flask(__name__)
CORS(app)

if not os.path.exists('uploads'):
    os.makedirs('uploads')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_pdf', methods=['POST'])
def generate_pdf():
    data = request.get_json()  # Get JSON data from request
    content = data['content']  # This should now be HTML
    
    # Wrap content in a container
    wrapped_content = f"<div class='container'>{content}</div>"
    
    pdf_file_path = 'uploads/output.pdf'

    # Generate PDF from HTML content using WeasyPrint
    HTML(string=wrapped_content, base_url=request.url_root).write_pdf(pdf_file_path, optimize_images=True, jpeg_quality=60, dpi=150)
    
    return send_file(pdf_file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)