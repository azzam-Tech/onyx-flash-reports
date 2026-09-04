using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.DTOs;

[DataContract]
public class FieldPriv
{
	[CompilerGenerated]
	private string? m_AccountSetter;

	[CompilerGenerated]
	private string? m_PredicateSetter;

	[CompilerGenerated]
	private string? _ContextSetter;

	[CompilerGenerated]
	private string? m_AdvisorSetter;

	[CompilerGenerated]
	private string? m_AuthenticationSetter;

	[DataMember]
	public string? P_code1
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
	public string? P_code1_NM
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
	public string? Add_Flag
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
	public string? View_Flag
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
	public string? Fill_Flag
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
	public FieldPriv()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool CancelIdentifier()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool RemoveIdentifier()
	{
		return true;
	}

	static FieldPriv()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
