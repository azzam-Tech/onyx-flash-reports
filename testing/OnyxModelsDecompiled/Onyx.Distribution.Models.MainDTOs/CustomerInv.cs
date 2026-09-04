using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using System.Xml.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

[XmlRoot(ElementName = "STK")]
public class CustomerInv
{
	[CompilerGenerated]
	private ConnPara? m_PredicateIdentifier;

	[CompilerGenerated]
	private List<CustInv_MstObjct> _ContextIdentifier;

	[CompilerGenerated]
	private List<CustInv_DtlObjct> _AdvisorIdentifier;

	[CompilerGenerated]
	private int authenticationIdentifier;

	[CompilerGenerated]
	private int m_FilterIdentifier;

	[CompilerGenerated]
	private string? m_ExceptionIdentifier;

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

	[XmlElement(ElementName = "DTS_STK_CST_MST")]
	[DataMember]
	public List<CustInv_MstObjct> ListCustInv_Mst
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
	[XmlElement(ElementName = "DTS_STK_CST_DTL")]
	public List<CustInv_DtlObjct> ListCustInv_Dtl
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
	public int P_COMMIT_FLG
	{
		[MethodImpl(MethodImplOptions.NoInlining)]
		[CompilerGenerated]
		get
		{
			return 0;
		}
		[MethodImpl(MethodImplOptions.NoInlining)]
		[CompilerGenerated]
		set
		{
		}
	}

	[DataMember]
	public int P_DTS_ONLINE
	{
		[MethodImpl(MethodImplOptions.NoInlining)]
		[CompilerGenerated]
		get
		{
			return 0;
		}
		[MethodImpl(MethodImplOptions.NoInlining)]
		[CompilerGenerated]
		set
		{
		}
	}

	[DataMember]
	public string? LANG_NO
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
	public CustomerInv()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool SortRegistry()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool PushRegistry()
	{
		return true;
	}

	static CustomerInv()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
