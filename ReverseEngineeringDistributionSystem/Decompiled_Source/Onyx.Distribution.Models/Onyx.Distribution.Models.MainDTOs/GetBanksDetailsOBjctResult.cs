using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

public class GetBanksDetailsOBjctResult
{
	private GeneralResult reponseMock;

	private List<GetBanksDetailsOBjct> m_AttrMock;

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
	public List<GetBanksDetailsOBjct> _GetBanksDetailsOBjct
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
	public GetBanksDetailsOBjctResult()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool ChangeRequest()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool CalcRequest()
	{
		return true;
	}

	static GetBanksDetailsOBjctResult()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
