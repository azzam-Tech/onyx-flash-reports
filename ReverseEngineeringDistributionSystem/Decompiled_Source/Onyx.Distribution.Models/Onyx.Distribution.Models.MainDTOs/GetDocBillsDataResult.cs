using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

public class GetDocBillsDataResult
{
	[CompilerGenerated]
	private GeneralResult singletonDefinition;

	[CompilerGenerated]
	private List<Bill_DtlObjct> repositoryDefinition;

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
	public List<Bill_DtlObjct> ListBillDtlObjct
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
	public GetDocBillsDataResult()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool InstantiateRegistry()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool AddRegistry()
	{
		return true;
	}

	static GetDocBillsDataResult()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
