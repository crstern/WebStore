from flask import Flask, request, jsonify, make_response
from flask_mongoengine import MongoEngine
from flask_cors import CORS
from marshmallow import Schema, fields, post_load
from bson import ObjectId

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'authors',
    'host': 'db',
    'port': 27017,
    'alias': 'default',
    'username': 'root',
    'password': 'pass'
}
CORS(app)
db = MongoEngine(app)

Schema.TYPE_MAPPING[ObjectId] = fields.String


class Authors(db.Document):
    name = db.StringField()
    specialisation = db.StringField()


class AuthorsSchema(Schema):
    name = fields.String(required=True)
    specialisation = fields.String(required=True)


@app.route('/authors', methods = ['GET'])
def index():
    get_authors = Authors.objects.all()
    author_schema = AuthorsSchema(many=True, only=['name', 'specialisation'])
    authors = author_schema.dump(get_authors)
    return make_response(jsonify({"authors": authors}))

@app.route('/authors', methods=['POST'])
def create_author():
    data = request.get_json()
    author = Authors(name=data['name'], specialisation=data['specialisation'])
    author.save()
    author_schema = AuthorsSchema(only=['name', 'specialisation'])
    authors = author_schema.dump(author)
    print(authors)
    return make_response(jsonify({"author": authors}))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)