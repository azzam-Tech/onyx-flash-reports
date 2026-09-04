using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using System.Xml.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

[XmlRoot("OUT_REQUEST")]
public class RqTransfer
{
	[CompilerGenerated]
	private List<RqTransferMst> _ClientPolicy;

	[CompilerGenerated]
	private List<RqTransferDtl> broadcasterPolicy;

	[XmlElement("OUT_REQUEST_MST")]
	[DataMember]
	public List<RqTransferMst> ListRqTransferMst
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
	[XmlElement("OUT_REQUEST_DTL")]
	public List<RqTransferDtl> ListRqTransferDtl
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
	public RqTransfer()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool DisableRegistry()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool CancelRegistry()
	{
		return true;
	}

	static RqTransfer()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
