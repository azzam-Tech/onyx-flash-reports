using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

public class FieldValueDouble
{
	private GeneralResult _ConfigurationCustomer;

	private double _FactoryCustomer;

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
	public double _FieldValue
	{
		[MethodImpl(MethodImplOptions.NoInlining)]
		get
		{
			return 0.0;
		}
		[MethodImpl(MethodImplOptions.NoInlining)]
		set
		{
		}
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public FieldValueDouble()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool AddObserver()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool RevertObserver()
	{
		return true;
	}

	static FieldValueDouble()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
