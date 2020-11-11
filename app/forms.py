from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField, DateField, BooleanField, HiddenField
from wtforms.validators import InputRequired, Optional, Email, EqualTo, Length


APPLY_REASONS = [
    ('invalid', "我不符合申请条件或资格"),
    ('participate', "本年度内参加小聚或其他 LUG 举办的活动 (*)"),
    ('lead', "主讲过小聚或 Linux User Party (*)"),
    ('article', "撰写过新闻稿或向 LUG Planet 投稿，并被审核通过或采纳 (*)"),
    ('other_affairs', "参与过其他 LUG 社团活动或事务 (*)"),
    ('ustc_staff', "是科大在职教工或博士后（请使用工号申请）"),
    ('lug_staff', "在 LUG 中担任过任意职务"),
]


class RegisterForm(FlaskForm):
    email = StringField('USTC Email', [InputRequired(), Email(), Length(max=63)])
    password = PasswordField('Password', [InputRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password', [InputRequired()])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = StringField('Email', [InputRequired(), Email(), Length(max=63)])
    password = PasswordField('Password', [InputRequired()])
    submit = SubmitField('Login')


class ApplyForm(FlaskForm):
    name = StringField('Name as on your campus card (e.g. 张三)', [InputRequired()])
    studentno = StringField('Student/Staff No. (eg. PB18000001)', [InputRequired()])
    phone = StringField('Phone', [InputRequired()])
    reasonClass = SelectField('Qualification', [InputRequired()], choices=APPLY_REASONS)
    reasonText = TextAreaField('For asterisk-marked reasons, please provide details below', [Optional()], render_kw={"placeholder": "Enter any extra information here"})
    agree = BooleanField('I have read and agree to the Terms of Service and the Constitution', id='agreeConstitution')
    submit_btn = SubmitField('Apply')


class ChangePasswordForm(FlaskForm):
    oldpassword = PasswordField('Current Password', [InputRequired()])
    password = PasswordField('New Password', [InputRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password', [InputRequired()])
    submit = SubmitField('Change Password')


class RecoverPasswordForm(FlaskForm):
    email = StringField('Email', [InputRequired(), Email(), Length(max=63)])
    submit = SubmitField('Recover Password')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('New Password', [InputRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password', [InputRequired()])
    token = HiddenField("token")
    submit = SubmitField('Submit')


class CreateForm(FlaskForm):
    email = StringField('Email', [InputRequired(), Email(), Length(max=63)])
    password = PasswordField('Password', [InputRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password', [InputRequired()])
    submit = SubmitField('Register')


class RejectForm(FlaskForm):
    rejectreason = TextAreaField('Reject reason', [InputRequired()])
    expiration = DateField('Expiration date', [Optional()])
    force = BooleanField('Force (Cancel existing service)', [Optional()])
    submit = SubmitField('Reject')


class BanForm(FlaskForm):
    banreason = TextAreaField('Ban reason', [InputRequired()])
    submit = SubmitField('Ban')


class MailForm(FlaskForm):
    subject = StringField('Subject', [InputRequired()])
    content = TextAreaField('Content', [InputRequired()])
    submit = SubmitField('Send')


class EditForm(FlaskForm):
    name = StringField('Name')
    studentno = StringField('Student/Staff No.')
    phone = StringField('Phone')
    submit = SubmitField('Save')
