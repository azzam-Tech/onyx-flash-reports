using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;
using Onyx.Distribution.Models.DTOs;

namespace Onyx.Distribution.Models.MainDTOs;

public class GetPlanDetailsOBjctResult
{
	private GeneralResult _ListDecorator;

	private List<GetPlanDetailsOBjct> _ItemDecorator;

	[CompilerGenerated]
	private List<PlanSubDtl> m_CandidateDecorator;

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
	public List<GetPlanDetailsOBjct> _GetPlanDetailsOBjct
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
	public List<PlanSubDtl> PlanSubDtls
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
	public GetPlanDetailsOBjctResult()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool CalculateRequest()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool SelectRequest()
	{
		return true;
	}

	static GetPlanDetailsOBjctResult()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
