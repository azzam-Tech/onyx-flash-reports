using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

public class GetLevelPriceOBjct
{
	private int specificationConfiguration;

	private string m_ParamConfiguration;

	private string methodConfiguration;

	private string m_IdentifierConfiguration;

	[CompilerGenerated]
	private string? serverConfiguration;

	[DataMember]
	public int _LEV_NO
	{
		[MethodImpl(MethodImplOptions.NoInlining)]
		get
		{
			return 0;
		}
		[MethodImpl(MethodImplOptions.NoInlining)]
		set
		{
		}
	}

	[DataMember]
	public string? _LEV_A_NAME
	{
		[MethodImpl(MethodImplOptions.NoInlining)]
		get
		{
			return null;
		}
		[MethodImpl(MethodImplOptions.NoInlining)]
		set
		{
		}
	}

	[DataMember]
	public string? _LEV_E_NAME
	{
		[MethodImpl(MethodImplOptions.NoInlining)]
		get
		{
			return null;
		}
		[MethodImpl(MethodImplOptions.NoInlining)]
		set
		{
		}
	}

	[DataMember]
	public string? _A_CY
	{
		[MethodImpl(MethodImplOptions.NoInlining)]
		get
		{
			return null;
		}
		[MethodImpl(MethodImplOptions.NoInlining)]
		set
		{
		}
	}

	[DataMember]
	public string? _LEV_DEFLT
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
	public GetLevelPriceOBjct()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool CalcException()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool ResolveException()
	{
		return true;
	}

	static GetLevelPriceOBjct()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
