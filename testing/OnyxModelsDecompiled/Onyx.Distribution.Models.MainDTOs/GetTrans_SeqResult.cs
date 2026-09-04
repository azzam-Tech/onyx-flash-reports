using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

public class GetTrans_SeqResult
{
	private GeneralResult _MapperIndexer;

	private List<GetTrans_SeqObjct> _DispatcherIndexer;

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
	public List<GetTrans_SeqObjct> _List_GetTrans_SeqObjct
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
	public GetTrans_SeqResult()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool RevertRequest()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool DestroyException()
	{
		return true;
	}

	static GetTrans_SeqResult()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
