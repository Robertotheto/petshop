from flask import request, jsonify, Blueprint
from marshmallow import ValidationError
from flask_jwt_extended import jwt_required, get_jwt
from werkzeug.utils import secure_filename
from firebase_admin import storage
from src.composer.users_register_composer import users_register_composer
from src.composer.users_authenticate_composer import users_authenticate_composer
from src.composer.users_logout_composer import users_logout_composer
from src.composer.users_register_photo_composer import users_register_photo_composer
from src.composer.get_one_user_composer import get_one_user_composer
from src.validators.users_schema import validate_user_data
from src.validators.users_authenticate_schema import validate_user_authenticate_data

users_routes_bp = Blueprint('users', __name__)

@users_routes_bp.route('/create', methods=['POST'])
def create():
    data = request.json
    try:
        validate_user_data(data)
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        controller = users_register_composer()
        response, status_code = controller.register(name, email, password)
        return response, status_code
    except ValidationError as errors:
        formatted_errors = {field: ', '.join(
            messages) for field, messages in errors.messages.items()}
        return jsonify(formatted_errors), 400
@users_routes_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    try:
        validate_user_authenticate_data(data)
        email = data.get('email')
        password = data.get('password')
        controller = users_authenticate_composer()
        response, status_code = controller.authenticate(email, password)
        return response, status_code
    except ValidationError as errors:
        formatted_errors = {field: ', '.join(
            messages) for field, messages in errors.messages.items()}
        return jsonify(formatted_errors), 400

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@users_routes_bp.route('/upload', methods=['POST'])
@jwt_required()
def upload():
    user_id = get_jwt()['sub']
    if 'image' not in request.files:
        return {"error": "No image part"}, 400
    file = request.files['image']
    if file.filename == '':
        return {"error": "No selected file"}, 400
    if not allowed_file(file.filename):
        return {"error": "File type not allowed"}, 400
    user_folder = f'{user_id}'
    filename = secure_filename(f'{user_id}')
    image_path = f'{user_folder}/{filename}'
    bucket = storage.bucket()
    blob = bucket.blob(image_path)
    content_type = file.content_type
    blob.upload_from_file(file, content_type=content_type)

    image = blob.public_url
    controller = users_register_photo_composer()
    response, status_code = controller.register_photo(user_id, image)
    return response, status_code

@users_routes_bp.route('/one', methods=['GET'])
@jwt_required()
def get_one_user():
    user_id = get_jwt()['sub']
    controller = get_one_user_composer()
    response, status_code = controller.get_user(user_id)
    return response, status_code

@users_routes_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    jti = get_jwt()['jti']
    controller = users_logout_composer()
    response, status_code = controller.logout(jti)
    return response, status_code
