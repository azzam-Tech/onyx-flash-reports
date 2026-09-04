using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

public class GetCashCurrenciesDetailsOBjctResult
{
	private GeneralResult utilsMock;

	private List<GetCashCurrenciesDetailsOBjct> threadMock;

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
	public List<GetCashCurrenciesDetailsOBjct> _GetCashCurrenciesDetailsOBjct
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
	public GetCashCurrenciesDetailsOBjctResult()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool GetRequest()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool DisableRequest()
	{
		return true;
	}

	static GetCashCurrenciesDetailsOBjctResult()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
