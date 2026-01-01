#pragma once

#include "CoreMinimal.h"
#include "RobotTaskStruct.generated.h" 

UENUM(BlueprintType)
enum class ETaskType : uint8 {
    Idle,
    SayHello,
    MoveToLocation,
    MoveAlongPath,
    MoveToActor,
    PlayAnimation
};


USTRUCT(BlueprintType)
struct FTaskIdle {
    GENERATED_BODY()

    UPROPERTY(EditAnywhere, BlueprintReadWrite, SaveGame)
    float WaitTime = 0.0f;
};

USTRUCT(BlueprintType)
struct FTaskPlayAnimation {
    GENERATED_BODY()

    UPROPERTY(EditAnywhere, BlueprintReadWrite, SaveGame)
    FName AnimationName = NAME_None;
};

USTRUCT(BlueprintType)
struct FTaskMoveToLocation {
    GENERATED_BODY()

    UPROPERTY(EditAnywhere, BlueprintReadWrite, SaveGame)
    FVector Location = FVector::ZeroVector;
};

USTRUCT(BlueprintType)
struct FTaskMoveAlongPath {
    GENERATED_BODY()

    UPROPERTY(EditAnywhere, BlueprintReadWrite, SaveGame)
    FString PathName = "DefaultPath";

    UPROPERTY(EditAnywhere, BlueprintReadWrite, SaveGame)
    int32 PathStartIndex = 0;
    
    UPROPERTY(EditAnywhere, BlueprintReadWrite, SaveGame)
    int32 PathEndIndex = 99;
};

USTRUCT(BlueprintType)
struct FTaskMoveToActor {
    GENERATED_BODY()

    UPROPERTY(BlueprintReadWrite)
    FString ActorName = "ActorName";
};

USTRUCT(BlueprintType)
struct FTaskSayHello {
    GENERATED_BODY()

    UPROPERTY(BlueprintReadWrite)
    FString Message = "Hello, World!";

    UPROPERTY(BlueprintReadWrite)
    float Timer = 5.0f;
};

USTRUCT(BlueprintType)
struct FTaskEntry {
    GENERATED_BODY()

    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    ETaskType Type = ETaskType::Idle;

    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    FTaskIdle Idle;

	UPROPERTY(EditAnywhere, BlueprintReadWrite)
    FTaskSayHello SayHello;

    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    FTaskMoveToLocation MoveToLocation;
    
    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    FTaskMoveAlongPath MoveAlongPath;

    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    FTaskMoveToActor MoveToActor; 

    UPROPERTY(EditAnywhere, BlueprintReadWrite)
    FTaskPlayAnimation PlayAnimation;
    
};