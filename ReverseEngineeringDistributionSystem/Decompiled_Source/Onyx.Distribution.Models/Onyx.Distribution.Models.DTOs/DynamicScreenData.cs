using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Xml.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.DTOs;

[XmlRoot(ElementName = "DYNMC_SCREEN")]
public class DynamicScreenData
{
	[CompilerGenerated]
	private DYNMC_SCRN_MST? m_StateInterpreter;

	[CompilerGenerated]
	private List<DYNMC_SCRN_DTL>? mapInterpreter;

	public DYNMC_SCRN_MST? DYNMC_SCRN_MST
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

	public List<DYNMC_SCRN_DTL>? DYNMC_SCRN_DTL
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
	public DynamicScreenData()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool CheckIdentifier()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool SortIdentifier()
	{
		return true;
	}

	static DynamicScreenData()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
