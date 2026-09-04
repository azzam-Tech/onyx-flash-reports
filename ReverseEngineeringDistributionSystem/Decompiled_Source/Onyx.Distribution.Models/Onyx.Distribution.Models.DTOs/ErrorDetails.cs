using System.Runtime.CompilerServices;
using Onyx.Containers;

namespace Onyx.Distribution.Models.DTOs;

public class ErrorDetails
{
	[CompilerGenerated]
	private int _RegistrySetter;

	[CompilerGenerated]
	private string interpreterSetter;

	public int _ErrNo
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

	public string _ErrMsg
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
	public override string ToString()
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public ErrorDetails()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool VerifyIdentifier()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool PopIdentifier()
	{
		return true;
	}

	static ErrorDetails()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
