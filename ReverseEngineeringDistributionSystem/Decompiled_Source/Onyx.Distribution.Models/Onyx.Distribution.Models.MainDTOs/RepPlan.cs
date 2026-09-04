using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

public class RepPlan
{
	[CompilerGenerated]
	private List<RepPlanMst> m_PrinterPolicy;

	[CompilerGenerated]
	private List<RepPlanDtl> m_RolePolicy;

	[DataMember]
	public List<RepPlanMst> ListRepPlanMst
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

	[DataMember]
	public List<RepPlanDtl> ListRepPlanDtl
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
	public RepPlan()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool FillRegistry()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool SearchRegistry()
	{
		return true;
	}

	static RepPlan()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
