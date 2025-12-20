// Copyright Epic Games, Inc. All Rights Reserved.

using UnrealBuildTool;
using System.Collections.Generic;

public class TempoRoboticTarget : TargetRules
{
	public TempoRoboticTarget(TargetInfo Target) : base(Target)
	{
		Type = TargetType.Game;
		DefaultBuildSettings = BuildSettingsVersion.V5;
		IncludeOrderVersion = EngineIncludeOrderVersion.Latest;
		ExtraModuleNames.Add("TempoRobotic");

		if (Platform == UnrealTargetPlatform.Win64)
		{
			ToolChainName = "TempoVCToolChain";
		}
		else if (Platform == UnrealTargetPlatform.Mac)
		{
			ToolChainName = "TempoMacToolChain";
		}
		else if (Platform == UnrealTargetPlatform.Linux)
		{
			ToolChainName = "TempoLinuxToolChain";
		}
		// TEMPO_TOOLCHAIN_BLOCK BEGIN - Added by UseTempoToolChain.sh script
		if (Platform == UnrealTargetPlatform.Win64)
		{
			ToolChainName = "TempoVCToolChain";
		}
		else if (Platform == UnrealTargetPlatform.Mac)
		{
			ToolChainName = "TempoMacToolChain";
		}
		else if (Platform == UnrealTargetPlatform.Linux)
		{
			ToolChainName = "TempoLinuxToolChain";
		}
		// TEMPO_TOOLCHAIN_BLOCK END
	}
}
