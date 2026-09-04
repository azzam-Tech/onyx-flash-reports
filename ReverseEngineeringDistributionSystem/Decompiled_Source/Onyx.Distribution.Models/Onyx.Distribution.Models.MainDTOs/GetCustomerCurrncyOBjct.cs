using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

public class GetCustomerCurrncyOBjct
{
	private string _ParameterCustomer;

	private string m_OrderCustomer;

	private string _ParamsCustomer;

	private string m_MerchantCustomer;

	private double initializerCustomer;

	private string creatorCustomer;

	private string m_ErrorCustomer;

	private int _SerializerCustomer;

	private double templateCustomer;

	private double _RecordCustomer;

	public string? _CUR_CODE
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
	public string? _CUR_NAME
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
	public string? _CUR_E_NAME
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
	public double _CUR_RATE
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

	[DataMember]
	public string? _CUR_FRACTION
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
	public string? _CUR_E_FRACTION
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
	public int _L_F
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
	public double _MAX_CUR_RATE
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

	[DataMember]
	public double _MIN_CUR_RATE
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
	public GetCustomerCurrncyOBjct()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool StartRequest()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool UpdateRequest()
	{
		return true;
	}

	static GetCustomerCurrncyOBjct()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
