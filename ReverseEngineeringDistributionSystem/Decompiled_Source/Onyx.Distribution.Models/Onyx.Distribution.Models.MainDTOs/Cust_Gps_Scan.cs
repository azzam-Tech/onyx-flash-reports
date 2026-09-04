using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

public class Cust_Gps_Scan
{
	[CompilerGenerated]
	private ConnPara? m_IdentifierServer;

	[CompilerGenerated]
	private List<Cust_Gps_ScanObjct> m_ServerServer;

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
	public List<Cust_Gps_ScanObjct> ListCust_Gps_Scan
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
	public Cust_Gps_Scan()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool UpdateRegistry()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool VerifyRegistry()
	{
		return true;
	}

	static Cust_Gps_Scan()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
