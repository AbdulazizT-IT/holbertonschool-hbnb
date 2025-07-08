from flask_restx import Namespace, Resource, fields
from flask import request
from app.services import facade
from flask_jwt_extended import jwt_required, get_jwt_identity

api = Namespace('places', description='Place operations')

# Define the models for related entities
amenity_model = api.model('PlaceAmenity', {
    'id': fields.String(description='Amenity ID'),
    'name': fields.String(description='Name of the amenity')
})

user_model = api.model('PlaceUser', {
    'id': fields.String(description='User ID'),
    'first_name': fields.String(description='First name of the owner'),
    'last_name': fields.String(description='Last name of the owner'),
    'email': fields.String(description='Email of the owner')
})

review_model = api.model('PlaceReview', {
    'id': fields.String(description='Review ID'),
    'text': fields.String(description='Text of the review'),
    'rating': fields.Integer(description='Rating of the place (1-5)'),
    'user_id': fields.String(description='ID of the user')
})

# Define the place model for input validation and documentation
place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place'),
    'owner_id': fields.String(required=True, description='ID of the owner'),
    'owner': fields.Nested(user_model, description='Owner of the place'),
    'amenities': fields.List(fields.String, required=True, description="List of amenities ID's"),
    'reviews': fields.List(fields.Nested(review_model), description='List of reviews')
})

@api.route('/')
class PlaceList(Resource):
    @api.expect(place_model)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    @jwt_required()

    def post(self):
        """Register a new place"""
        data = request.get_json()
        current_user = get_jwt_identity()
        data['owner_id'] = current_user

        try:
            place = facade.create_place(data)
            return {"id": place.id, "title": place.title, "description": place.description, "price": place.price, "latitude": place.latitude, "longitude": place.longitude, "owner_id": place.owner_id}, 201
        except Exception as e:
            return {"error": str(e)}, 400


    @api.response(200, 'List of places retrieved successfully')
    def get(self):
        """Retrieve a list of all places"""
        places = facade.get_all_places()
        result = []
        for place in places:
            owner = facade.get_user(place.owner_id)
            amenities = []
            for amenity in place.amenities:
                amenities.append({
                    "id": amenity.id,
                    "name": amenity.name
                })
        result.append({
            "id": place.id,
            "title": place.title,
            "latitude": place.latitude,
            "longitude": place.longitude,
            "owner": {
                "id": owner.id if owner else None,
                "first_name": owner.first_name if owner else None,
                "last_name": owner.last_name if owner else None,
                "email": owner.email if owner else None
            },
            "amenities": amenities
        })
        return result, 200

@api.route('/<place_id>')
class PlaceResource(Resource):
    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get place details by ID"""
        place = facade.get_place(place_id)
        if not place:
            return {"error": "Place not found"}, 404

        owner = place.owner
        
        return {
            "id": place.id,
            "title": place.title,
            "description": place.description,
            "latitude": place.latitude,
            "longitude": place.longitude,
            "owner": {
                "id": owner.id,
                "first_name": owner.first_name,
                "last_name": owner.last_name,
                "email": owner.email
            },
            "amenities": [
                {
                    "id": a.id,
                    "name": a.name
                } for a in place.amenities
            ]
            }, 200

    @api.expect(place_model)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid input data')
    @jwt_required()

    def put(self, place_id):
        """Update a place's information"""

        place = facade.get_place(place_id)
        if not place:
            return {"error": "Place not found"}, 404

        current_user = get_jwt_identity()
        if place.owner_id != current_user:
            return {"error": "Unauthorized to update this place"}, 403

        data = request.get_json()

        try:
            updated = facade.update_place(place_id, data)
            return {"id": updated.id, "name": updated.title}, 200
        except Exception as e:
            return {"error": str(e)}, 400

@api.route('/')
class PublicPlaceList(Resource):
    def get(self):
        places = facade.get_all_places()
        return marshal(places, place_model), 200

@api.route('/<place_id>')
class PublicPlaceResource(Resource):
    def get(self, place_id):
        place = facade.get_place(place_id)
        if not place:
            return {'error': 'Place not found'}, 404
        return marshal(place, place_model), 200
