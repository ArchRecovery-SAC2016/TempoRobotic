#include "Actors/RobotBase.h"
#include "GameFramework/CharacterMovementComponent.h"

ARobotBase ::ARobotBase () {
	PrimaryActorTick.bCanEverTick = false;

    // Garante que o robô tenha um AI Controller assim que nascer, 
    // seja arrastado no editor ou spawnado via código.
    AutoPossessAI = EAutoPossessAI::PlacedInWorldOrSpawned;
    
    // Desacopla a rotação da câmera/controller direto
    bUseControllerRotationYaw = false; 

    // Permite que o CharacterMovement gire o mesh
    GetCharacterMovement()->bOrientRotationToMovement = true; 
    
    // Define a velocidade de rotação (O quão rápido ele gira no próprio eixo)
    // 180.0f = meio segundo para dar meia volta. Ajuste conforme o "motor" do seu robô.
    GetCharacterMovement()->RotationRate = FRotator(0.0f, 180.0f, 0.0f);
    
    // Para robôs, é bom aumentar o atrito para ele não "deslizar" nas curvas
    GetCharacterMovement()->GroundFriction = 8.0f;
}

void ARobotBase ::BeginPlay() {
    Super::BeginPlay();
	
}


