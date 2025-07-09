
from flask_restx import Namespace, Resource, fields
from flask import request
from app.services import facade
from flask_jwt_extended import jwt_required, get_jwt_identity

api = Namespace('amenities', description='Amenity operations')

# Define the amenity model for input validation and documentation
amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Name of the amenity')
})

@api.route('/')
class AmenityList(Resource):
    @api.expect(amenity_model)
    @api.response(201, 'Amenity successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new amenity"""
        data = request.get_json()
        try:
            amenity = facade.create_amenity(data)
            return {"id": amenity.id, "name": amenity.name}, 201
        except Exception as e:
            return {"error": str(e)}, 400

    @api.response(200, 'List of amenities retrieved successfully')
    def get(self):
        """Retrieve a list of all amenities"""
        amenities = facade.get_all_amenities()
        return [{"id": a.id, "name": a.name} for a in amenities], 200

@api.route('/<amenity_id>')
class AmenityResource(Resource):
    @api.response(200, 'Amenity details retrieved successfully')
    @api.response(404, 'Amenity not found')
    def get(self, amenity_id):
        """Get amenity details by ID"""
        amenity = facade.get_amenity(amenity_id)
        if amenity:
            return {"id": amenity.id, "name": amenity.name}, 200
        else:
            return {"error": "Amenity not found"}, 404

    @api.expect(amenity_model)
    @api.response(200, 'Amenity updated successfully')
    @api.response(404, 'Amenity not found')
    @api.response(400, 'Invalid input data')
    def put(self, amenity_id):
        """Update an amenity's information"""
        data = request.get_json()
        amenity = facade.get_amenity(amenity_id)
        if not amenity:
            return {"error": "Amenity not found"}, 404

        try:
            updated = facade.update_amenity(amenity_id, data)
            return {"id": updated.id, "name": updated.name}, 200
        except Exception as e:
            return {"error": str(e)}, 400

@api.route('/amenities/')
class AdminAmenityCreate(Resource):
    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()
        user = facade.get_user(user_id)
        if not user or not user.is_admin:
            return {'error': 'Admin privileges required'}, 403

        data = request.get_json()
        name = data.get('name')
        if not name:
            return {'error': 'Amenity name is required'}, 400

        existing_amenity = facade.get_amenity_by_name(name)
        if existing_amenity:
            return {'error': 'Amenity already exists'}, 400

        new_amenity = facade.create_amenity(data)
        return {
            'id': new_amenity.id,
            'name': new_amenity.name
        }, 201

@api.route('/amenities/<amenity_id>')
class AdminAmenityModify(Resource):
    @jwt_required()
    def put(self, amenity_id):
        user_id = get_jwt_identity()
        user = facade.get_user(user_id)
        if not user or not user.is_admin:
            return {'error': 'Admin privileges required'}, 403

        data = request.get_json()
        name = data.get('name')

        amenity = facade.get_amenity(amenity_id)
        if not amenity:
            return {'error': 'Amenity not found'}, 404

        if name:
            existing_amenity = facade.get_amenity_by_name(name)
            if existing_amenity and existing_amenity.id != amenity_id:
                return {'error': 'Amenity name already in use'}, 400

            amenity.name = name

        facade.amenity_repo.update(amenity_id, data)
        return {
            'id': amenity.id,
            'name': amenity.name
        }, 200


