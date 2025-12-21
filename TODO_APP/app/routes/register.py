from flask import Blueprint,request,render_template,redirect,url_for,flash,session
from app.models import User
from app import db
register_bp=Blueprint('register',__name__)

@register_bp.route('/register',methods=["GET","POST"])
def register():
    if request.method=="POST":
        username=request.form.get('username')
        password1=request.form.get('password1')
        password2=request.form.get('password2')
        if password1 != password2:
            flash("two passwords must be equal",'info')
            return render_template('register.html')
        elif User.query.filter_by(username=username).first():
            flash("username already exists try another",'info')
            return render_template('register.html')
        else:
            user=User(username=username,password=password1)
            db.session.add(user)
            db.session.commit()
            flash("registration successfull login with your credintals",'success')
            return redirect(url_for('auth.login'))
    return render_template('register.html')

