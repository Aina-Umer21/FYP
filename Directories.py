from os import makedirs

from config import app
import os
def create_all_directories():
    # # Operators
    # operators_folder = './uploads/operators'
    # os.makedirs(operators_folder,exist_ok=True)
    # operator_profile_pictures_folder = './uploads/operators/profile_pictures'
    # os.makedirs(operator_profile_pictures_folder,exist_ok=True)
    # app.config['OPERATOR_PROFILE_PICTURES_FOLDER'] = operator_profile_pictures_folder
    drone_folder = './uploads/drones'
    os.makedirs(drone_folder,exist_ok=True)
    drone_profile_pictures_folder = './uploads/drones/profile_pictures'
    os.makedirs(drone_profile_pictures_folder,exist_ok=True)
    app.config['DRONE_PROFILE_PICTURES_FOLDER'] = drone_profile_pictures_folder
    missions_folder = './uploads/missions'
    os.makedirs(missions_folder,exist_ok=True)
    app.config['MISSIONS_FOLDER'] = missions_folder

def make_mission_dirs(data):
    mission_planner_folder = f"{app.config['MISSIONS_FOLDER']}/{data['mission_planner_id']}"
    os.makedirs(mission_planner_folder, exist_ok = True)
    video_folder = f"{mission_planner_folder}/videos"
    os.makedirs(video_folder, exist_ok = True)
    model_results_folder = f"{mission_planner_folder}/model_results"
    os.makedirs(model_results_folder, exist_ok = True)
    predictions_folder = f"{model_results_folder}/{data['location_pin_id']}"
    os.makedirs(predictions_folder, exist_ok = True)
    return video_folder,predictions_folder

