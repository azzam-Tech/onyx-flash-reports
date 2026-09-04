using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.DTOs;

[DataContract]
public class MandatoryData
{
	[CompilerGenerated]
	private string? m_RoleDatabase;

	[CompilerGenerated]
	private string? _ListenerDatabase;

	[CompilerGenerated]
	private string? m_InvocationDatabase;

	[DataMember]
	public string? FORM_NO
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
	public string? TBL_NM
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
	public string? FLD_NM
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
	public MandatoryData()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool ReflectAttribute()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool CustomizeAttribute()
	{
		return true;
	}

	static MandatoryData()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
