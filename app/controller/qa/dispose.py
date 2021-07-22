from flask import jsonify

from . import qa


@qa.route('/test', methods=['GET'])
def test():
    print(123123)
    return jsonify({'tasks': "123123123"})
