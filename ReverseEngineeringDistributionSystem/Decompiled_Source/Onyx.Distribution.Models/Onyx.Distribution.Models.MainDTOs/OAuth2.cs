using System.ComponentModel.DataAnnotations;
using System.Runtime.CompilerServices;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

public class OAuth2
{
	[CompilerGenerated]
	private string? m_StateTask;

	[CompilerGenerated]
	private string? m_MapTask;

	[Required(ErrorMessage = "ClientId is Required")]
	public string? ClientId
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

	[Required(ErrorMessage = "ClientSecret is Required")]
	public string? ClientSecret
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
	public OAuth2()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool ExcludeSystem()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool IncludeSystem()
	{
		return true;
	}

	static OAuth2()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
