using System;
using System.Runtime.CompilerServices;
using System.Security.Cryptography;
using System.Security.Cryptography.X509Certificates;
using Onyx.Containers;
using Onyx.Writers;
using Org.BouncyCastle.Crypto;
using Org.BouncyCastle.Crypto.Parameters;

namespace Onyx.Distribution.Models;

public static class Crypto
{
	[Serializable]
	[CompilerGenerated]
	private sealed class PoolDescriptorList
	{
		public static readonly PoolDescriptorList _003C_003E9;

		public static Func<object, RSA> _003C_003E9__16_0;

		public static Func<RSA, string> _003C_003E9__16_1;

		public static Func<object, RSA> _003C_003E9__16_2;

		public static Func<RSA, string> _003C_003E9__16_3;

		[MethodImpl(MethodImplOptions.NoInlining)]
		static PoolDescriptorList()
		{
			ThreadIndexerContainer.IncludeClass();
			ProducerCustomerWriter.SLV0fFIsptsZtjvFft17();
			_003C_003E9 = new PoolDescriptorList();
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		public PoolDescriptorList()
		{
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal RSA DisableClass(object obj)
		{
			return null;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal string InitClass(RSA rsa)
		{
			return null;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal RSA ReflectClass(object obj)
		{
			return null;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal string AssetClass(RSA rsa)
		{
			return null;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool DeleteExpression()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool PostExpression()
		{
			return true;
		}
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public static X509Certificate2 GetPublicKey()
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public static X509Certificate2 GetPrivateKey()
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public static string Encrypt(string textToEncrypt)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public static string Decrypt(string encryptedText)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public static byte[] stringToBytesASCII(string str)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private static byte[] UpdateClass(object P_0)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private static long CloneClass(DateTime P_0)
	{
		return 0L;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public static string DecodeFromBase64(string data)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private static void ResolveClass(object P_0, object P_1, bool P_2 = true)
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public static string ExportPublicKey(RSAParameters parameters, bool armor = true, bool base64Encode = true)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private static void RestartClass(object P_0, int P_1)
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public static string XmlToPem(string xml)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public static AsymmetricCipherKeyPair GetKeyPair(this RSA rsa)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public static RsaKeyParameters GetPublicKey(this RSA rsa)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private static string CollectClass(object P_0, object P_1)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public static string ToXmlString(RSAParameters rsaParams)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public static string PemToXml(string pem)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private static string InsertClass(object P_0, Func<object, RSA> P_1, Func<RSA, string> P_2)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool ManageObserver()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool CloneObserver()
	{
		return true;
	}

	static Crypto()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
