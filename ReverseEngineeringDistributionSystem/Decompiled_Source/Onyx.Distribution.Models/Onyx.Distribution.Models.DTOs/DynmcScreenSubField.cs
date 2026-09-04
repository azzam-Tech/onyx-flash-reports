using System.Runtime.CompilerServices;
using Onyx.Containers;

namespace Onyx.Distribution.Models.DTOs;

public class DynmcScreenSubField
{
	[CompilerGenerated]
	private string? m_ProcInterpreter;

	[CompilerGenerated]
	private string? _ClassSetter;

	[CompilerGenerated]
	private string? m_CustomerSetter;

	[CompilerGenerated]
	private int mockSetter;

	public string? FLD_CODE
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

	public string? FLD_L_NM
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

	public string? FLD_F_NM
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

	public int langFlag
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
	public DynmcScreenSubField()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool PatchIdentifier()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool ReflectIdentifier()
	{
		return true;
	}

	static DynmcScreenSubField()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
