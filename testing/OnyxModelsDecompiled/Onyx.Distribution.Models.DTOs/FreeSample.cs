using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using System.Xml.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.DTOs;

[DataContract]
[XmlRoot(ElementName = "SAMPLE")]
public class FreeSample
{
	[CompilerGenerated]
	private FreeSampleMst? _WatcherSetter;

	[CompilerGenerated]
	private List<FreeSampleDtl>? strategySetter;

	[XmlElement(ElementName = "DTS_FREE_SMPL_MST")]
	[DataMember]
	public FreeSampleMst? DTS_FREE_SMPL_MST
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

	[XmlElement(ElementName = "DTS_FREE_SMPL_DTL")]
	[DataMember]
	public List<FreeSampleDtl>? DTS_FREE_SMPL_DTL
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
	public FreeSample()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool ForgotIdentifier()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool FillIdentifier()
	{
		return true;
	}

	static FreeSample()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
