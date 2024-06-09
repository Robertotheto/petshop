from marshmallow import Schema, fields, ValidationError

class PetsRegisterSchema(Schema):
    name = fields.Str(required=True)
    race = fields.Str(required=True)
    age = fields.Str(required=True)

def validate_pet_data(data):
    schema = PetsRegisterSchema()
    if errors := schema.validate(data):
        raise ValidationError(errors)
    