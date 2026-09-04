using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

public class GetPriceLevelsResult
{
	[CompilerGenerated]
	private List<PriceLevels> m_ManagerPolicy;

	[CompilerGenerated]
	private GeneralResult containerPolicy;

	[DataMember]
	public List<PriceLevels> PriceLevelsList
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
	public GetPriceLevelsResult()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool NewRegistry()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool CollectRegistry()
	{
		return true;
	}

	static GetPriceLevelsResult()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
