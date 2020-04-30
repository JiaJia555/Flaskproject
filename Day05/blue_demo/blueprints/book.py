from flask import Blueprint, url_for

book_bp = Blueprint('book', __name__, url_prefix="/book")

@book_bp.route("/")
def book():
    print(url_for("book.book_detail", bid=3))
    return "图书首页"


@book_bp.route("/detail/<bid>")
def book_detail(bid):
    return "图书的ID %s" % bid