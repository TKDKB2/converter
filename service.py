from models import Rule

"""Transforming Rule object into dictionary to be serializable"""

def rule_to_dict(rule: Rule) -> dict:
    return {
        'id': rule.id,
        'input_format': rule.input_format,
        'output_format': rule.output_format,
        'flags': rule.flags
    }