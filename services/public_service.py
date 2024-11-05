from flask import jsonify

def public_route():
    public_data = [
        {'id': 1, 'name': 'Apple', 'price':'$2'},
        {'id': 2, 'name': 'Orange', 'price':'$3'},
        {'id': 3, 'name': 'Banana', 'price':'$5'}
    ]
    return jsonify({'public_data': public_data}), 200
