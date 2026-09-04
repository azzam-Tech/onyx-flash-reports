using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using System.Xml.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.DTOs;

[DataContract]
[XmlRoot(ElementName = "ADD_DISC_RQ")]
public class BillNoteRequestData
{
	[CompilerGenerated]
	private BillNoteRequestForSave? m_MessageFacade;

	[CompilerGenerated]
	private List<BillNoteRequestDtlForSave>? writerFacade;

	[DataMember]
	[XmlElement(ElementName = "IAS_BILL_MST_ADD_DISC_RQ")]
	public BillNoteRequestForSave? BillNoteForSave
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
	[XmlElement(ElementName = "IAS_BILL_DTL_ADD_DSIC_RQ")]
	public List<BillNoteRequestDtlForSave>? billNoteDtlsForSave
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
	public BillNoteRequestData()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool DestroyAuthentication()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool PrepareAuthentication()
	{
		return true;
	}

	static BillNoteRequestData()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
