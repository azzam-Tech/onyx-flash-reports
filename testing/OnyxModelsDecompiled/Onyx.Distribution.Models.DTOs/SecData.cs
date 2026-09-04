using System.Runtime.CompilerServices;
using Onyx.Containers;

namespace Onyx.Distribution.Models.DTOs;

public class SecData
{
	[CompilerGenerated]
	private string? writerTag;

	[CompilerGenerated]
	private string? m_ServiceTag;

	[CompilerGenerated]
	private string? m_ExporterTag;

	[CompilerGenerated]
	private string? _RegistryTag;

	[CompilerGenerated]
	private string? interpreterTag;

	[CompilerGenerated]
	private string? _SetterTag;

	public string? MOD_ID
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

	public string? CLIENT_ID
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

	public string? CLIENT_SEC
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

	public string? CLIENT_KEY
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

	public string? EXP_DATE
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

	public string? DBID
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
	public SecData()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool RestartAttribute()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool CreateAttribute()
	{
		return true;
	}

	static SecData()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
