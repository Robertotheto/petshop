from flask import request, jsonify, Blueprint
from marshmallow import ValidationError
from flask_jwt_extended import jwt_required, get_jwt
from werkzeug.utils import secure_filename
from firebase_admin import storage
from src.composer.pets_register_composer import pets_register_composer
from src.composer.pet_update_photo_composer import pet_update_photo_composer
from src.composer.get_one_pet_composer import get_one_pet_composer
from src.validators.pets_schema import validate_pet_data

pets_routes_bp = Blueprint('pets', __name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@pets_routes_bp.route('/create', methods=['POST'])
@jwt_required()
def create():
    data = request.json
    try:
        validate_pet_data(data)
        name = data.get('name')
        race = data.get('race')
        age = data.get('age')
        user_id = get_jwt()['sub']
        controller = pets_register_composer()
        response, status_code = controller.register(name, race, age, user_id)
        return response, status_code
    except ValidationError as errors:
        formatted_errors = {field: ', '.join(
            messages) for field, messages in errors.messages.items()}
        return jsonify(formatted_errors), 400
@pets_routes_bp.route('/update/photo/<pet_id>', methods=['PUT'])
@jwt_required()
def update_photo(pet_id):
    if 'image' not in request.files:
        return {"error": "No image part"}, 400
    file = request.files['image']
    if file.filename == '':
        return {"error": "No selected file"}, 400
    if not allowed_file(file.filename):
        return {"error": "File type not allowed"}, 400
    user_id = get_jwt()['sub']
    user_folder = f'{user_id}'
    filename = secure_filename(f'{pet_id}')
    image_path = f'{user_folder}/pets/{filename}'
    bucket = storage.bucket()
    blob = bucket.blob(image_path)
    content_type = file.content_type
    blob.upload_from_file(file, content_type=content_type)

    image = blob.public_url
    controller = pet_update_photo_composer()
    response, status_code = controller.pet_update_photo(pet_id, image)
    return response, status_code
@pets_routes_bp.route('/<pet_id>', methods=['GET'])
@jwt_required()
def get_one_pet(pet_id):
    controller = get_one_pet_composer()
    response, status_code = controller.get_pet(pet_id)
    return response, status_code
