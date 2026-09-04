using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

public class GetGnrTaxCodeResult
{
	[CompilerGenerated]
	private GeneralResult _TestsDefinition;

	[CompilerGenerated]
	private List<GnrTaxCode> m_RefDefinition;

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

	[DataMember]
	public List<GnrTaxCode> ListGnrTaxCode
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
	public GetGnrTaxCodeResult()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool PatchSystem()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool ReflectSystem()
	{
		return true;
	}

	static GetGnrTaxCodeResult()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
