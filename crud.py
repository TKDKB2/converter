from models import Rule
from database import session


"""Rule creation"""

def create_rule(input_format, output_format, flags):
    new_rule = Rule(input_format=input_format, output_format=output_format, flags=flags)
    session.add(new_rule)
    session.commit()
    return new_rule


"""Getting all rules"""

def get_all_rules():
    return session.query(Rule).all()


"""Updating a rule"""

def update_rule(rule_id, input_format, output_format, flags):
    rule = session.query(Rule).get(rule_id)
    if rule:
        rule.input_format = input_format
        rule.output_format = output_format
        rule.flags = flags
        session.commit()
        return rule
    return None


"""Deleting a rule"""

def delete_rule(rule_id):
    rule = session.query(Rule).get(rule_id)
    if rule:
        session.delete(rule)
        session.commit()
        return rule
    return None
