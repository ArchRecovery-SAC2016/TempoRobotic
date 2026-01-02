import tempo.tempo_world as tw
from robot_defs import TaskType, RobotKeys

async def cmd_print_to_screen(robot_id, message, duration=5.0):

    await tw.set_string_property(robot_id, "", RobotKeys.PRINT_TO_SCREEN_MSG, message)
    await tw.set_float_property(robot_id, "", RobotKeys.PRINT_TO_SCREEN_DURATION, duration)

    await tw.set_int_property(robot_id, "", RobotKeys.TYPE, int(TaskType.PrintToScreen))
    await tw.call_function(robot_id, "", "ExecuteNewTask")


async def cmd_move_to_location(robot_id, x, y, z):
    """
    Move o robô para uma coordenada.
    Uso: await cmd_move_to_location("BP_Robot", 100, 200, 0)
    """
    # O Tempo tem set_vector_property, usamos ele para facilitar
    await tw.set_vector_property(robot_id, "", RobotKeys.MOVE_LOC_VEC, x=x, y=y, z=z)
    await tw.set_int_property(robot_id, "", RobotKeys.TYPE, int(TaskType.MoveToLocation))
    
    await tw.call_function(robot_id, "", "ExecuteNewTask")

async def cmd_move_to_actor(robot_id, target_actor_name):
    """
    Manda o robô seguir outro ator.
    """
    await tw.set_string_property(robot_id, "", RobotKeys.MOVE_ACTOR_NAME, target_actor_name)
    await tw.set_int_property(robot_id, "", RobotKeys.TYPE, int(TaskType.MoveToActor))
    
    await tw.call_function(robot_id, "", "ExecuteNewTask")