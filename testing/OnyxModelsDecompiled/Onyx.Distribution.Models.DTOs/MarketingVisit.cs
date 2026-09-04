using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using System.Xml.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.DTOs;

[XmlRoot(ElementName = "DOC")]
[DataContract]
public class MarketingVisit
{
	[CompilerGenerated]
	private MarktVistMst? _ConnectionDatabase;

	[CompilerGenerated]
	private List<MarktVistDtlDtl>? m_ModelDatabase;

	[CompilerGenerated]
	private List<MarktVistDtl>? m_PublisherDatabase;

	[XmlElement(ElementName = "MST")]
	[DataMember]
	public MarktVistMst? MARKT_VIST_MST
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

	[XmlElement(ElementName = "DTL_DTL")]
	[DataMember]
	public List<MarktVistDtlDtl>? MARKT_VIST_DTL_DTL
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
	[XmlElement(ElementName = "DTL")]
	public List<MarktVistDtl>? MARKT_VIST_DTL
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
	public MarketingVisit()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool ValidateAttribute()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool ConnectAttribute()
	{
		return true;
	}

	static MarketingVisit()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
