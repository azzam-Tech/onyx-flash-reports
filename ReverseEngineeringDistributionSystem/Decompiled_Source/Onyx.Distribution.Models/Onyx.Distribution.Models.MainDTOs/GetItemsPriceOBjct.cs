using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

public class GetItemsPriceOBjct
{
	private int _CustomerConfiguration;

	private string _MockConfiguration;

	private string _DecoratorConfiguration;

	private int _RulesConfiguration;

	private double indexerConfiguration;

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
	public string? _I_CODE
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
	public string? _ITM_UNT
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
	public int _W_CODE
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
	public double _I_PRICE
	{
		[MethodImpl(MethodImplOptions.NoInlining)]
		get
		{
			return 0.0;
		}
		[MethodImpl(MethodImplOptions.NoInlining)]
		set
		{
		}
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public GetItemsPriceOBjct()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool CallException()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool PublishException()
	{
		return true;
	}

	static GetItemsPriceOBjct()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
