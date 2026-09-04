using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

public class VoucherData
{
	[CompilerGenerated]
	private ConnPara? m_SerializerMethod;

	[CompilerGenerated]
	private List<VoucherObjct> m_TemplateMethod;

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
	public List<VoucherObjct> ListVoucherObjct
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
	public VoucherData()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool CollectException()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool LogoutException()
	{
		return true;
	}

	static VoucherData()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
