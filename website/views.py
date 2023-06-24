from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import  Center, person #,Notes
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    centers = Center.query.all()
    if request.method == 'POST': 
        aname = request.form.get('aname')
        name = request.form.get('cname')
        date = request.form.get('date')

        center = Center.query.filter_by(data=name).first()
        if center:
            if center.date==date:
                new_person = person(name=aname, cname=name, date=date)
                center.dose+=1
                db.session.add(new_person) #adding the note to the database 
                db.session.commit()
                flash('Vacination slot Booked successfully!', category='success')
            else:
                flash('That date is not available', category='error')
        else:
            flash('Center not available', category='error')  
    return render_template("home.html", user=current_user, centers=centers)


@views.route('/a', methods=['GET', 'POST'])
@login_required
def ahome():
    centers = Center.query.all()
    persons = person.query.all()
    if request.method == 'POST': 
        name = request.form.get('cname')
        date = request.form.get('date')
        wh = request.form.get('wh')

        center = Center.query.filter_by(data=name).first()
        if center:
            flash('Center already exists.', category='error')
        else:
            center = Center(data=name, date=date, wh=wh, dose=0)
            db.session.add(center)
            db.session.commit()
            flash('Center added!', category='success')


    return render_template("ahome.html", centers=centers , user=current_user, persons=persons)


# @views.route('/delete-note', methods=['POST'])
# def delete_note():  
#     note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
#     noteId = note['noteId']
#     note = Note.query.get(noteId)
#     if note:
#         if note.user_id == current_user.id:
#             db.session.delete(note)
#             db.session.commit()

    return jsonify({})

@views.route('/delete-center', methods=['POST'])
def delete_center():  
    center = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    centerId = center['centerId']
    center = Center.query.get(centerId)
    if center:
        # if center.user_id == current_user.id:
        db.session.delete(center)
        db.session.commit()

    return jsonify({})