using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

public class GetCurrncyOBjctResult
{
	private GeneralResult issuerCustomer;

	private List<GetCurrncyOBjct> _MappingCustomer;

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
	public List<GetCurrncyOBjct> _GetCurrncyOBjct
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
	public GetCurrncyOBjctResult()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool WriteRequest()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool OrderRequest()
	{
		return true;
	}

	static GetCurrncyOBjctResult()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
