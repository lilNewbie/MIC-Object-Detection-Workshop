from flask import Flask,render_template,request
from werkzeug.utils import secure_filename
import os
from ultralytics import YOLO
import cv2
import shutil

app=Flask(__name__)
app.config['UPLOAD_FOLDER']="static/input/"

@app.route('/') 
def index():
    return render_template('index.html')

ALLOWED_EXTENSTIONS={'mp4'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSTIONS

@app.route('/upload',methods=['POST'])
def upload():
    if 'video' not in request.files:
        return "No video file selected"
    
    video=request.files['video']
    
    if video.filename =="":
        return "Filename is empty"
    
    if video and allowed_file(video.filename):
        video.save(os.path.join(app.config['UPLOAD_FOLDER'],video.filename))
        
        mdl=YOLO("best.pt")
        r=mdl.predict(source="static/input/"+video.filename, project="static/output/", name="pred_"+video.filename, save=True)

        cap=cv2.VideoCapture("static/output/"+"pred_"+video.filename+"/"+video.filename)
        if (cap.isOpened()== False):
            print("Error opening video file")
        while (cap.isOpened()):
            ret,frame=cap.read()
            if ret==True:
                cv2.imshow('Frame',frame)
                if cv2.waitKey(25) & 0xFF==ord('q'):
                    break
            else:
                break
        cap.release()
        cv2.destroyAllWindows()
        os.remove("static/input/"+video.filename)
        return render_template('preview.html')
    
    return "Invalid file type"

if __name__=='__main__':
    app.run(debug=True)
