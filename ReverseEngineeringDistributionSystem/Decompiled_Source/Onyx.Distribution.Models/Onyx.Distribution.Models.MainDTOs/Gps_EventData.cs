using System.Collections.Generic;
using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

public class Gps_EventData
{
	[CompilerGenerated]
	private ConnPara? m_WriterIdentifier;

	[CompilerGenerated]
	private List<Gps_EventObjct> m_ServiceIdentifier;

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
	public List<Gps_EventObjct> ListGps_Event_Objct
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
	public Gps_EventData()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool VisitException()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool SetException()
	{
		return true;
	}

	static Gps_EventData()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
