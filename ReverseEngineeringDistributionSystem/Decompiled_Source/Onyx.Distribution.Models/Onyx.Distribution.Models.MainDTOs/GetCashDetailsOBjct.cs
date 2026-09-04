using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

public class GetCashDetailsOBjct
{
	private string parserMock;

	private string _StatusMock;

	private string _TokenMock;

	private string testMock;

	private string m_HelperMock;

	private string m_WorkerMock;

	public string? _REP_CODE
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
	public string? _CASH_NO
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
	public string? _CASH_NAME
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
	public string? _CASH_E_NAME
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
	public string? _CASH_SR
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
	public string? _A_CODE
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

	[MethodImpl(MethodImplOptions.NoInlining)]
	public GetCashDetailsOBjct()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool CancelRequest()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool RemoveRequest()
	{
		return true;
	}

	static GetCashDetailsOBjct()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
