using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.DTOs;

[DataContract]
public class SalesManAdditionalData
{
	[CompilerGenerated]
	private string m_SerializerSchema;

	[CompilerGenerated]
	private string m_TemplateSchema;

	[CompilerGenerated]
	private string _RecordSchema;

	[CompilerGenerated]
	private string _StateSchema;

	[CompilerGenerated]
	private string _MapSchema;

	[CompilerGenerated]
	private string _RequestSchema;

	[DataMember]
	public string AR_HIDE_QTY_IN_TRNS
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
	public string SHOW_AVL_QTY_IN_REQ
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
	public string SHW_ACTV_NO_VCHR_APP
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
	public string SHW_PJ_NO_VCHR_APP
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
	public string SEND_GPS_PRD
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
	public string READ_GPS_DSTNC
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
	public SalesManAdditionalData()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool ReadAttribute()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool RunAttribute()
	{
		return true;
	}

	static SalesManAdditionalData()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
