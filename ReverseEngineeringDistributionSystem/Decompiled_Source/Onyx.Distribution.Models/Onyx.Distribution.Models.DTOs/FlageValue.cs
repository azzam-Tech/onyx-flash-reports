using System.Runtime.CompilerServices;
using Onyx.Containers;

namespace Onyx.Distribution.Models.DTOs;

public class FlageValue
{
	[CompilerGenerated]
	private string? m_FilterSetter;

	[CompilerGenerated]
	private string? m_ExceptionSetter;

	[CompilerGenerated]
	private double m_SystemSetter;

	public string? Code
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

	public string? Name
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

	public double Typ
	{
		[MethodImpl(MethodImplOptions.NoInlining)]
		[CompilerGenerated]
		get
		{
			return 0.0;
		}
		[MethodImpl(MethodImplOptions.NoInlining)]
		[CompilerGenerated]
		set
		{
		}
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public FlageValue()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool InterruptIdentifier()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool DefineIdentifier()
	{
		return true;
	}

	static FlageValue()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
