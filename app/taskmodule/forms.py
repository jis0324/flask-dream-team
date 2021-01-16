from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from ..models import TaskHeader,TaskLine


class TaskForm(FlaskForm):
    """
    Form to Create or Edit a Task
    """
    title = StringField('Title', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')


class TaskLineForm(FlaskForm):
    """
    Form for admin to assign departments and roles to employees
    """
    task_id = QuerySelectField(query_factory=lambda: TaskHeader.query.all(),
                                  get_label="description")
 
    description = StringField('Description', validators=[DataRequired()])
    done = BooleanField('done') 
    submit = SubmitField('Submit')