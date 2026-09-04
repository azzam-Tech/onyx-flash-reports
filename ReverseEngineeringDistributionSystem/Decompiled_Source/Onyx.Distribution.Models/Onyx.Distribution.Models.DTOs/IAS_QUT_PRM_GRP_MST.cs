using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.DTOs;

[DataContract]
public class IAS_QUT_PRM_GRP_MST
{
	[CompilerGenerated]
	private string? filterInterceptor;

	[CompilerGenerated]
	private string? m_ExceptionInterceptor;

	[CompilerGenerated]
	private string? m_SystemInterceptor;

	[CompilerGenerated]
	private string? _WatcherInterceptor;

	[CompilerGenerated]
	private string? m_StrategyInterceptor;

	[CompilerGenerated]
	private string? testsInterceptor;

	[DataMember]
	public string? PRM_GRP_NO
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
	public string? PRM_GRP_L_NM
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
	public string? PRM_GRP_F_NM
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
	public string? NVLCHK_ALL_ITMS
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
	public string? NVLGRNT_FREE_QTY_TYP
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
	public string? PRM_GRP_TYP
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
	public IAS_QUT_PRM_GRP_MST()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool CollectIdentifier()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool LogoutIdentifier()
	{
		return true;
	}

	static IAS_QUT_PRM_GRP_MST()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
