using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.DTOs;

[DataContract]
public class GpsPara
{
	[CompilerGenerated]
	private string? predicateInterceptor;

	[CompilerGenerated]
	private string? m_ContextInterceptor;

	[CompilerGenerated]
	private string? m_AdvisorInterceptor;

	[CompilerGenerated]
	private string? _AuthenticationInterceptor;

	[DataMember]
	public string? INACTIVEGPS
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
	public string? GPS_TRACK_INTRVAL_IN_SEC
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
	public string? GPS_POST_INTRVAL_IN_SEC
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
	public string? GPS_DISTANCE_TRACK_IN_METR
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
	public GpsPara()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool RegisterIdentifier()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool NewIdentifier()
	{
		return true;
	}

	static GpsPara()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
