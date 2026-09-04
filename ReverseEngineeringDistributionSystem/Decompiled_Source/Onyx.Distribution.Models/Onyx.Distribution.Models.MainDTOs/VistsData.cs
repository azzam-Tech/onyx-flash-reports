using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using System.Xml.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

[XmlRoot(ElementName = "VST")]
public class VistsData
{
	[CompilerGenerated]
	private ConnPara? _RepositoryIdentifier;

	[CompilerGenerated]
	private List<Vists_MstObjct>? m_ReponseIdentifier;

	[CompilerGenerated]
	private List<Vist_DtlObjct>? m_AttrIdentifier;

	[DataMember]
	public ConnPara? ConnPara
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
	[XmlElement(ElementName = "DTS_CST_VST_MST")]
	public List<Vists_MstObjct>? ListVists_MstObjct
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

	[XmlElement(ElementName = "DTS_CST_VST_DTL")]
	[DataMember]
	public List<Vist_DtlObjct>? ListVist_DtlObjct
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
	public VistsData()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool AddException()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool RevertException()
	{
		return true;
	}

	static VistsData()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
