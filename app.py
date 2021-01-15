from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
from skimage import io
import functools, sys, cv2, numpy

app = Flask(__name__)
api = Api(app)

def ok_user_and_password(username, password):
    return username == app.config['USERNAME'] and password == app.config['PASSWORD']

def authenticate():
    message = {'message': "Authenticate."}
    resp = jsonify(message)

    resp.status_code = 401
    resp.headers['WWW-Authenticate'] = 'Basic realm="Main"'

    return resp

def requires_authorization(f):
    @functools.wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not ok_user_and_password(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

class img_comp(Resource):

    @app.route('/<id>/',methods=['GET'])
    @requires_authorization
    def get(self, id):
        images = request.get_json()
        image_one = image_two = None

        if "https://" in images["image-one"]:
            print('Doing something')
            image_one = io.imread(images["image-one"])
        else:
            image_one = cv2.imread(images["image-one"])
        if "https://" in images["image-two"]:
            image_two = io.imread(images["image-two"])
        else:
            image_two = cv2.imread(images["image-two"])

        comp_percent = self.compare_images(image_one, image_two)
        
        return jsonify(
                {'Percentage Comparison': str(comp_percent) + '%' }
                )

    def compare_images(self, image_one, image_two):
        diff = cv2.absdiff(image_one, image_two)
        diff = diff.astype(numpy.uint8)
        percentage_difference = (numpy.count_nonzero(diff) * 100 ) / diff.size

        return percentage_difference


api.add_resource(img_comp, '/comp/<id>/', '/comp/<id>')

if __name__ == '__main__':
    user = sys.argv[1]
    password = sys.argv[2]

    app.config['USERNAME']=user
    app.config['PASSWORD']=password

    app.run(debug=True)
