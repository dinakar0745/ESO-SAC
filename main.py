from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('test.html')

@app.route('/search', methods=['POST'])
def search_and_open_pdf():
    co = request.form['co']
    activity = request.form['activity']
    roll_number = request.form['rollNumber']

    # Construct the file path for the PDF using the submitted roll number
    pdf_file_name = f'certs/{co}/{activity}/{roll_number}.pdf'
    pdf_file_path = os.path.join(app.root_path, pdf_file_name)

    if os.path.isfile(pdf_file_path):
        print(f"PDF Path: {os.path.abspath(pdf_file_path)}")
        return send_from_directory(app.root_path, pdf_file_name)
    else:
        return "PDF not found for the given roll number."

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
