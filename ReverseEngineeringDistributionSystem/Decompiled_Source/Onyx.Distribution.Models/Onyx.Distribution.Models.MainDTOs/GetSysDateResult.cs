using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

public class GetSysDateResult
{
	private GeneralResult _ServerCustomer;

	private string m_PolicyCustomer;

	[CompilerGenerated]
	private int _DefinitionCustomer;

	[CompilerGenerated]
	private int _DescriptorCustomer;

	[CompilerGenerated]
	private int m_TaskCustomer;

	[CompilerGenerated]
	private string? m_InfoCustomer;

	[CompilerGenerated]
	private string? clientCustomer;

	[CompilerGenerated]
	private string? _BroadcasterCustomer;

	[DataMember]
	public GeneralResult GeneralResult
	{
		[MethodImpl(MethodImplOptions.NoInlining)]
		get
		{
			return null;
		}
		[MethodImpl(MethodImplOptions.NoInlining)]
		set
		{
		}
	}

	[DataMember]
	public string? _Sys_Date
	{
		[MethodImpl(MethodImplOptions.NoInlining)]
		get
		{
			return null;
		}
		[MethodImpl(MethodImplOptions.NoInlining)]
		set
		{
		}
	}

	[DataMember]
	public int YEAR_NO
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
	public int BRN_USR
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
	public int FORCE_UPDATE
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
	public string? DBversionCode
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
	public string? WsVer_No
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
	public string? Token
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
	public GetSysDateResult()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool SortRequest()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool PushRequest()
	{
		return true;
	}

	static GetSysDateResult()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
