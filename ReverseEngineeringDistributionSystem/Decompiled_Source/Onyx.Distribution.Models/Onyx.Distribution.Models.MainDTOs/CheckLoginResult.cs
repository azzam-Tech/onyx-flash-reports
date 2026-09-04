using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

public class CheckLoginResult
{
	private string _MockCustomer;

	private GeneralResult m_DecoratorCustomer;

	[DataMember]
	public string? _User_Name
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
	public GeneralResult _Result
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
	public CheckLoginResult()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool VisitObserver()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool SetObserver()
	{
		return true;
	}

	static CheckLoginResult()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
