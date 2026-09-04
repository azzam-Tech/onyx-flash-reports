using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.DTOs;

[DataContract]
public class ReportNameModel
{
	[CompilerGenerated]
	private string? m_InvocationSchema;

	[CompilerGenerated]
	private string? m_ConnectionSchema;

	[CompilerGenerated]
	private string? modelSchema;

	[DataMember]
	public string? DocType
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
	public string? ReportName
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
	public string? ReportTitle
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
	public ReportNameModel()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool ListAttribute()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool PrintAttribute()
	{
		return true;
	}

	static ReportNameModel()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
