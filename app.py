from flask import Flask, request, jsonify
from crud import create_rule, get_all_rules, update_rule, delete_rule
from models import create_tables
from service import rule_to_dict

app = Flask(__name__)

create_tables()


"""Rule creation endpoint"""

@app.route('/rule', methods=['POST'])
def add_rule():
    try:
        data = request.get_json()
        input_format = data.get('input_format')
        output_format = data.get('output_format')
        flags = data.get('flags')

        new_rule = create_rule(input_format, output_format, flags)
        return jsonify(rule_to_dict(new_rule)), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400


"""Getting all rules endpoint"""

@app.route('/rules', methods=['GET'])
def get_rules():
    try:
        rules = get_all_rules()
        return jsonify([rule_to_dict(rule) for rule in rules])
    except Exception as e:
        return jsonify({'error': str(e)}), 500


"""Updating a rule endpoint"""

@app.route('/rule/<int:rule_id>', methods=['PUT'])
def update_rule_by_id(rule_id):
    try:
        data = request.get_json()
        input_format = data.get('input_format')
        output_format = data.get('output_format')
        flags = data.get('flags')

        updated_rule = update_rule(rule_id, input_format, output_format, flags)
        if updated_rule:
            return jsonify(rule_to_dict(updated_rule))
        else:
            return jsonify({'message': 'Rule not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400


"""Deleting a rule endpoint"""

@app.route('/rule/<int:rule_id>', methods=['DELETE'])
def delete_rule_by_id(rule_id):
    try:
        deleted_rule = delete_rule(rule_id)
        if deleted_rule:
            return jsonify(rule_to_dict(deleted_rule))
        else:
            return jsonify({'message': 'Rule not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)