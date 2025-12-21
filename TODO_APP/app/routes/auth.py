from flask import Blueprint,request,render_template,redirect,url_for,flash,session
from app.models import User
auth_bp=Blueprint('auth',__name__)

@auth_bp.route('/login',methods=["GET","POST"])
def login():
    if request.method=="POST":
        username=request.form.get('username')
        password=request.form.get('password')
        user=User.query.filter_by(username=username).first()
        if user and user.password == password:
            session['user']=user.username
            session['user_id']=user.id
            flash("login successful",'success')
            return redirect(url_for('tasks.view_tasks'))
        else:
            flash("invalid credintials register if you are a new user",'danger')
    return render_template('login.html')
@auth_bp.route('/logout')
def logout():
    session.pop('user',None)
    session.pop('user_id',None)
    flash("Logged out",'info')
    return redirect(url_for('auth.login'))

