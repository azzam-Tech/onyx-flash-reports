using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

public class DocDescriptionObjct
{
	private int _PolicyIdentifier;

	private int m_DefinitionIdentifier;

	private string descriptorIdentifier;

	public int _LANG_NO
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
	public int _LABEL_NO
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
	public string? _CAPTION_DET
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
	public DocDescriptionObjct()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool InitException()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool RestartException()
	{
		return true;
	}

	static DocDescriptionObjct()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
