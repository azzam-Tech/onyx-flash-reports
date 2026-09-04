using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

public class FieldValueInt
{
	private GeneralResult m_MethodCustomer;

	private int m_IdentifierCustomer;

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
	public int _FieldValue
	{
		[MethodImpl(MethodImplOptions.NoInlining)]
		get
		{
			return 0;
		}
		[MethodImpl(MethodImplOptions.NoInlining)]
		set
		{
		}
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public FieldValueInt()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool FlushRequest()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool CheckRequest()
	{
		return true;
	}

	static FieldValueInt()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
