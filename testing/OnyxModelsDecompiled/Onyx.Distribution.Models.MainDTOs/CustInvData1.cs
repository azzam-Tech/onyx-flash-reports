using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

public class CustInvData1
{
	[CompilerGenerated]
	private ConnPara? _SystemIdentifier;

	[CompilerGenerated]
	private List<CustInv_MstObjct> m_WatcherIdentifier;

	[CompilerGenerated]
	private List<CustInv_DtlObjct> _StrategyIdentifier;

	[DataMember]
	public ConnPara? ConnPara
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
	public List<CustInv_MstObjct> ListCustInv_MstObjct
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
	public List<CustInv_DtlObjct> ListCustInv_DtlObjct
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
	public CustInvData1()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool FindRegistry()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool PatchRegistry()
	{
		return true;
	}

	static CustInvData1()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
