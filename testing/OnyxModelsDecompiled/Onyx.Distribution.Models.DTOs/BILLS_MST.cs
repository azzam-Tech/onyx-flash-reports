using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.DTOs;

[DataContract]
public class BILLS_MST
{
	[CompilerGenerated]
	private string? itemWriter;

	[CompilerGenerated]
	private string? m_CandidateWriter;

	[CompilerGenerated]
	private string? m_ComparatorWriter;

	[DataMember]
	public string? BILL_SER
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
	public string? BILL_NO
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
	public string? BILL_DATE
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
	public BILLS_MST()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool WriteAuthentication()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool OrderAuthentication()
	{
		return true;
	}

	static BILLS_MST()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
