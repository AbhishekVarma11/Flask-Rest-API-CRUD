from flask import Flask
from flask_restful import Api,Resource

app=Flask(__name__)
api=Api(app)
names={"abhishek":{"age":23,"gender":"male"},
       "guru":{"age":90,"gender":"male"}}


class Helloworld(Resource):
    def get(self,name):
        return names[name]
    def post(self):
        return {"data":"data posted"}
api.add_resource(Helloworld,"/helloworld/<string:name>")

  
if __name__=="__main__":
    app.run(debug=True)
