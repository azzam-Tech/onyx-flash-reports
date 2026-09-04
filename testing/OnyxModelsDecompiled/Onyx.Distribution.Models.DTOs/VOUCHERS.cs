using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using System.Xml.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.DTOs;

[DataContract]
[XmlRoot(ElementName = "ROWSET")]
public class VOUCHERS
{
	[CompilerGenerated]
	private VOUCHER_MST? _InterpreterSingleton;

	[CompilerGenerated]
	private List<VOUCHER_DTL>? m_SetterSingleton;

	[DataMember]
	[XmlElement(ElementName = "ROW")]
	public VOUCHER_MST? VOUCHER_MST
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

	[XmlElement(ElementName = "ROW_DTL")]
	[DataMember]
	public List<VOUCHER_DTL>? VOUCHER_DTL_LIST
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
	public VOUCHERS()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool PopExpression()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool ComputeExpression()
	{
		return true;
	}

	static VOUCHERS()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
