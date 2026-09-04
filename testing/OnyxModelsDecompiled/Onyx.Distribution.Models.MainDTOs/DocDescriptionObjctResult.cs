using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

public class DocDescriptionObjctResult
{
	private GeneralResult _TaskIdentifier;

	private List<DocDescriptionObjct> _InfoIdentifier;

	[DataMember]
	public GeneralResult _Result
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
	public List<DocDescriptionObjct> _DocDescriptionObjct
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
	public DocDescriptionObjctResult()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool CreateException()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool ResetException()
	{
		return true;
	}

	static DocDescriptionObjctResult()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
