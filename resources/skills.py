
# import models
# from flask import Blueprint, jsonify, request
# from playhouse.shortcuts import model_to_dict
# from flask_login import current_user, login_required



# skill = Blueprint('skills', 'skill')

# # url_prefix='/skill'


# # index route
# @skill.route('/', methods=["GET"])
# @login_required
# def get_all_skills():

# 	try:
# 		this_users_skill_instances = models.Skill.select().where(models.Skill.owner_id == current_user.id)

# 		this_users_skill_dicts = [model_to_dict(skill) for skill in this_users_skill_instances]


# 		# skills = [model_to_dict(skill) for skill in models.Skill.select()]
# 		# print(skills)
# 		return jsonify(data=skill, status={"code": 200, "message": "Successful route"})
# 	except models.DoesNotExist:
# 		return jsonify(data={}, status={"code": 401, "message": "Error getting the resources"})


# # create route
# @skill.route('/', methods=["POST"])
# def create_skills():
# 	# payload = request.get_json()
# 	# skill = models.Skill.create(**payload)
# 	# print(skill.__dict__)
# 	# skill_dict = model_to_dict(skill)

# 	payload = request.get_json()
# 	skill = models.Skill.create(
#     	goal=payload['goal'], 
#         owner=current_user.id, 
#         objective=payload["objective"],
#         time=payload["time"])


# 	print(model_to_dict(skill), 'model to dict')
# 	skill_dict = model_to_dict(skill)

# 	skill_dict['owner'].pop('password')
# 	return jsonify(data=skill_dict, status={"code": 200, "message": "Success"}) 


# @skill.route('/<owner_id>', methods=['POST'])
# def create_skill_with_owner(owner_id):
#     payload = request.get_json()
#     skill = models.Skill.create(goal=payload['goal'], objective=payload['objective'], time=payload['time'], owner=owner_id)

#     skill_dict = model_to_dict(skill)

#     skill_dict['owner'].pop('password')

#     return jsonify(data=skill_dict, status={
#             'code': 201,
#             "message": "Succesfully created skill"
#         }), 201





# # show dat route
# @skill.route('/<id>', methods=["GET"])
# def get_one_skill(id):
#     skill = models.Skill.get_by_id(id)
#     return jsonify(data=model_to_dict(skill), status={"code": 200, "message": "Success"}) 



# #update
# @skill.route('/<id>', methods=['PUT'])
# def update_skill(id):
#     payload = request.get_json()
#     query = models.Skill.update(**payload).where(models.Skill.id == id)
#     query.execute()
#     skill = models.Skill.get_by_id(id)
#     skill_dict = model_to_dict(skill)
#     return jsonify(data=skill_dict, status={'code': 200, 'message': 'Updated successfully'}) 

# # deletion route 
# @skill.route('/<id>', methods=["Delete"])
# def delete_skill(id):
#     query = models.Skill.delete().where(models.Skill.id==id)
#     query.execute()
#     return jsonify(data='Resource Deleted', status={"code": 200, "message": "Success deletion"}) 


import models
from flask import Blueprint, jsonify, request
from flask_login import current_user, login_required
from playhouse.shortcuts import model_to_dict

skill_bp = Blueprint('skills', 'skill', url_prefix='/skill')


# index route
# @skill_bp.route('/all', methods=["GET"])
# @login_required
# def get_all_skills():
# 	# breakpoint()
# 	try:
# 		skills = [model_to_dict(skill) for skill in models.Skill.select()]
# 		print(skills)
# 		return jsonify(data=skills, status={"code": 200, "message": "Successful route"})
# 	except models.DoesNotExist:
# 		return jsonify(data={}, status={"code": 401, "message": "Error getting the resources"})

@skill_bp.route('/', methods=["GET"])
@login_required 
def skills_index():
  try:
    this_users_skill_instances = models.Skill.select().where(
        models.Skill.owner_id == current_user.id
    )

    this_users_skill_dicts = [model_to_dict(skill) for skill in this_users_skill_instances]

    return jsonify(data=this_users_skill_dicts, status={
            "code": 200, 
            "message": "Success"
        }), 200

  except models.DoesNotExist:
    return jsonify(data={}, status={
            "code": 401, 
            "message": "Error getting the resources"
        }), 401


# create route
@skill_bp.route('/', methods=["POST"])
@login_required
def create_skills():
	payload = request.get_json()

	# skill = models.Skill.create(**payload)
	skill = models.Skill.create(goal=payload['goal'],
		owner=current_user.id,
		objective=payload["objective"],
		time=payload["time"]
		)

	print(skill.__dict__)

	skill_dict = model_to_dict(skill)
	skill_dict['owner'].pop('password')
	return jsonify(data=skill_dict, status={"code": 200, "message": "Success"}) 

# show dat route
# @skill_bp.route('/<id>', methods=["GET"])
# @login_required
# def get_one_skill(id):
#     skill = models.Skill.get_by_id(id)
#     return jsonify(data=model_to_dict(skill), status={"code": 200, "message": "Success"}) 

# show route 2
# @skill.route('/<id>', methods=["GET"])
# @login_required
# def get_one_skill(id):
#     skill = models.Skill.get_by_id(id)

#     if not current_user.is_authenticated:
#         return jsonify(data={
#                 'goal': skill.goal,
#                 'objective': skill.objective,
#                 'time': skill.time
#             }, status={
#                 'code': 200,
#                 'message': "Registered users can access more info about this skill"
#             }), 200

#     else: 
#         skill_dict = model_to_dict(skill)
#         skill_dict['owner'].pop('password')

#         if skill.owner_id != current_user.id: 
#             skill_dict.pop('created_at')


#         return jsonify(data=skill_dict, status={
#                 'code': 200,
#                 "message": "Found skill with id {}".format(skill.id)
#             }), 200


#update
# @skill_bp.route('/<id>', methods=['PUT'])
# @login_required
# def update_skill(id):
#     payload = request.get_json()

#     query = models.Skill.update(**payload).where(models.Skill.id == id)
#     query.execute()

#     skill.save()

#     skill = models.Skill.get_by_id(id)
#     skill_dict = model_to_dict(skill)

#     return jsonify(data=skill_dict, status={'code': 200, 'message': 'Updated successfully'}) 

@skill_bp.route('/<id>', methods=["PUT"])
@login_required
def update_skill(id):
    payload = request.get_json()


    skill = models.Skill.get_by_id(id) 
    
 
    if(skill.owner.id == current_user.id):

        skill.goal = payload['goal'] if 'goal' in payload else None 
        skill.objective = payload['objective'] if 'objective' in payload else None 
        skill.time = payload['time'] if 'time' in payload else None 


        skill.save()

        skill_dict = model_to_dict(skill)
        skill_dict['owner'].pop('password')

        return jsonify(data=skill_dict, status={
                'code': 200,
                'message': 'Resource updated successfully'
            }), 200    


# deletion route 
@skill_bp.route('/<id>', methods=["Delete"])
def delete_skill(id):
    query = models.Skill.delete().where(models.Skill.id==id)
    query.execute()
    return jsonify(data='Resource Deleted', status={"code": 200, "message": "Success deletion"}) 







