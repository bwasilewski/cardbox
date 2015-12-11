from flask import Blueprint, request, redirect, render_template, url_for
from flask.ext.mongoengine.wtf import model_form
from flask.views import MethodView
from cardbox.models import Card

cards = Blueprint('cards', __name__, template_folder='templates')

class ListView(MethodView):
	def get(self):
		cards = Card.objects.all()
		return render_template('cards/list.html', cards=cards)

class AddView(MethodView):

    form = model_form(Card, exclude=['created_at'])

    def get_context(self):
        form = self.form(request.form)

        context = {
            "form": form
        }
        return context

    def get(self):
        context = self.get_context()
     	return render_template('cards/add.html', **context)

    def post(self):
        context = self.get_context()
        form = context.get('form')

        if form.validate():
            card = Card()
            form.populate_obj(card)

            card.save()

            cards = Card.objects.all()
            return redirect(url_for('cards.list', cards=cards))

        return render_template('cards/add.html', **context)

# Register the urls
cards.add_url_rule('/cards/', view_func=ListView.as_view('list'))
cards.add_url_rule('/addcard/', view_func=AddView.as_view('addcard'))