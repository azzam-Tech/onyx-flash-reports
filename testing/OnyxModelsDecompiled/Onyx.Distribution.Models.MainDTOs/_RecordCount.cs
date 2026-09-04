using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

public class _RecordCount
{
	private GeneralResult m_RulesCustomer;

	private long m_IndexerCustomer;

	[DataMember]
	public GeneralResult GeneralResult
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
	public long _Cnt
	{
		[MethodImpl(MethodImplOptions.NoInlining)]
		get
		{
			return 0L;
		}
		[MethodImpl(MethodImplOptions.NoInlining)]
		set
		{
		}
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public _RecordCount()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool RateObserver()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool InstantiateObserver()
	{
		return true;
	}

	static _RecordCount()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
