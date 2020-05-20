import os
from flask import Flask, request, render_template, send_from_directory, Response
from werkzeug.utils import secure_filename      # 给上传的图片规范命名
from forms import UploadForm
from werkzeug.datastructures import CombinedMultiDict

app = Flask(__name__)
# 绝对路径
# upload_path = os.path.join(os.path.dirname(__file__), 'images')

@app.route("/")
def index():
    res = Response('逻辑教育')
    res.set_cookie('username', 'futongxue', max_age=30)
    return res
    # return "首页"

@app.route("/upload/", methods=['GET','POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')
    else:
        # desc = request.form.get('desc')
        # image_file = request.files.get('image_file')
        # # print(image_file)
        # # print(type(image_file))
        # # 参数：路径 文件名
        # # images 1.jpg 木马文件  jpg png gig
        # # 验证问题 重命名问题 文件名字+日期+随机数 uuid
        # # image_file.save(upload_path, image_file.filename)
        # filename = secure_filename(image_file.filename)
        # image_file.save(os.path.join("images", filename))
        # CombinedMultiDict 可以传入多个参数
        form = UploadForm(CombinedMultiDict([request.form, request.files]))
        if form.validate():
            # desc = request.form.get('desc')
            # image_file = request.files.get('image_file')
            desc = form.desc.data
            image_file = form.image_file.data
            filename = secure_filename(image_file.filename)
            image_file.save(os.path.join("images", filename))
            return '文件上传成功'
        else:
            print(form.errors)
            return "fail"

# 通过路由访问图片  参数 文件目录 名字
@app.route("/images/<filename>")
def get_image(filename):
    return send_from_directory("images", filename)
if __name__=="__main__":
    app.run(debug=True)


