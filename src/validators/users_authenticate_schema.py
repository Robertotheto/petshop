from marshmallow import Schema, fields, validate, ValidationError

class UsersAuthenticateSchema(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.Length(min=6))

def validate_user_authenticate_data(data):
    schema = UsersAuthenticateSchema()
    if errors := schema.validate(data):
        raise ValidationError(errors)
    