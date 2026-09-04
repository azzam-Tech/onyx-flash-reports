using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using System.Xml.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

[DataContract]
[XmlRoot(ElementName = "RT_BILL")]
public class RtBillsData
{
	[CompilerGenerated]
	private ConnPara? m_PageDefinition;

	[CompilerGenerated]
	private RtBillMst? m_IssuerDefinition;

	[CompilerGenerated]
	private List<RtBill_DtlObjct>? m_MappingDefinition;

	[CompilerGenerated]
	private List<Other_Charges>? _ParameterDefinition;

	[CompilerGenerated]
	private List<Bill_TaxObjct>? _OrderDefinition;

	[CompilerGenerated]
	private List<Bill_TaxObjct>? paramsDefinition;

	[DataMember(EmitDefaultValue = false)]
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

	[XmlElement(ElementName = "IAS_RT_BILL_MST")]
	[DataMember]
	public RtBillMst? ListBill_MstObjct
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
	[XmlElement(ElementName = "IAS_RT_BILL_DTL")]
	public List<RtBill_DtlObjct>? ListBill_DtlObjct
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
	public RtBillsData()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool OrderSystem()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool StartSystem()
	{
		return true;
	}

	static RtBillsData()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
