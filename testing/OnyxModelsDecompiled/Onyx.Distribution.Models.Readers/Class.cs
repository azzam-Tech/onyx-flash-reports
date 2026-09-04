using System.Diagnostics;
using System.Runtime.CompilerServices;
using Onyx.Containers;

namespace Onyx.Distribution.Models.Readers;

[CompilerGenerated]
internal sealed class Class<_003CMessage_003Ej__TPar, _003CErrorNo_003Ej__TPar>
{
	[DebuggerBrowsable(DebuggerBrowsableState.Never)]
	private readonly _003CMessage_003Ej__TPar _003CMessage_003Ei__Field;

	[DebuggerBrowsable(DebuggerBrowsableState.Never)]
	private readonly _003CErrorNo_003Ej__TPar _003CErrorNo_003Ei__Field;

	public _003CMessage_003Ej__TPar Message
	{
		[MethodImpl(MethodImplOptions.NoInlining)]
		get
		{
			return (_003CMessage_003Ej__TPar)null;
		}
	}

	public _003CErrorNo_003Ej__TPar ErrorNo
	{
		[MethodImpl(MethodImplOptions.NoInlining)]
		get
		{
			return (_003CErrorNo_003Ej__TPar)null;
		}
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[DebuggerHidden]
	public Class(_003CMessage_003Ej__TPar Message, _003CErrorNo_003Ej__TPar ErrorNo)
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
	internal static bool AwakeObserver()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool GetObserver()
	{
		return true;
	}

	static Class()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
