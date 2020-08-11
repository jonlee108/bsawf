from flask import (
    Blueprint,
    flash,
    redirect,
    request,
    url_for,
    render_template)

from snakeeyes.blueprints.contact.forms import ContactForm
from snakeeyes.blueprints.contact.forms import FeedbackForm

contact = Blueprint('contact', __name__, template_folder='templates')

@contact.route('/contact', methods=['GET', 'POST'])
def index():
    form = ContactForm()

    if form.validate_on_submit():
        # This prevents circular imports.
        from snakeeyes.blueprints.contact.tasks import deliver_contact_email

        deliver_contact_email.delay(request.form.get('email'),
                                    request.form.get('message'))

        flash('Thanks, expect a response shortly.', 'success')
        
        print("HELLO FROM CONTACT")
        
        return redirect(url_for('contact.index'))

    return render_template('contact/index.html', form=form)

@contact.route('/feedback', methods=['GET', 'POST'])
def feedback():
    form = FeedbackForm()
    print("kjsckljsakljdsa")

    if form.validate_on_submit():
        # This prevents circular imports
        from snakeeyes.blueprints.contact.tasks import deliver_feedback_email

        print(f"request 09129d {request}")

        deliver_feedback_email.delay(
            request.form.get('email'),
            request.form.get('message'), 
            request.form.get('nps'))
                                    
        flash('Thanks, expect a response to your feedback shortly.', 'success')

        return redirect(url_for('contact.feedback'))
        
    return render_template('contact/feedback.html', form=form)
    