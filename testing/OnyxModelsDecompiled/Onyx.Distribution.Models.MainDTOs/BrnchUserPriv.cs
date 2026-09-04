using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

public class BrnchUserPriv
{
	[CompilerGenerated]
	private string? m_DicPolicy;

	[DataMember]
	public string? BRN_NO
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
	public BrnchUserPriv()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool ManageRegistry()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool CloneRegistry()
	{
		return true;
	}

	static BrnchUserPriv()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
