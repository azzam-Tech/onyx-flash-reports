using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

public class GetGnrTaxItemsResult
{
	[CompilerGenerated]
	private GeneralResult m_ConfigDefinition;

	[CompilerGenerated]
	private List<GnrTaxItems> _ReaderDefinition;

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
	public List<GnrTaxItems> ListGnrTaxItems
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
	public GetGnrTaxItemsResult()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool ConnectSystem()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool WriteSystem()
	{
		return true;
	}

	static GetGnrTaxItemsResult()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
