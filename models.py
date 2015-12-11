import datetime
from flask import url_for
from cardbox import db

class Card(db.Document):
  created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
  name = db.StringField()

  def display(self):
  	return '{}'.format(self.name)