using System.Diagnostics;
using System.Runtime.CompilerServices;
using Onyx.Distribution.APIs.Filter;

namespace System.Consumers;

[CompilerGenerated]
internal sealed class RepositoryManagerConsumer<_003CtokenType_003Ej__TPar, _003Ctoken_003Ej__TPar, _003Cexpiration_003Ej__TPar>
{
	[DebuggerBrowsable(DebuggerBrowsableState.Never)]
	private readonly _003CtokenType_003Ej__TPar _003CtokenType_003Ei__Field;

	[DebuggerBrowsable(DebuggerBrowsableState.Never)]
	private readonly _003Ctoken_003Ej__TPar _003Ctoken_003Ei__Field;

	[DebuggerBrowsable(DebuggerBrowsableState.Never)]
	private readonly _003Cexpiration_003Ej__TPar _003Cexpiration_003Ei__Field;

	public _003CtokenType_003Ej__TPar tokenType
	{
		[MethodImpl(MethodImplOptions.NoInlining)]
		get
		{
			return (_003CtokenType_003Ej__TPar)null;
		}
	}

	public _003Ctoken_003Ej__TPar token
	{
		[MethodImpl(MethodImplOptions.NoInlining)]
		get
		{
			return (_003Ctoken_003Ej__TPar)null;
		}
	}

	public _003Cexpiration_003Ej__TPar expiration
	{
		[MethodImpl(MethodImplOptions.NoInlining)]
		get
		{
			return (_003Cexpiration_003Ej__TPar)null;
		}
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[DebuggerHidden]
	public RepositoryManagerConsumer(_003CtokenType_003Ej__TPar tokenType, _003Ctoken_003Ej__TPar token, _003Cexpiration_003Ej__TPar expiration)
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
	internal static bool FindCandidate()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool PatchCandidate()
	{
		return true;
	}

	static RepositoryManagerConsumer()
	{
		Decorator.EnablePage();
	}
}
