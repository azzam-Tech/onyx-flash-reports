using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

public class UpdateCustomerData
{
	[CompilerGenerated]
	private List<UpCustData> mapPolicy;

	[DataMember]
	public List<UpCustData> ListUpCustData
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
	public UpdateCustomerData()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool ViewRegistry()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool InvokeRegistry()
	{
		return true;
	}

	static UpdateCustomerData()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
