from enum import IntEnum

# Tasks disponíveis para o robô. A unreal precisa imprementar essas tasks
class TaskType(IntEnum):
    Idle = 0
    PrintToScreen = 1
    MoveToLocation = 2
    MoveAlongPath = 3
    MoveToActor = 4
    PlayAnimation = 5

# Mapeamento dos caminhos das propriedades (Property Paths)
# Isso evita erro de digitação de strings no script principal
class RobotKeys:
    # O nome da variável principal no seu Blueprint/C++
    ROOT = "CurrentTask" 
    
    # Seletor de Tipo
    TYPE = f"{ROOT}.Type"
    
    # Sub-structs. Pq precisamos passar as propriedades aninhadas
    PRINT_TO_SCREEN_MSG       = f"{ROOT}.PrintToScreen.Message"
    PRINT_TO_SCREEN_DURATION  = f"{ROOT}.PrintToScreen.Duration"
    
    MOVE_LOC_VEC    = f"{ROOT}.MoveToLocation.NewLocation"
    MOVE_LOC_X    = f"{ROOT}.MoveToLocation.MoveLocationX"
    MOVE_LOC_Y    = f"{ROOT}.MoveToLocation.MoveLocationY"
    MOVE_LOC_ACCEPTANCE_RADIUS  = f"{ROOT}.MoveToLocation.AcceptanceRadius"
    
    MOVE_PATH_NAME  = f"{ROOT}.MoveAlongPath.PathName"
    MOVE_PATH_START = f"{ROOT}.MoveAlongPath.PathStartIndex"
    MOVE_PATH_END   = f"{ROOT}.MoveAlongPath.PathEndIndex"
    
    MOVE_ACTOR_NAME = f"{ROOT}.MoveToActor.ActorName"
    
    ANIM_NAME       = f"{ROOT}.PlayAnimation.AnimationName"
    IDLE_WAIT       = f"{ROOT}.Idle.WaitTime"