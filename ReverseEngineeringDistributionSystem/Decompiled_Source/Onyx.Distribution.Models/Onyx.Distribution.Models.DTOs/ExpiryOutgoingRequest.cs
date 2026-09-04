using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using System.Xml.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.DTOs;

[DataContract]
[XmlRoot(ElementName = "EXPIRYOUTGOINGREQ")]
public class ExpiryOutgoingRequest
{
	[CompilerGenerated]
	private BillExpireMaster? setterSetter;

	[CompilerGenerated]
	private List<BillExpireDetail>? interceptorSetter;

	[XmlElement(ElementName = "IAS_BILL_EXPIRE_MST")]
	[DataMember]
	public BillExpireMaster? BillExpireMaster
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

	[XmlElement(ElementName = "IAS_BILL_EXPIRE_DTL")]
	[DataMember]
	public List<BillExpireDetail>? BillExpireDetails
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
	public ExpiryOutgoingRequest()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool ComputeIdentifier()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool CountIdentifier()
	{
		return true;
	}

	static ExpiryOutgoingRequest()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
