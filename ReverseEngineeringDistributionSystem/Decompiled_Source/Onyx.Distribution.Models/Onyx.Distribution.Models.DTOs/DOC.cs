using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.DTOs;

[DataContract]
public class DOC
{
	[CompilerGenerated]
	private List<DOC_MST> ruleExporter;

	[CompilerGenerated]
	private List<DOC_DTL> m_ConfigExporter;

	[DataMember]
	public List<DOC_MST> DOC_MST
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
	public List<DOC_DTL> DOC_DTL
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
	public DOC()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool ReadAuthentication()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool RunAuthentication()
	{
		return true;
	}

	static DOC()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
