import asyncio
import time 
import tempo.tempo_world as tw
import tempo.tempo_core_editor as tce

# Importamos nosso novo arquivo de definições
from robot_api import cmd_print_to_screen, cmd_move_to_location, cmd_move_to_actor

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

async def main(): 
    robot_id = "BP_Robot"
    
    # abre o editor e inicia a simulação
    await tce.play_in_editor()
    print("Iniciando Simulação...")
   
    await wait_for_robot(robot_id)

    # --- TASK 1: SAY HELLO ---
    print("\n[Tarefa 1] Configurando: PrintToScreen Message...")
    await cmd_print_to_screen(robot_id, "THIS MESSAGE WILL APPEAR ON THE SCREEN FOR 10 SECONDS!!!", duration=10.0)

      # Espera o feedback da Unreal
    sucesso = await wait_for_task_finished(robot_id, timeout=10)
    if not sucesso:
        print("A tarefa 1 falhou")


    print("\nFim do script.")

if __name__ == "__main__":
    asyncio.run(main())