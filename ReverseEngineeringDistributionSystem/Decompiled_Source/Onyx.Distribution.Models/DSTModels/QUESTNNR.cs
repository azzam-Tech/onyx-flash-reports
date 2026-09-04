using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Xml.Serialization;
using Onyx.Containers;

namespace DSTModels;

[XmlRoot]
public class QUESTNNR
{
	[CompilerGenerated]
	private QST_MST? singleton;

	[CompilerGenerated]
	private List<QST_DTL>? repository;

	[CompilerGenerated]
	private List<QST_SUB_DTL>? _Reponse;

	[XmlElement]
	public QST_MST? QST_MST
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

	[XmlElement]
	public List<QST_DTL>? QST_DTL
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

	[XmlElement]
	public List<QST_SUB_DTL>? QST_SUB_DTL
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
	public QUESTNNR()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool PrintObserver()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool CalculateObserver()
	{
		return true;
	}

	static QUESTNNR()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
