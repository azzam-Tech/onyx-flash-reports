using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

public class GetBanksCurrenciesDetailsOBjctResult
{
	private GeneralResult _ResolverMock;

	private List<GetBanksCurrenciesDetailsOBjct> _GlobalMock;

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
	public List<GetBanksCurrenciesDetailsOBjct> _GetBanksCurrenciesDetailsOBjct
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
	public GetBanksCurrenciesDetailsOBjctResult()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool IncludeRequest()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool DeleteRequest()
	{
		return true;
	}

	static GetBanksCurrenciesDetailsOBjctResult()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
