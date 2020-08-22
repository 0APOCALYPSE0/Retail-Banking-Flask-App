from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField, SelectField, RadioField
from wtforms.validators import DataRequired, Length, EqualTo

class AddCustomerForm(FlaskForm):
    ssnid = StringField('Customer SSN Id', validators=[DataRequired(), Length(min=9, max=9)])
    name = StringField('Customer Name', validators=[DataRequired()])
    age = StringField('Age', validators=[DataRequired()])
    add = TextAreaField('Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    submit = SubmitField('Submit')

class EditCustomerForm(FlaskForm):
    name = StringField('New Customer Name', validators=[DataRequired()])
    age = StringField('New Age', validators=[DataRequired()])
    add = TextAreaField('New Address', validators=[DataRequired()])
    city = StringField('New City', validators=[DataRequired()])
    state = StringField('New State', validators=[DataRequired()])
    submit = SubmitField('Update')

class DeleteCustomerForm(FlaskForm):
    submit = SubmitField('Delete')

class AddAccountForm(FlaskForm):
    customerid = StringField('Customer ID', validators=[DataRequired(), Length(min=9, max=9)])
    accType = SelectField('Account Type', choices=[('S', 'Saving'), ('C', 'Current')], validators=[DataRequired()])
    depositeAmount = IntegerField('Deposite Amount', validators=[DataRequired()])
    submit = SubmitField('Submit')

class DeleteAccountForm(FlaskForm):
    submit = SubmitField('Delete')

class DepositeForm(FlaskForm):
    deposite = IntegerField('Deposite Amount', validators=[DataRequired()])
    submit = SubmitField('Submit')

class WithdrawForm(FlaskForm):
    withdraw = IntegerField('Withdraw Amount', validators=[DataRequired()])
    submit = SubmitField('Submit')

class TransferForm(FlaskForm):
    sourceAcc = SelectField('Source Account Type', choices=[], validators=[DataRequired()])
    targetAcc = SelectField('Target Account Type', choices=[], validators=[DataRequired()])
    transfer = IntegerField('Transfer Amount', validators=[DataRequired()])
    submit = SubmitField('Submit')

class StatementForm(FlaskForm):
    accid = SelectField('Account ID', choices=[], validators=[DataRequired()])
    stmtOption = RadioField('Choose Option', choices=[('trans', 'Last No Of Transaction'), ('date', 'Start End Date')], validators=[DataRequired()])
    transNo = SelectField('Last Number Of Transacion', choices=[(1, '1'),(2, '2'),(3, '3'),(4, '4'),(5, '5'),(6, '6'),(7, '7'),(8, '8'),(9, '9'),(10,'10')], validators=[DataRequired()])
    startDate = SelectField('Start Date', choices=[], validators=[DataRequired()])
    endDate = SelectField('End Date', choices=[], validators=[DataRequired()])
    submit = SubmitField('Submit')

class SearchForm(FlaskForm):
    custId = StringField('Customer ID')
    accId = StringField('Account ID')
    submit = SubmitField('Search')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')