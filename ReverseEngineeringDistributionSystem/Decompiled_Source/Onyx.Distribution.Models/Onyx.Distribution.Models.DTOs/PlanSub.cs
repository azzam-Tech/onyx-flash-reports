using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using System.Xml.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.DTOs;

[DataContract]
[XmlRoot("TASKS")]
public class PlanSub
{
	[CompilerGenerated]
	private List<PlanSubDtl>? bridgeBase;

	[DataMember]
	[XmlElement("TASK")]
	public List<PlanSubDtl>? PlanTask
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
	public PlanSub()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool ChangeAttribute()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool CalcAttribute()
	{
		return true;
	}

	static PlanSub()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
