using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using System.Xml.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.DTOs;

[DataContract]
[XmlRoot(ElementName = "ADD_DISC")]
public class CustomerNote
{
	[CompilerGenerated]
	private CustomerNoteMst? m_FactoryService;

	[CompilerGenerated]
	private List<CustomerNoteDtl>? m_SpecificationService;

	[DataMember]
	[XmlElement(ElementName = "IAS_BILL_MST_ADD_DISC")]
	public CustomerNoteMst? CustomerNoteMst
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

	[XmlElement(ElementName = "IAS_BILL_DTL_ADD_DISC")]
	[DataMember]
	public List<CustomerNoteDtl>? CustomerNoteDtls
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
	public CustomerNote()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool DefineAuthentication()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool ForgotAuthentication()
	{
		return true;
	}

	static CustomerNote()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
