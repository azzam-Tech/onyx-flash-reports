using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

public class GetFormsPrivilegeResult
{
	[CompilerGenerated]
	private GeneralResult tagDefinition;

	[CompilerGenerated]
	private List<FormsPrivilege> consumerDefinition;

	[DataMember]
	public GeneralResult Result
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
	public List<FormsPrivilege> LsitFormsPrivilege
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
	public GetFormsPrivilegeResult()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool SetRegistry()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool RateRegistry()
	{
		return true;
	}

	static GetFormsPrivilegeResult()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
