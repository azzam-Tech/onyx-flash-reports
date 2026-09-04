using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using System.Xml.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

[XmlRoot(ElementName = "BILL")]
[DataContract]
public class BillsData
{
	[CompilerGenerated]
	private Bill_MstObjct? facadeConfiguration;

	[CompilerGenerated]
	private ConnPara? messageConfiguration;

	[CompilerGenerated]
	private List<Bill_MstObjct>? _WriterConfiguration;

	[CompilerGenerated]
	private List<Bill_DtlObjct>? serviceConfiguration;

	[CompilerGenerated]
	private List<Other_Charges>? _ExporterConfiguration;

	[CompilerGenerated]
	private List<Bill_TaxObjct>? _RegistryConfiguration;

	[CompilerGenerated]
	private List<Bill_TaxObjct>? _InterpreterConfiguration;

	[DataMember]
	[XmlElement(ElementName = "IAS_BILL_MST")]
	public Bill_MstObjct? IAS_BILL_MST
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

	[DataMember]
	public List<Bill_MstObjct>? ListBill_MstObjct
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
	[XmlElement(ElementName = "IAS_BILL_DTL")]
	public List<Bill_DtlObjct>? ListBill_DtlObjct
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
	public BillsData()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool DisableException()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool CancelException()
	{
		return true;
	}

	static BillsData()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
