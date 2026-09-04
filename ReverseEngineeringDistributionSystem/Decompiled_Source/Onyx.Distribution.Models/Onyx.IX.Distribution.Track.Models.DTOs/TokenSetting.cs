using System.Runtime.CompilerServices;
using Onyx.Containers;

namespace Onyx.IX.Distribution.Track.Models.DTOs;

public class TokenSetting
{
	[CompilerGenerated]
	private int _List;

	public int ExpirationTimeInSeconds
	{
		[MethodImpl(MethodImplOptions.NoInlining)]
		[CompilerGenerated]
		get
		{
			return 0;
		}
		[MethodImpl(MethodImplOptions.NoInlining)]
		[CompilerGenerated]
		set
		{
		}
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public TokenSetting()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool SelectObserver()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool CompareObserver()
	{
		return true;
	}

	static TokenSetting()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
