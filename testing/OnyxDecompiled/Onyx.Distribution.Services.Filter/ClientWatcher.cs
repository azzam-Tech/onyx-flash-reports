using System.Diagnostics;
using System.Runtime.CompilerServices;
using System.Writers;

namespace Onyx.Distribution.Services.Filter;

[CompilerGenerated]
internal sealed class ClientWatcher<_003Cphn_003Ej__TPar, _003Cmsg_003Ej__TPar>
{
	[DebuggerBrowsable(DebuggerBrowsableState.Never)]
	private readonly _003Cphn_003Ej__TPar _003Cphn_003Ei__Field;

	[DebuggerBrowsable(DebuggerBrowsableState.Never)]
	private readonly _003Cmsg_003Ej__TPar _003Cmsg_003Ei__Field;

	public _003Cphn_003Ej__TPar phn
	{
		[MethodImpl(MethodImplOptions.NoInlining)]
		get
		{
			return (_003Cphn_003Ej__TPar)null;
		}
	}

	public _003Cmsg_003Ej__TPar msg
	{
		[MethodImpl(MethodImplOptions.NoInlining)]
		get
		{
			return (_003Cmsg_003Ej__TPar)null;
		}
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[DebuggerHidden]
	public ClientWatcher(_003Cphn_003Ej__TPar phn, _003Cmsg_003Ej__TPar msg)
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[DebuggerHidden]
	public override bool Equals(object value)
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[DebuggerHidden]
	public override int GetHashCode()
	{
		return 0;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[DebuggerHidden]
	public override string ToString()
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool PopService()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool ComputeService()
	{
		return true;
	}

	static ClientWatcher()
	{
		IssuerWatcherWriter.CustomizeUtils();
	}
}
