from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

names = {"tim": {"age":40,"gender":"Male"},
         "joe": {"age":38,"gender":"Female"},
         "marty": {"age":28,"gender":"Male"}}


class HelloWorld(Resource):
    def get(self):
        return "Hello world" #names[name]
    
    
api.add_resource(HelloWorld, "/hello")

if __name__ == "__main__":
    app.run(debug=True)