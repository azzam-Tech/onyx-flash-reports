using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

public class GetSales_discountOBjctResult
{
	private GeneralResult m_ItemIndexer;

	private List<GetSales_discountOBjct> candidateIndexer;

	[DataMember]
	public GeneralResult _Result
	{
		[MethodImpl(MethodImplOptions.NoInlining)]
		get
		{
			return null;
		}
		[MethodImpl(MethodImplOptions.NoInlining)]
		set
		{
		}
	}

	[DataMember]
	public List<GetSales_discountOBjct> _GetSales_discountOBjct
	{
		[MethodImpl(MethodImplOptions.NoInlining)]
		get
		{
			return null;
		}
		[MethodImpl(MethodImplOptions.NoInlining)]
		set
		{
		}
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public GetSales_discountOBjctResult()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool ResetRequest()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool ConcatRequest()
	{
		return true;
	}

	static GetSales_discountOBjctResult()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
