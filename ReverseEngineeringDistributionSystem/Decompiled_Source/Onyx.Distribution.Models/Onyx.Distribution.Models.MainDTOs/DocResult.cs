using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

public class DocResult
{
	[CompilerGenerated]
	private string? _Proc;

	[CompilerGenerated]
	private int _ClassCustomer;

	[CompilerGenerated]
	private string? m_CustomerCustomer;

	[DataMember]
	public string? Doc_Ser
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
	public int ErrNo
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
	public string? ErrMsg
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
	public DocResult()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool ConcatObserver()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool StopObserver()
	{
		return true;
	}

	static DocResult()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
