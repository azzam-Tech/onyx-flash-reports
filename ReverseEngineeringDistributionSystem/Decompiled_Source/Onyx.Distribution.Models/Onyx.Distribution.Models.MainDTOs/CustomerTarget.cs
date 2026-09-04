using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using System.Xml.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

[XmlRoot(ElementName = "CST")]
public class CustomerTarget
{
	[CompilerGenerated]
	private ConnPara? contextServer;

	[CompilerGenerated]
	private List<CustTrgtObjct> m_AdvisorServer;

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
	[XmlElement(ElementName = "DTS_CUSTOMER_TRGT")]
	public List<CustTrgtObjct> ListCustTrgtObjct
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
	public CustomerTarget()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool SetupRegistry()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool ChangeRegistry()
	{
		return true;
	}

	static CustomerTarget()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
