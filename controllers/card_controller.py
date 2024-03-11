from flask import Blueprint
from init import db
from model.card import Card, cards_schema

cards_bp = Blueprint('cards', __name__, url_prefix='/cards')

@cards_bp.route('/')
def get_all_cards():
    stmt = db.session.query(Card).order_by(Card.date.desc())
    cards = stmt.all()
    return cards_schema.dump(cards)
    
    #stmt = db.select(Card).order_by(Card.date.desc())
    #cards = db.session.scalar(stmt)
    #return card_schema.dump(cards)