#pragma once

#include "CoreMinimal.h"
#include "RobotTaskStruct.h" // Sua struct anterior
#include "RobotConfig.generated.h"

// Configuração de Custo de Tarefa
USTRUCT(BlueprintType)
struct FTaskCostConfig {
    GENERATED_BODY()

    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    ETaskType TaskType = ETaskType::Idle;

    // Custo energético apenas para manter a tarefa ativa
    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    float EnergyCostPerSecond = 5.0f;

    // Custo extra baseado em esforço (ex: por metro andado)
    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    float EnergyCostPerUnit = 2.0f; 
};

// Configuração dos Sensores
USTRUCT(BlueprintType)
struct FSensorConfig {
    GENERATED_BODY()

    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    bool bHasLidar = true;

    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    float LidarRange = 1000.0f; // 10 metros

    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    bool bHasCamera = false;
    
    // Ruído simulado (0.0 = perfeito, 0.1 = 10% de erro na leitura)
    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    float SensorNoiseLevel = 0.0f;
};

USTRUCT(BlueprintType)
struct FRobotState {
    GENERATED_BODY()

    UPROPERTY(VisibleAnywhere, BlueprintReadOnly)
    float CurrentBattery = 100.0f;

    UPROPERTY(VisibleAnywhere, BlueprintReadOnly)
    FVector CurrentLocation = FVector::ZeroVector;

    UPROPERTY(VisibleAnywhere, BlueprintReadOnly)
    FRotator CurrentRotation = FRotator::ZeroRotator;

    UPROPERTY(VisibleAnywhere, BlueprintReadOnly)
    ETaskType CurrentTask = ETaskType::Idle;
    
    UPROPERTY(VisibleAnywhere, BlueprintReadOnly)
    bool bIsStuck = false; 
};

USTRUCT(BlueprintType)
struct FRobotConfig {
    GENERATED_BODY()

    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    FString RobotID = "Robot_01";
    // Física
    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    float MaxSpeed = 600.0f; // cm/s

    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    float MaxAngularSpeed = 90.0f; // graus/s (importante para robôs diferenciais)

    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    float MaxAcceleration = 200.0f; // Para movimentos mais suaves/realistas

    // Energia
    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    float BatteryCapacity = 100.0f;

    // Dimensões (Para o Python calcular pathfinding)
    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    float CollisionRadius = 40.0f; 

    // Lista de custos por tarefa (Usar TMap seria ideal em C++, mas TArray é mais seguro p/ Blueprints antigos)
    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    TArray<FTaskCostConfig> TaskCosts;
    
    // Configuração dos sensores
    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    FSensorConfig Sensors;
};