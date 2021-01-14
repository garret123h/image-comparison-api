from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
import cv2
import numpy 

app = Flask(__name__)
api = Api(app)

class img_comp(Resource):

    @app.route('/<id>/',methods=['GET'])
    def get(self, id):
        images = request.get_json()
        image_one = cv2.imread(images['image-one'], 0)
        image_two = cv2.imread(images['image-two'], 0)

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
    app.run(debug=True)
