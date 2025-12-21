from flask import Blueprint,render_template,request,redirect,session,flash,url_for
from app import db
from app.models import Task,User
tasks_bp=Blueprint('tasks',__name__)
@tasks_bp.route('/')
def view_tasks():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    tasks=Task.query.filter_by(user_id=session['user_id']).all()
    return render_template('task.html',tasks=tasks)
@tasks_bp.route('/add',methods=["POST"])
def add_task():
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    title=request.form.get('title')
    if title:
        new_task=Task(title=title,status="pending",user_id=session['user_id'])
        db.session.add(new_task)
        db.session.commit()
        flash("task added",'success')
    return redirect(url_for('tasks.view_tasks'))
@tasks_bp.route('/toggle/<int:task_id>',methods=["POST"])
def toggle_status(task_id):
    task=Task.query.filter_by(id=task_id,user_id=session['user_id']).first()
    if task:
        if task.status=="pending":
            task.status="working"
        elif task.status=="working":
            task.status="done"
        else:
            task.status="pending"
        db.session.commit()
    return redirect(url_for('tasks.view_tasks'))
@tasks_bp.route('/clear/<int:task_id>',methods=["POST"])
def clear_tasks(task_id):
    task=Task.query.filter_by(id=task_id,user_id=session['user_id']).first()
    if task:
        db.session.delete(task)
        db.session.commit()
        flash(f" task {task_id} cleared",'info')
    return redirect(url_for('tasks.view_tasks'))

