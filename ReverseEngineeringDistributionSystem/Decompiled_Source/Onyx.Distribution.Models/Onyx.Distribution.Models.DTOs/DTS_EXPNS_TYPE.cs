using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.DTOs;

[DataContract]
public class DTS_EXPNS_TYPE
{
	[CompilerGenerated]
	private string? _FilterInterpreter;

	[CompilerGenerated]
	private string? exceptionInterpreter;

	[CompilerGenerated]
	private string? systemInterpreter;

	[CompilerGenerated]
	private string? _WatcherInterpreter;

	[CompilerGenerated]
	private string? m_StrategyInterpreter;

	[CompilerGenerated]
	private string? m_TestsInterpreter;

	[CompilerGenerated]
	private string? _RefInterpreter;

	[DataMember]
	public string? EXPN_NO
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
	public string? EXPN_L_NM
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
	public string? EXPN_F_NM
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
	public string? AC_CODE
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
	public string? AC_CODE_DTL
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
	public string? AC_DTL_TYP
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
	public string? A_CY
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
	public DTS_EXPNS_TYPE()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool InstantiateAuthentication()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool AddAuthentication()
	{
		return true;
	}

	static DTS_EXPNS_TYPE()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
