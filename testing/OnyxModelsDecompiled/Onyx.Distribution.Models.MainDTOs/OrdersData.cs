using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using System.Xml.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

[XmlRoot(ElementName = "SAL_ORDR")]
public class OrdersData
{
	[CompilerGenerated]
	private ConnPara? tagSpecification;

	[CompilerGenerated]
	private Order_MstObjct? _ConsumerSpecification;

	[CompilerGenerated]
	private List<Order_MstObjct>? _SingletonSpecification;

	[CompilerGenerated]
	private List<Order_DtlObjct>? _RepositorySpecification;

	[CompilerGenerated]
	private List<Other_Charges>? m_ReponseSpecification;

	[CompilerGenerated]
	private List<Bill_TaxObjct>? m_AttrSpecification;

	[CompilerGenerated]
	private List<Bill_TaxObjct>? m_ExpressionSpecification;

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
	[XmlElement(ElementName = "SALES_ORDER")]
	public Order_MstObjct? SALES_ORDER
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
	public List<Order_MstObjct>? ListOrder_MstObjct
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

	[XmlElement(ElementName = "ORDER_DETAIL")]
	[DataMember]
	public List<Order_DtlObjct>? ListOrder_DtlObjct
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
	[XmlElement(ElementName = "OTHER_CHARGES")]
	public List<Other_Charges>? ListOther_ChargesObjct
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
	[XmlElement(ElementName = "GNR_TAX_ITM_MOVMNT")]
	public List<Bill_TaxObjct>? ListBill_TaxObjct
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
	[XmlElement(ElementName = "GNR_TAX_INPT_MOVMNT")]
	public List<Bill_TaxObjct>? GNR_TAX_INPT_MOVMNT
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
	public OrdersData()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool SearchException()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool EnableException()
	{
		return true;
	}

	static OrdersData()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
