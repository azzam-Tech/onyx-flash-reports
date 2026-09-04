using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

public class GetInventroyTypesOBjct
{
	private int _ContainerIndexer;

	private string algoIndexer;

	private string m_ComposerIndexer;

	[DataMember]
	public int _Inv_Type_No
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

	[DataMember]
	public string? _Inv_Type_Name
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
	public string? _Inv_Type_Ename
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
	public GetInventroyTypesOBjct()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool PopException()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool ComputeException()
	{
		return true;
	}

	static GetInventroyTypesOBjct()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
