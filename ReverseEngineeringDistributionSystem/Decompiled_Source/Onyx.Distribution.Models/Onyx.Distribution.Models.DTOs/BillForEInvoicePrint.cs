using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using System.Xml.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.DTOs;

[DataContract]
[XmlRoot("DOC")]
public class BillForEInvoicePrint
{
	[CompilerGenerated]
	private BillMstForEInvoicePrint m_PublisherObject;

	[CompilerGenerated]
	private List<BillDtlForEInvoicePrint> _ValObject;

	[DataMember(EmitDefaultValue = false)]
	[XmlElement("DOC_MST")]
	public BillMstForEInvoicePrint BillMstForEInvoicePrint
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
	[XmlElement("DOC_DTL")]
	public List<BillDtlForEInvoicePrint> BillDtlsForEInvoicePrint
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
	public BillForEInvoicePrint()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool LoginSystem()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool QuerySystem()
	{
		return true;
	}

	static BillForEInvoicePrint()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
