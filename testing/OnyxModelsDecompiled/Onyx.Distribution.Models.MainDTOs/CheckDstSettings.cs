using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

public class CheckDstSettings
{
	[CompilerGenerated]
	private int _AdapterPolicy;

	[DataMember]
	public int BRN_NO
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
	public CheckDstSettings()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool RunRegistry()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool RegisterRegistry()
	{
		return true;
	}

	static CheckDstSettings()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
