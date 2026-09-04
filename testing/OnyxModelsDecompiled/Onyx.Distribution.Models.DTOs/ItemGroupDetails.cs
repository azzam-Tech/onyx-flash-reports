using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.DTOs;

[DataContract]
public class ItemGroupDetails
{
	[CompilerGenerated]
	private string? requestProccesor;

	[CompilerGenerated]
	private string? _WrapperProccesor;

	[CompilerGenerated]
	private string? propertyProccesor;

	[DataMember]
	public string? G_CODE
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
	public string? G_A_NAME
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
	public string? G_E_NAME
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
	public ItemGroupDetails()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool VisitIdentifier()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool SetIdentifier()
	{
		return true;
	}

	static ItemGroupDetails()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
