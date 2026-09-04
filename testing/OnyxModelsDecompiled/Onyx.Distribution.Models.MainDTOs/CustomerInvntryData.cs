using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

public class CustomerInvntryData
{
	[CompilerGenerated]
	private ConnPara? m_SystemMethod;

	[CompilerGenerated]
	private List<Customer_Invntry_MstObjct> m_WatcherMethod;

	[CompilerGenerated]
	private List<Customer_Invntry_DtlObjct> strategyMethod;

	[DataMember]
	public ConnPara? ConnPara
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
	public List<Customer_Invntry_MstObjct> ListCustomerInvntry_MstObjct
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
	public List<Customer_Invntry_DtlObjct> ListCustomerInvntry_DtlObjct
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
	public CustomerInvntryData()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool MoveException()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool ReadException()
	{
		return true;
	}

	static CustomerInvntryData()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
