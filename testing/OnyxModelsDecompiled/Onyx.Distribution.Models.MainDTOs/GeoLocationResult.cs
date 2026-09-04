using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

public class GeoLocationResult
{
	[CompilerGenerated]
	private GeneralResult _StubServer;

	[CompilerGenerated]
	private List<GeoLocationObjct> _TokenizerServer;

	[DataMember]
	public GeneralResult _Result
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
	public List<GeoLocationObjct> GeoLocationList
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
	public GeoLocationResult()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool ExcludeRegistry()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool IncludeRegistry()
	{
		return true;
	}

	static GeoLocationResult()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
