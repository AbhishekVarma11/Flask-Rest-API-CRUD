from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
import pymysql
from sqlalchemy.orm import sessionmaker


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/book_store'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
api = Api(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50), nullable=False)

# with app.app_context():
#     db.create_all()

class BookResource(Resource):
    def get(self, id=None):
        if id is None:
            books = Book.query.all()
            data = []
            for book in books:
                data.append({'id': book.id, 'title': book.title, 'author': book.author, 'genre': book.genre})
            return {'data': data}, 200
        else:
            book = Book.query.get(id)
            if book is not None:
                return {'id': book.id, 'title': book.title, 'author': book.author, 'genre': book.genre}, 200
            else:
                return {'message': 'Book not found'}, 404

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=True)
        parser.add_argument('author', type=str, required=True)
        parser.add_argument('genre', type=str, required=True)
        args = parser.parse_args()
        book = Book(title=args['title'], author=args['author'], genre=args['genre'])
        db.session.add(book)
        db.session.commit()
        return {'message': 'Book created successfully', 'id': book.id}, 201

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=True)
        parser.add_argument('author', type=str, required=True)
        parser.add_argument('genre', type=str, required=True)
        args = parser.parse_args()
        book = Book.query.get(id)
        if book is not None:
            book.title = args['title']
            book.author = args['author']
            book.genre = args['genre']
            db.session.commit()
            return {'message': 'Book updated successfully', 'id': book.id}, 200
        else:
            return {'message': 'Book not found'}, 404

    def delete(self, id):
        book = Book.query.get(id)
        if book is not None:
            db.session.delete(book)
            db.session.commit()
            return {'message': 'Book deleted successfully'}, 200
        else:
            return {'message': 'Book not found'}, 404

api.add_resource(BookResource, '/books', '/books/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
