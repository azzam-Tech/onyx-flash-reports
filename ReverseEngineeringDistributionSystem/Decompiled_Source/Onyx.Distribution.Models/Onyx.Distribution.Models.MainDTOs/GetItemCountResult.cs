using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

public class GetItemCountResult
{
	[CompilerGenerated]
	private GeneralResult _RegistryDefinition;

	[CompilerGenerated]
	private string? m_InterpreterDefinition;

	[DataMember]
	public GeneralResult GeneralResult
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
	public string? ItemCount
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
	public GetItemCountResult()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool ResetRegistry()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool ConcatRegistry()
	{
		return true;
	}

	static GetItemCountResult()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
