#include "Actors/RobotBase.h"

ARobotBase ::ARobotBase () {
	PrimaryActorTick.bCanEverTick = false;

}

void ARobotBase ::BeginPlay() {
    Super::BeginPlay();
	
}

void ARobotBase::ExecuteTask(const FTaskEntry &Task) {
	UE_LOG(LogTemp, Warning, TEXT("Executing Task of type: %d"), static_cast<uint8>(Task.Type));
	while (true) {
		switch (Task.Type) {
		case ETaskType::Idle:
			UE_LOG(LogTemp, Warning, TEXT("Idle for %f seconds"), Task.Idle.WaitTime);
			return;
		case ETaskType::SayHello:
			UE_LOG(LogTemp, Warning, TEXT("Saying Hello: %s for %f seconds"), *Task.SayHello.Message, Task.SayHello.Timer);
			return;
		case ETaskType::MoveToLocation:
			UE_LOG(LogTemp, Warning, TEXT("Moving to Location: %s"), *Task.MoveToLocation.Location.ToString());
			return;
		case ETaskType::MoveAlongPath:
			UE_LOG(LogTemp, Warning, TEXT("Moving along Path: %s from %d to %d"), *Task.MoveAlongPath.PathName, Task.MoveAlongPath.PathStartIndex, Task.MoveAlongPath.PathEndIndex);
			return;
		case ETaskType::MoveToActor:
			UE_LOG(LogTemp, Warning, TEXT("Moving to Actor: %s"), *Task.MoveToActor.ActorName);
			return;
		case ETaskType::PlayAnimation:
			UE_LOG(LogTemp, Warning, TEXT("Playing Animation: %s"), *Task.PlayAnimation.AnimationName.ToString());
			return;
		default:
			UE_LOG(LogTemp, Error, TEXT("Unknown Task Type: %d"), static_cast<uint8>(Task.Type));
			return;
		}
	}
}

