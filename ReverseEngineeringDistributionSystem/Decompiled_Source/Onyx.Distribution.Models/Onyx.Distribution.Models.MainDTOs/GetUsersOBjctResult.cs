using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;
using Onyx.Distribution.Models.DTOs;

namespace Onyx.Distribution.Models.MainDTOs;

public class GetUsersOBjctResult
{
	private GeneralResult _ContextCustomer;

	private List<GetUsersOBjct> m_AdvisorCustomer;

	[CompilerGenerated]
	private List<GeneralConfigerationData> _AuthenticationCustomer;

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
	public List<GetUsersOBjct> _GetUsersOBjct
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
	public List<GeneralConfigerationData> GeneralConfigerationDataList
	{
		[MethodImpl(MethodImplOptions.NoInlining)]
		[CompilerGenerated]
		get
		{
			return null;
		}
		[MethodImpl(MethodImplOptions.NoInlining)]
		[CompilerGenerated]
		set
		{
		}
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public GetUsersOBjctResult()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool ReflectRequest()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool CustomizeRequest()
	{
		return true;
	}

	static GetUsersOBjctResult()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
