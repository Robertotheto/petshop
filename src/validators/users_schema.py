from marshmallow import Schema, fields, validate, ValidationError

class UsersRegisterSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=3))
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.Length(min=6))

def validate_user_data(data):
    schema = UsersRegisterSchema()
    if errors := schema.validate(data):
        raise ValidationError(errors)
    