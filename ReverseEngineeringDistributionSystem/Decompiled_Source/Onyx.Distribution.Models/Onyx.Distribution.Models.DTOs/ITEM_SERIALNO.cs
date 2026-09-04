using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.DTOs;

[DataContract]
public class ITEM_SERIALNO
{
	[CompilerGenerated]
	private string? _ConfigurationDatabase;

	[CompilerGenerated]
	private string? m_FactoryDatabase;

	[CompilerGenerated]
	private string? _SpecificationDatabase;

	[CompilerGenerated]
	private string? m_ParamDatabase;

	[CompilerGenerated]
	private string? methodDatabase;

	[CompilerGenerated]
	private string? _IdentifierDatabase;

	[DataMember(EmitDefaultValue = false)]
	public string? I_CODE
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

	[DataMember(EmitDefaultValue = false)]
	public string? ITM_UNT
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

	[DataMember(EmitDefaultValue = false)]
	public string? SERIALNO
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

	[DataMember(EmitDefaultValue = false)]
	public string? W_CODE
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

	[DataMember(EmitDefaultValue = false)]
	public string? EXPIRE_DATE
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

	[DataMember(EmitDefaultValue = false)]
	public string? BATCH_NO
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
	public ITEM_SERIALNO()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool DestroyAttribute()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool PrepareAttribute()
	{
		return true;
	}

	static ITEM_SERIALNO()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
