using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

public class GetVistFailReasonsOBjctResult
{
	[CompilerGenerated]
	private List<VistFailReasons> m_CollectionPolicy;

	[CompilerGenerated]
	private GeneralResult _IteratorPolicy;

	[DataMember]
	public List<VistFailReasons> VistFailReasonsOBjctList
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
	public GetVistFailReasonsOBjctResult()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool SelectRegistry()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool CompareRegistry()
	{
		return true;
	}

	static GetVistFailReasonsOBjctResult()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
