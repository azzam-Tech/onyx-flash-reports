using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.DTOs;

[DataContract]
public class CUSTOMER_CLASS
{
	[CompilerGenerated]
	private string? _AnnotationExporter;

	[CompilerGenerated]
	private string? m_PoolExporter;

	[CompilerGenerated]
	private string? attributeExporter;

	[CompilerGenerated]
	private string? _PrinterExporter;

	[DataMember]
	public string? C_CLASS
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
	public string? C_CLASS_NAME
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
	public string? C_CLASS_E_NAME
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
	public string? TYP
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
	public CUSTOMER_CLASS()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool CompareAuthentication()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool ManageAuthentication()
	{
		return true;
	}

	static CUSTOMER_CLASS()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
