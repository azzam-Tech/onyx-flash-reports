using System.Runtime.CompilerServices;
using Onyx.Containers;

namespace DSTModels;

public class QST_DTL
{
	[CompilerGenerated]
	private string? _Registry;

	[CompilerGenerated]
	private string? _Interpreter;

	public string? I_CODE
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

	public string? QUESTNR_NO
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
	public QST_DTL()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool InsertObserver()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool ViewObserver()
	{
		return true;
	}

	static QST_DTL()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
