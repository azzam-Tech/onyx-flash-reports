using System.Diagnostics;
using System.IO;
using System.Reflection;
using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;
using System.Security.Cryptography;
using System.Text;
using Onyx.Distribution.Services.Filter;

namespace System.Writers;

internal class IssuerWatcherWriter
{
	internal class ConfigurationFilterContainer : Attribute
	{
		internal class ComposerPoolCollection<T>
		{
			[MethodImpl(MethodImplOptions.NoInlining)]
			public ComposerPoolCollection()
			{
			}

			[MethodImpl(MethodImplOptions.NoInlining)]
			internal static bool WriteAdapter()
			{
				return true;
			}

			[MethodImpl(MethodImplOptions.NoInlining)]
			internal static bool OrderAdapter()
			{
				return true;
			}

			static ComposerPoolCollection()
			{
				IssuerWatcherWriter.CustomizeUtils();
			}
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		[ConfigurationFilterContainer(typeof(ComposerPoolCollection<object>[]))]
		public ConfigurationFilterContainer(object P_0)
		{
		}

		static ConfigurationFilterContainer()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[Flags]
	private enum LocalPendingChangeFlags
	{

	}

	private static object producerWatcher;

	private static nint m_AccountWatcher;

	private static long m_RepositoryWatcher;

	private static bool broadcasterWatcher;

	private static object proxyWatcher;

	private static object _WrapperWatcher;

	private static int _ModelWatcher;

	private static bool m_ObserverWatcher;

	private static object _ContainerWatcher;

	private static object facadeWatcher;

	private static object dicWatcher;

	private static int _StubWatcher;

	private static object valueWatcher;

	private static bool m_BaseWatcher;

	private static nint printerWatcher;

	[MethodImpl(MethodImplOptions.NoInlining)]
	static IssuerWatcherWriter()
	{
		producerWatcher = new uint[64]
		{
			3614090360u, 3905402710u, 606105819u, 3250441966u, 4118548399u, 1200080426u, 2821735955u, 4249261313u, 1770035416u, 2336552879u,
			4294925233u, 2304563134u, 1804603682u, 4254626195u, 2792965006u, 1236535329u, 4129170786u, 3225465664u, 643717713u, 3921069994u,
			3593408605u, 38016083u, 3634488961u, 3889429448u, 568446438u, 3275163606u, 4107603335u, 1163531501u, 2850285829u, 4243563512u,
			1735328473u, 2368359562u, 4294588738u, 2272392833u, 1839030562u, 4259657740u, 2763975236u, 1272893353u, 4139469664u, 3200236656u,
			681279174u, 3936430074u, 3572445317u, 76029189u, 3654602809u, 3873151461u, 530742520u, 3299628645u, 4096336452u, 1126891415u,
			2878612391u, 4237533241u, 1700485571u, 2399980690u, 4293915773u, 2240044497u, 1873313359u, 4264355552u, 2734768916u, 1309151649u,
			4149444226u, 3174756917u, 718787259u, 3951481745u
		};
		m_ObserverWatcher = false;
		m_BaseWatcher = false;
		dicWatcher = new byte[0];
		valueWatcher = new byte[0];
		facadeWatcher = new byte[0];
		_WrapperWatcher = new byte[0];
		printerWatcher = IntPtr.Zero;
		m_AccountWatcher = IntPtr.Zero;
		proxyWatcher = new string[0];
		_ContainerWatcher = new int[0];
		_StubWatcher = 1;
		m_RepositoryWatcher = 0L;
		_ModelWatcher = 0;
		broadcasterWatcher = false;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private void leHifFIJCLsZtKEFfM1i()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static byte[] NewUtils(object P_0)
	{
		uint[] array = new uint[16];
		uint num = (uint)((448 - ((Array)P_0).Length * 8 % 512 + 512) % 512);
		if (num == 0)
		{
			num = 512u;
		}
		uint num2 = (uint)(((Array)P_0).Length + num / 8 + 8);
		ulong num3 = (ulong)((Array)P_0).Length * 8uL;
		byte[] array2 = new byte[num2];
		for (int i = 0; i < ((Array)P_0).Length; i++)
		{
			array2[i] = ((byte[])P_0)[i];
		}
		array2[((Array)P_0).Length] |= 128;
		for (int num4 = 8; num4 > 0; num4--)
		{
			array2[num2 - num4] = (byte)((num3 >> (8 - num4) * 8) & 0xFF);
		}
		uint num5 = (uint)(array2.Length * 8) / 32u;
		uint num6 = 1732584193u;
		uint num7 = 4023233417u;
		uint num8 = 2562383102u;
		uint num9 = 271733878u;
		for (uint num10 = 0u; num10 < num5 / 16; num10++)
		{
			uint num11 = num10 << 6;
			for (uint num12 = 0u; num12 < 61; num12 += 4)
			{
				array[num12 >> 2] = (uint)((array2[num11 + (num12 + 3)] << 24) | (array2[num11 + (num12 + 2)] << 16) | (array2[num11 + (num12 + 1)] << 8) | array2[num11 + num12]);
			}
			uint num13 = num6;
			uint num14 = num7;
			uint num15 = num8;
			uint num16 = num9;
			InstantiateUtils(ref num6, num7, num8, num9, 0u, 7, 1u, array);
			InstantiateUtils(ref num9, num6, num7, num8, 1u, 12, 2u, array);
			InstantiateUtils(ref num8, num9, num6, num7, 2u, 17, 3u, array);
			InstantiateUtils(ref num7, num8, num9, num6, 3u, 22, 4u, array);
			InstantiateUtils(ref num6, num7, num8, num9, 4u, 7, 5u, array);
			InstantiateUtils(ref num9, num6, num7, num8, 5u, 12, 6u, array);
			InstantiateUtils(ref num8, num9, num6, num7, 6u, 17, 7u, array);
			InstantiateUtils(ref num7, num8, num9, num6, 7u, 22, 8u, array);
			InstantiateUtils(ref num6, num7, num8, num9, 8u, 7, 9u, array);
			InstantiateUtils(ref num9, num6, num7, num8, 9u, 12, 10u, array);
			InstantiateUtils(ref num8, num9, num6, num7, 10u, 17, 11u, array);
			InstantiateUtils(ref num7, num8, num9, num6, 11u, 22, 12u, array);
			InstantiateUtils(ref num6, num7, num8, num9, 12u, 7, 13u, array);
			InstantiateUtils(ref num9, num6, num7, num8, 13u, 12, 14u, array);
			InstantiateUtils(ref num8, num9, num6, num7, 14u, 17, 15u, array);
			InstantiateUtils(ref num7, num8, num9, num6, 15u, 22, 16u, array);
			ViewUtils(ref num6, num7, num8, num9, 1u, 5, 17u, array);
			ViewUtils(ref num9, num6, num7, num8, 6u, 9, 18u, array);
			ViewUtils(ref num8, num9, num6, num7, 11u, 14, 19u, array);
			ViewUtils(ref num7, num8, num9, num6, 0u, 20, 20u, array);
			ViewUtils(ref num6, num7, num8, num9, 5u, 5, 21u, array);
			ViewUtils(ref num9, num6, num7, num8, 10u, 9, 22u, array);
			ViewUtils(ref num8, num9, num6, num7, 15u, 14, 23u, array);
			ViewUtils(ref num7, num8, num9, num6, 4u, 20, 24u, array);
			ViewUtils(ref num6, num7, num8, num9, 9u, 5, 25u, array);
			ViewUtils(ref num9, num6, num7, num8, 14u, 9, 26u, array);
			ViewUtils(ref num8, num9, num6, num7, 3u, 14, 27u, array);
			ViewUtils(ref num7, num8, num9, num6, 8u, 20, 28u, array);
			ViewUtils(ref num6, num7, num8, num9, 13u, 5, 29u, array);
			ViewUtils(ref num9, num6, num7, num8, 2u, 9, 30u, array);
			ViewUtils(ref num8, num9, num6, num7, 7u, 14, 31u, array);
			ViewUtils(ref num7, num8, num9, num6, 12u, 20, 32u, array);
			PublishUtils(ref num6, num7, num8, num9, 5u, 4, 33u, array);
			PublishUtils(ref num9, num6, num7, num8, 8u, 11, 34u, array);
			PublishUtils(ref num8, num9, num6, num7, 11u, 16, 35u, array);
			PublishUtils(ref num7, num8, num9, num6, 14u, 23, 36u, array);
			PublishUtils(ref num6, num7, num8, num9, 1u, 4, 37u, array);
			PublishUtils(ref num9, num6, num7, num8, 4u, 11, 38u, array);
			PublishUtils(ref num8, num9, num6, num7, 7u, 16, 39u, array);
			PublishUtils(ref num7, num8, num9, num6, 10u, 23, 40u, array);
			PublishUtils(ref num6, num7, num8, num9, 13u, 4, 41u, array);
			PublishUtils(ref num9, num6, num7, num8, 0u, 11, 42u, array);
			PublishUtils(ref num8, num9, num6, num7, 3u, 16, 43u, array);
			PublishUtils(ref num7, num8, num9, num6, 6u, 23, 44u, array);
			PublishUtils(ref num6, num7, num8, num9, 9u, 4, 45u, array);
			PublishUtils(ref num9, num6, num7, num8, 12u, 11, 46u, array);
			PublishUtils(ref num8, num9, num6, num7, 15u, 16, 47u, array);
			PublishUtils(ref num7, num8, num9, num6, 2u, 23, 48u, array);
			ComputeUtils(ref num6, num7, num8, num9, 0u, 6, 49u, array);
			ComputeUtils(ref num9, num6, num7, num8, 7u, 10, 50u, array);
			ComputeUtils(ref num8, num9, num6, num7, 14u, 15, 51u, array);
			ComputeUtils(ref num7, num8, num9, num6, 5u, 21, 52u, array);
			ComputeUtils(ref num6, num7, num8, num9, 12u, 6, 53u, array);
			ComputeUtils(ref num9, num6, num7, num8, 3u, 10, 54u, array);
			ComputeUtils(ref num8, num9, num6, num7, 10u, 15, 55u, array);
			ComputeUtils(ref num7, num8, num9, num6, 1u, 21, 56u, array);
			ComputeUtils(ref num6, num7, num8, num9, 8u, 6, 57u, array);
			ComputeUtils(ref num9, num6, num7, num8, 15u, 10, 58u, array);
			ComputeUtils(ref num8, num9, num6, num7, 6u, 15, 59u, array);
			ComputeUtils(ref num7, num8, num9, num6, 13u, 21, 60u, array);
			ComputeUtils(ref num6, num7, num8, num9, 4u, 6, 61u, array);
			ComputeUtils(ref num9, num6, num7, num8, 11u, 10, 62u, array);
			ComputeUtils(ref num8, num9, num6, num7, 2u, 15, 63u, array);
			ComputeUtils(ref num7, num8, num9, num6, 9u, 21, 64u, array);
			num6 += num13;
			num7 += num14;
			num8 += num15;
			num9 += num16;
		}
		byte[] array3 = new byte[16];
		Array.Copy(BitConverter.GetBytes(num6), 0, array3, 0, 4);
		Array.Copy(BitConverter.GetBytes(num7), 0, array3, 4, 4);
		Array.Copy(BitConverter.GetBytes(num8), 0, array3, 8, 4);
		Array.Copy(BitConverter.GetBytes(num9), 0, array3, 12, 4);
		return array3;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private static void InstantiateUtils(ref uint P_0, uint P_1, uint P_2, uint P_3, uint P_4, ushort P_5, uint P_6, object P_7)
	{
		P_0 = P_1 + IncludeUtils(P_0 + ((P_1 & P_2) | (~P_1 & P_3)) + ((uint[])P_7)[P_4] + ((uint[])producerWatcher)[P_6 - 1], P_5);
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private static void ViewUtils(ref uint P_0, uint P_1, uint P_2, uint P_3, uint P_4, ushort P_5, uint P_6, object P_7)
	{
		P_0 = P_1 + IncludeUtils(P_0 + ((P_1 & P_3) | (P_2 & ~P_3)) + ((uint[])P_7)[P_4] + ((uint[])producerWatcher)[P_6 - 1], P_5);
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private static void PublishUtils(ref uint P_0, uint P_1, uint P_2, uint P_3, uint P_4, ushort P_5, uint P_6, object P_7)
	{
		P_0 = P_1 + IncludeUtils(P_0 + (P_1 ^ P_2 ^ P_3) + ((uint[])P_7)[P_4] + ((uint[])producerWatcher)[P_6 - 1], P_5);
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private static void ComputeUtils(ref uint P_0, uint P_1, uint P_2, uint P_3, uint P_4, ushort P_5, uint P_6, object P_7)
	{
		P_0 = P_1 + IncludeUtils(P_0 + (P_2 ^ (P_1 | ~P_3)) + ((uint[])P_7)[P_4] + ((uint[])producerWatcher)[P_6 - 1], P_5);
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private static uint IncludeUtils(uint P_0, ushort P_1)
	{
		return (P_0 >> 32 - P_1) | (P_0 << (int)P_1);
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool PopUtils()
	{
		if (!m_ObserverWatcher)
		{
			CollectUtils();
			m_ObserverWatcher = true;
		}
		return m_BaseWatcher;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static void CollectUtils()
	{
		try
		{
			new MD5CryptoServiceProvider();
		}
		catch
		{
			m_BaseWatcher = true;
			return;
		}
		try
		{
			m_BaseWatcher = (bool)Type.GetTypeFromHandle(QueueDefinitionFilter.e53w34m968awCm9P85taUZe(16777629)).Assembly.GetType("System.Security.Cryptography.CryptoConfig", throwOnError: false).GetMethod("get_AllowOnlyFipsAlgorithms", BindingFlags.Static | BindingFlags.Public).Invoke(null, new object[0]);
		}
		catch
		{
		}
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static SymmetricAlgorithm CompareUtils()
	{
		SymmetricAlgorithm symmetricAlgorithm = null;
		if (PopUtils())
		{
			try
			{
				return new AesCryptoServiceProvider();
			}
			catch
			{
				return new RijndaelManaged();
			}
		}
		return new RijndaelManaged();
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static byte[] RegisterUtils(object P_0)
	{
		if (!PopUtils())
		{
			return new MD5CryptoServiceProvider().ComputeHash((byte[])P_0);
		}
		return NewUtils(P_0);
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	static bool SetupUtils(int P_0)
	{
		int num = 5;
		int num4 = default(int);
		bool result = default(bool);
		while (true)
		{
			int num2 = num;
			while (true)
			{
				int num3 = num2;
				while (true)
				{
					switch (num3)
					{
					case 6:
						dicWatcher = DestroyUtils(CalcUtils(typeof(IssuerWatcherWriter).Assembly).ToString());
						num2 = 3;
						break;
					case 5:
						if (((Array)valueWatcher).Length == 0)
						{
							_ = 0;
							if (WriteService())
							{
								num3 = 4;
								continue;
							}
							num2 = 0;
							break;
						}
						goto case 0;
					case 0:
					case 2:
						if (((Array)dicWatcher).Length != 0)
						{
							goto end_IL_007c;
						}
						goto case 6;
					default:
						num3 = 6;
						continue;
					case 1:
					case 4:
					{
						BinaryReader binaryReader = new BinaryReader(typeof(IssuerWatcherWriter).Assembly.GetManifestResourceStream("f43b3953-983c-48d5-ae3e-23ff3ea0e14a"));
						binaryReader.BaseStream.Position = 0L;
						byte[] array = binaryReader.ReadBytes((int)binaryReader.BaseStream.Length);
						byte[] array2 = new byte[32];
						array2[0] = 99;
						array2[0] = 62;
						array2[0] = 192;
						array2[1] = 28;
						array2[1] = 133;
						int num7 = 119 + 124;
						array2[1] = (byte)num7;
						num7 = 126 + 17;
						array2[1] = (byte)num7;
						int num8 = 112 + 101;
						array2[2] = (byte)num8;
						array2[2] = 237;
						num8 = 221 - 73;
						array2[2] = (byte)num8;
						array2[2] = 137;
						num7 = 156 - 58;
						array2[2] = (byte)num7;
						num7 = 119 + 2;
						array2[3] = (byte)num7;
						array2[3] = 97;
						num7 = 133 - 44;
						array2[3] = (byte)num7;
						array2[3] = 105;
						num7 = 192 - 64;
						array2[3] = (byte)num7;
						num7 = 104 - 55;
						array2[3] = (byte)num7;
						num8 = 33 + 61;
						array2[4] = (byte)num8;
						num7 = 7 + 3;
						array2[4] = (byte)num7;
						num8 = 74 + 96;
						array2[4] = (byte)num8;
						array2[5] = 144;
						array2[5] = 140;
						array2[5] = 211;
						array2[5] = 94;
						array2[6] = 94;
						num7 = 19 + 104;
						array2[6] = (byte)num7;
						array2[6] = 93;
						num8 = 15 + 44;
						array2[6] = (byte)num8;
						num8 = 10 + 117;
						array2[6] = (byte)num8;
						num7 = 74 + 20;
						array2[7] = (byte)num7;
						num7 = 51 + 55;
						array2[7] = (byte)num7;
						num7 = 103 + 90;
						array2[7] = (byte)num7;
						array2[8] = 147;
						num8 = 103 + 15;
						array2[8] = (byte)num8;
						num8 = 41 + 103;
						array2[8] = (byte)num8;
						array2[8] = 166;
						array2[8] = 111;
						num8 = 74 - 19;
						array2[8] = (byte)num8;
						num8 = 207 - 69;
						array2[9] = (byte)num8;
						num7 = 49 + 124;
						array2[9] = (byte)num7;
						array2[9] = 84;
						num8 = 118 + 23;
						array2[10] = (byte)num8;
						array2[10] = 103;
						array2[10] = 113;
						array2[10] = 3;
						array2[11] = 98;
						num8 = 129 - 43;
						array2[11] = (byte)num8;
						array2[11] = 92;
						num8 = 230 - 76;
						array2[12] = (byte)num8;
						num8 = 40 + 70;
						array2[12] = (byte)num8;
						num7 = 198 - 66;
						array2[12] = (byte)num7;
						num7 = 125 + 34;
						array2[12] = (byte)num7;
						array2[13] = 98;
						array2[13] = 121;
						array2[13] = 142;
						num7 = 67 + 88;
						array2[13] = (byte)num7;
						array2[13] = 90;
						array2[13] = 54;
						array2[14] = 146;
						array2[14] = 136;
						num8 = 241 - 80;
						array2[14] = (byte)num8;
						num8 = 123 + 124;
						array2[14] = (byte)num8;
						array2[14] = 0;
						array2[15] = 107;
						array2[15] = 167;
						num7 = 210 - 70;
						array2[15] = (byte)num7;
						num8 = 119 + 42;
						array2[15] = (byte)num8;
						array2[15] = 228;
						num8 = 56 + 100;
						array2[16] = (byte)num8;
						array2[16] = 146;
						num7 = 149 - 49;
						array2[16] = (byte)num7;
						num8 = 114 + 58;
						array2[16] = (byte)num8;
						num8 = 171 - 57;
						array2[16] = (byte)num8;
						num7 = 141 - 66;
						array2[16] = (byte)num7;
						num8 = 137 - 45;
						array2[17] = (byte)num8;
						array2[17] = 173;
						array2[17] = 129;
						array2[17] = 117;
						num7 = 206 - 68;
						array2[17] = (byte)num7;
						array2[17] = 135;
						array2[18] = 117;
						num7 = 198 - 66;
						array2[18] = (byte)num7;
						num8 = 61 + 106;
						array2[18] = (byte)num8;
						array2[18] = 91;
						array2[18] = 177;
						array2[19] = 84;
						num8 = 156 - 52;
						array2[19] = (byte)num8;
						array2[19] = 164;
						array2[19] = 111;
						array2[19] = 227;
						array2[20] = 88;
						array2[20] = 123;
						array2[20] = 160;
						num8 = 204 - 68;
						array2[20] = (byte)num8;
						num8 = 157 - 52;
						array2[20] = (byte)num8;
						array2[20] = 8;
						array2[21] = 149;
						num7 = 84 + 65;
						array2[21] = (byte)num7;
						num8 = 39 - 27;
						array2[21] = (byte)num8;
						num8 = 131 - 43;
						array2[22] = (byte)num8;
						array2[22] = 129;
						array2[22] = 132;
						num8 = 11 + 56;
						array2[22] = (byte)num8;
						array2[22] = 90;
						num7 = 53 - 43;
						array2[22] = (byte)num7;
						num7 = 161 - 53;
						array2[23] = (byte)num7;
						array2[23] = 142;
						num8 = 102 + 79;
						array2[23] = (byte)num8;
						num7 = 142 - 47;
						array2[23] = (byte)num7;
						num7 = 118 + 60;
						array2[23] = (byte)num7;
						num8 = 122 + 108;
						array2[23] = (byte)num8;
						num8 = 243 - 81;
						array2[24] = (byte)num8;
						array2[24] = 92;
						num7 = 122 + 76;
						array2[24] = (byte)num7;
						array2[24] = 75;
						num7 = 173 - 57;
						array2[24] = (byte)num7;
						array2[24] = 228;
						array2[25] = 67;
						array2[25] = 100;
						num7 = 218 - 72;
						array2[25] = (byte)num7;
						num7 = 226 - 75;
						array2[25] = (byte)num7;
						array2[25] = 120;
						array2[25] = 133;
						num7 = 144 - 48;
						array2[26] = (byte)num7;
						num8 = 100 + 64;
						array2[26] = (byte)num8;
						num8 = 164 - 54;
						array2[26] = (byte)num8;
						array2[26] = 135;
						num8 = 61 + 46;
						array2[26] = (byte)num8;
						array2[26] = 23;
						array2[27] = 115;
						array2[27] = 88;
						array2[27] = 72;
						num7 = 88 - 17;
						array2[27] = (byte)num7;
						array2[28] = 176;
						array2[28] = 115;
						num8 = 112 + 123;
						array2[28] = (byte)num8;
						array2[28] = 98;
						array2[28] = 164;
						num7 = 176 + 36;
						array2[28] = (byte)num7;
						num8 = 192 - 64;
						array2[29] = (byte)num8;
						array2[29] = 162;
						array2[29] = 96;
						array2[30] = 112;
						array2[30] = 143;
						num7 = 159 - 53;
						array2[30] = (byte)num7;
						num7 = 37 + 108;
						array2[30] = (byte)num7;
						num7 = 133 - 53;
						array2[30] = (byte)num7;
						num7 = 242 - 80;
						array2[31] = (byte)num7;
						num7 = 5 + 5;
						array2[31] = (byte)num7;
						array2[31] = 132;
						array2[31] = 178;
						array2[31] = 83;
						byte[] rgbKey = array2;
						byte[] array3 = new byte[16];
						int num9 = 207 - 69;
						array3[0] = (byte)num9;
						array3[0] = 146;
						int num10 = 26 + 113;
						array3[0] = (byte)num10;
						num9 = 241 + 12;
						array3[0] = (byte)num9;
						array3[1] = 101;
						num10 = 231 - 77;
						array3[1] = (byte)num10;
						num9 = 254 - 84;
						array3[1] = (byte)num9;
						array3[1] = 96;
						array3[1] = 213;
						num9 = 146 - 114;
						array3[1] = (byte)num9;
						num9 = 17 + 92;
						array3[2] = (byte)num9;
						array3[2] = 137;
						num9 = 58 + 123;
						array3[2] = (byte)num9;
						num9 = 128 - 42;
						array3[2] = (byte)num9;
						num9 = 145 - 48;
						array3[2] = (byte)num9;
						num9 = 153 + 65;
						array3[2] = (byte)num9;
						array3[3] = 55;
						array3[3] = 133;
						array3[3] = 122;
						array3[3] = 226;
						num10 = 61 + 116;
						array3[4] = (byte)num10;
						array3[4] = 10;
						num9 = 160 - 70;
						array3[4] = (byte)num9;
						num9 = 157 - 52;
						array3[5] = (byte)num9;
						num10 = 81 + 91;
						array3[5] = (byte)num10;
						num9 = 139 - 118;
						array3[5] = (byte)num9;
						array3[6] = 63;
						array3[6] = 134;
						array3[6] = 149;
						num10 = 81 - 57;
						array3[6] = (byte)num10;
						array3[7] = 59;
						num10 = 117 + 75;
						array3[7] = (byte)num10;
						array3[7] = 5;
						array3[8] = 168;
						array3[8] = 205;
						num10 = 134 + 91;
						array3[8] = (byte)num10;
						array3[9] = 155;
						array3[9] = 120;
						num10 = 232 - 77;
						array3[9] = (byte)num10;
						array3[9] = 166;
						num10 = 14 + 97;
						array3[9] = (byte)num10;
						num10 = 168 + 19;
						array3[9] = (byte)num10;
						num10 = 78 + 66;
						array3[10] = (byte)num10;
						array3[10] = 170;
						array3[10] = 111;
						num9 = 170 + 23;
						array3[10] = (byte)num9;
						num9 = 15 + 88;
						array3[11] = (byte)num9;
						array3[11] = 90;
						array3[11] = 126;
						array3[11] = 106;
						array3[11] = 86;
						array3[11] = 176;
						num9 = 172 - 57;
						array3[12] = (byte)num9;
						array3[12] = 132;
						array3[12] = 156;
						num10 = 217 - 72;
						array3[12] = (byte)num10;
						array3[12] = 163;
						num10 = 131 - 109;
						array3[12] = (byte)num10;
						array3[13] = 155;
						array3[13] = 140;
						array3[13] = 167;
						num10 = 171 - 57;
						array3[13] = (byte)num10;
						num9 = 241 - 80;
						array3[13] = (byte)num9;
						num9 = 124 + 35;
						array3[13] = (byte)num9;
						num9 = 154 - 51;
						array3[14] = (byte)num9;
						num9 = 124 + 44;
						array3[14] = (byte)num9;
						num9 = 90 + 17;
						array3[14] = (byte)num9;
						array3[14] = 40;
						num10 = 238 - 79;
						array3[15] = (byte)num10;
						num9 = 210 - 70;
						array3[15] = (byte)num9;
						num10 = 249 - 83;
						array3[15] = (byte)num10;
						array3[15] = 177;
						byte[] array4 = array3;
						byte[] publicKeyToken = typeof(IssuerWatcherWriter).Assembly.GetName().GetPublicKeyToken();
						if (publicKeyToken != null && publicKeyToken.Length != 0)
						{
							array4[1] = publicKeyToken[0];
							array4[3] = publicKeyToken[1];
							array4[5] = publicKeyToken[2];
							array4[7] = publicKeyToken[3];
							array4[9] = publicKeyToken[4];
							array4[11] = publicKeyToken[5];
							array4[13] = publicKeyToken[6];
							array4[15] = publicKeyToken[7];
						}
						SymmetricAlgorithm symmetricAlgorithm = CompareUtils();
						symmetricAlgorithm.Mode = CipherMode.CBC;
						ICryptoTransform transform = symmetricAlgorithm.CreateDecryptor(rgbKey, array4);
						MemoryStream memoryStream = new MemoryStream();
						CryptoStream cryptoStream = new CryptoStream(memoryStream, transform, CryptoStreamMode.Write);
						cryptoStream.Write(array, 0, array.Length);
						cryptoStream.FlushFinalBlock();
						valueWatcher = memoryStream.ToArray();
						memoryStream.Close();
						cryptoStream.Close();
						binaryReader.Close();
						goto case 0;
					}
					case 3:
						goto end_IL_007c;
					case 7:
						try
						{
							num4 = BitConverter.ToInt32(new byte[4]
							{
								((byte[])valueWatcher)[P_0],
								((byte[])valueWatcher)[P_0 + 1],
								((byte[])valueWatcher)[P_0 + 2],
								((byte[])valueWatcher)[P_0 + 3]
							}, 0);
						}
						catch
						{
						}
						try
						{
							if (((byte[])dicWatcher)[num4] == 128)
							{
								StartService();
								int num5;
								if (WriteService())
								{
									num5 = 2;
								}
								else
								{
									int num6 = 3;
									num5 = num6;
								}
								switch (num5)
								{
								case 0:
								case 2:
									return true;
								default:
									return result;
								}
							}
						}
						catch
						{
						}
						return false;
					}
					break;
				}
				continue;
				end_IL_007c:
				break;
			}
			num4 = 0;
			num = 7;
		}
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	static string ReadUtils(int P_0)
	{
		int num = 295;
		byte[] array5 = default(byte[]);
		int num6 = default(int);
		byte[] array4 = default(byte[]);
		int num7 = default(int);
		byte[] array2 = default(byte[]);
		byte[] publicKeyToken = default(byte[]);
		int num10 = default(int);
		int num35 = default(int);
		int num28 = default(int);
		int num25 = default(int);
		byte[] array7 = default(byte[]);
		uint num26 = default(uint);
		uint num27 = default(uint);
		BinaryReader binaryReader = default(BinaryReader);
		uint num37 = default(uint);
		int num38 = default(int);
		int num9 = default(int);
		int num36 = default(int);
		byte[] array = default(byte[]);
		uint num39 = default(uint);
		byte[] array6 = default(byte[]);
		int num4 = default(int);
		int num8 = default(int);
		uint num31 = default(uint);
		MemoryStream memoryStream = default(MemoryStream);
		ICryptoTransform transform = default(ICryptoTransform);
		int num33 = default(int);
		uint num12 = default(uint);
		uint num30 = default(uint);
		int num34 = default(int);
		uint num29 = default(uint);
		int num32 = default(int);
		while (true)
		{
			int num2;
			int num3;
			switch (num)
			{
			case 243:
				array5[8] = (byte)num6;
				num2 = 67;
				goto IL_0249;
			case 239:
				array4[0] = (byte)num7;
				num3 = 214;
				goto IL_024d;
			case 240:
				array2[9] = publicKeyToken[4];
				num3 = 409;
				goto IL_024d;
			case 332:
				array5 = new byte[16];
				num3 = 66;
				if (false)
				{
					goto case 241;
				}
				goto IL_024d;
			case 241:
				array5[6] = (byte)num6;
				num3 = 185;
				if (1 == 0)
				{
					goto case 58;
				}
				goto IL_024d;
			case 58:
				num7 = 212 - 70;
				num2 = 389;
				goto IL_0249;
			case 113:
				publicKeyToken = typeof(IssuerWatcherWriter).Assembly.GetName().GetPublicKeyToken();
				num3 = 98;
				goto IL_024d;
			case 213:
				array5[10] = 98;
				num3 = 341;
				if (1 == 0)
				{
					goto case 62;
				}
				goto IL_024d;
			case 62:
				array5[13] = 56;
				num3 = 43;
				if (ConnectService())
				{
					goto case 168;
				}
				goto IL_024d;
			case 168:
				array5[2] = 162;
				num3 = 379;
				if (!ValidateService())
				{
					goto case 57;
				}
				goto IL_024d;
			case 57:
				array4[30] = 110;
				num2 = 91;
				goto IL_0249;
			case 372:
				array4[5] = 197;
				num3 = 306;
				if (!ConnectService())
				{
					goto IL_024d;
				}
				goto case 366;
			case 379:
				array5[2] = 205;
				num2 = 319;
				goto IL_0249;
			case 133:
				num10 = 137 - 105;
				num3 = 53;
				goto IL_024d;
			case 353:
				array5[7] = 107;
				num2 = 0;
				goto IL_0249;
			case 53:
				array5[1] = (byte)num10;
				num3 = 99;
				if (!ConnectService())
				{
					goto IL_024d;
				}
				goto case 362;
			case 264:
				array5[6] = (byte)num10;
				num2 = 342;
				goto IL_0249;
			case 84:
				array4[29] = (byte)num7;
				goto case 236;
			default:
				num3 = 236;
				goto IL_024d;
			case 24:
				num7 = 208 - 69;
				num = 410;
				break;
			case 351:
				num6 = 148 - 101;
				num3 = 358;
				goto IL_024d;
			case 149:
			case 382:
				if (num35 >= num28)
				{
					num = 378;
					break;
				}
				if (num35 > 0)
				{
					num = 404;
					break;
				}
				goto case 126;
			case 158:
				num25 = array7.Length / 4;
				num3 = 338;
				if (ValidateService())
				{
					goto IL_024d;
				}
				goto case 390;
			case 174:
				num26++;
				num3 = 108;
				goto IL_024d;
			case 11:
				array5[11] = 104;
				num3 = 47;
				goto IL_024d;
			case 126:
				num27 |= array7[^(1 + num35)];
				num = 170;
				break;
			case 160:
				num7 = 224 - 74;
				num = 94;
				break;
			case 105:
				num6 = 173 - 57;
				num = 396;
				break;
			case 374:
				array4[20] = 122;
				num2 = 151;
				goto IL_0249;
			case 91:
				array4[30] = 166;
				num3 = 120;
				if (!ConnectService())
				{
					goto IL_024d;
				}
				goto case 174;
			case 90:
				array4[21] = 122;
				num3 = 10;
				if (true)
				{
					goto IL_024d;
				}
				goto case 85;
			case 85:
				array4[29] = 120;
				num = 101;
				break;
			case 179:
				array4[11] = 156;
				num3 = 119;
				if (ValidateService())
				{
					goto IL_024d;
				}
				goto case 337;
			case 167:
				array4[6] = 133;
				num3 = 190;
				if (true)
				{
					goto IL_024d;
				}
				goto case 205;
			case 205:
				array5[14] = 167;
				num2 = 346;
				goto IL_0249;
			case 209:
				num6 = 12 + 18;
				num2 = 20;
				goto IL_0249;
			case 334:
				array4[17] = 122;
				num = 7;
				break;
			case 363:
				array5[14] = (byte)num10;
				num3 = 315;
				if (!ConnectService())
				{
					goto IL_024d;
				}
				goto case 42;
			case 117:
				array4[10] = (byte)num7;
				num2 = 74;
				goto IL_0249;
			case 278:
				num7 = 140 - 46;
				num = 201;
				break;
			case 3:
				num28 = array7.Length % 4;
				num = 158;
				break;
			case 365:
				array4[8] = 116;
				num3 = 299;
				goto IL_024d;
			case 297:
				array4[18] = (byte)num7;
				num2 = 312;
				goto IL_0249;
			case 95:
				array4[7] = (byte)num7;
				num3 = 400;
				if (ValidateService())
				{
					goto IL_024d;
				}
				goto case 36;
			case 325:
				array4[31] = (byte)num7;
				num3 = 227;
				if (true)
				{
					goto IL_024d;
				}
				goto case 67;
			case 67:
				num6 = 40 + 4;
				_ = 1;
				num2 = (ConnectService() ? 233 : 203);
				goto IL_0249;
			case 333:
				array5[12] = 165;
				num2 = 260;
				goto IL_0249;
			case 171:
				binaryReader.Close();
				num2 = 4;
				goto IL_0249;
			case 267:
				array4[6] = 143;
				num = 167;
				break;
			case 225:
				num10 = 171 - 57;
				num3 = 286;
				if (!ConnectService())
				{
					goto IL_024d;
				}
				goto case 158;
			case 93:
				array5[4] = (byte)num6;
				num3 = 249;
				goto IL_024d;
			case 151:
				array4[20] = 158;
				num2 = 253;
				goto IL_0249;
			case 321:
				num37 <<= 8;
				num2 = 195;
				goto IL_0249;
			case 355:
				num6 = 82 + 56;
				num2 = 335;
				goto IL_0249;
			case 135:
				array4[25] = (byte)num7;
				num3 = 50;
				if (true)
				{
					goto IL_024d;
				}
				goto case 92;
			case 92:
				num7 = 131 - 43;
				num = 5;
				break;
			case 6:
				num38 = 0;
				num = 207;
				break;
			case 22:
				if (num9 == num25 - 1)
				{
					num2 = 96;
					goto IL_0249;
				}
				goto IL_2995;
			case 223:
				array4[5] = 72;
				num2 = 288;
				goto IL_0249;
			case 242:
				num6 = 166 - 55;
				num3 = 373;
				goto IL_024d;
			case 136:
				num6 = 13 + 1;
				num2 = 192;
				goto IL_0249;
			case 50:
				array4[26] = 159;
				num = 160;
				break;
			case 401:
				num6 = 54 - 20;
				num = 39;
				break;
			case 312:
				array4[18] = 152;
				num3 = 194;
				goto IL_024d;
			case 263:
				num35 = 0;
				num = 149;
				break;
			case 102:
				array5[12] = (byte)num10;
				num3 = 333;
				if (ValidateService())
				{
					goto IL_024d;
				}
				goto case 144;
			case 101:
				num7 = 166 - 55;
				num2 = 284;
				goto IL_0249;
			case 199:
				array4 = new byte[32];
				num3 = 75;
				if (ValidateService())
				{
					goto IL_024d;
				}
				goto case 360;
			case 360:
				array4[17] = (byte)num7;
				num2 = 177;
				goto IL_0249;
			case 86:
			case 109:
				if (num36 >= array2.Length)
				{
					num2 = 54;
				}
				else
				{
					array[num36] ^= array2[num36];
					num2 = 345;
				}
				goto IL_0249;
			case 212:
				num7 = 124 - 59;
				num = 232;
				break;
			case 76:
				num38++;
				num3 = 330;
				goto IL_024d;
			case 193:
				num39 = num26 ^ num27;
				num = 6;
				break;
			case 69:
				array5[10] = (byte)num6;
				num3 = 134;
				if (true)
				{
					goto IL_024d;
				}
				goto case 338;
			case 338:
				array6 = new byte[array7.Length];
				num2 = 304;
				goto IL_0249;
			case 230:
				array4[2] = 95;
				num = 139;
				break;
			case 21:
				array5[2] = 168;
				num2 = 348;
				goto IL_0249;
			case 147:
				array4[23] = (byte)num7;
				num3 = 311;
				goto IL_024d;
			case 284:
				array4[29] = (byte)num7;
				num2 = 407;
				goto IL_0249;
			case 289:
				array4[21] = (byte)num7;
				num3 = 65;
				if (true)
				{
					goto IL_024d;
				}
				goto case 308;
			case 308:
				array4[17] = (byte)num7;
				num3 = 71;
				if (ValidateService())
				{
					goto IL_024d;
				}
				goto case 340;
			case 340:
				array5[11] = 174;
				num2 = 401;
				goto IL_0249;
			case 183:
				array4[25] = 96;
				num = 413;
				break;
			case 268:
				num7 = 240 - 80;
				num3 = 88;
				goto IL_024d;
			case 328:
				num10 = 121 + 107;
				num2 = 235;
				goto IL_0249;
			case 407:
				num7 = 209 - 69;
				num3 = 73;
				if (!ConnectService())
				{
					goto IL_024d;
				}
				goto case 106;
			case 79:
				array4[20] = 98;
				num3 = 331;
				if (0 == 0)
				{
					goto IL_024d;
				}
				goto case 173;
			case 173:
				array4[4] = (byte)num7;
				num3 = 152;
				if (0 == 0)
				{
					goto IL_024d;
				}
				goto case 277;
			case 277:
				num25++;
				num2 = 252;
				goto IL_0249;
			case 348:
				array5[2] = 136;
				num3 = 168;
				goto IL_024d;
			case 248:
				num7 = 27 + 104;
				num3 = 157;
				if (ValidateService())
				{
					goto IL_024d;
				}
				goto case 54;
			case 54:
				if (P_0 == -1)
				{
					num = 48;
					break;
				}
				goto case 3;
			case 377:
				array4[31] = (byte)num7;
				num3 = 386;
				goto IL_024d;
			case 259:
				array4[27] = 1;
				num2 = 64;
				goto IL_0249;
			case 344:
				array5[15] = 96;
				num2 = 29;
				goto IL_0249;
			case 120:
				num7 = 69 + 0;
				num2 = 274;
				goto IL_0249;
			case 276:
				num7 = 136 - 45;
				num2 = 84;
				goto IL_0249;
			case 300:
				array5[5] = (byte)num6;
				num = 83;
				break;
			case 326:
				num7 = 136 - 45;
				num = 297;
				break;
			case 249:
				array5[4] = 233;
				num2 = 186;
				goto IL_0249;
			case 55:
				array2[15] = publicKeyToken[7];
				num2 = 316;
				goto IL_0249;
			case 114:
				num4 = BitConverter.ToInt32((byte[])facadeWatcher, P_0);
				num3 = 416;
				goto IL_024d;
			case 309:
				array4[6] = (byte)num7;
				num2 = 52;
				goto IL_0249;
			case 219:
				array4[10] = 23;
				num3 = 110;
				if (true)
				{
					goto IL_024d;
				}
				goto case 345;
			case 345:
				num36++;
				num2 = 109;
				goto IL_0249;
			case 313:
				array4[8] = (byte)num7;
				num3 = 383;
				if (true)
				{
					goto IL_024d;
				}
				goto case 42;
			case 42:
				array5[10] = (byte)num10;
				num = 11;
				break;
			case 49:
				num7 = 116 + 109;
				num2 = 63;
				goto IL_0249;
			case 226:
				array5[13] = 115;
				num3 = 254;
				goto IL_024d;
			case 128:
				array4[12] = (byte)num7;
				num = 154;
				break;
			case 262:
				array4[18] = (byte)num7;
				num3 = 175;
				if (!ConnectService())
				{
					goto IL_024d;
				}
				goto case 405;
			case 405:
				array6[num8 + 1] = (byte)((num31 & 0xFF00) >> 8);
				num2 = 302;
				goto IL_0249;
			case 34:
				array5[1] = 134;
				num2 = 137;
				goto IL_0249;
			case 310:
				num7 = 160 + 70;
				num2 = 33;
				goto IL_0249;
			case 251:
				num7 = 71 + 103;
				num = 204;
				break;
			case 224:
				array4[0] = (byte)num7;
				num2 = 61;
				goto IL_0249;
			case 60:
				array4[9] = (byte)num7;
				num3 = 212;
				goto IL_024d;
			case 68:
				num7 = 23 + 62;
				num = 238;
				break;
			case 258:
				array4[8] = 163;
				num3 = 314;
				if (true)
				{
					goto IL_024d;
				}
				goto case 260;
			case 260:
				num6 = 239 - 79;
				num3 = 146;
				if (ValidateService())
				{
					goto IL_024d;
				}
				goto case 19;
			case 19:
				array2[1] = publicKeyToken[0];
				num2 = 156;
				goto IL_0249;
			case 176:
				num7 = 47 + 20;
				num = 211;
				break;
			case 376:
			{
				CryptoStream cryptoStream = new CryptoStream(memoryStream, transform, CryptoStreamMode.Write);
				cryptoStream.Write(array7, 0, array7.Length);
				cryptoStream.FlushFinalBlock();
				facadeWatcher = memoryStream.ToArray();
				memoryStream.Close();
				cryptoStream.Close();
				num3 = 171;
				if (0 == 0)
				{
					goto IL_024d;
				}
				goto case 400;
			}
			case 400:
				num7 = 124 + 98;
				num3 = 38;
				goto IL_024d;
			case 232:
				array4[9] = (byte)num7;
				num = 14;
				break;
			case 14:
				num7 = 196 - 65;
				num3 = 364;
				if (ValidateService())
				{
					goto IL_024d;
				}
				goto case 143;
			case 207:
			case 330:
				if (num38 < num28)
				{
					if (num38 > 0)
					{
						num3 = 321;
						if (0 == 0)
						{
							goto IL_024d;
						}
						goto case 223;
					}
					goto case 165;
				}
				num = 293;
				break;
			case 140:
				array4[24] = 104;
				num2 = 162;
				goto IL_0249;
			case 195:
				num33 += 8;
				num = 165;
				break;
			case 127:
				num27 = 0u;
				num3 = 189;
				if (!ConnectService())
				{
					goto IL_024d;
				}
				goto case 352;
			case 352:
				num37 = 255u;
				num3 = 16;
				if (0 == 0)
				{
					goto IL_024d;
				}
				goto case 40;
			case 40:
			case 378:
				num12 = num26;
				num = 174;
				break;
			case 384:
				facadeWatcher = array6;
				num2 = 114;
				goto IL_0249;
			case 46:
				num6 = 143 - 47;
				num3 = 280;
				if (true)
				{
					goto IL_024d;
				}
				goto case 130;
			case 130:
				num9 = 0;
				num = 172;
				break;
			case 177:
				array4[17] = 156;
				num2 = 56;
				goto IL_0249;
			case 214:
				array4[0] = 148;
				num3 = 229;
				goto IL_024d;
			case 337:
				num27 = 0u;
				num3 = 45;
				if (ValidateService())
				{
					goto IL_024d;
				}
				goto case 177;
			case 386:
				num7 = 131 - 43;
				num2 = 325;
				goto IL_0249;
			case 32:
				num7 = 56 + 82;
				num2 = 392;
				goto IL_0249;
			case 280:
				array5[9] = (byte)num6;
				num3 = 242;
				if (0 == 0)
				{
					goto IL_024d;
				}
				goto case 381;
			case 381:
				array4[24] = 42;
				num2 = 323;
				goto IL_0249;
			case 23:
				array5[8] = (byte)num6;
				num3 = 261;
				if (0 == 0)
				{
					goto IL_024d;
				}
				goto case 124;
			case 124:
				num6 = 172 - 57;
				num = 184;
				break;
			case 132:
				array5[1] = (byte)num10;
				num3 = 133;
				goto IL_024d;
			case 166:
				num6 = 242 - 80;
				num3 = 69;
				if (ValidateService())
				{
					goto IL_024d;
				}
				goto case 15;
			case 15:
				array4[25] = (byte)num7;
				num = 183;
				break;
			case 36:
				num7 = 68 - 45;
				num3 = 173;
				if (ValidateService())
				{
					goto IL_024d;
				}
				goto case 120;
			case 73:
				array4[29] = (byte)num7;
				num = 276;
				break;
			case 388:
				num7 = 188 - 62;
				num = 371;
				break;
			case 77:
				num7 = 92 + 84;
				num3 = 191;
				if (ValidateService())
				{
					goto IL_024d;
				}
				goto case 26;
			case 26:
				array4[21] = (byte)num7;
				num3 = 278;
				if (ValidateService())
				{
					goto IL_024d;
				}
				goto case 66;
			case 66:
				num6 = 225 - 75;
				num = 385;
				break;
			case 301:
				num7 = 181 - 60;
				num3 = 147;
				if (true)
				{
					goto IL_024d;
				}
				goto case 202;
			case 202:
				num30 = (uint)(num34 * 4);
				num3 = 369;
				if (true)
				{
					goto IL_024d;
				}
				goto case 189;
			case 189:
				if (num28 > 0)
				{
					num3 = 277;
					if (!ConnectService())
					{
						goto IL_024d;
					}
					goto case 150;
				}
				goto case 252;
			case 150:
				array4[26] = (byte)num7;
				num = 163;
				break;
			case 112:
				array4[15] = (byte)num7;
				num2 = 187;
				goto IL_0249;
			case 397:
				num7 = 127 - 42;
				num2 = 237;
				goto IL_0249;
			case 20:
				array5[12] = (byte)num6;
				num = 329;
				break;
			case 47:
				array5[11] = 90;
				num3 = 322;
				if (ValidateService())
				{
					goto IL_024d;
				}
				goto case 159;
			case 198:
				array5[8] = (byte)num10;
				num3 = 328;
				if (true)
				{
					goto IL_024d;
				}
				goto case 83;
			case 83:
				array5[6] = 109;
				num = 136;
				break;
			case 285:
				array4[2] = 48;
				num = 347;
				break;
			case 52:
				array4[6] = 137;
				num = 303;
				break;
			case 252:
				num30 = 0u;
				num3 = 130;
				goto IL_024d;
			case 206:
				array4[8] = (byte)num7;
				num2 = 365;
				goto IL_0249;
			case 346:
				num10 = 168 + 36;
				num3 = 363;
				if (0 == 0)
				{
					goto IL_024d;
				}
				goto case 244;
			case 244:
				num7 = 152 - 50;
				num = 360;
				break;
			case 87:
				array4[19] = (byte)num7;
				num2 = 79;
				goto IL_0249;
			case 318:
				num6 = 209 - 69;
				num3 = 93;
				if (ValidateService())
				{
					goto IL_024d;
				}
				goto case 155;
			case 314:
				array4[8] = 148;
				num = 317;
				break;
			case 389:
				array4[13] = (byte)num7;
				num3 = 403;
				goto IL_024d;
			case 256:
				array5[4] = 149;
				num2 = 318;
				goto IL_0249;
			case 142:
				array5[10] = 116;
				num2 = 213;
				goto IL_0249;
			case 9:
				num7 = 180 - 94;
				num = 143;
				break;
			case 288:
				array4[5] = 144;
				num = 372;
				break;
			case 316:
				num36 = 0;
				num3 = 86;
				if (0 == 0)
				{
					goto IL_024d;
				}
				goto case 406;
			case 406:
				array4[22] = 3;
				num2 = 301;
				goto IL_0249;
			case 187:
				array4[15] = 123;
				num = 310;
				break;
			case 0:
				array5[8] = 226;
				num2 = 106;
				goto IL_0249;
			case 210:
				array4[3] = 80;
				num2 = 28;
				goto IL_0249;
			case 28:
				array4[3] = 93;
				num3 = 2;
				goto IL_024d;
			case 347:
				array4[3] = 102;
				num3 = 210;
				if (true)
				{
					goto IL_024d;
				}
				goto case 383;
			case 383:
				num7 = 92 + 36;
				num3 = 100;
				goto IL_024d;
			case 413:
				num7 = 143 - 47;
				num3 = 218;
				if (!ConnectService())
				{
					goto IL_024d;
				}
				goto case 71;
			case 71:
				num7 = 184 - 61;
				num3 = 262;
				if (ValidateService())
				{
					goto IL_024d;
				}
				goto case 162;
			case 200:
				array4[15] = 170;
				num3 = 250;
				if (ValidateService())
				{
					goto IL_024d;
				}
				goto case 390;
			case 390:
				array5[7] = (byte)num6;
				num = 399;
				break;
			case 253:
				array4[20] = 146;
				num3 = 145;
				goto IL_024d;
			case 409:
				array2[11] = publicKeyToken[5];
				num = 89;
				break;
			case 274:
				array4[30] = (byte)num7;
				num3 = 266;
				if (ValidateService())
				{
					goto IL_024d;
				}
				goto case 414;
			case 414:
				num7 = 159 - 53;
				num2 = 270;
				goto IL_0249;
			case 305:
				num7 = 143 - 47;
				num = 51;
				break;
			case 88:
				array4[19] = (byte)num7;
				num2 = 271;
				goto IL_0249;
			case 164:
				array2 = array5;
				num3 = 113;
				if (true)
				{
					goto IL_024d;
				}
				goto case 25;
			case 25:
				array5[1] = (byte)num10;
				num2 = 34;
				goto IL_0249;
			case 201:
				array4[22] = (byte)num7;
				num3 = 305;
				if (!ConnectService())
				{
					goto IL_024d;
				}
				goto case 162;
			case 162:
				array4[24] = 195;
				num3 = 197;
				if (ValidateService())
				{
					goto IL_024d;
				}
				goto case 36;
			case 4:
				array7 = (byte[])facadeWatcher;
				num3 = 3;
				goto IL_024d;
			case 17:
				array5[9] = 162;
				num = 46;
				break;
			case 255:
				array4[12] = 71;
				num3 = 269;
				if (0 == 0)
				{
					goto IL_024d;
				}
				goto case 357;
			case 357:
				array5[9] = 133;
				num2 = 142;
				goto IL_0249;
			case 39:
				array5[11] = (byte)num6;
				num = 209;
				break;
			case 269:
				array4[12] = 136;
				num = 231;
				break;
			case 247:
				array4[1] = 237;
				num2 = 230;
				goto IL_0249;
			case 10:
				array4[21] = 35;
				num3 = 115;
				if (0 == 0)
				{
					goto IL_024d;
				}
				goto case 211;
			case 211:
				array4[22] = (byte)num7;
				num3 = 406;
				if (0 == 0)
				{
					goto IL_024d;
				}
				goto case 81;
			case 81:
				num29 = 0u;
				num = 127;
				break;
			case 270:
				array4[14] = (byte)num7;
				num = 402;
				break;
			case 385:
				array5[0] = (byte)num6;
				num3 = 366;
				goto IL_024d;
			case 343:
				array5[14] = (byte)num6;
				num2 = 354;
				goto IL_0249;
			case 5:
				array4[16] = (byte)num7;
				num2 = 208;
				goto IL_0249;
			case 222:
				array5[15] = (byte)num10;
				num3 = 164;
				goto IL_024d;
			case 394:
				array4[14] = 99;
				num2 = 414;
				goto IL_0249;
			case 208:
				array4[16] = 86;
				num2 = 298;
				goto IL_0249;
			case 65:
				array4[21] = 160;
				num3 = 90;
				if (true)
				{
					goto IL_024d;
				}
				goto case 148;
			case 148:
				num7 = 132 - 44;
				num = 273;
				break;
			case 292:
				num30 = (uint)num8;
				num = 307;
				break;
			case 31:
				array4[28] = 100;
				num2 = 37;
				goto IL_0249;
			case 56:
				array4[17] = 197;
				num3 = 70;
				if (!ConnectService())
				{
					goto IL_024d;
				}
				goto case 306;
			case 306:
				array4[5] = 198;
				num3 = 267;
				if (0 == 0)
				{
					goto IL_024d;
				}
				goto case 161;
			case 161:
				array4[14] = (byte)num7;
				num3 = 116;
				if (0 == 0)
				{
					goto IL_024d;
				}
				goto case 361;
			case 361:
				array4[11] = 70;
				num = 27;
				break;
			case 89:
				array2[13] = publicKeyToken[6];
				num3 = 55;
				if (true)
				{
					goto IL_024d;
				}
				goto case 261;
			case 261:
				num6 = 60 - 6;
				num2 = 243;
				goto IL_0249;
			case 315:
				array5[15] = 152;
				num3 = 344;
				if (!ConnectService())
				{
					goto IL_024d;
				}
				goto case 218;
			case 218:
				array4[25] = (byte)num7;
				num3 = 356;
				goto IL_024d;
			case 402:
				num7 = 124 + 44;
				num2 = 161;
				goto IL_0249;
			case 8:
				array4[4] = (byte)num7;
				num3 = 148;
				goto IL_024d;
			case 339:
				array4[1] = 164;
				num = 24;
				break;
			case 362:
				num10 = 139 - 82;
				num2 = 222;
				goto IL_0249;
			case 145:
				array4[20] = 177;
				num3 = 122;
				if (0 == 0)
				{
					goto IL_024d;
				}
				goto case 143;
			case 143:
				array4[16] = (byte)num7;
				num = 334;
				break;
			case 37:
				num7 = 10 + 6;
				num = 281;
				break;
			case 146:
				array5[12] = (byte)num6;
				num3 = 225;
				if (ValidateService())
				{
					goto IL_024d;
				}
				goto case 316;
			case 170:
				num35++;
				num3 = 382;
				goto IL_024d;
			case 246:
				array4[13] = (byte)num7;
				num = 58;
				break;
			case 367:
				array4[23] = 145;
				num = 415;
				break;
			case 349:
				array2[7] = publicKeyToken[3];
				num3 = 240;
				if (!ConnectService())
				{
					goto IL_024d;
				}
				goto case 188;
			case 188:
				num10 = 111 + 104;
				num3 = 42;
				goto IL_024d;
			case 234:
				num7 = 61 + 97;
				num3 = 217;
				if (ValidateService())
				{
					goto IL_024d;
				}
				goto case 111;
			case 111:
				binaryReader.BaseStream.Position = 0L;
				num = 296;
				break;
			case 119:
				array4[11] = 112;
				num = 361;
				break;
			case 70:
				num7 = 86 - 30;
				num = 308;
				break;
			case 154:
				array4[13] = 125;
				num3 = 265;
				if (0 == 0)
				{
					goto IL_024d;
				}
				goto case 266;
			case 266:
				array4[30] = 211;
				num = 387;
				break;
			case 181:
				num6 = 5 + 113;
				num3 = 23;
				goto IL_024d;
			case 236:
				array4[29] = 3;
				num = 257;
				break;
			case 190:
				num7 = 23 + 7;
				num3 = 309;
				goto IL_024d;
			case 273:
				array4[4] = (byte)num7;
				num2 = 36;
				goto IL_0249;
			case 254:
				array5[13] = 167;
				num3 = 105;
				if (!ConnectService())
				{
					goto IL_024d;
				}
				goto case 172;
			case 115:
				num7 = 121 + 112;
				num3 = 26;
				if (ValidateService())
				{
					goto IL_024d;
				}
				goto case 396;
			case 307:
				num27 = (uint)((array7[num30 + 3] << 24) | (array7[num30 + 2] << 16) | (array7[num30 + 1] << 8) | array7[num30]);
				num3 = 40;
				goto IL_024d;
			case 169:
				array5[14] = (byte)num10;
				num = 205;
				break;
			case 196:
				array5[9] = 148;
				num3 = 357;
				goto IL_024d;
			case 122:
				num7 = 57 + 79;
				num2 = 289;
				goto IL_0249;
			case 398:
				num7 = 90 - 47;
				num3 = 87;
				if (ValidateService())
				{
					goto IL_024d;
				}
				goto case 233;
			case 233:
			case 336:
				array5[15] = (byte)num10;
				num3 = 362;
				goto IL_024d;
			case 16:
				num33 = 0;
				num3 = 375;
				goto IL_024d;
			case 157:
				array4[9] = (byte)num7;
				num2 = 41;
				goto IL_0249;
			case 80:
				array4[5] = (byte)num7;
				num3 = 223;
				goto IL_024d;
			case 281:
				array4[29] = (byte)num7;
				num3 = 85;
				if (!ConnectService())
				{
					goto IL_024d;
				}
				goto case 71;
			case 153:
				if (num28 > 0)
				{
					num3 = 337;
					goto IL_024d;
				}
				goto IL_1f02;
			case 294:
				num6 = 106 + 64;
				num3 = 97;
				if (true)
				{
					goto IL_024d;
				}
				goto case 191;
			case 191:
				array4[27] = (byte)num7;
				num = 259;
				break;
			case 250:
				num7 = 71 + 71;
				num2 = 112;
				goto IL_0249;
			case 159:
				array5[10] = (byte)num10;
				num2 = 188;
				goto IL_0249;
			case 286:
				array5[12] = (byte)num10;
				num3 = 351;
				goto IL_024d;
			case 104:
				array4[24] = (byte)num7;
				num3 = 140;
				goto IL_024d;
			case 35:
				if (publicKeyToken.Length != 0)
				{
					num = 19;
					break;
				}
				goto case 316;
			case 12:
				array4[28] = 68;
				num = 72;
				break;
			case 366:
				array5[0] = 100;
				num2 = 290;
				goto IL_0249;
			case 229:
				num7 = 38 - 2;
				num2 = 224;
				goto IL_0249;
			case 296:
				array7 = binaryReader.ReadBytes((int)binaryReader.BaseStream.Length);
				num3 = 199;
				if (ValidateService())
				{
					goto IL_024d;
				}
				goto case 118;
			case 118:
				array6[num8 + 3] = (byte)((num31 & 0xFF000000u) >> 24);
				num3 = 220;
				if (0 == 0)
				{
					goto IL_024d;
				}
				goto case 282;
			case 282:
				num7 = 118 + 18;
				num = 95;
				break;
			case 298:
				array4[16] = 35;
				num = 9;
				break;
			case 139:
				array4[2] = 122;
				num3 = 228;
				if (true)
				{
					goto IL_024d;
				}
				goto case 290;
			case 290:
				num10 = 92 + 68;
				num2 = 82;
				goto IL_0249;
			case 356:
				num7 = 104 + 30;
				num3 = 135;
				if (ValidateService())
				{
					goto IL_024d;
				}
				goto case 215;
			case 215:
				num7 = 186 - 62;
				num3 = 104;
				if (0 == 0)
				{
					goto IL_024d;
				}
				goto case 396;
			case 396:
				array5[13] = (byte)num6;
				num2 = 62;
				goto IL_0249;
			case 43:
				num6 = 9 + 120;
				num3 = 343;
				goto IL_024d;
			case 110:
				array4[10] = 124;
				num3 = 18;
				if (true)
				{
					goto IL_024d;
				}
				goto case 272;
			case 272:
				array4[7] = (byte)num7;
				num2 = 251;
				goto IL_0249;
			case 303:
				num7 = 60 + 30;
				num = 272;
				break;
			case 123:
				num7 = 117 - 75;
				num = 150;
				break;
			case 408:
				array4[24] = 7;
				num = 381;
				break;
			case 371:
				array4[11] = (byte)num7;
				num2 = 179;
				goto IL_0249;
			case 317:
				num7 = 157 - 52;
				num = 206;
				break;
			case 370:
				num10 = 98 + 47;
				num3 = 368;
				if (!ConnectService())
				{
					goto IL_024d;
				}
				goto case 350;
			case 155:
				num10 = 56 + 5;
				num2 = 264;
				goto IL_0249;
			case 265:
				num7 = 38 + 53;
				num3 = 246;
				goto IL_024d;
			case 18:
				num7 = 146 - 41;
				num3 = 117;
				if (ValidateService())
				{
					goto IL_024d;
				}
				goto case 138;
			case 138:
				array4[10] = (byte)num7;
				num2 = 219;
				goto IL_0249;
			case 165:
				array6[num8 + num38] = (byte)((num39 & num37) >> num33);
				num = 76;
				break;
			case 44:
				array4[20] = (byte)num7;
				num3 = 374;
				if (true)
				{
					goto IL_024d;
				}
				goto case 194;
			case 194:
				array4[18] = 133;
				num2 = 268;
				goto IL_0249;
			case 94:
				array4[26] = (byte)num7;
				num3 = 123;
				if (0 == 0)
				{
					goto IL_024d;
				}
				goto case 392;
			case 392:
				array4[15] = (byte)num7;
				num = 49;
				break;
			case 275:
				array5[0] = 217;
				num3 = 355;
				goto IL_024d;
			case 178:
				array4[10] = 121;
				num3 = 107;
				goto IL_024d;
			case 116:
				array4[14] = 99;
				num3 = 68;
				if (!ConnectService())
				{
					goto IL_024d;
				}
				goto case 304;
			case 304:
				num32 = array.Length / 4;
				num2 = 327;
				goto IL_0249;
			case 335:
				array5[1] = (byte)num6;
				num3 = 245;
				goto IL_024d;
			case 29:
				num10 = 229 - 76;
				goto case 233;
			case 393:
				array4[12] = (byte)num7;
				num3 = 255;
				goto IL_024d;
			case 391:
				array6[num8] = (byte)(num31 & 0xFF);
				num3 = 405;
				if (0 == 0)
				{
					goto IL_024d;
				}
				goto case 350;
			case 350:
				array = array4;
				num2 = 332;
				goto IL_0249;
			case 319:
				array5[3] = 92;
				num = 395;
				break;
			case 156:
				array2[3] = publicKeyToken[1];
				num3 = 59;
				goto IL_024d;
			case 271:
				array4[19] = 165;
				num3 = 398;
				if (true)
				{
					goto IL_024d;
				}
				goto case 217;
			case 217:
				array4[23] = (byte)num7;
				num2 = 408;
				goto IL_0249;
			case 364:
				array4[10] = (byte)num7;
				num3 = 178;
				if (!ConnectService())
				{
					goto IL_024d;
				}
				goto case 38;
			case 38:
				array4[7] = (byte)num7;
				num3 = 258;
				if (ValidateService())
				{
					goto IL_024d;
				}
				goto case 222;
			case 220:
			case 293:
				num9++;
				num3 = 380;
				goto IL_024d;
			case 134:
				num10 = 101 + 24;
				num = 159;
				break;
			case 185:
				num6 = 168 - 56;
				num2 = 390;
				goto IL_0249;
			case 100:
				array4[8] = (byte)num7;
				num3 = 248;
				if (!ConnectService())
				{
					goto IL_024d;
				}
				goto case 2;
			case 2:
				num7 = 34 + 120;
				num = 8;
				break;
			case 238:
				array4[14] = (byte)num7;
				num3 = 279;
				if (true)
				{
					goto IL_024d;
				}
				goto case 291;
			case 291:
				array4[30] = (byte)num7;
				num3 = 57;
				if (true)
				{
					goto IL_024d;
				}
				goto case 341;
			case 341:
				array5[10] = 116;
				num = 166;
				break;
			case 13:
				num6 = 71 + 59;
				num = 300;
				break;
			case 368:
				array5[7] = (byte)num10;
				num2 = 124;
				goto IL_0249;
			case 63:
				array4[15] = (byte)num7;
				num2 = 200;
				goto IL_0249;
			case 412:
				array5[5] = (byte)num6;
				num3 = 13;
				if (!ConnectService())
				{
					goto IL_024d;
				}
				goto case 302;
			case 302:
				array6[num8 + 2] = (byte)((num31 & 0xFF0000) >> 16);
				num = 118;
				break;
			case 295:
				if (((Array)facadeWatcher).Length == 0)
				{
					num = 144;
					break;
				}
				goto case 114;
			case 144:
				binaryReader = new BinaryReader(typeof(IssuerWatcherWriter).Assembly.GetManifestResourceStream("4bfa769b-e910-4a24-8c2e-8cda9b1bd4b6"));
				num2 = 111;
				goto IL_0249;
			case 172:
			case 380:
				if (num9 < num25)
				{
					num34 = num9 % num32;
					num2 = 411;
					goto IL_0249;
				}
				num = 384;
				break;
			case 103:
				array4[18] = (byte)num7;
				num2 = 326;
				goto IL_0249;
			case 75:
				num7 = 164 - 54;
				num3 = 239;
				if (ValidateService())
				{
					goto IL_024d;
				}
				goto case 403;
			case 403:
				num7 = 209 - 118;
				num3 = 30;
				if (ConnectService())
				{
					goto case 379;
				}
				goto IL_024d;
			case 141:
				array4[1] = 168;
				num = 339;
				break;
			case 327:
				num26 = 0u;
				num = 81;
				break;
			case 228:
				array4[2] = 130;
				num = 285;
				break;
			case 373:
				array5[9] = (byte)num6;
				num3 = 196;
				if (ValidateService())
				{
					goto IL_024d;
				}
				goto case 292;
			case 237:
				array4[23] = (byte)num7;
				num3 = 234;
				goto IL_024d;
			case 1:
				array5[2] = (byte)num6;
				num = 21;
				break;
			case 78:
				array4[17] = (byte)num7;
				num3 = 244;
				goto IL_024d;
			case 369:
				num29 = (uint)((array[num30 + 3] << 24) | (array[num30 + 2] << 16) | (array[num30 + 1] << 8) | array[num30]);
				num = 352;
				break;
			case 192:
				array5[6] = (byte)num6;
				num2 = 155;
				goto IL_0249;
			case 99:
				num6 = 254 - 84;
				num2 = 1;
				goto IL_0249;
			case 152:
				num7 = 186 - 62;
				num3 = 80;
				if (ValidateService())
				{
					goto IL_024d;
				}
				goto case 331;
			case 331:
				num7 = 73 + 86;
				num3 = 44;
				goto IL_024d;
			case 216:
				num10 = 95 + 39;
				num3 = 132;
				if (!ConnectService())
				{
					goto IL_024d;
				}
				goto case 107;
			case 107:
				num7 = 36 + 59;
				num2 = 138;
				goto IL_0249;
			case 324:
				array4[31] = (byte)num7;
				num3 = 125;
				goto IL_024d;
			case 399:
				array5[7] = 132;
				num = 370;
				break;
			case 203:
			case 287:
				array5[9] = (byte)num6;
				num = 17;
				break;
			case 180:
				array5[3] = 58;
				num2 = 294;
				goto IL_0249;
			case 329:
				num10 = 220 - 73;
				num3 = 102;
				if (!ConnectService())
				{
					goto IL_024d;
				}
				goto case 364;
			case 45:
				num26 += num29;
				num3 = 263;
				if (ValidateService())
				{
					goto IL_024d;
				}
				goto case 354;
			case 354:
				num10 = 95 + 70;
				num2 = 169;
				goto IL_0249;
			case 96:
				if (num28 > 0)
				{
					num3 = 193;
					goto IL_024d;
				}
				goto IL_2995;
			case 106:
				num10 = 232 - 77;
				num3 = 198;
				if (!ConnectService())
				{
					goto IL_024d;
				}
				goto case 323;
			case 323:
				array4[24] = 119;
				num2 = 215;
				goto IL_0249;
			case 235:
				array5[8] = (byte)num10;
				num = 181;
				break;
			case 59:
				array2[5] = publicKeyToken[2];
				num2 = 349;
				goto IL_0249;
			case 231:
				num7 = 79 - 72;
				num = 128;
				break;
			case 51:
				array4[22] = (byte)num7;
				num2 = 359;
				goto IL_0249;
			case 359:
				array4[22] = 128;
				num3 = 176;
				if (ValidateService())
				{
					goto IL_024d;
				}
				goto case 86;
			case 245:
				num10 = 207 - 69;
				num = 25;
				break;
			case 415:
				array4[23] = 156;
				num = 397;
				break;
			case 358:
				array5[12] = (byte)num6;
				num3 = 226;
				goto IL_024d;
			case 97:
				array5[4] = (byte)num6;
				num2 = 256;
				goto IL_0249;
			case 404:
				num27 <<= 8;
				num3 = 126;
				goto IL_024d;
			case 41:
				num7 = 3 + 98;
				num = 60;
				break;
			case 311:
				array4[23] = 120;
				num = 367;
				break;
			case 320:
				num26 = num12;
				num = 22;
				break;
			case 387:
				num7 = 154 - 51;
				num3 = 324;
				if (ValidateService())
				{
					goto IL_024d;
				}
				goto case 256;
			case 299:
				num7 = 73 + 107;
				num3 = 313;
				if (!ConnectService())
				{
					goto IL_024d;
				}
				goto case 375;
			case 375:
				if (num9 == num25 - 1)
				{
					num = 153;
					break;
				}
				goto IL_1f02;
			case 74:
				array4[11] = 177;
				num2 = 388;
				goto IL_0249;
			case 410:
				array4[1] = (byte)num7;
				num3 = 247;
				if (ValidateService())
				{
					goto IL_024d;
				}
				goto case 351;
			case 227:
				array4[31] = 187;
				num2 = 350;
				goto IL_0249;
			case 27:
				num7 = 62 + 34;
				num3 = 393;
				if (0 == 0)
				{
					goto IL_024d;
				}
				goto case 121;
			case 121:
				array4[7] = 73;
				num2 = 282;
				goto IL_0249;
			case 64:
				num7 = 207 - 69;
				num = 129;
				break;
			case 163:
				array4[27] = 93;
				num3 = 77;
				goto IL_024d;
			case 221:
				array5[1] = (byte)num10;
				num2 = 216;
				goto IL_0249;
			case 7:
				num7 = 43 + 8;
				num3 = 78;
				goto IL_024d;
			case 98:
				if (publicKeyToken == null)
				{
					goto case 316;
				}
				num3 = 35;
				if (0 == 0)
				{
					goto IL_024d;
				}
				goto case 186;
			case 186:
				array5[5] = 84;
				num3 = 182;
				if (true)
				{
					goto IL_024d;
				}
				goto case 33;
			case 33:
				array4[15] = (byte)num7;
				num3 = 92;
				if (ValidateService())
				{
					goto IL_024d;
				}
				goto case 283;
			case 283:
				num7 = 214 - 71;
				num2 = 15;
				goto IL_0249;
			case 279:
				array4[14] = 163;
				num = 32;
				break;
			case 204:
				array4[7] = (byte)num7;
				num = 121;
				break;
			case 30:
				array4[13] = (byte)num7;
				num2 = 394;
				goto IL_0249;
			case 72:
				array4[28] = 100;
				num = 31;
				break;
			case 257:
				num7 = 4 + 88;
				num3 = 291;
				goto IL_024d;
			case 342:
				num6 = 64 + 105;
				num = 241;
				break;
			case 175:
				num7 = 250 - 83;
				num = 103;
				break;
			case 108:
			{
				uint num11 = num12;
				uint num13 = num12;
				uint num14 = 399522727u;
				uint num15 = 1175363962u;
				uint num16 = 656276816u;
				uint num17 = 297323369u;
				uint num18 = num13;
				uint num19 = 1356102888u;
				ulong num20 = num15 * 371293044;
				num20 |= 1;
				num17 = (uint)(num17 * num17 % num20);
				uint num21 = ((num16 >> 5) | (num16 << 27)) + num14;
				uint num22 = num21 & 0x55555555;
				num21 &= 0xAAAAAAAAu;
				num16 = (num21 >> 1) | (num22 << 1);
				if ((double)num14 == 0.0)
				{
					num14--;
				}
				uint num23 = (uint)(64079.0 / (double)num14 + (double)num14);
				num14 = (uint)((uint)((short)num17 + (ushort)num17 + (int)num23) + (short)num17);
				num15 += num17;
				ulong num24 = num17 * num17;
				if (num24 == 0)
				{
					num24--;
				}
				num19 = (uint)(num19 * num19 % num24);
				num18 ^= num18 << 9;
				num18 += num14;
				num18 ^= num18 >> 21;
				num18 += num15;
				num18 ^= num18 << 2;
				num18 += num19;
				num18 = (((num17 << 6) + num17) ^ num15) + num18;
				num12 = num11 + (uint)(double)num18;
				num3 = 320;
				goto IL_024d;
			}
			case 82:
				array5[0] = (byte)num10;
				num3 = 275;
				if (!ConnectService())
				{
					goto IL_024d;
				}
				goto case 197;
			case 197:
				array4[25] = 139;
				num2 = 283;
				goto IL_0249;
			case 125:
				num7 = 70 + 40;
				num = 377;
				break;
			case 61:
				array4[1] = 89;
				num = 141;
				break;
			case 137:
				num10 = 30 + 69;
				num2 = 221;
				goto IL_0249;
			case 411:
				num8 = num9 * 4;
				num = 202;
				break;
			case 322:
				array5[11] = 91;
				num3 = 340;
				if (ValidateService())
				{
					goto IL_024d;
				}
				goto case 395;
			case 395:
				array5[3] = 197;
				num = 180;
				break;
			case 184:
				array5[7] = (byte)num6;
				num = 353;
				break;
			case 182:
				num6 = 128 - 42;
				num = 412;
				break;
			case 129:
				array4[28] = (byte)num7;
				num3 = 12;
				if (ValidateService())
				{
					goto IL_024d;
				}
				goto case 170;
			case 416:
				try
				{
					byte[] array3 = new byte[num4];
					ValidateService();
					int num5;
					if (!ConnectService())
					{
						num5 = 2;
						if (false)
						{
							goto IL_36ac;
						}
					}
					else
					{
						num5 = 3;
					}
					switch (num5)
					{
					case 0:
					case 2:
						break;
					default:
						goto IL_372c;
					}
					goto IL_36ac;
					IL_372c:
					return Encoding.Unicode.GetString(array3, 0, array3.Length);
					IL_36ac:
					Array.Copy((Array)facadeWatcher, P_0 + 4, array3, 0, num4);
					goto IL_372c;
				}
				catch
				{
				}
				return "";
			case 48:
			{
				SymmetricAlgorithm symmetricAlgorithm = CompareUtils();
				symmetricAlgorithm.Mode = CipherMode.CBC;
				transform = symmetricAlgorithm.CreateDecryptor(array, array2);
				num3 = 131;
				goto IL_024d;
			}
			case 131:
				{
					memoryStream = new MemoryStream();
					num2 = 376;
					goto IL_0249;
				}
				IL_1f02:
				num26 += num29;
				num3 = 292;
				if (0 == 0)
				{
					goto IL_024d;
				}
				goto case 65;
				IL_2995:
				num31 = num26 ^ num27;
				num = 391;
				break;
				IL_0249:
				num3 = num2;
				goto IL_024d;
				IL_024d:
				num = num3;
				break;
			}
		}
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static string CreateUtils(object P_0)
	{
		byte[] array = Convert.FromBase64String((string)P_0);
		return Encoding.Unicode.GetString(array, 0, array.Length);
	}

	[DllImport("kernel32.dll", EntryPoint = "VirtualProtect")]
	private static extern int OrderUtils(nint P_0, int P_1, int P_2, ref int P_3);

	[MethodImpl(MethodImplOptions.NoInlining)]
	[ConfigurationFilterContainer(typeof(ConfigurationFilterContainer.ComposerPoolCollection<object>[]))]
	static void CustomizeUtils()
	{
		int num = 293;
		byte[] array = default(byte[]);
		int num17 = default(int);
		int num13 = default(int);
		byte[] array2 = default(byte[]);
		int num14 = default(int);
		uint num38 = default(uint);
		uint num24 = default(uint);
		uint num18 = default(uint);
		byte[] array5 = default(byte[]);
		int num20 = default(int);
		uint num21 = default(uint);
		byte[] array4 = default(byte[]);
		byte[] publicKeyToken = default(byte[]);
		int num40 = default(int);
		uint num46 = default(uint);
		byte[] array3 = default(byte[]);
		uint num39 = default(uint);
		BinaryReader binaryReader = default(BinaryReader);
		int num48 = default(int);
		nint num16 = default(nint);
		int num9 = default(int);
		nint hINSTANCE = default(nint);
		int num47 = default(int);
		byte[] array6 = default(byte[]);
		uint num42 = default(uint);
		int num43 = default(int);
		int num15 = default(int);
		nint num12 = default(nint);
		byte[] array7 = default(byte[]);
		int num41 = default(int);
		int num37 = default(int);
		int num45 = default(int);
		int num44 = default(int);
		int num19 = default(int);
		int num22 = default(int);
		nint num7 = default(nint);
		int num11 = default(int);
		int num6 = default(int);
		int num8 = default(int);
		while (true)
		{
			int num2 = num;
			while (true)
			{
				IL_1e5e:
				int num3 = num2;
				while (true)
				{
					nint zero;
					switch (num3)
					{
					case 196:
						array[26] = 191;
						num2 = 3;
						if (InterruptAdapter())
						{
							goto IL_1e5e;
						}
						goto case 283;
					case 283:
						array[6] = 46;
						num3 = 330;
						continue;
					case 193:
						num17 = 64 + 98;
						num3 = 135;
						continue;
					case 280:
						num13 = 101 + 92;
						num2 = 347;
						if (true)
						{
							goto IL_1e5e;
						}
						goto case 143;
					case 54:
						array[1] = 95;
						num = 174;
						goto end_IL_1e62;
					case 458:
						array2[15] = (byte)num14;
						num3 = 98;
						continue;
					case 60:
						num13 = 142 - 47;
						num2 = 372;
						goto IL_1e5e;
					case 26:
						num38 = num24 ^ num18;
						num2 = 204;
						if (InterruptAdapter())
						{
							goto IL_1e5e;
						}
						goto case 172;
					case 172:
						num17 = 152 - 50;
						num = 130;
						goto end_IL_1e62;
					case 171:
						num13 = 34 + 50;
						num3 = 256;
						continue;
					case 34:
						array[1] = 156;
						num2 = 54;
						if (0 == 0)
						{
							goto IL_1e5e;
						}
						goto case 297;
					case 297:
						array[9] = 177;
						num2 = 131;
						goto IL_1e5e;
					case 15:
						array[28] = 11;
						num3 = 371;
						continue;
					case 197:
						array[22] = 145;
						num2 = 279;
						if (0 == 0)
						{
							goto IL_1e5e;
						}
						goto case 51;
					case 51:
						array[13] = (byte)num13;
						num3 = 97;
						continue;
					case 42:
						array[6] = 134;
						num2 = 368;
						goto IL_1e5e;
					case 93:
						array[2] = (byte)num13;
						num2 = 307;
						if (0 == 0)
						{
							goto IL_1e5e;
						}
						goto case 186;
					case 186:
						array[2] = (byte)num13;
						num2 = 353;
						if (!MapAdapter())
						{
							goto IL_1e5e;
						}
						goto case 280;
					case 74:
						array5[num20 + 2] = (byte)((num21 & 0xFF0000) >> 16);
						num3 = 367;
						continue;
					case 73:
						array2[5] = 60;
						num2 = 413;
						goto IL_1e5e;
					case 218:
						array4[7] = publicKeyToken[3];
						num = 182;
						goto end_IL_1e62;
					case 101:
						array4[5] = publicKeyToken[2];
						num = 218;
						goto end_IL_1e62;
					case 155:
						array5[num20] = (byte)(num21 & 0xFF);
						num2 = 362;
						if (0 == 0)
						{
							goto IL_1e5e;
						}
						goto case 57;
					case 57:
						array[3] = (byte)num13;
						num = 340;
						goto end_IL_1e62;
					case 204:
						num40 = 0;
						num2 = 149;
						if (true)
						{
							goto IL_1e5e;
						}
						goto case 179;
					case 179:
						array[30] = (byte)num13;
						num = 219;
						goto end_IL_1e62;
					case 152:
						num46 = (uint)((array3[num39 + 3] << 24) | (array3[num39 + 2] << 16) | (array3[num39 + 1] << 8) | array3[num39]);
						num = 275;
						goto end_IL_1e62;
					case 366:
						array2[10] = 111;
						num2 = 55;
						goto IL_1e5e;
					case 420:
						num13 = 162 + 8;
						num2 = 57;
						if (InterruptAdapter())
						{
							goto IL_1e5e;
						}
						goto case 294;
					case 59:
						array[3] = 142;
						num = 316;
						goto end_IL_1e62;
					case 378:
						array[17] = 144;
						num2 = 107;
						if (InterruptAdapter())
						{
							goto IL_1e5e;
						}
						goto case 182;
					case 323:
						array2[9] = (byte)num17;
						num2 = 366;
						goto IL_1e5e;
					case 88:
						if (publicKeyToken != null)
						{
							num3 = 335;
							continue;
						}
						goto case 157;
					case 153:
						num13 = 82 + 0;
						num2 = 454;
						if (0 == 0)
						{
							goto IL_1e5e;
						}
						goto case 110;
					case 110:
					{
						byte[] buffer = array5;
						Array.Clear(array4, 0, array4.Length);
						binaryReader.Close();
						binaryReader = new BinaryReader(new MemoryStream(buffer));
						num2 = 358;
						if (true)
						{
							goto IL_1e5e;
						}
						goto case 327;
					}
					case 327:
						array[9] = (byte)num13;
						num3 = 321;
						continue;
					case 296:
						array2[2] = (byte)num14;
						num3 = 356;
						continue;
					case 105:
						num39 = (uint)(num48 * 4);
						num2 = 152;
						if (0 == 0)
						{
							goto IL_1e5e;
						}
						goto case 80;
					case 80:
						array[18] = 21;
						num2 = 407;
						if (true)
						{
							goto IL_1e5e;
						}
						goto case 248;
					case 248:
						array[20] = (byte)num13;
						num2 = 12;
						if (0 == 0)
						{
							goto IL_1e5e;
						}
						goto case 340;
					case 340:
						array[4] = 74;
						num2 = 142;
						if (InterruptAdapter())
						{
							goto IL_1e5e;
						}
						goto case 288;
					case 87:
						array[7] = (byte)num13;
						num = 438;
						goto end_IL_1e62;
					case 464:
						num13 = 171 - 97;
						num2 = 233;
						if (!MapAdapter())
						{
							goto IL_1e5e;
						}
						goto case 173;
					case 391:
						num13 = 14 + 19;
						num2 = 63;
						if (!MapAdapter())
						{
							goto IL_1e5e;
						}
						goto case 116;
					case 456:
						array[23] = 200;
						num3 = 50;
						continue;
					case 147:
						array2[0] = 142;
						num2 = 43;
						if (0 == 0)
						{
							goto IL_1e5e;
						}
						goto case 63;
					case 63:
						array[30] = (byte)num13;
						num2 = 245;
						if (!MapAdapter())
						{
							goto IL_1e5e;
						}
						goto case 339;
					case 339:
						array4[11] = publicKeyToken[5];
						num3 = 259;
						continue;
					case 405:
						array[26] = 127;
						num2 = 127;
						if (true)
						{
							goto IL_1e5e;
						}
						goto case 92;
					case 92:
						num13 = 149 - 49;
						num3 = 126;
						continue;
					case 231:
						array[21] = (byte)num13;
						num3 = 67;
						continue;
					case 422:
						array2[11] = 114;
						num = 271;
						goto end_IL_1e62;
					case 289:
						OrderUtils(num16, 4, 4, ref num9);
						num = 95;
						goto end_IL_1e62;
					case 148:
						m_RepositoryWatcher = ((IntPtr)hINSTANCE).ToInt64();
						num = 158;
						goto end_IL_1e62;
					case 177:
						array2[11] = 69;
						num = 417;
						goto end_IL_1e62;
					case 219:
						num13 = 169 - 65;
						num2 = 178;
						if (0 == 0)
						{
							goto IL_1e5e;
						}
						goto case 444;
					case 444:
						array[5] = 148;
						num = 129;
						goto end_IL_1e62;
					case 36:
						array[26] = (byte)num13;
						num = 153;
						goto end_IL_1e62;
					case 267:
						num14 = 104 - 101;
						num = 462;
						goto end_IL_1e62;
					case 178:
						array[30] = (byte)num13;
						num2 = 286;
						if (true)
						{
							goto IL_1e5e;
						}
						goto case 56;
					case 56:
						array[17] = 143;
						num2 = 398;
						if (!MapAdapter())
						{
							goto IL_1e5e;
						}
						goto case 227;
					case 227:
						array[7] = (byte)num13;
						num3 = 263;
						continue;
					case 438:
						num13 = 43 + 18;
						num2 = 81;
						if (true)
						{
							goto IL_1e5e;
						}
						goto case 150;
					case 150:
						array2[2] = (byte)num17;
						num = 173;
						goto end_IL_1e62;
					case 207:
						array[24] = 70;
						num = 429;
						goto end_IL_1e62;
					case 97:
						array[13] = 197;
						num3 = 379;
						continue;
					case 182:
						array4[9] = publicKeyToken[4];
						num = 339;
						goto end_IL_1e62;
					case 355:
						num47 = array6.Length / 4;
						num2 = 375;
						goto IL_1e5e;
					case 386:
						array2[14] = 95;
						num = 304;
						goto end_IL_1e62;
					case 305:
						array2[9] = (byte)num14;
						num = 313;
						goto end_IL_1e62;
					case 6:
						array2[15] = 62;
						num2 = 328;
						if (0 == 0)
						{
							goto IL_1e5e;
						}
						goto case 300;
					case 300:
						array4[3] = publicKeyToken[1];
						num2 = 101;
						if (InterruptAdapter())
						{
							goto IL_1e5e;
						}
						goto case 118;
					case 118:
						array[4] = 163;
						num2 = 60;
						if (true)
						{
							goto IL_1e5e;
						}
						goto case 137;
					case 137:
						array4[15] = publicKeyToken[7];
						num2 = 20;
						if (!MapAdapter())
						{
							goto IL_1e5e;
						}
						goto case 351;
					case 351:
						array2[10] = (byte)num17;
						num2 = 111;
						if (!MapAdapter())
						{
							goto IL_1e5e;
						}
						goto case 269;
					case 269:
						num14 = 104 - 4;
						num3 = 296;
						continue;
					case 363:
						array[4] = (byte)num13;
						num3 = 464;
						continue;
					case 245:
						array[30] = 93;
						num3 = 13;
						continue;
					case 235:
						array[28] = 102;
						num2 = 264;
						if (InterruptAdapter())
						{
							goto IL_1e5e;
						}
						goto case 450;
					case 423:
						num24 += num46;
						num2 = 134;
						if (!MapAdapter())
						{
							goto IL_1e5e;
						}
						goto case 275;
					case 275:
						num42 = 255u;
						num2 = 76;
						goto IL_1e5e;
					case 25:
						array[31] = 91;
						num3 = 61;
						continue;
					case 298:
						array[21] = 44;
						num2 = 75;
						goto IL_1e5e;
					case 377:
						num13 = 13 + 6;
						num2 = 248;
						if (true)
						{
							goto IL_1e5e;
						}
						goto case 356;
					case 356:
						array2[3] = 126;
						num2 = 288;
						goto IL_1e5e;
					case 162:
						num43 = 0;
						num2 = 183;
						if (0 == 0)
						{
							goto IL_1e5e;
						}
						goto case 353;
					case 353:
						array[2] = 145;
						num2 = 403;
						if (InterruptAdapter())
						{
							goto IL_1e5e;
						}
						goto case 46;
					case 46:
						array[25] = 153;
						num = 437;
						goto end_IL_1e62;
					case 274:
						num17 = 9 + 66;
						num = 399;
						goto end_IL_1e62;
					case 432:
						num13 = 59 + 17;
						num2 = 348;
						goto IL_1e5e;
					case 125:
						num13 = 240 - 80;
						num2 = 93;
						if (true)
						{
							goto IL_1e5e;
						}
						goto case 176;
					case 176:
						array2[5] = 102;
						num = 73;
						goto end_IL_1e62;
					case 82:
						array2[4] = 38;
						num2 = 250;
						if (true)
						{
							goto IL_1e5e;
						}
						goto case 210;
					case 210:
						num17 = 117 + 97;
						num2 = 230;
						goto IL_1e5e;
					case 216:
						array[5] = 148;
						num3 = 280;
						continue;
					case 317:
						array[2] = 71;
						num2 = 187;
						goto IL_1e5e;
					case 5:
						num18 <<= 8;
						num3 = 199;
						continue;
					case 381:
						num13 = 52 - 24;
						num2 = 388;
						goto IL_1e5e;
					case 241:
						array2[0] = 93;
						num2 = 401;
						goto IL_1e5e;
					case 84:
						array[27] = (byte)num13;
						num3 = 146;
						continue;
					case 47:
						num13 = 158 - 52;
						num = 161;
						goto end_IL_1e62;
					case 263:
						array[7] = 114;
						num2 = 282;
						if (InterruptAdapter())
						{
							goto IL_1e5e;
						}
						goto case 404;
					case 32:
						num14 = 56 + 37;
						num = 376;
						goto end_IL_1e62;
					case 441:
						array2[7] = (byte)num17;
						num = 274;
						goto end_IL_1e62;
					case 188:
						array[24] = 125;
						num2 = 203;
						if (!MapAdapter())
						{
							goto IL_1e5e;
						}
						goto case 66;
					case 409:
						array[8] = 88;
						num2 = 273;
						goto IL_1e5e;
					case 318:
						num46 = 0u;
						num3 = 442;
						continue;
					case 215:
						array[16] = 48;
						num3 = 315;
						continue;
					case 91:
						array[6] = (byte)num13;
						num = 70;
						goto end_IL_1e62;
					case 130:
						array2[12] = (byte)num17;
						num2 = 425;
						if (InterruptAdapter())
						{
							goto IL_1e5e;
						}
						goto case 119;
					case 104:
						array[8] = 46;
						num = 291;
						goto end_IL_1e62;
					case 94:
						if (num43 == num47 - 1)
						{
							num2 = 109;
							if (InterruptAdapter())
							{
								goto IL_1e5e;
							}
							goto case 339;
						}
						goto IL_2a6b;
					case 114:
						array[29] = 213;
						num2 = 239;
						goto IL_1e5e;
					case 412:
						array2[9] = (byte)num17;
						num2 = 284;
						goto IL_1e5e;
					case 183:
					case 198:
						if (num43 >= num47)
						{
							num2 = 110;
							goto IL_1e5e;
						}
						num48 = num43 % num15;
						num2 = 352;
						if (0 == 0)
						{
							goto IL_1e5e;
						}
						goto case 212;
					case 223:
						num13 = 234 - 78;
						num = 443;
						goto end_IL_1e62;
					case 308:
						num39 = 0u;
						num2 = 162;
						if (0 == 0)
						{
							goto IL_1e5e;
						}
						goto case 250;
					case 250:
						array2[4] = 169;
						num3 = 176;
						continue;
					case 288:
						array2[3] = 161;
						num = 33;
						goto end_IL_1e62;
					case 387:
						array2[6] = 164;
						num3 = 193;
						continue;
					case 49:
						array2[11] = (byte)num17;
						goto case 244;
					case 261:
						array[31] = 140;
						num = 25;
						goto end_IL_1e62;
					case 65:
						array[12] = 161;
						num2 = 58;
						if (true)
						{
							goto IL_1e5e;
						}
						goto case 233;
					case 233:
						array[4] = (byte)num13;
						num = 216;
						goto end_IL_1e62;
					case 20:
						Array.Clear(publicKeyToken, 0, publicKeyToken.Length);
						num3 = 157;
						continue;
					case 286:
						array[31] = 225;
						num3 = 159;
						continue;
					case 38:
						num14 = 118 + 58;
						num2 = 447;
						if (!MapAdapter())
						{
							goto IL_1e5e;
						}
						goto case 257;
					case 257:
						array[0] = 164;
						num3 = 252;
						continue;
					case 119:
						array[23] = 178;
						num3 = 167;
						continue;
					case 185:
						binaryReader.ReadInt32();
						num3 = 0;
						continue;
					case 220:
						array[17] = (byte)num13;
						num2 = 457;
						if (InterruptAdapter())
						{
							goto IL_1e5e;
						}
						goto case 161;
					case 161:
						array[31] = (byte)num13;
						num = 217;
						goto end_IL_1e62;
					case 395:
						array[29] = 92;
						num = 156;
						goto end_IL_1e62;
					case 292:
						num47++;
						num2 = 308;
						if (InterruptAdapter())
						{
							goto IL_1e5e;
						}
						goto case 70;
					case 70:
						array[7] = 114;
						num2 = 106;
						if (0 == 0)
						{
							goto IL_1e5e;
						}
						goto case 264;
					case 264:
						array[28] = 86;
						num2 = 320;
						if (0 == 0)
						{
							goto IL_1e5e;
						}
						goto case 31;
					case 31:
						array[18] = 110;
						num2 = 181;
						goto IL_1e5e;
					case 86:
						array[5] = (byte)num13;
						num3 = 272;
						continue;
					case 195:
						num13 = 246 - 82;
						num = 121;
						goto end_IL_1e62;
					case 309:
						array2[8] = (byte)num17;
						num = 45;
						goto end_IL_1e62;
					case 103:
						array[23] = (byte)num13;
						num3 = 223;
						continue;
					case 121:
						array[0] = (byte)num13;
						num = 136;
						goto end_IL_1e62;
					case 156:
						array[29] = 234;
						num3 = 166;
						continue;
					case 165:
						num13 = 16 + 112;
						num2 = 389;
						if (!MapAdapter())
						{
							goto IL_1e5e;
						}
						goto case 124;
					case 124:
						array[22] = 148;
						num = 175;
						goto end_IL_1e62;
					case 133:
						array[21] = 159;
						num2 = 277;
						if (0 == 0)
						{
							goto IL_1e5e;
						}
						goto case 252;
					case 252:
						array[0] = 146;
						num2 = 246;
						if (true)
						{
							goto IL_1e5e;
						}
						goto case 232;
					case 232:
						array2[11] = (byte)num14;
						num = 177;
						goto end_IL_1e62;
					case 187:
						array[3] = 170;
						num = 44;
						goto end_IL_1e62;
					case 8:
						array2[6] = 101;
						num2 = 387;
						if (!MapAdapter())
						{
							goto IL_1e5e;
						}
						goto case 213;
					case 213:
						array2[13] = (byte)num14;
						num = 154;
						goto end_IL_1e62;
					case 346:
						if (num43 != num47 - 1)
						{
							goto IL_03ab;
						}
						num2 = 336;
						if (!MapAdapter())
						{
							goto IL_1e5e;
						}
						goto case 180;
					case 169:
						num13 = 129 - 43;
						num = 332;
						goto end_IL_1e62;
					case 115:
						broadcasterWatcher = true;
						num3 = 431;
						continue;
					case 58:
						array[12] = 89;
						num3 = 427;
						continue;
					case 414:
						array[30] = (byte)num13;
						num3 = 390;
						continue;
					case 450:
						array[21] = (byte)num13;
						num3 = 225;
						continue;
					case 335:
						if (publicKeyToken.Length != 0)
						{
							num = 333;
							goto end_IL_1e62;
						}
						goto case 157;
					case 209:
						array[16] = 217;
						num3 = 460;
						continue;
					case 439:
						array2[2] = (byte)num17;
						num = 269;
						goto end_IL_1e62;
					case 249:
						array[15] = (byte)num13;
						num2 = 215;
						if (0 == 0)
						{
							goto IL_1e5e;
						}
						goto case 265;
					case 164:
						array[15] = (byte)num13;
						num2 = 452;
						if (InterruptAdapter())
						{
							goto IL_1e5e;
						}
						goto case 300;
					case 428:
						num12 = IntPtr.Zero;
						num = 102;
						goto end_IL_1e62;
					case 211:
						array2[14] = 112;
						num3 = 373;
						continue;
					case 40:
						array[11] = (byte)num13;
						num2 = 290;
						if (true)
						{
							goto IL_1e5e;
						}
						goto case 287;
					case 287:
						num14 = 187 + 38;
						num2 = 458;
						goto IL_1e5e;
					case 436:
						array7 = binaryReader.ReadBytes((int)binaryReader.BaseStream.Length);
						num2 = 281;
						if (true)
						{
							goto IL_1e5e;
						}
						goto case 160;
					case 160:
						num13 = 19 + 43;
						num3 = 227;
						continue;
					case 43:
						array2[0] = 206;
						num = 365;
						goto end_IL_1e62;
					case 306:
						array5[num20 + num40] = (byte)((num38 & num42) >> num41);
						num2 = 312;
						if (!MapAdapter())
						{
							goto IL_1e5e;
						}
						goto case 256;
					case 256:
						array[8] = (byte)num13;
						num2 = 104;
						if (true)
						{
							goto IL_1e5e;
						}
						goto case 95;
					case 35:
						array2[7] = 84;
						num3 = 32;
						continue;
					case 417:
						num14 = 220 - 73;
						num = 212;
						goto end_IL_1e62;
					case 253:
						num41 += 8;
						num2 = 306;
						if (!MapAdapter())
						{
							goto IL_1e5e;
						}
						goto case 184;
					case 184:
						num24 += num46;
						num3 = 384;
						continue;
					case 13:
						num13 = 76 + 11;
						num2 = 414;
						if (!MapAdapter())
						{
							goto IL_1e5e;
						}
						goto case 66;
					case 66:
						num13 = 30 + 37;
						num3 = 84;
						continue;
					case 348:
						array[29] = (byte)num13;
						num3 = 419;
						continue;
					case 373:
						num14 = 88 + 62;
						num2 = 238;
						if (0 == 0)
						{
							goto IL_1e5e;
						}
						goto case 354;
					case 354:
						array2[15] = 149;
						num3 = 262;
						continue;
					case 273:
						array[8] = 84;
						num2 = 171;
						goto IL_1e5e;
					case 394:
						array[3] = (byte)num13;
						num2 = 168;
						goto IL_1e5e;
					case 454:
						array[26] = (byte)num13;
						num3 = 268;
						continue;
					case 19:
						array[12] = 144;
						num2 = 4;
						if (!MapAdapter())
						{
							goto IL_1e5e;
						}
						goto case 441;
					case 332:
						array[19] = (byte)num13;
						num2 = 92;
						if (0 == 0)
						{
							goto IL_1e5e;
						}
						goto case 349;
					case 349:
						array[27] = 241;
						num = 66;
						goto end_IL_1e62;
					case 145:
						array2[3] = (byte)num17;
						num2 = 77;
						if (0 == 0)
						{
							goto IL_1e5e;
						}
						goto case 14;
					case 14:
						SetUtils(num12, num16, BitConverter.GetBytes(binaryReader.ReadInt32()), 4u, out zero);
						num2 = 79;
						goto IL_1e5e;
					case 266:
						array2[2] = (byte)num14;
						num = 37;
						goto end_IL_1e62;
					case 271:
						num14 = 96 + 107;
						num = 232;
						goto end_IL_1e62;
					case 290:
						array[11] = 128;
						num = 117;
						goto end_IL_1e62;
					case 315:
						num13 = 73 + 51;
						num2 = 243;
						if (InterruptAdapter())
						{
							goto IL_1e5e;
						}
						goto case 75;
					case 75:
						num13 = 151 - 50;
						num2 = 231;
						if (!MapAdapter())
						{
							goto IL_1e5e;
						}
						goto case 190;
					case 336:
						if (num37 <= 0)
						{
							goto IL_03ab;
						}
						num2 = 423;
						if (InterruptAdapter())
						{
							goto IL_1e5e;
						}
						goto case 407;
					case 407:
						num13 = 16 + 6;
						num = 319;
						goto end_IL_1e62;
					case 236:
						num17 = 195 - 65;
						num = 150;
						goto end_IL_1e62;
					case 159:
						array[31] = 105;
						num3 = 47;
						continue;
					case 254:
						array[11] = (byte)num13;
						num2 = 455;
						if (!MapAdapter())
						{
							goto IL_1e5e;
						}
						goto case 251;
					case 117:
						num13 = 57 - 38;
						num = 254;
						goto end_IL_1e62;
					case 360:
						array[14] = 147;
						num3 = 190;
						continue;
					case 426:
						num13 = 145 - 48;
						num2 = 220;
						if (InterruptAdapter())
						{
							goto IL_1e5e;
						}
						goto case 396;
					case 100:
						num13 = 100 + 124;
						num2 = 363;
						if (0 == 0)
						{
							goto IL_1e5e;
						}
						goto case 268;
					case 268:
						array[26] = 136;
						num2 = 405;
						goto IL_1e5e;
					case 313:
						num17 = 215 - 71;
						num3 = 412;
						continue;
					case 294:
						array2[13] = (byte)num14;
						num3 = 28;
						continue;
					case 344:
						array[5] = (byte)num13;
						num2 = 393;
						if (true)
						{
							goto IL_1e5e;
						}
						goto case 260;
					case 260:
						num17 = 157 - 52;
						num = 9;
						goto end_IL_1e62;
					case 142:
						array[4] = 98;
						num = 345;
						goto end_IL_1e62;
					case 333:
						array4[1] = publicKeyToken[0];
						num = 300;
						goto end_IL_1e62;
					case 168:
						array[3] = 198;
						num3 = 420;
						continue;
					case 234:
						num45++;
						num = 299;
						goto end_IL_1e62;
					case 361:
						array[20] = (byte)num13;
						num3 = 133;
						continue;
					case 320:
						array[29] = 234;
						num = 114;
						goto end_IL_1e62;
					case 138:
						array[8] = (byte)num13;
						num2 = 297;
						if (true)
						{
							goto IL_1e5e;
						}
						goto case 90;
					case 90:
						array[25] = (byte)num13;
						num2 = 46;
						if (!MapAdapter())
						{
							goto IL_1e5e;
						}
						goto case 410;
					case 410:
						num17 = 39 + 56;
						num3 = 441;
						continue;
					case 131:
						num13 = 120 + 15;
						num2 = 327;
						goto IL_1e5e;
					case 191:
						num44++;
						num3 = 265;
						continue;
					case 64:
						array[17] = (byte)num13;
						num3 = 426;
						continue;
					case 284:
						array2[9] = 116;
						num = 214;
						goto end_IL_1e62;
					case 411:
						num17 = 132 - 44;
						num3 = 145;
						continue;
					case 109:
						if (num37 > 0)
						{
							num = 26;
							goto end_IL_1e62;
						}
						goto IL_2a6b;
					case 21:
					case 299:
						if (num45 >= array4.Length)
						{
							num3 = 108;
							continue;
						}
						array3[num45] ^= array4[num45];
						num2 = 234;
						if (!MapAdapter())
						{
							goto IL_1e5e;
						}
						goto case 73;
					case 78:
						num13 = 160 - 53;
						num2 = 86;
						if (InterruptAdapter())
						{
							goto IL_1e5e;
						}
						goto case 38;
					case 418:
						array[30] = (byte)num13;
						num2 = 391;
						goto IL_1e5e;
					case 7:
					case 359:
						num43++;
						num3 = 198;
						continue;
					case 102:
					{
						Assembly assembly = Type.GetTypeFromHandle(QueueDefinitionFilter.e53w34m968awCm9P85taUZe(33554650)).Assembly;
						num12 = DisableUtils(56u, 1, (uint)Process.GetCurrentProcess().Id);
						hINSTANCE = Marshal.GetHINSTANCE(assembly.GetModules()[0]);
						num = 148;
						goto end_IL_1e62;
					}
					case 425:
						array2[12] = 111;
						num = 53;
						goto end_IL_1e62;
					case 399:
						array2[7] = (byte)num17;
						num2 = 461;
						if (0 == 0)
						{
							goto IL_1e5e;
						}
						goto case 416;
					case 416:
						num17 = 223 - 74;
						num = 351;
						goto end_IL_1e62;
					case 146:
						array[27] = 109;
						num3 = 68;
						continue;
					case 154:
						array2[13] = 100;
						num2 = 446;
						if (InterruptAdapter())
						{
							goto IL_1e5e;
						}
						goto case 229;
					case 282:
						array[8] = 72;
						num3 = 409;
						continue;
					case 265:
					case 430:
						if (num44 < num37)
						{
							if (num44 <= 0)
							{
								goto case 199;
							}
							num2 = 5;
							if (!MapAdapter())
							{
								goto IL_1e5e;
							}
							goto case 69;
						}
						num = 16;
						goto end_IL_1e62;
					case 174:
						array[2] = 71;
						num = 125;
						goto end_IL_1e62;
					case 240:
						array[19] = 234;
						num2 = 169;
						if (true)
						{
							goto IL_1e5e;
						}
						goto case 85;
					case 85:
						array2[11] = (byte)num17;
						num = 116;
						goto end_IL_1e62;
					case 242:
						array[1] = 137;
						num2 = 29;
						if (true)
						{
							goto IL_1e5e;
						}
						goto case 452;
					case 452:
						num13 = 3 + 53;
						num3 = 2;
						continue;
					case 431:
						binaryReader = new BinaryReader(Type.GetTypeFromHandle(QueueDefinitionFilter.e53w34m968awCm9P85taUZe(33554650)).Assembly.GetManifestResourceStream("56ca8863-e352-4f3f-bebc-b159812e86be"));
						num = 374;
						goto end_IL_1e62;
					case 163:
						num13 = 118 + 87;
						num3 = 40;
						continue;
					case 279:
						array[22] = 133;
						num = 408;
						goto end_IL_1e62;
					case 132:
						num13 = 106 + 72;
						num2 = 325;
						goto IL_1e5e;
					case 382:
						array[19] = 85;
						num3 = 89;
						continue;
					case 435:
						array[10] = 152;
						num2 = 381;
						if (0 == 0)
						{
							goto IL_1e5e;
						}
						goto case 457;
					case 457:
						array[17] = 132;
						num3 = 52;
						continue;
					case 208:
						array[11] = 19;
						num2 = 163;
						goto IL_1e5e;
					case 324:
						num24 = 0u;
						num = 318;
						goto end_IL_1e62;
					case 81:
						array[7] = (byte)num13;
						num3 = 341;
						continue;
					case 443:
						array[23] = (byte)num13;
						num2 = 456;
						if (0 == 0)
						{
							goto IL_1e5e;
						}
						goto case 206;
					case 206:
						num13 = 98 - 14;
						num3 = 361;
						continue;
					case 62:
						array[12] = (byte)num13;
						num = 65;
						goto end_IL_1e62;
					case 37:
						num17 = 130 - 43;
						num3 = 439;
						continue;
					case 370:
						array2[13] = (byte)num17;
						num2 = 30;
						if (InterruptAdapter())
						{
							goto IL_1e5e;
						}
						goto case 328;
					case 352:
						num20 = num43 * 4;
						num2 = 105;
						if (!MapAdapter())
						{
							goto IL_1e5e;
						}
						goto case 340;
					case 136:
						num13 = 164 - 54;
						num2 = 397;
						if (0 == 0)
						{
							goto IL_1e5e;
						}
						goto case 89;
					case 89:
						num13 = 231 + 3;
						num3 = 11;
						continue;
					case 406:
						num9 = 0;
						num = 424;
						goto end_IL_1e62;
					case 433:
						num42 <<= 8;
						num = 253;
						goto end_IL_1e62;
					case 372:
						array[4] = (byte)num13;
						num2 = 100;
						goto IL_1e5e;
					case 402:
						num13 = 112 + 116;
						num3 = 249;
						continue;
					case 76:
						num41 = 0;
						num2 = 346;
						if (true)
						{
							goto IL_1e5e;
						}
						goto case 419;
					case 419:
						array[29] = 168;
						goto case 395;
					default:
						num2 = 395;
						goto IL_1e5e;
					case 325:
						array[12] = (byte)num13;
						num3 = 19;
						continue;
					case 447:
						array2[0] = (byte)num14;
						num = 241;
						goto end_IL_1e62;
					case 203:
						array[24] = 98;
						num3 = 421;
						continue;
					case 175:
						array[22] = 102;
						num3 = 197;
						continue;
					case 189:
						array[9] = 134;
						num = 311;
						goto end_IL_1e62;
					case 334:
						array[20] = (byte)num13;
						num = 369;
						goto end_IL_1e62;
					case 230:
						array2[1] = (byte)num17;
						num2 = 226;
						goto IL_1e5e;
					case 228:
						num13 = 96 + 15;
						num3 = 51;
						continue;
					case 390:
						num13 = 158 - 52;
						num = 179;
						goto end_IL_1e62;
					case 403:
						array[2] = 156;
						num2 = 357;
						goto IL_1e5e;
					case 437:
						num13 = 118 + 56;
						num2 = 17;
						if (true)
						{
							goto IL_1e5e;
						}
						goto case 224;
					case 224:
						array2[1] = 104;
						num2 = 210;
						goto IL_1e5e;
					case 445:
						num17 = 254 - 84;
						num2 = 295;
						goto IL_1e5e;
					case 122:
						num17 = 94 + 4;
						num3 = 309;
						continue;
					case 368:
						array[6] = 151;
						num2 = 283;
						if (!MapAdapter())
						{
							goto IL_1e5e;
						}
						goto case 2;
					case 2:
						array[15] = (byte)num13;
						num3 = 402;
						continue;
					case 181:
						array[18] = 116;
						num3 = 80;
						continue;
					case 278:
						array[17] = 143;
						num2 = 378;
						goto IL_1e5e;
					case 17:
						array[25] = (byte)num13;
						num3 = 196;
						continue;
					case 385:
						array[9] = 177;
						num = 180;
						goto end_IL_1e62;
					case 166:
						array[30] = 104;
						num2 = 112;
						if (InterruptAdapter())
						{
							goto IL_1e5e;
						}
						goto case 379;
					case 312:
						num40++;
						num2 = 143;
						if (!MapAdapter())
						{
							goto IL_1e5e;
						}
						goto case 16;
					case 322:
						array[16] = (byte)num13;
						num2 = 209;
						goto IL_1e5e;
					case 3:
						num13 = 100 + 34;
						num2 = 36;
						goto IL_1e5e;
					case 201:
						array2[8] = 57;
						num3 = 139;
						continue;
					case 302:
						num17 = 47 + 34;
						num2 = 49;
						if (true)
						{
							goto IL_1e5e;
						}
						goto case 157;
					case 157:
						num45 = 0;
						num2 = 21;
						goto IL_1e5e;
					case 251:
						array2[4] = 164;
						num2 = 364;
						if (!MapAdapter())
						{
							goto IL_1e5e;
						}
						goto case 27;
					case 461:
						num14 = 58 - 47;
						_ = 0;
						if (!InterruptAdapter())
						{
							num2 = 244;
							if (!MapAdapter())
							{
								goto IL_1e5e;
							}
							goto case 261;
						}
						num2 = 258;
						if (!MapAdapter())
						{
							goto IL_1e5e;
						}
						goto case 384;
					case 384:
						num18 = (uint)((array6[num39 + 3] << 24) | (array6[num39 + 2] << 16) | (array6[num39 + 1] << 8) | array6[num39]);
						num2 = 314;
						goto IL_1e5e;
					case 116:
						num17 = 192 - 64;
						num2 = 144;
						goto IL_1e5e;
					case 316:
						num13 = 92 + 5;
						num = 394;
						goto end_IL_1e62;
					case 170:
						publicKeyToken = Type.GetTypeFromHandle(QueueDefinitionFilter.e53w34m968awCm9P85taUZe(33554650)).Assembly.GetName().GetPublicKeyToken();
						num2 = 88;
						goto IL_1e5e;
					case 244:
					case 337:
						num17 = 103 + 17;
						num3 = 85;
						continue;
					case 380:
						array2[10] = 254;
						num = 302;
						goto end_IL_1e62;
					case 303:
						array2[2] = 131;
						num = 236;
						goto end_IL_1e62;
					case 199:
						num18 |= array6[^(1 + num44)];
						num3 = 191;
						continue;
					case 397:
						array[0] = (byte)num13;
						num = 257;
						goto end_IL_1e62;
					case 222:
						array[27] = 86;
						num = 276;
						goto end_IL_1e62;
					case 453:
						Array.Reverse(array4);
						num2 = 170;
						goto IL_1e5e;
					case 68:
						array[27] = 105;
						num2 = 222;
						if (!MapAdapter())
						{
							goto IL_1e5e;
						}
						goto case 26;
					case 151:
						array2[14] = 85;
						num3 = 211;
						continue;
					case 427:
						array[13] = 197;
						num2 = 72;
						goto IL_1e5e;
					case 379:
						array[14] = 26;
						num3 = 360;
						continue;
					case 408:
						array[22] = 165;
						num3 = 329;
						continue;
					case 229:
						num44 = 0;
						num2 = 430;
						if (true)
						{
							goto IL_1e5e;
						}
						goto case 396;
					case 396:
						num14 = 178 - 59;
						num3 = 392;
						continue;
					case 44:
						array[3] = 126;
						num3 = 59;
						continue;
					case 434:
						if (num37 > 0)
						{
							num = 292;
							goto end_IL_1e62;
						}
						goto case 308;
					case 270:
						num19++;
						num2 = 463;
						if (true)
						{
							goto IL_1e5e;
						}
						goto case 134;
					case 134:
						num18 = 0u;
						num2 = 229;
						if (InterruptAdapter())
						{
							goto IL_1e5e;
						}
						goto case 93;
					case 83:
						array2[6] = 77;
						num2 = 35;
						if (true)
						{
							goto IL_1e5e;
						}
						goto case 10;
					case 10:
						array[17] = (byte)num13;
						num3 = 56;
						continue;
					case 328:
						num17 = 221 - 73;
						num = 449;
						goto end_IL_1e62;
					case 129:
						array[6] = 139;
						num3 = 42;
						continue;
					case 371:
						array[28] = 148;
						num3 = 235;
						continue;
					case 259:
						array4[13] = publicKeyToken[6];
						num2 = 137;
						goto IL_1e5e;
					case 247:
						array2 = new byte[16];
						num2 = 38;
						if (true)
						{
							goto IL_1e5e;
						}
						goto case 398;
					case 398:
						array[18] = 45;
						num2 = 31;
						if (InterruptAdapter())
						{
							goto IL_1e5e;
						}
						goto case 374;
					case 281:
						array = new byte[32];
						num3 = 120;
						continue;
					case 330:
						num13 = 36 + 103;
						num2 = 91;
						if (true)
						{
							goto IL_1e5e;
						}
						goto case 421;
					case 421:
						array[24] = 171;
						num2 = 207;
						if (true)
						{
							goto IL_1e5e;
						}
						goto case 22;
					case 22:
						num14 = 170 - 56;
						num2 = 305;
						if (InterruptAdapter())
						{
							goto IL_1e5e;
						}
						goto case 238;
					case 4:
						num13 = 157 - 52;
						num3 = 62;
						continue;
					case 246:
						array[0] = 168;
						num2 = 96;
						if (0 == 0)
						{
							goto IL_1e5e;
						}
						goto case 293;
					case 293:
						if (!broadcasterWatcher)
						{
							num2 = 115;
							if (InterruptAdapter())
							{
								goto IL_1e5e;
							}
							goto case 406;
						}
						return;
					case 69:
						array2[12] = 108;
						num2 = 255;
						goto IL_1e5e;
					case 135:
						array2[6] = (byte)num17;
						num = 83;
						goto end_IL_1e62;
					case 342:
					{
						uint num23 = num24;
						uint num25 = num24;
						uint num26 = 399522727u;
						uint num27 = 1175363962u;
						uint num28 = 656276816u;
						uint num29 = 297323369u;
						uint num30 = num25;
						uint num31 = 1356102888u;
						ulong num32 = num27 * 371293044;
						num32 |= 1;
						num29 = (uint)(num29 * num29 % num32);
						uint num33 = ((num28 >> 5) | (num28 << 27)) + num26;
						uint num34 = num33 & 0x55555555;
						num33 &= 0xAAAAAAAAu;
						num28 = (num33 >> 1) | (num34 << 1);
						if ((double)num26 == 0.0)
						{
							num26--;
						}
						uint num35 = (uint)(64079.0 / (double)num26 + (double)num26);
						num26 = (uint)((uint)((short)num29 + (ushort)num29 + (int)num35) + (short)num29);
						num27 += num29;
						ulong num36 = num29 * num29;
						if (num36 == 0)
						{
							num36--;
						}
						num31 = (uint)(num31 * num31 % num36);
						num30 ^= num30 << 9;
						num30 += num26;
						num30 ^= num30 >> 21;
						num30 += num27;
						num30 ^= num30 << 2;
						num30 += num31;
						num30 = (((num29 << 6) + num29) ^ num27) + num30;
						num24 = num23 + (uint)(double)num30;
						num2 = 94;
						goto IL_1e5e;
					}
					case 375:
						array5 = new byte[array6.Length];
						num3 = 326;
						continue;
					case 319:
						array[18] = (byte)num13;
						num = 400;
						goto end_IL_1e62;
					case 262:
						array2[15] = 100;
						num2 = 6;
						if (InterruptAdapter())
						{
							goto IL_1e5e;
						}
						goto case 411;
					case 272:
						num13 = 129 - 43;
						num2 = 344;
						if (true)
						{
							goto IL_1e5e;
						}
						goto case 143;
					case 143:
					case 149:
						if (num40 < num37)
						{
							if (num40 <= 0)
							{
								goto case 306;
							}
							num2 = 433;
							if (InterruptAdapter())
							{
								goto IL_1e5e;
							}
							goto case 41;
						}
						num3 = 359;
						continue;
					case 311:
						array[9] = 136;
						num = 385;
						goto end_IL_1e62;
					case 158:
						zero = IntPtr.Zero;
						num3 = 406;
						continue;
					case 18:
						array[21] = (byte)num13;
						num2 = 298;
						goto IL_1e5e;
					case 446:
						num14 = 135 - 45;
						num2 = 294;
						if (true)
						{
							goto IL_1e5e;
						}
						goto case 71;
					case 71:
						array2[4] = 77;
						num = 82;
						goto end_IL_1e62;
					case 111:
						array2[10] = 74;
						num2 = 380;
						if (!MapAdapter())
						{
							goto IL_1e5e;
						}
						goto case 451;
					case 451:
						array[20] = (byte)num13;
						num2 = 165;
						if (true)
						{
							goto IL_1e5e;
						}
						goto case 226;
					case 226:
						num14 = 10 + 39;
						num = 140;
						goto end_IL_1e62;
					case 393:
						array[5] = 142;
						num = 48;
						goto end_IL_1e62;
					case 1:
						array[10] = 136;
						num3 = 435;
						continue;
					case 61:
						array[31] = 225;
						num2 = 128;
						if (InterruptAdapter())
						{
							goto IL_1e5e;
						}
						goto case 424;
					case 424:
						num22 = binaryReader.ReadInt32();
						num2 = 185;
						goto IL_1e5e;
					case 365:
						array2[1] = 137;
						num2 = 224;
						if (0 == 0)
						{
							goto IL_1e5e;
						}
						goto case 364;
					case 364:
						array2[4] = 92;
						num = 71;
						goto end_IL_1e62;
					case 367:
						array5[num20 + 3] = (byte)((num21 & 0xFF000000u) >> 24);
						num3 = 7;
						continue;
					case 48:
						array[5] = 108;
						num3 = 444;
						continue;
					case 23:
						array[27] = (byte)num13;
						num2 = 123;
						goto IL_1e5e;
					case 141:
						array[0] = 72;
						num2 = 195;
						if (!MapAdapter())
						{
							goto IL_1e5e;
						}
						goto case 429;
					case 429:
						array[25] = 174;
						num = 350;
						goto end_IL_1e62;
					case 126:
						array[19] = (byte)num13;
						num2 = 382;
						goto IL_1e5e;
					case 276:
						num13 = 187 + 54;
						num3 = 23;
						continue;
					case 357:
						array[2] = 128;
						num2 = 317;
						goto IL_1e5e;
					case 329:
						array[23] = 200;
						num = 285;
						goto end_IL_1e62;
					case 128:
						array3 = array;
						num3 = 247;
						continue;
					case 400:
						array[18] = 45;
						num3 = 240;
						continue;
					case 455:
						array[12] = 89;
						num2 = 202;
						goto IL_1e5e;
					case 362:
						array5[num20 + 1] = (byte)((num21 & 0xFF00) >> 8);
						num3 = 74;
						continue;
					case 107:
						num13 = 246 - 82;
						num2 = 64;
						if (!MapAdapter())
						{
							goto IL_1e5e;
						}
						goto case 195;
					case 212:
						array2[12] = (byte)num14;
						num3 = 69;
						continue;
					case 404:
						num17 = 212 - 70;
						num3 = 370;
						continue;
					case 33:
						array2[3] = 115;
						num = 411;
						goto end_IL_1e62;
					case 53:
						array2[12] = 195;
						num = 404;
						goto end_IL_1e62;
					case 217:
						num13 = 203 - 67;
						num = 237;
						goto end_IL_1e62;
					case 345:
						array[4] = 124;
						num = 118;
						goto end_IL_1e62;
					case 167:
						num13 = 146 - 48;
						num3 = 103;
						continue;
					case 401:
						array2[0] = 206;
						num2 = 445;
						goto IL_1e5e;
					case 239:
						array[29] = 102;
						num3 = 432;
						continue;
					case 11:
						array[19] = (byte)num13;
						num = 113;
						goto end_IL_1e62;
					case 255:
						array2[12] = 119;
						num2 = 172;
						if (InterruptAdapter())
						{
							goto IL_1e5e;
						}
						goto case 338;
					case 338:
						num13 = 39 + 66;
						num = 192;
						goto end_IL_1e62;
					case 331:
						array[14] = 161;
						num = 383;
						goto end_IL_1e62;
					case 238:
						array2[14] = (byte)num14;
						num = 386;
						goto end_IL_1e62;
					case 258:
					case 310:
						array2[7] = (byte)num14;
						num3 = 396;
						continue;
					case 214:
						num17 = 184 - 63;
						num2 = 323;
						goto IL_1e5e;
					case 383:
						array[14] = 26;
						num2 = 41;
						if (0 == 0)
						{
							goto IL_1e5e;
						}
						goto case 24;
					case 24:
						array2[8] = (byte)num17;
						num2 = 260;
						if (InterruptAdapter())
						{
							goto IL_1e5e;
						}
						goto case 201;
					case 106:
						num13 = 240 - 80;
						num2 = 87;
						goto IL_1e5e;
					case 194:
					case 463:
						break;
					case 98:
						array4 = array2;
						num2 = 453;
						goto IL_1e5e;
					case 144:
						array2[11] = (byte)num17;
						num3 = 422;
						continue;
					case 77:
						array2[3] = 50;
						num3 = 415;
						continue;
					case 225:
						array[22] = 165;
						num2 = 124;
						if (!MapAdapter())
						{
							goto IL_1e5e;
						}
						goto case 0;
					case 0:
						num19 = 0;
						num3 = 194;
						continue;
					case 448:
						num17 = 20 + 121;
						num2 = 24;
						if (0 == 0)
						{
							goto IL_1e5e;
						}
						goto case 449;
					case 449:
						array2[15] = (byte)num17;
						num2 = 287;
						if (InterruptAdapter())
						{
							goto IL_1e5e;
						}
						goto case 99;
					case 67:
						num13 = 57 + 102;
						num3 = 450;
						continue;
					case 28:
						array2[13] = 158;
						num3 = 459;
						continue;
					case 50:
						array[24] = 70;
						num3 = 188;
						continue;
					case 190:
						array[14] = 151;
						num3 = 331;
						continue;
					case 27:
						num37 = array6.Length % 4;
						num3 = 355;
						continue;
					case 304:
						array2[14] = 138;
						num2 = 205;
						goto IL_1e5e;
					case 180:
						array[10] = 28;
						num2 = 1;
						if (true)
						{
							goto IL_1e5e;
						}
						goto case 108;
					case 108:
						array6 = array7;
						num = 27;
						goto end_IL_1e62;
					case 285:
						array[23] = 193;
						num = 119;
						goto end_IL_1e62;
					case 112:
						num13 = 88 + 50;
						num = 418;
						goto end_IL_1e62;
					case 442:
						num18 = 0u;
						num = 434;
						goto end_IL_1e62;
					case 462:
						array2[5] = (byte)num14;
						num2 = 8;
						if (!MapAdapter())
						{
							goto IL_1e5e;
						}
						goto case 109;
					case 113:
						array[20] = 84;
						num3 = 377;
						continue;
					case 173:
						num14 = 127 - 42;
						num2 = 266;
						goto IL_1e5e;
					case 369:
						num13 = 82 + 44;
						num2 = 451;
						goto IL_1e5e;
					case 123:
						array[28] = 86;
						num = 15;
						goto end_IL_1e62;
					case 301:
						array2[14] = (byte)num14;
						num = 354;
						goto end_IL_1e62;
					case 29:
						array[1] = 116;
						num2 = 34;
						goto IL_1e5e;
					case 52:
						num13 = 85 + 105;
						num3 = 10;
						continue;
					case 41:
						array[15] = 228;
						num = 338;
						goto end_IL_1e62;
					case 139:
						array2[9] = 101;
						num2 = 22;
						if (InterruptAdapter())
						{
							goto IL_1e5e;
						}
						goto case 425;
					case 55:
						array2[10] = 135;
						num3 = 416;
						continue;
					case 243:
						array[16] = (byte)num13;
						num2 = 39;
						goto IL_1e5e;
					case 12:
						num13 = 31 + 100;
						num = 334;
						goto end_IL_1e62;
					case 413:
						array2[5] = 88;
						num2 = 267;
						goto IL_1e5e;
					case 72:
						array[13] = 84;
						num = 228;
						goto end_IL_1e62;
					case 9:
						array2[8] = (byte)num17;
						num2 = 201;
						if (0 == 0)
						{
							goto IL_1e5e;
						}
						goto case 440;
					case 440:
						array[9] = (byte)num13;
						num3 = 189;
						continue;
					case 343:
						array[15] = 66;
						num = 99;
						goto end_IL_1e62;
					case 16:
					case 314:
						num24 = num24;
						num2 = 342;
						if (0 == 0)
						{
							goto IL_1e5e;
						}
						goto case 295;
					case 295:
						array2[0] = (byte)num17;
						num = 147;
						goto end_IL_1e62;
					case 307:
						num13 = 222 - 74;
						num3 = 186;
						continue;
					case 376:
						array2[7] = (byte)num14;
						num = 410;
						goto end_IL_1e62;
					case 389:
						array[20] = (byte)num13;
						num3 = 206;
						continue;
					case 45:
						array2[8] = 168;
						num3 = 448;
						continue;
					case 237:
						array[31] = (byte)num13;
						num2 = 261;
						if (true)
						{
							goto IL_1e5e;
						}
						goto case 347;
					case 347:
						array[5] = (byte)num13;
						num2 = 78;
						if (0 == 0)
						{
							goto IL_1e5e;
						}
						goto case 79;
					case 79:
					case 221:
						OrderUtils(num16, 4, num9, ref num9);
						num2 = 270;
						if (0 == 0)
						{
							goto IL_1e5e;
						}
						goto case 388;
					case 388:
						array[10] = (byte)num13;
						num3 = 208;
						continue;
					case 459:
						array2[13] = 77;
						num3 = 151;
						continue;
					case 415:
						array2[4] = 130;
						num3 = 251;
						continue;
					case 205:
						num14 = 108 - 23;
						num2 = 301;
						goto IL_1e5e;
					case 374:
						binaryReader.BaseStream.Position = 0L;
						num3 = 436;
						continue;
					case 291:
						num13 = 133 - 61;
						num2 = 138;
						goto IL_1e5e;
					case 39:
						num13 = 193 - 64;
						num2 = 322;
						if (true)
						{
							goto IL_1e5e;
						}
						goto case 326;
					case 326:
						num15 = array3.Length / 4;
						num2 = 324;
						if (true)
						{
							goto IL_1e5e;
						}
						goto case 277;
					case 277:
						num13 = 37 + 25;
						num2 = 18;
						if (true)
						{
							goto IL_1e5e;
						}
						goto case 127;
					case 127:
						array[26] = 191;
						num2 = 349;
						if (0 == 0)
						{
							goto IL_1e5e;
						}
						goto case 192;
					case 192:
						array[15] = (byte)num13;
						num3 = 343;
						continue;
					case 140:
						array2[2] = (byte)num14;
						num = 303;
						goto end_IL_1e62;
					case 350:
						num13 = 60 + 82;
						num3 = 90;
						continue;
					case 200:
						array[7] = (byte)num13;
						num = 160;
						goto end_IL_1e62;
					case 358:
						binaryReader.BaseStream.Position = 0L;
						num2 = 428;
						goto IL_1e5e;
					case 30:
						num14 = 239 - 79;
						num = 213;
						goto end_IL_1e62;
					case 99:
						num13 = 225 - 75;
						num2 = 164;
						if (InterruptAdapter())
						{
							goto IL_1e5e;
						}
						goto case 183;
					case 392:
						array2[8] = (byte)num14;
						num2 = 122;
						if (0 == 0)
						{
							goto IL_1e5e;
						}
						goto case 120;
					case 120:
						array[0] = 168;
						num2 = 141;
						goto IL_1e5e;
					case 96:
						array[1] = 95;
						num3 = 242;
						continue;
					case 341:
						num13 = 196 - 65;
						num2 = 200;
						if (!MapAdapter())
						{
							goto IL_1e5e;
						}
						goto case 321;
					case 321:
						num13 = 11 + 3;
						num3 = 440;
						continue;
					case 202:
						array[12] = 84;
						num2 = 132;
						goto IL_1e5e;
					case 460:
						array[16] = 48;
						num = 278;
						goto end_IL_1e62;
					case 465:
						try
						{
							while (binaryReader.BaseStream.Position < binaryReader.BaseStream.Length - 1)
							{
								_ = 0;
								int num4;
								if (InterruptAdapter())
								{
									num4 = 6;
									goto IL_3de8;
								}
								int num5 = 8;
								goto IL_3de4;
								IL_3de8:
								while (true)
								{
									int num10;
									switch (num4)
									{
									case 11:
										break;
									case 4:
										num7 = new IntPtr(m_RepositoryWatcher + num11);
										num10 = 10;
										goto IL_3de0;
									case 3:
										num6 = 0;
										goto default;
									case 7:
										OrderUtils(num7, num8 * 4, 4, ref num9);
										num5 = 3;
										if (InterruptAdapter())
										{
											goto IL_3de4;
										}
										goto default;
									default:
										if (num6 >= num8)
										{
											num4 = 1;
											continue;
										}
										Marshal.WriteInt32(new IntPtr(((IntPtr)num7).ToInt64() + num6 * 4), binaryReader.ReadInt32());
										num5 = 9;
										goto IL_3de4;
									case 10:
										num8 = binaryReader.ReadInt32();
										num5 = 7;
										if (true)
										{
											goto IL_3de4;
										}
										goto case 0;
									case 0:
									case 6:
										num11 = binaryReader.ReadInt32();
										num4 = 4;
										continue;
									case 1:
										OrderUtils(num7, num8 * 4, num9, ref num9);
										num10 = 11;
										goto IL_3de0;
									case 9:
										{
											num6++;
											num5 = 2;
											if (0 == 0)
											{
												goto IL_3de4;
											}
											goto default;
										}
										IL_3de0:
										num5 = num10;
										goto IL_3de4;
									}
									break;
								}
								continue;
								IL_3de4:
								num4 = num5;
								goto IL_3de8;
							}
							ChangeUtils(num12);
							return;
						}
						catch
						{
							return;
						}
					case 95:
						{
							if (IntPtr.Size == 4)
							{
								num3 = 14;
								continue;
							}
							SetUtils(num12, num16, BitConverter.GetBytes(binaryReader.ReadInt32()), 4u, out zero);
							num2 = 221;
							if (true)
							{
								goto IL_1e5e;
							}
							goto case 319;
						}
						IL_2a6b:
						num21 = num24 ^ num18;
						num3 = 155;
						continue;
					}
					if (num19 >= num22)
					{
						num3 = 465;
						continue;
					}
					num16 = new IntPtr(m_RepositoryWatcher + binaryReader.ReadInt32());
					num3 = 289;
					continue;
					IL_03ab:
					num39 = (uint)num20;
					num = 184;
					break;
					continue;
					end_IL_1e62:
					break;
				}
				break;
			}
		}
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static object CalcUtils(object P_0)
	{
		try
		{
			if (File.Exists(((Assembly)P_0).Location))
			{
				return ((Assembly)P_0).Location;
			}
		}
		catch
		{
		}
		try
		{
			if (File.Exists(((Assembly)P_0).GetName().CodeBase.ToString().Replace("file:///", "")))
			{
				return ((Assembly)P_0).GetName().CodeBase.ToString().Replace("file:///", "");
			}
		}
		catch
		{
		}
		try
		{
			if (File.Exists(P_0.GetType().GetProperty("Location").GetValue(P_0, new object[0])
				.ToString()))
			{
				return P_0.GetType().GetProperty("Location").GetValue(P_0, new object[0])
					.ToString();
			}
		}
		catch
		{
		}
		return "";
	}

	[DllImport("kernel32.dll", EntryPoint = "WriteProcessMemory")]
	private static extern int SetUtils(nint P_0, nint P_1, [In][Out] byte[] P_2, uint P_3, out nint P_4);

	[DllImport("kernel32.dll", EntryPoint = "ReadProcessMemory")]
	private static extern int MapUtils(nint P_0, nint P_1, [In][Out] byte[] P_2, uint P_3, out nint P_4);

	[DllImport("kernel32.dll", EntryPoint = "OpenProcess")]
	private static extern nint DisableUtils(uint P_0, int P_1, uint P_2);

	[DllImport("kernel32.dll", EntryPoint = "CloseHandle")]
	private static extern int ChangeUtils(nint P_0);

	[MethodImpl(MethodImplOptions.NoInlining)]
	private static byte[] DestroyUtils(object P_0)
	{
		using FileStream fileStream = new FileStream((string)P_0, FileMode.Open, FileAccess.Read, FileShare.Read);
		int num = 0;
		int num2 = (int)fileStream.Length;
		byte[] array = new byte[num2];
		while (num2 > 0)
		{
			int num3 = fileStream.Read(array, num, num2);
			num += num3;
			num2 -= num3;
		}
		return array;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private static byte[] InsertUtils(object P_0)
	{
		MemoryStream memoryStream = new MemoryStream();
		SymmetricAlgorithm symmetricAlgorithm = CompareUtils();
		symmetricAlgorithm.Key = new byte[32]
		{
			247, 127, 9, 223, 214, 108, 55, 220, 127, 21,
			105, 10, 152, 11, 49, 106, 232, 249, 164, 129,
			160, 186, 38, 106, 44, 217, 10, 173, 121, 2,
			33, 169
		};
		symmetricAlgorithm.IV = new byte[16]
		{
			222, 199, 57, 223, 217, 172, 110, 162, 51, 33,
			225, 113, 245, 127, 83, 195
		};
		CryptoStream cryptoStream = new CryptoStream(memoryStream, symmetricAlgorithm.CreateDecryptor(), CryptoStreamMode.Write);
		cryptoStream.Write((byte[])P_0, 0, ((Array)P_0).Length);
		cryptoStream.Close();
		return memoryStream.ToArray();
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private byte[] AssetUtils()
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private byte[] ListUtils()
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private byte[] ValidateUtils()
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private byte[] MoveUtils()
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private byte[] AwakeUtils()
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private byte[] RateUtils()
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal byte[] PostUtils()
	{
		_ = "{11111-22222-40001-00001}".Length;
		_ = 0;
		return new byte[2] { 1, 2 };
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal byte[] GetUtils()
	{
		_ = "{11111-22222-40001-00002}".Length;
		_ = 0;
		return new byte[2] { 1, 2 };
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal byte[] TestUtils()
	{
		_ = "{11111-22222-50001-00001}".Length;
		_ = 0;
		return new byte[2] { 1, 2 };
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal byte[] CalculateUtils()
	{
		_ = "{11111-22222-50001-00002}".Length;
		_ = 0;
		return new byte[2] { 1, 2 };
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal byte[] StopUtils()
	{
		_ = "{11111-22222-60001-00001}".Length;
		_ = 0;
		return new byte[2] { 1, 2 };
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal byte[] FillUtils()
	{
		_ = "{11111-22222-60001-00002}".Length;
		_ = 0;
		return new byte[2] { 1, 2 };
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static string EnableUtils(object P_0, object P_1)
	{
		byte[] bytes = Encoding.Unicode.GetBytes((string)P_0);
		byte[] key = new byte[32]
		{
			82, 102, 104, 110, 32, 77, 24, 34, 118, 181,
			51, 17, 18, 51, 12, 109, 10, 32, 77, 24,
			34, 158, 161, 41, 97, 28, 118, 181, 5, 25,
			1, 88
		};
		byte[] iV = RegisterUtils(Encoding.Unicode.GetBytes((string)P_1));
		MemoryStream memoryStream = new MemoryStream();
		SymmetricAlgorithm symmetricAlgorithm = CompareUtils();
		symmetricAlgorithm.Key = key;
		symmetricAlgorithm.IV = iV;
		CryptoStream cryptoStream = new CryptoStream(memoryStream, symmetricAlgorithm.CreateEncryptor(), CryptoStreamMode.Write);
		cryptoStream.Write(bytes, 0, bytes.Length);
		cryptoStream.Close();
		return Convert.ToBase64String(memoryStream.ToArray());
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public IssuerWatcherWriter()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool ValidateService()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool ConnectService()
	{
		return false;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool WriteService()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool StartService()
	{
		return false;
	}

	internal static bool InterruptAdapter()
	{
		return true;
	}

	internal static bool MapAdapter()
	{
		return false;
	}
}
