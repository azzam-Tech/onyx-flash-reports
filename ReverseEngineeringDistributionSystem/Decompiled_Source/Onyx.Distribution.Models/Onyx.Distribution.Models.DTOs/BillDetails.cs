using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;
using Onyx.Distribution.Models.MainDTOs;

namespace Onyx.Distribution.Models.DTOs;

public class BillDetails
{
	[CompilerGenerated]
	private List<BillDetail> _ServiceObject;

	[CompilerGenerated]
	private List<BillOtherCharge> exporterObject;

	[CompilerGenerated]
	private List<Bill_TaxObjct> _RegistryObject;

	[DataMember]
	public List<BillDetail> BillDetailList
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
	public List<BillOtherCharge> BillOtherChargeList
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
	public List<Bill_TaxObjct> BillTaxList
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
	public BillDetails()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool RunSystem()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool RegisterSystem()
	{
		return true;
	}

	static BillDetails()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
