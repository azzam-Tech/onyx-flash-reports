using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

public class FieldValueString
{
	private GeneralResult _SpecificationCustomer;

	private string m_ParamCustomer;

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
	public string? _FieldValue
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

	[MethodImpl(MethodImplOptions.NoInlining)]
	public FieldValueString()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool DestroyRequest()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool PrepareRequest()
	{
		return true;
	}

	static FieldValueString()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
