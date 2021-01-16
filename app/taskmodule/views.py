# app/taskmodule/views.py

from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import taskmodule
from .forms import TaskForm, TaskLineForm
from .. import db
from ..models import TaskHeader, TaskLine


def check_admin():
    """
    Prevent non-admins from accessing the page
    """
    if not current_user.is_admin:
        abort(403)


# Taskmodule Views


@taskmodule.route('/tasks', methods=['GET', 'POST'])
@login_required
def list_tasks():
    """
    List all tasks
    """
    #check_admin()

    tasks = TaskHeader.query.all()

    return render_template('taskmodule/tasks.html',
                           mytasks=tasks, title="Tasks")

@taskmodule.route('/tasks/add', methods=['GET', 'POST'])
@login_required
def add_task():
    """
    Add a task to the database
    """
    #check_admin()

    add_task = True

    
    form = TaskForm()
    if form.validate_on_submit():
        task = TaskHeader(title=form.title.data,
                                description=form.description.data)
        try:
            # add Task to the database
            db.session.add(task)
            db.session.commit()
            flash('You have successfully added a new Task.')
        except:
            # in case Task name already exists
            flash('Error: task already exists.')

        # redirect to departments page
        return redirect(url_for('taskmodule.list_tasks'))

    # load department template
    return render_template('taskmodule/task.html', action="Add",
                           add_task=add_task, form=form,
                           title="Add Task")

@taskmodule.route('/tasks/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_task(id):
    """
    Edit a task
    """
    #check_admin()

    add_task = False

    task = TaskHeader.query.get_or_404(id)
    form = TaskForm(obj=task)
    if form.validate_on_submit():
        task.title = form.title.data
        task.description = form.description.data
        db.session.commit()
        flash('You have successfully edited the task.')

        # redirect to the departments page
        return redirect(url_for('taskmodule.list_tasks'))

    form.title.data = task.title
    form.description.data = task.description
    return render_template('taskmodule/task.html', action="Edit",
                           add_task=add_task, form=form,
                           task=task, title="Edit Department")


@taskmodule.route('/tasks/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_task(id):
    """
    Delete a task from the database
    """
    #check_admin()

    task = TaskHeader.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    flash('You have successfully deleted the department.')

    # redirect to the departments page
    return redirect(url_for('taskmodule.list_tasks'))

    return render_template(title="Delete Task")


