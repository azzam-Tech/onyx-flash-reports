using System.Runtime.CompilerServices;
using System.Runtime.Serialization;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

[DataContract]
public class Value<T>
{
	[CompilerGenerated]
	private T _SerializerClient;

	[DataMember]
	public T ResponceObject
	{
		[MethodImpl(MethodImplOptions.NoInlining)]
		[CompilerGenerated]
		get
		{
			return (T)null;
		}
		[MethodImpl(MethodImplOptions.NoInlining)]
		[CompilerGenerated]
		set
		{
		}
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public Value()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool ForgotSystem()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool FillSystem()
	{
		return true;
	}

	static Value()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
