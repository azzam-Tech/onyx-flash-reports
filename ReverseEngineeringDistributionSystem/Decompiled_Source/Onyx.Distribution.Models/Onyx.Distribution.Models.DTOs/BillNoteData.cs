using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using System.Xml.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.DTOs;

[XmlRoot(ElementName = "ADD_DISC_RQ")]
public class BillNoteData
{
	[CompilerGenerated]
	private BillNoteForSave? m_ClientCode;

	[DataMember]
	[XmlElement(ElementName = "IAS_BILL_MST_ADD_DISC_RQ")]
	public BillNoteForSave? BillNoteForSave
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
	public BillNoteData()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool ConcatSystem()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool StopSystem()
	{
		return true;
	}

	static BillNoteData()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
