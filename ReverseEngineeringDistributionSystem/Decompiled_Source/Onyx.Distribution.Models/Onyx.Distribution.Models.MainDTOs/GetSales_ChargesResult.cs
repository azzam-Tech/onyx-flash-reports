using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

public class GetSales_ChargesResult
{
	[CompilerGenerated]
	private GeneralResult m_ListenerDefinition;

	[CompilerGenerated]
	private List<Sales_Charges> m_InvocationDefinition;

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
	public List<Sales_Charges> ListSales_Charges
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
	public GetSales_ChargesResult()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool PrepareSystem()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool FlushSystem()
	{
		return true;
	}

	static GetSales_ChargesResult()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
