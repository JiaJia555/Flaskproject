from wtforms import Form, FileField, StringField
from wtforms.validators import InputRequired
from flask_wtf.file import FileAllowed, FileRequired

class UploadForm(Form):
    # FileRequired 必须要上传
    # FileAllowed 允许上传的类型
    image_file = FileField(validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif'])])
    desc = StringField(validators=[InputRequired()])