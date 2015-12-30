import datetime
from flask import url_for
from cardbox import db

class Card(db.Document):
  created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
  name = db.StringField()
  card_id = db.StringField()
  url = db.StringField()
  store_url = db.StringField()
  types = db.StringField()
  subtypes = db.StringField()
  colors = db.StringField()
  cmc = db.IntField()
  cost = db.StringField()
  text = db.StringField()
  power = db.IntField()
  toughness = db.IntField()
  formats = db.StringField()
  editions = db.StringField()
  loyalty = db.StringField()
  supertypes = db.StringField()

  def display(self):
  	return '{} {}/{}'.format(self.name, self.power, self.toughness)


