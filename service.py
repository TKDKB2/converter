"""Transforming Rule object into dictionary to be serializable"""

def rule_to_dict(rule):
    return {
        'id': rule.id,
        'input_format': rule.input_format,
        'output_format': rule.output_format,
        'flags': rule.flags
    }