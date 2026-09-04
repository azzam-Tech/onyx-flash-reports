using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

public class CustCreditPreiodResult
{
	[CompilerGenerated]
	private GeneralResult _SetterServer;

	[CompilerGenerated]
	private List<CustCreditPreiodObjct> interceptorServer;

	[CompilerGenerated]
	private List<GetCurrncyOBjct> proccesorServer;

	[DataMember]
	public GeneralResult _Result
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
	public List<CustCreditPreiodObjct> CustCreditPreiodObjctList
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
	public List<GetCurrncyOBjct> _GetCurrncyOBjct
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
	public CustCreditPreiodResult()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool CountRegistry()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool AssetRegistry()
	{
		return true;
	}

	static CustCreditPreiodResult()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
