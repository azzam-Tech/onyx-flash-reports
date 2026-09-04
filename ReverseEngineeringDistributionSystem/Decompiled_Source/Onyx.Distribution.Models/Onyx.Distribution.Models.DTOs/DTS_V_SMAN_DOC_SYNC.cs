using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.DTOs;

[DataContract]
public class DTS_V_SMAN_DOC_SYNC
{
	[CompilerGenerated]
	private string? _TemplateInterpreter;

	[CompilerGenerated]
	private string? recordInterpreter;

	[DataMember]
	public string? DOC_TYPE
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
	public string? SYNC_METHOD
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
	public DTS_V_SMAN_DOC_SYNC()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool PrepareIdentifier()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool FlushIdentifier()
	{
		return true;
	}

	static DTS_V_SMAN_DOC_SYNC()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
