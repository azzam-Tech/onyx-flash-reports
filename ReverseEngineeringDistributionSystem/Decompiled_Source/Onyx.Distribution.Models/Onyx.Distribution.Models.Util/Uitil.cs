using System;
using System.Collections.Generic;
using System.Data;
using System.IO;
using System.Net.Http;
using System.Net.Security;
using System.Reflection;
using System.Runtime.CompilerServices;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using Onyx.Containers;
using Onyx.Distribution.Models.MainDTOs;
using Onyx.Writers;
using Oracle.ManagedDataAccess.Client;

namespace Onyx.Distribution.Models.Util;

public static class Uitil
{
	public sealed class StringWriterWithEncoding : StringWriter
	{
		private readonly Encoding _ValueRepository;

		public override Encoding Encoding
		{
			[MethodImpl(MethodImplOptions.NoInlining)]
			get
			{
				return null;
			}
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		public StringWriterWithEncoding(StringBuilder sb)
		{
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		public StringWriterWithEncoding(Encoding encoding)
		{
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		public StringWriterWithEncoding(StringBuilder sb, Encoding encoding)
		{
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool DisableExpression()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CancelExpression()
		{
			return true;
		}

		static StringWriterWithEncoding()
		{
			ThreadIndexerContainer.IncludeClass();
		}
	}

	public sealed class StringReaderWithEncoding : StringReader
	{
		private readonly Encoding instanceRepository;

		[MethodImpl(MethodImplOptions.NoInlining)]
		public StringReaderWithEncoding(string sb)
		{
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		public StringReaderWithEncoding(string sb, Encoding encoding)
		{
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool RemoveExpression()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool InterruptExpression()
		{
			return true;
		}

		static StringReaderWithEncoding()
		{
			ThreadIndexerContainer.IncludeClass();
		}
	}

	[Serializable]
	[CompilerGenerated]
	private sealed class CustomerRulesImporter
	{
		public static readonly CustomerRulesImporter _003C_003E9;

		public static Comparison<PropertyInfo> _003C_003E9__6_0;

		public static Func<HttpRequestMessage, X509Certificate2?, X509Chain?, SslPolicyErrors, bool> _003C_003E9__11_0;

		[MethodImpl(MethodImplOptions.NoInlining)]
		static CustomerRulesImporter()
		{
			ThreadIndexerContainer.IncludeClass();
			ProducerCustomerWriter.SLV0fFIsptsZtjvFft17();
			_003C_003E9 = new CustomerRulesImporter();
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		public CustomerRulesImporter()
		{
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal int LogoutClass(PropertyInfo propertyInfo1, PropertyInfo propertyInfo2)
		{
			return 0;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal bool AddClass(HttpRequestMessage sender, X509Certificate2? cert, X509Chain? chain, SslPolicyErrors sslPolicyErrors)
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool MapExpression()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool DefineExpression()
		{
			return true;
		}
	}

	[CompilerGenerated]
	private static class ReponseConfigurationResolver<T> where T : notnull
	{
		public static CallSite<Func<CallSite, Type, object, object>> _003C_003Ep__0;

		public static CallSite<Func<CallSite, object, string>> _003C_003Ep__1;

		static ReponseConfigurationResolver()
		{
			ThreadIndexerContainer.IncludeClass();
		}
	}

	[CompilerGenerated]
	private static class MapperRepository
	{
		public static CallSite<Func<CallSite, object, IDictionary<string, object>>> _003C_003Ep__0;

		static MapperRepository()
		{
			ThreadIndexerContainer.IncludeClass();
		}
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public static string SerializeToXML<T>(T dataToSerialize)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public static T DeserializeObject<T>(string json)
	{
		return (T)null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public static T DeserializeFromXml<T>(string xml)
	{
		return (T)null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public static Result SaveToFile(string dataAsxml, string folderName = "", string serail = "")
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public static List<T> FillDataToObjectFromXml<T>(string xml)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public static DataTable BuildDataTableFromXml(Type ty, string Name, string XMLString)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private static dynamic ReadClass(object P_0)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public static FieldValueString GetFieldValueString(string TableName, string FieldName, OracleConnection con, int IsCompleteStatement = 0)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public static string getPreviousDate(int noOfDays)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public static HttpClientHandler CreateInsecureHandler()
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public static void LogWriteHistory(string data = "", dynamic model = null, Headers headers = null, string Type = "RQ")
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public static void LogHistory(string logMessage, TextWriter txtWriter)
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public static bool IsEmptyExpireDate(string s)
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public static bool IsEmptyBatchNo(string s)
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public static bool MatchExpireDate(string d, string item)
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public static bool MatchBatchNo(string d, string item)
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool CollectObserver()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool LogoutObserver()
	{
		return true;
	}

	static Uitil()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
