import asyncio
import tempo.tempo_world as tw
import tempo.tempo_core_editor as tce

# Importamos metodos utilitários do robot_api.py
from robot_api import cmd_print_to_screen, cmd_move_to_location, cmd_move_to_actor, cmd_move_along_path, wait_for_robot, wait_for_task_finished


async def main(): 
    robot_id = "BP_Robot"
    
    # abre o editor e inicia a simulação
    await tce.play_in_editor()
    print("Iniciando Simulação...")
   
    # Espera o robô ficar disponível
    await wait_for_robot(robot_id)
    
    # --- TASK 1: SAY HELLO 
    print("\n[Tarefa 1] Configurando: PrintToScreen Message...")
    await cmd_print_to_screen(robot_id, "THIS MESSAGE WILL APPEAR ON THE SCREEN FOR 10 SECONDS!!!", duration=10.0)

    # Espera o feedback da Unreal
    sucesso = await wait_for_task_finished(robot_id, timeout=10)
    if not sucesso:
        print("A tarefa 1 falhou")
    
    # --- TASK 2: Moving to point 0, 1500, 0
    print("\n[Tarefa 2] Configurando: MoveToLocation, vai andar 5 metros no eixo Y com aceitação de 10 unidades...")
    await cmd_move_to_location(robot_id, 1500, 500, 50.0)
    sucesso = await wait_for_task_finished(robot_id, timeout=50)
    if not sucesso:
        print("A tarefa 2 falhou")


    # --- TASK 3: Moving to Actor
    print("\n[Tarefa 3] Configurando: MoveToActor, vai procurar o Actor com o Identificador RoomAEntrance e se mover pra la...")
    await cmd_move_to_actor(robot_id, "RoomA_Entrance")
    sucesso = await wait_for_task_finished(robot_id, timeout=50)
    if not sucesso:
        print("A tarefa 3 falhou")

    # --- TASK 4: Moving along Path
    print("\n[Tarefa 4] Configurando: MoveAlongPath, vai procurar o Actor com o Identificador Path_A e se mover do ponto 0 até o final (-1)...")
    await cmd_move_along_path(robot_id, "Path_A", 0, -1)
    sucesso = await wait_for_task_finished(robot_id, timeout=50)
    if not sucesso:
        print("A tarefa 4 falhou")


    print("\nFim do script.")

if __name__ == "__main__":
    asyncio.run(main())