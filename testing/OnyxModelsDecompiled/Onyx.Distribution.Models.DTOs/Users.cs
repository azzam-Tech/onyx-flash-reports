using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.DTOs;

public class Users
{
	[CompilerGenerated]
	private string? _CandidateConsumer;

	[CompilerGenerated]
	private string? _ComparatorConsumer;

	[DataMember]
	public string? U_ID
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
	public string? U_NAME
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
	public Users()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool ConnectExpression()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool WriteExpression()
	{
		return true;
	}

	static Users()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
