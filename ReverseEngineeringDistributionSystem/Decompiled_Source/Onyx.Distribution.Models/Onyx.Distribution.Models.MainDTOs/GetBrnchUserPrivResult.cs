using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

public class GetBrnchUserPrivResult
{
	[CompilerGenerated]
	private List<BrnchUserPriv> productPolicy;

	[CompilerGenerated]
	private GeneralResult eventPolicy;

	[DataMember]
	public List<BrnchUserPriv> BrnchUserPrivList
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
	public GetBrnchUserPrivResult()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool MoveRegistry()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool ReadRegistry()
	{
		return true;
	}

	static GetBrnchUserPrivResult()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
