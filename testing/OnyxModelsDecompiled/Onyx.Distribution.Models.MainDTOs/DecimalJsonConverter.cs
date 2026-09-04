using System;
using System.Runtime.CompilerServices;
using Newtonsoft.Json;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

public class DecimalJsonConverter : JsonConverter<decimal>
{
	[MethodImpl(MethodImplOptions.NoInlining)]
	public override decimal ReadJson(JsonReader reader, Type objectType, decimal existingValue, bool hasExistingValue, JsonSerializer serializer)
	{
		return (decimal)(object)null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public override void WriteJson(JsonWriter writer, decimal value, JsonSerializer serializer)
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public DecimalJsonConverter()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool InitObserver()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool RestartObserver()
	{
		return true;
	}

	static DecimalJsonConverter()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
