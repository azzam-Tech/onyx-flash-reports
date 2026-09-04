using System;
using System.ComponentModel;
using System.Globalization;
using System.Runtime.CompilerServices;
using Onyx.Containers;

namespace Onyx.Distribution.Models.MainDTOs;

public class RequstObjectTypeConverter<T> : TypeConverter
{
	[MethodImpl(MethodImplOptions.NoInlining)]
	public override bool CanConvertFrom(ITypeDescriptorContext context, Type sourceType)
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public override object ConvertFrom(ITypeDescriptorContext context, CultureInfo culture, object value)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public override object ConvertTo(ITypeDescriptorContext context, CultureInfo culture, object value, Type destinationType)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public RequstObjectTypeConverter()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool AwakeSystem()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool GetSystem()
	{
		return true;
	}

	static RequstObjectTypeConverter()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
