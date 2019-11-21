import models
from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict



skill = Blueprint('skills', 'skill', url_prefix='/skill')

# index route
@skill.route('/', methods=["GET"])
def get_all_skills():
	try:
		skills = [model_to_dict(skill) for skill in models.Skill.select()]
		print(skills)
		return jsonify(data=skills, status={"code": 200, "message": "Successful route"})
	except models.DoesNotExist:
		return jsonify(data={}, status={"code": 401, "message": "Error getting the resources"})



# create route
@skill.route('/', methods=["POST"])
def create_skills():
	payload = request.get_json()
	skill = models.Skill.create(**payload)
	print(skill.__dict__)
	skill_dict = model_to_dict(skill)
	return jsonify(data=skill_dict, status={"code": 201, "message": "Success"})


# show dat route
@skill.route('/<id>', methods=["GET"])
def get_one_skill(id):
    skill = models.Skill.get_by_id(id)
    return jsonify(data=model_to_dict(skill), status={"code": 200, "message": "Success"})


#update
@skill.route('/<id>', methods=['PUT'])
def update_skill(id):
    payload = request.get_json()
    query = models.Skill.update(**payload).where(models.Skill.id == id)
    query.execute()
    skill = models.Skill.get_by_id(id)
    skill_dict = model_to_dict(skill)
    return jsonify(data=skill_dict, status={'code': 200, 'message': 'Updated successfully'})
















