import tempo.tempo_world as tw
from robot_defs import TaskType, RobotKeys
import time 
import asyncio


async def wait_for_robot(actor_name):
    print(f"Aguardando {actor_name} ficar disponível...")
    while True:
        try:
            state = await tw.get_current_actor_state(actor_name=actor_name)
            if state:
                print(f" Robot: {actor_name} detectado!")
                return True
        except Exception:
            pass
        await asyncio.sleep(0.5)

async def wait_for_task_finished(robot_id, timeout=None):
    print(f"--- Aguardando tarefa no {robot_id} ---")
    start_time = time.time()

    while True:
        if timeout is not None and (time.time() - start_time) > timeout:
            print(f"!!! Timeout de {timeout}s atingido !!!")
            return False

        try:
            # Assume que "TaskState" é uma variável separada no seu Actor (não dentro da struct de input)
            response = await tw.get_actor_properties(actor=robot_id, include_components=False)
            for prop in response.properties:
                if prop.name == "TaskState":
                    val = str(prop.value)
                    if val == "Finished":
                        print("Tarefa finalizada!")
                        return True
        except Exception as e:
            print(f"Erro leitura: {e}")
            
        await asyncio.sleep(0.5)

async def cmd_get_current_task(robot_id):
    """
    Retorna o tipo da tarefa atual do robô.
    """
    props = await tw.get_actor_properties(robot_id, include_components=False)  # Sem componentes

    # print("Todas props:", [p.name for p in props.properties])  # Lista nomes
    # Procure CurrentTask
    for prop in props.properties:
            if 'CurrentTask' in prop.name:
                # se quiser imprimir:
                # print(f"CurrentTask: {prop.name} = {prop.value}")
                 return prop.value
                
    return None

async def cmd_print_to_screen(robot_id, message, duration=5.0):
    await tw.set_string_property(robot_id, "", RobotKeys.PRINT_TO_SCREEN_MSG, message)
    await tw.set_float_property(robot_id, "", RobotKeys.PRINT_TO_SCREEN_DURATION, duration)

    await tw.set_int_property(robot_id, "", RobotKeys.TYPE, int(TaskType.PrintToScreen))
    await tw.call_function(robot_id, "", "ExecuteNewTask")


async def cmd_move_to_location(robot_id, eixo_x, eixo_y, acceptance_radius=10.0):
    """
    Move o robô para uma coordenada.
    Uso: await cmd_move_to_location("BP_Robot", 100, 200, 10)
    """   
    await tw.set_float_property(robot_id, "", RobotKeys.MOVE_LOC_X, eixo_x)
    await tw.set_float_property(robot_id, "", RobotKeys.MOVE_LOC_Y, eixo_y)
    await tw.set_float_property(robot_id, "", RobotKeys.MOVE_LOC_ACCEPTANCE_RADIUS, acceptance_radius)
    await tw.set_int_property(robot_id, "", RobotKeys.TYPE, int(TaskType.MoveToLocation))
    
    await tw.call_function(robot_id, "", "ExecuteNewTask")

async def cmd_move_to_actor(robot_id, target_actor_name):
    """
    Manda o robô seguir outro ator.
    """
    await tw.set_string_property(robot_id, "", RobotKeys.MOVE_ACTOR_NAME, target_actor_name)
    await tw.set_int_property(robot_id, "", RobotKeys.TYPE, int(TaskType.MoveToActor))
    
    await tw.call_function(robot_id, "", "ExecuteNewTask")

async def cmd_move_along_path(robot_id, path_actor_name, start_index=0, end_index=-1):
    """
    Manda o robô seguir outro ator.
    """
    await tw.set_string_property(robot_id, "", RobotKeys.MOVE_PATH_NAME, path_actor_name)
    await tw.set_int_property(robot_id, "", RobotKeys.MOVE_PATH_START_INDEX, start_index)
    await tw.set_int_property(robot_id, "", RobotKeys.MOVE_PATH_END_INDEX, end_index)
    await tw.set_int_property(robot_id, "", RobotKeys.TYPE, int(TaskType.MoveAlongPath))
    
    await tw.call_function(robot_id, "", "ExecuteNewTask")