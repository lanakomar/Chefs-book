from flask import Blueprint, request
from flask_login import login_required
from app.models import db, Note
from app.forms.note_form import NoteForm
from app.forms.delete_form import DeleteForm
from app.api.recipe_routes import validation_errors_to_error_messages

note_routes = Blueprint('notes', __name__)

@note_routes.route('/<int:id>', methods=["PUT"])
@login_required
def update_note(id):
    """
    Updates comment
    """

    form = NoteForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        note = Note.query.get(id)
        if note:
            note.content = form.data["content"]
            db.session.add(note)
            db.session.commit()
            return note.to_dict()
        else:
            return {'errors': ["Comment not found"]}, 404
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401
