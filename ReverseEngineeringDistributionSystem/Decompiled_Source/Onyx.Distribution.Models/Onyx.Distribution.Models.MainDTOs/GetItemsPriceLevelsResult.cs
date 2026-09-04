using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

public class GetItemsPriceLevelsResult
{
	[CompilerGenerated]
	private List<ItemsPriceLevels> m_PolicyDefinition;

	[CompilerGenerated]
	private GeneralResult m_DefinitionDefinition;

	[DataMember]
	public List<ItemsPriceLevels> ItemsPriceLevelsList
	{
		[MethodImpl(MethodImplOptions.NoInlining)]
		[CompilerGenerated]
		get
		{
			return null;
		}
		[MethodImpl(MethodImplOptions.NoInlining)]
		[CompilerGenerated]
		set
		{
		}
	}

	[DataMember]
	public GeneralResult Result
	{
		[MethodImpl(MethodImplOptions.NoInlining)]
		[CompilerGenerated]
		get
		{
			return null;
		}
		[MethodImpl(MethodImplOptions.NoInlining)]
		[CompilerGenerated]
		set
		{
		}
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public GetItemsPriceLevelsResult()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool QueryRegistry()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool InitRegistry()
	{
		return true;
	}

	static GetItemsPriceLevelsResult()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
