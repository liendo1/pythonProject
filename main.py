from flask import Flask,request,send_from_directory,jsonify
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['IMAGE_FOLDER'] = os.path.abspath('.')+'\\images\\'
ALLOWED_EXTENSIONS=set(['png','jpg','jpeg','gif'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS

@app.route('/api/upload',methods=['POST'])
def upload_file():
    if request.method=='POST':
        for k in request.files:
            file = request.files[k]

            image_urls = []
            if file and allowed_file(file.filename):
                filename=secure_filename(file.filename)
                file = file.save(os.path.join(app.config['IMAGE_FOLDER'],filename))
                print("images/"+filename)
                path = "images/"+filename
                image_urls.append("images/%s"%filename)

        return jsonify("images/"+filename)

#static
@app.route("/images/<imgname>",methods=['GET'])
def images(imgname):
    return send_from_directory(app.config['IMAGE_FOLDER'],imgname)

if __name__ == "__main__":
    # IMAGE_FOLDER
    if not os.path.exists(app.config['IMAGE_FOLDER']):
        os.mkdir(app.config['IMAGE_FOLDER'])
    app.run(host="192.168.0.14", port=5000, debug=True)