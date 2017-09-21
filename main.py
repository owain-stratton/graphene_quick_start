from flask import Flask, request
import graphene
import json

DEBUG = True
HOST = '0.0.0.0'
PORT = 8000

app = Flask(__name__)

class Query(graphene.ObjectType):
    hello = graphene.String(
        name=graphene.String(default_value="stranger"),
        age=graphene.Int()
    )

    def resolve_hello(self, info, name, age):
        return 'Hello {} you are {} years old'.format(name, age)

schema = graphene.Schema(query=Query)


@app.route('/graphql', methods=['POST'])
def hello():
    # print(dir(request))
    data = json.loads(request.data)
    return json.dumps(schema.execute(data['query']).data)

if __name__ == '__main__':
    # run app on http://localhost:8000
    app.run(debug=DEBUG, host=HOST, port=PORT)
