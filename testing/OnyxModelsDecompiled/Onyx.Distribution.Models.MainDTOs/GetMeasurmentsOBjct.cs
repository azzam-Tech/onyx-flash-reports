using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

public class GetMeasurmentsOBjct
{
	private string m_MockDecorator;

	private string decoratorDecorator;

	[CompilerGenerated]
	private string? _RulesDecorator;

	public string? _MEASURE_CODE
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
	public string? _MEASURE
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
	public string? UNT_SALE_TYP
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
	public GetMeasurmentsOBjct()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool EnableRequest()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool InsertRequest()
	{
		return true;
	}

	static GetMeasurmentsOBjct()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
