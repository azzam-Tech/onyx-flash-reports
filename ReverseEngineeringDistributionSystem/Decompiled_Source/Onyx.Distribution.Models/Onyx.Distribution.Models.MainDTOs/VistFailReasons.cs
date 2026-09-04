using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

public class VistFailReasons
{
	[CompilerGenerated]
	private string? requestPolicy;

	[CompilerGenerated]
	private string? _WrapperPolicy;

	[CompilerGenerated]
	private string? m_PropertyPolicy;

	[DataMember]
	public string? RESON_TYP
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
	public string? RESON_L_DSC
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
	public string? RESON_F_DSC
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
	public VistFailReasons()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool PrintRegistry()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool CalculateRegistry()
	{
		return true;
	}

	static VistFailReasons()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
