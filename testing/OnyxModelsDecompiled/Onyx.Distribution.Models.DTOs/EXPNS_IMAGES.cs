using System.Runtime.CompilerServices;
using Onyx.Containers;

namespace Onyx.Distribution.Models.DTOs;

public class EXPNS_IMAGES
{
	[CompilerGenerated]
	private string? valSetter;

	public string? FILE_NAME
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
	public EXPNS_IMAGES()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool IncludeIdentifier()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool DeleteIdentifier()
	{
		return true;
	}

	static EXPNS_IMAGES()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
