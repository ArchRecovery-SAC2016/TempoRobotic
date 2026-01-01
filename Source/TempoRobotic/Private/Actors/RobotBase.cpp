#include "Actors/RobotBase.h"

// Sets default values
ARobotBase ::ARobotBase () {
 	// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
	PrimaryActorTick.bCanEverTick = false;

}

// Called when the game starts or when spawned
void ARobotBase ::BeginPlay() {
	Super::BeginPlay();
	
}

// Called every frame
void ARobotBase ::Tick(float DeltaTime) {
	Super::Tick(DeltaTime);

}

