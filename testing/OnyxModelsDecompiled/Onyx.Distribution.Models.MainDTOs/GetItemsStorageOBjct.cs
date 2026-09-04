using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

public class GetItemsStorageOBjct
{
	private string _CollectionIndexer;

	private int _IteratorIndexer;

	private string _DicIndexer;

	private string _ProductIndexer;

	private double m_EventIndexer;

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
	public int _W_Code
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
	public string? _EXPIRE_DATE
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
	public string? _BATCH_NO
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
	public double _AVL_QTY
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
	public GetItemsStorageOBjct()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool OrderException()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool StartException()
	{
		return true;
	}

	static GetItemsStorageOBjct()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
