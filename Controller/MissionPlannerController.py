from Controller import SortieController,DroneAvailabilityLogController
from config import db
from Model import MissionPlanner,Sortie, Drone,DroneAvailabilityLog


class MissionPlannerController():
    @staticmethod
    def insert_mission_plan(data):
        try:
            mission_plan = MissionPlanner(
                name=data.get('name'),
                drone_id=data.get('drone_id'),
                route_id=data.get('route_id'),
                start_date=data.get('start_date'),
                start_time=data.get('start_time'),
                status=data.get('status')
            )

            db.session.add(mission_plan)
            db.session.commit()
            data['mission_planner_id'] = mission_plan.id
            drone_availability_log = DroneAvailabilityLogController.insert_drone_availability_log(data)
            return {
               "id": mission_plan.id,
               "name": mission_plan.name,
               "drone_id": mission_plan.drone_id,
               "start_date": mission_plan.start_date.strftime('%d-%m-%Y'),
                "start_time": str(mission_plan.start_time.strftime('%I:%M:%S %p')),
               "status": mission_plan.status,
                "drone_availability_log_id":drone_availability_log.get('id')
            }
        except Exception as e:
            print(e)
            return {}


    @staticmethod
    def update_mission_plan_by_id(data):
        try:
            mission_plan = MissionPlanner.query.filter_by(id=data.get('id'),validity=1).first()
            print(mission_plan.drone_id)
            drone_availability_log = DroneAvailabilityLog.query.filter_by(mission_planner_id=mission_plan.id,validity=1).first()
            if mission_plan:
                mission_plan.name = data.get('name',mission_plan.name)
                mission_plan.drone_id = data.get('drone_id',mission_plan.drone_id)
                mission_plan.route_id = data.get('route_id', mission_plan.route_id)
                mission_plan.start_date = data.get('start_date',mission_plan.start_date)
                mission_plan.start_time = data.get('start_time',mission_plan.start_time)
                mission_plan.status = data.get('status',mission_plan.status)
                if drone_availability_log:
                    drone_availability_log.drone_id = data.get('drone_id', drone_availability_log.drone_id)


                db.session.commit()
                return {
                    "id": mission_plan.id,
                    "name": mission_plan.name,
                    "drone_id": mission_plan.drone_id,
                    "start_date": mission_plan.start_date.strftime('%d-%m-%Y'),
                    "start_time": str(mission_plan.start_time.strftime('%I:%M:%S %p')),
                    "status": mission_plan.status,
                }
            else:
                return {}
        except Exception as e:
            print(e)
            return {}

    @staticmethod
    def delete_mission_plan_by_id(mission_planner_id):
        try:
            mission_plan = MissionPlanner.query.filter_by(id=mission_planner_id, validity=1).first()
            if mission_plan:
                mission_plan.validity = 0
            else:
                return {}

            drone_availability_log = DroneAvailabilityLog.query.filter_by(drone_id=mission_plan.drone_id,validity=1).first()
            if drone_availability_log:
                drone_availability_log.validity = 0


            # Commit all changes to the database in one transaction
            db.session.commit()
            return {
                        "id": mission_plan.id,
                        "name": mission_plan.name,
                        "route_id": mission_plan.route_id,
                        "drone_id": mission_plan.drone_id,
                        "start_date": mission_plan.start_date.strftime('%d-%m-%Y'),
                        "start_time": str(mission_plan.start_time.strftime('%I:%M:%S %p')),
                        "status": mission_plan.status,
                    }
        except Exception as e:
            print(e)
            return {}

    @staticmethod
    def get_all_mission_plans():
        try:
            mission_plans = MissionPlanner.query.filter_by(validity=1).all()
            if mission_plans:
                result = []
                for mission_plan in mission_plans:


                    mission_dict = {
                        "id": mission_plan.id,
                        "name": mission_plan.name,
                        "route_id": mission_plan.route_id,
                        "drone_id": mission_plan.drone_id,
                        "start_date": mission_plan.start_date.strftime('%d-%m-%Y'),
                        "start_time": mission_plan.start_time.strftime('%I:%M:%S %p'),
                        "status": mission_plan.status
                    }
                    if mission_plan.status not in ('completed', 'aborted'):
                        result.append(mission_dict)
                return result
            else:
                return []
        except Exception as e:
            print(e)
            return []

    @staticmethod
    def get_mission_plan_by_id(mission_plan_id):
        try:
            mission_plan = MissionPlanner.query.filter_by(id=mission_plan_id, validity=1).first()
            if mission_plan:
                return {
                    "id": mission_plan.id,
                    "name": mission_plan.name,
                    "route_id": mission_plan.route_id,
                    "drone_id": mission_plan.drone_id,
                    "start_date": mission_plan.start_date.strftime('%d-%m-%Y'),
                    "start_time": str(mission_plan.start_time.strftime('%I:%M:%S %p')),
                    "status": mission_plan.status
                }
            else:
                return {}
        except Exception as e:
            print(e)
            return {}

