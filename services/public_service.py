from flask import jsonify

def public_route():
    public_data = [
        {'id': 1, 'name': 'Public Item 1'},
        {'id': 2, 'name': 'Public Item 2'},
        {'id': 3, 'name': 'Public Item 3'}
    ]
    return jsonify({'public_data': public_data}), 200
