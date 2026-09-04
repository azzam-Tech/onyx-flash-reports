using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using System.Xml.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

[XmlRoot(ElementName = "QUOT")]
public class QuotationsData
{
	[CompilerGenerated]
	private ConnPara? m_ValueParam;

	[CompilerGenerated]
	private Quotation_MstObjct? m_InstanceParam;

	[CompilerGenerated]
	private List<Quotation_DtlObjct>? mapperParam;

	[CompilerGenerated]
	private List<Other_Charges>? m_DispatcherParam;

	[CompilerGenerated]
	private List<Bill_TaxObjct>? fieldParam;

	[CompilerGenerated]
	private List<Bill_TaxObjct>? m_AccountParam;

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
	[XmlElement(ElementName = "QUOTATION")]
	public Quotation_MstObjct? ListQuotation_MstObjct
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
	[XmlElement(ElementName = "QUOTATION_DETAIL")]
	public List<Quotation_DtlObjct>? ListQuotation_DtlObjct
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

	[XmlElement(ElementName = "OTHER_CHARGES")]
	[DataMember]
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
	public QuotationsData()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool PrintException()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool CalculateException()
	{
		return true;
	}

	static QuotationsData()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
