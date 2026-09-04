using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

public class GetInvSerialParameterObjctResult
{
	private GeneralResult descriptorConfiguration;

	private int m_TaskConfiguration;

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
	public int _Man_Inv_Serail
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

	[MethodImpl(MethodImplOptions.NoInlining)]
	public GetInvSerialParameterObjctResult()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool DeleteException()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool PostException()
	{
		return true;
	}

	static GetInvSerialParameterObjctResult()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
