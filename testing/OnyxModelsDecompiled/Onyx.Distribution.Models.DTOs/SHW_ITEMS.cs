using System.Collections.Generic;
using System.Runtime.CompilerServices;
using Onyx.Containers;

namespace Onyx.Distribution.Models.DTOs;

public class SHW_ITEMS
{
	[CompilerGenerated]
	private SHW_ITEMS_MST? reponseTag;

	[CompilerGenerated]
	private List<SHW_ITEMS_DTL>? _AttrTag;

	[CompilerGenerated]
	private List<SHW_ITEMS_IMGS>? _ExpressionTag;

	public SHW_ITEMS_MST? SHW_ITEMS_MST
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

	public List<SHW_ITEMS_DTL>? SHW_ITEMS_DTLLIST
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

	public List<SHW_ITEMS_IMGS>? SHW_ITEMS_IMGSLIST
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
	public SHW_ITEMS()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool StopAttribute()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool VisitAttribute()
	{
		return true;
	}

	static SHW_ITEMS()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
