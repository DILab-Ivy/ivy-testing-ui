import json
from typing import List

from skills.planning.planner.instances.blockworld_planner import BlockWorldPlanner
from skills.planning.planner.planner import Planner
from skills.planning.planner.instances.robot_painting_planner import RobotPaintingPlanner
from skills.planning.state.instances.robot_painting_state import RobotPaintingState
from skills.planning.state.state import State


def get_planner(problem_type: str) -> Planner:
    """Function to load planner for appropriate problem instance"""
    if problem_type == 'robot':
        return RobotPaintingPlanner()
    elif problem_type == 'blockworld':
        # return BlockWorldPlanner()
        raise ValueError("Blockworld planner not implemented")
    else:
        raise ValueError("Unknown problem type. Please choose 'blockworld' or 'robot'.")

def get_state_object(problem_type: str, state_conditions_list: str) -> State:
    """Function to load State object for appropriate problem instance"""
    if problem_type == 'robot':
        return RobotPaintingState.from_conditions_list(state_conditions_list)
    elif problem_type == 'blockworld':
        # return BlockWorldPlanner()
        raise ValueError("Blockworld State creation not implemented")
    else:
        raise ValueError("Unknown problem type. Please choose 'blockworld' or 'robot'.")


# Wrapper functions that use the planner
def generate_plan(problem_type: str, start_state_conditions: str, goal_state_conditions: str):
    # Initialize Planner based on problem_type
    planner = get_planner(problem_type)

    # Convert conditions string from agent into appropriate State instances based on problem type
    start_state = get_state_object(problem_type, start_state_conditions)
    goal_state = get_state_object(problem_type, goal_state_conditions)

    return planner.generate_partial_plan(start_state, goal_state)

def reorder_to_avoid(problem_type: str, plans: List[List[str]]):
    planner = get_planner(problem_type)
    return planner.reorder_partial_plans(plans)

def generate_complete_plan(problem_type: str, start_state_conditions, goal_state_conditions):
    # Initialize Planner based on problem_type
    planner = get_planner(problem_type)

    # Convert conditions string from agent into appropriate State instances based on problem type
    start_state = get_state_object(problem_type, start_state_conditions)
    goal_state = get_state_object(problem_type, goal_state_conditions)

    return planner.generate_complete_plan(start_state, goal_state)