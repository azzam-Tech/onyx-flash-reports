using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Xml.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.DTOs;

[XmlRoot(ElementName = "EXPNS")]
public class EXPNS_DOC
{
	[CompilerGenerated]
	private DTS_EXPNS_MS? _SchemaSetter;

	[CompilerGenerated]
	private List<DTS_EXPNS_DTL>? m_TagSetter;

	[CompilerGenerated]
	private List<EXPNS_IMAGES>? _ConsumerSetter;

	[XmlElement]
	public DTS_EXPNS_MS? DTS_EXPNS_MST
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

	[XmlElement]
	public List<DTS_EXPNS_DTL>? DTS_EXPNS_DTL
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

	[XmlElement(ElementName = "IMAGES")]
	public List<EXPNS_IMAGES>? IMAGES
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
	public EXPNS_DOC()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool PublishIdentifier()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool SetupIdentifier()
	{
		return true;
	}

	static EXPNS_DOC()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
