using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using System.Xml.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.DTOs;

[DataContract]
[XmlRoot(ElementName = "PRM")]
public class PromoterData
{
	[CompilerGenerated]
	private PromoterMst? _ReponseBase;

	[CompilerGenerated]
	private List<PromoterDtl>? m_AttrBase;

	[XmlElement(ElementName = "MST")]
	[DataMember]
	public PromoterMst? PromoterMst
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
	public List<PromoterDtl>? PromoterDtl
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
	public PromoterData()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool PostAttribute()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool AwakeAttribute()
	{
		return true;
	}

	static PromoterData()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
