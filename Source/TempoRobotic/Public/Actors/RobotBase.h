#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Structs/RobotTaskStruct.h"
#include "Structs/RobotConfig.h"

#include "RobotBase.generated.h"

UCLASS()
class TEMPOROBOTIC_API ARobotBase : public AActor {
	GENERATED_BODY()
	
public:	
	// Sets default values for this actor's properties
	ARobotBase ();

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category="Robot Configuration")
	FRobotConfig RobotConfig;

	UFUNCTION(BlueprintCallable, Category="Robot Tasks")
	void ExecuteTask(const FTaskEntry& Task);

protected:
	// Called when the game starts or when spawned
	virtual void BeginPlay() override;


};
