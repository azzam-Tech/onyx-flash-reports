using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.DTOs;

[DataContract]
public class SalesManBranchPriv
{
	[CompilerGenerated]
	private string? _WrapperSchema;

	[CompilerGenerated]
	private string? propertySchema;

	[CompilerGenerated]
	private string? _CollectionSchema;

	[CompilerGenerated]
	private string? m_IteratorSchema;

	[DataMember]
	public string? REP_CODE
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
	public string? BRN_NO
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
	public string? BRN_LNAME
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
	public string? BRN_FNAME
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
	public SalesManBranchPriv()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool RegisterAttribute()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool NewAttribute()
	{
		return true;
	}

	static SalesManBranchPriv()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
