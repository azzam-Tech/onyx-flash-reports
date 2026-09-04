using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

public class GetItemsStorageOBjctResult
{
	private GeneralResult _AdapterIndexer;

	private List<GetItemsStorageOBjct> _ManagerIndexer;

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

	[DataMember]
	public List<GetItemsStorageOBjct> _GetItemsStorageOBjct
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
	public GetItemsStorageOBjctResult()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool UpdateException()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool VerifyException()
	{
		return true;
	}

	static GetItemsStorageOBjctResult()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
