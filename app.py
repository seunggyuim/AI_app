import os
from flask import Flask, render_template, flash, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'files'
ALLOWED_EXTENSIONS = {'m4a', 'mp3'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
           
@app.route('/')
    #get voice file from the web 
def upload_file():
    return render_template('index.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_files():
   if request.method == 'POST':

      if 'file' not in request.files:
            flash('No file part!')
            return redirect(request.url)
            
      file = request.files['file']      
      if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
       
      if  file and allowed_file(file.filename):
          filename = secure_filename(file.filename)
          file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
          return 'file uploaded successfully'

if __name__ == '__main__':
   app.run(debug = True)


