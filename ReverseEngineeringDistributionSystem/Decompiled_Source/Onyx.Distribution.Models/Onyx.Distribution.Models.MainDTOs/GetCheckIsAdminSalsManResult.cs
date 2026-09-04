using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

public class GetCheckIsAdminSalsManResult
{
	private GeneralResult m_HelperTask;

	[CompilerGenerated]
	private string? workerTask;

	[CompilerGenerated]
	private bool valueTask;

	[CompilerGenerated]
	private string? m_InstanceTask;

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

	public string? Sub_Rep_code
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

	public bool IsAdmin
	{
		[MethodImpl(MethodImplOptions.NoInlining)]
		[CompilerGenerated]
		get
		{
			return true;
		}
		[MethodImpl(MethodImplOptions.NoInlining)]
		[CompilerGenerated]
		set
		{
		}
	}

	public string? AppendWhr
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
	public GetCheckIsAdminSalsManResult()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool CallSystem()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool PublishSystem()
	{
		return true;
	}

	static GetCheckIsAdminSalsManResult()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
