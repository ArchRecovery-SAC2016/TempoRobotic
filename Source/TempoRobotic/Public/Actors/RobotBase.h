#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Character.h"
#include "Structs/RobotTaskStruct.h"
#include "Structs/RobotConfig.h"

#include "RobotBase.generated.h"

UCLASS()
class TEMPOROBOTIC_API ARobotBase : public ACharacter {
	GENERATED_BODY()
	
public:	
	// Sets default values for this actor's properties
	ARobotBase ();

protected:
	// Called when the game starts or when spawned
	virtual void BeginPlay() override;


};
