using System;
using System.Containers;
using System.Diagnostics;
using System.IO;
using System.Reflection;
using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;
using System.Security.Cryptography;
using System.Text;

namespace Onyx.Distribution.APIs.Filter;

internal class Decorator
{
	internal class ReaderRulesStatus : Attribute
	{
		internal class SchemaSpecificationResolver<T>
		{
			[MethodImpl(MethodImplOptions.NoInlining)]
			public SchemaSpecificationResolver()
			{
			}

			[MethodImpl(MethodImplOptions.NoInlining)]
			internal static bool PrepareObserver()
			{
				return true;
			}

			[MethodImpl(MethodImplOptions.NoInlining)]
			internal static bool FlushObserver()
			{
				return true;
			}

			static SchemaSpecificationResolver()
			{
				Decorator.EnablePage();
			}
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		[ReaderRulesStatus(typeof(SchemaSpecificationResolver<object>[]))]
		public ReaderRulesStatus(object P_0)
		{
		}

		static ReaderRulesStatus()
		{
			Decorator.EnablePage();
		}
	}

	[Flags]
	private enum FontSize
	{

	}

	private static bool _Container;

	private static bool value;

	private static long _Adapter;

	private static object _Attr;

	private static object _Message;

	private static int test;

	private static object m_Service;

	private static nint initializer;

	private static object candidate;

	private static bool _Expression;

	private static object _Indexer;

	private static object _Customer;

	private static object info;

	private static int interceptor;

	private static nint m_Property;

	[MethodImpl(MethodImplOptions.NoInlining)]
	static Decorator()
	{
		_Message = new uint[64]
		{
			3614090360u, 3905402710u, 606105819u, 3250441966u, 4118548399u, 1200080426u, 2821735955u, 4249261313u, 1770035416u, 2336552879u,
			4294925233u, 2304563134u, 1804603682u, 4254626195u, 2792965006u, 1236535329u, 4129170786u, 3225465664u, 643717713u, 3921069994u,
			3593408605u, 38016083u, 3634488961u, 3889429448u, 568446438u, 3275163606u, 4107603335u, 1163531501u, 2850285829u, 4243563512u,
			1735328473u, 2368359562u, 4294588738u, 2272392833u, 1839030562u, 4259657740u, 2763975236u, 1272893353u, 4139469664u, 3200236656u,
			681279174u, 3936430074u, 3572445317u, 76029189u, 3654602809u, 3873151461u, 530742520u, 3299628645u, 4096336452u, 1126891415u,
			2878612391u, 4237533241u, 1700485571u, 2399980690u, 4293915773u, 2240044497u, 1873313359u, 4264355552u, 2734768916u, 1309151649u,
			4149444226u, 3174756917u, 718787259u, 3951481745u
		};
		_Container = false;
		value = false;
		m_Service = new byte[0];
		candidate = new byte[0];
		_Attr = new byte[0];
		_Indexer = new byte[0];
		m_Property = IntPtr.Zero;
		initializer = IntPtr.Zero;
		info = new string[0];
		_Customer = new int[0];
		interceptor = 1;
		_Adapter = 0L;
		test = 0;
		_Expression = false;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private void leHifFIJCLsZtKEFfM1i()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static byte[] CallPage(object P_0)
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
			InsertPage(ref num6, num7, num8, num9, 0u, 7, 1u, array);
			InsertPage(ref num9, num6, num7, num8, 1u, 12, 2u, array);
			InsertPage(ref num8, num9, num6, num7, 2u, 17, 3u, array);
			InsertPage(ref num7, num8, num9, num6, 3u, 22, 4u, array);
			InsertPage(ref num6, num7, num8, num9, 4u, 7, 5u, array);
			InsertPage(ref num9, num6, num7, num8, 5u, 12, 6u, array);
			InsertPage(ref num8, num9, num6, num7, 6u, 17, 7u, array);
			InsertPage(ref num7, num8, num9, num6, 7u, 22, 8u, array);
			InsertPage(ref num6, num7, num8, num9, 8u, 7, 9u, array);
			InsertPage(ref num9, num6, num7, num8, 9u, 12, 10u, array);
			InsertPage(ref num8, num9, num6, num7, 10u, 17, 11u, array);
			InsertPage(ref num7, num8, num9, num6, 11u, 22, 12u, array);
			InsertPage(ref num6, num7, num8, num9, 12u, 7, 13u, array);
			InsertPage(ref num9, num6, num7, num8, 13u, 12, 14u, array);
			InsertPage(ref num8, num9, num6, num7, 14u, 17, 15u, array);
			InsertPage(ref num7, num8, num9, num6, 15u, 22, 16u, array);
			ClonePage(ref num6, num7, num8, num9, 1u, 5, 17u, array);
			ClonePage(ref num9, num6, num7, num8, 6u, 9, 18u, array);
			ClonePage(ref num8, num9, num6, num7, 11u, 14, 19u, array);
			ClonePage(ref num7, num8, num9, num6, 0u, 20, 20u, array);
			ClonePage(ref num6, num7, num8, num9, 5u, 5, 21u, array);
			ClonePage(ref num9, num6, num7, num8, 10u, 9, 22u, array);
			ClonePage(ref num8, num9, num6, num7, 15u, 14, 23u, array);
			ClonePage(ref num7, num8, num9, num6, 4u, 20, 24u, array);
			ClonePage(ref num6, num7, num8, num9, 9u, 5, 25u, array);
			ClonePage(ref num9, num6, num7, num8, 14u, 9, 26u, array);
			ClonePage(ref num8, num9, num6, num7, 3u, 14, 27u, array);
			ClonePage(ref num7, num8, num9, num6, 8u, 20, 28u, array);
			ClonePage(ref num6, num7, num8, num9, 13u, 5, 29u, array);
			ClonePage(ref num9, num6, num7, num8, 2u, 9, 30u, array);
			ClonePage(ref num8, num9, num6, num7, 7u, 14, 31u, array);
			ClonePage(ref num7, num8, num9, num6, 12u, 20, 32u, array);
			FlushPage(ref num6, num7, num8, num9, 5u, 4, 33u, array);
			FlushPage(ref num9, num6, num7, num8, 8u, 11, 34u, array);
			FlushPage(ref num8, num9, num6, num7, 11u, 16, 35u, array);
			FlushPage(ref num7, num8, num9, num6, 14u, 23, 36u, array);
			FlushPage(ref num6, num7, num8, num9, 1u, 4, 37u, array);
			FlushPage(ref num9, num6, num7, num8, 4u, 11, 38u, array);
			FlushPage(ref num8, num9, num6, num7, 7u, 16, 39u, array);
			FlushPage(ref num7, num8, num9, num6, 10u, 23, 40u, array);
			FlushPage(ref num6, num7, num8, num9, 13u, 4, 41u, array);
			FlushPage(ref num9, num6, num7, num8, 0u, 11, 42u, array);
			FlushPage(ref num8, num9, num6, num7, 3u, 16, 43u, array);
			FlushPage(ref num7, num8, num9, num6, 6u, 23, 44u, array);
			FlushPage(ref num6, num7, num8, num9, 9u, 4, 45u, array);
			FlushPage(ref num9, num6, num7, num8, 12u, 11, 46u, array);
			FlushPage(ref num8, num9, num6, num7, 15u, 16, 47u, array);
			FlushPage(ref num7, num8, num9, num6, 2u, 23, 48u, array);
			SelectPage(ref num6, num7, num8, num9, 0u, 6, 49u, array);
			SelectPage(ref num9, num6, num7, num8, 7u, 10, 50u, array);
			SelectPage(ref num8, num9, num6, num7, 14u, 15, 51u, array);
			SelectPage(ref num7, num8, num9, num6, 5u, 21, 52u, array);
			SelectPage(ref num6, num7, num8, num9, 12u, 6, 53u, array);
			SelectPage(ref num9, num6, num7, num8, 3u, 10, 54u, array);
			SelectPage(ref num8, num9, num6, num7, 10u, 15, 55u, array);
			SelectPage(ref num7, num8, num9, num6, 1u, 21, 56u, array);
			SelectPage(ref num6, num7, num8, num9, 8u, 6, 57u, array);
			SelectPage(ref num9, num6, num7, num8, 15u, 10, 58u, array);
			SelectPage(ref num8, num9, num6, num7, 6u, 15, 59u, array);
			SelectPage(ref num7, num8, num9, num6, 13u, 21, 60u, array);
			SelectPage(ref num6, num7, num8, num9, 4u, 6, 61u, array);
			SelectPage(ref num9, num6, num7, num8, 11u, 10, 62u, array);
			SelectPage(ref num8, num9, num6, num7, 2u, 15, 63u, array);
			SelectPage(ref num7, num8, num9, num6, 9u, 21, 64u, array);
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
	private static void InsertPage(ref uint P_0, uint P_1, uint P_2, uint P_3, uint P_4, ushort P_5, uint P_6, object P_7)
	{
		P_0 = P_1 + VisitPage(P_0 + ((P_1 & P_2) | (~P_1 & P_3)) + ((uint[])P_7)[P_4] + ((uint[])_Message)[P_6 - 1], P_5);
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private static void ClonePage(ref uint P_0, uint P_1, uint P_2, uint P_3, uint P_4, ushort P_5, uint P_6, object P_7)
	{
		P_0 = P_1 + VisitPage(P_0 + ((P_1 & P_3) | (P_2 & ~P_3)) + ((uint[])P_7)[P_4] + ((uint[])_Message)[P_6 - 1], P_5);
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private static void FlushPage(ref uint P_0, uint P_1, uint P_2, uint P_3, uint P_4, ushort P_5, uint P_6, object P_7)
	{
		P_0 = P_1 + VisitPage(P_0 + (P_1 ^ P_2 ^ P_3) + ((uint[])P_7)[P_4] + ((uint[])_Message)[P_6 - 1], P_5);
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private static void SelectPage(ref uint P_0, uint P_1, uint P_2, uint P_3, uint P_4, ushort P_5, uint P_6, object P_7)
	{
		P_0 = P_1 + VisitPage(P_0 + (P_2 ^ (P_1 | ~P_3)) + ((uint[])P_7)[P_4] + ((uint[])_Message)[P_6 - 1], P_5);
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private static uint VisitPage(uint P_0, ushort P_1)
	{
		return (P_0 >> 32 - P_1) | (P_0 << (int)P_1);
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool ReflectPage()
	{
		if (!_Container)
		{
			FindPage();
			_Container = true;
		}
		return value;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static void FindPage()
	{
		try
		{
			new MD5CryptoServiceProvider();
		}
		catch
		{
			value = true;
			return;
		}
		try
		{
			value = (bool)Type.GetTypeFromHandle(AuthenticationClientContainer.e53w34m968awCm9P85taUZe(16777455)).Assembly.GetType("System.Security.Cryptography.CryptoConfig", throwOnError: false).GetMethod("get_AllowOnlyFipsAlgorithms", BindingFlags.Static | BindingFlags.Public).Invoke(null, new object[0]);
		}
		catch
		{
		}
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static SymmetricAlgorithm AssetPage()
	{
		SymmetricAlgorithm symmetricAlgorithm = null;
		if (ReflectPage())
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
	internal static byte[] ExcludePage(object P_0)
	{
		if (!ReflectPage())
		{
			return new MD5CryptoServiceProvider().ComputeHash((byte[])P_0);
		}
		return CallPage(P_0);
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	static bool StopPage(int P_0)
	{
		int num = 3;
		int num3 = default(int);
		bool result = default(bool);
		while (true)
		{
			int num2 = num;
			while (true)
			{
				switch (num2)
				{
				case 4:
					num3 = 0;
					num2 = 7;
					continue;
				case 3:
					if (((Array)candidate).Length == 0)
					{
						CheckCandidate();
						num2 = (FlushCandidate() ? 5 : 0);
						continue;
					}
					goto case 0;
				case 6:
					m_Service = CollectPage(GetPage(typeof(Decorator).Assembly).ToString());
					num2 = 4;
					continue;
				case 1:
				case 5:
				{
					BinaryReader binaryReader = new BinaryReader(typeof(Decorator).Assembly.GetManifestResourceStream("e7416e12-a13f-41a4-84a5-65eed03575cb"));
					binaryReader.BaseStream.Position = 0L;
					byte[] array = binaryReader.ReadBytes((int)binaryReader.BaseStream.Length);
					byte[] array2 = new byte[32];
					int num5 = 0 + 68;
					array2[0] = (byte)num5;
					array2[0] = 162;
					array2[0] = 214;
					array2[1] = 94;
					array2[1] = 144;
					array2[1] = 112;
					array2[1] = 228;
					num5 = 1 + 50;
					array2[2] = (byte)num5;
					array2[2] = 130;
					num5 = 111 + 84;
					array2[2] = (byte)num5;
					array2[2] = 98;
					num5 = 210 + 41;
					array2[2] = (byte)num5;
					num5 = 10 + 94;
					array2[3] = (byte)num5;
					num5 = 48 + 31;
					array2[3] = (byte)num5;
					num5 = 38 + 52;
					array2[3] = (byte)num5;
					array2[3] = 89;
					num5 = 143 + 76;
					array2[3] = (byte)num5;
					array2[4] = 155;
					array2[4] = 125;
					num5 = 101 + 89;
					array2[4] = (byte)num5;
					array2[4] = 110;
					num5 = 80 + 57;
					array2[4] = (byte)num5;
					num5 = 206 - 68;
					array2[5] = (byte)num5;
					array2[5] = 136;
					num5 = 114 + 123;
					array2[5] = (byte)num5;
					array2[6] = 239;
					num5 = 66 + 56;
					array2[6] = (byte)num5;
					num5 = 222 - 74;
					array2[6] = (byte)num5;
					array2[6] = 50;
					array2[6] = 188;
					array2[6] = 45;
					array2[7] = 106;
					array2[7] = 97;
					num5 = 228 - 76;
					array2[7] = (byte)num5;
					num5 = 190 - 63;
					array2[7] = (byte)num5;
					num5 = 150 - 68;
					array2[7] = (byte)num5;
					array2[8] = 94;
					num5 = 165 - 55;
					array2[8] = (byte)num5;
					array2[8] = 168;
					num5 = 146 - 70;
					array2[8] = (byte)num5;
					array2[9] = 162;
					num5 = 189 - 63;
					array2[9] = (byte)num5;
					num5 = 168 - 56;
					array2[9] = (byte)num5;
					num5 = 30 + 105;
					array2[9] = (byte)num5;
					array2[9] = 147;
					array2[10] = 167;
					array2[10] = 145;
					num5 = 20 + 10;
					array2[10] = (byte)num5;
					num5 = 102 + 77;
					array2[10] = (byte)num5;
					array2[10] = 127;
					array2[10] = 116;
					array2[11] = 48;
					num5 = 156 - 52;
					array2[11] = (byte)num5;
					num5 = 49 + 17;
					array2[11] = (byte)num5;
					array2[11] = 179;
					array2[12] = 143;
					num5 = 217 - 72;
					array2[12] = (byte)num5;
					array2[12] = 86;
					num5 = 152 - 50;
					array2[12] = (byte)num5;
					num5 = 152 - 50;
					array2[12] = (byte)num5;
					num5 = 94 - 59;
					array2[12] = (byte)num5;
					num5 = 233 - 77;
					array2[13] = (byte)num5;
					num5 = 52 + 68;
					array2[13] = (byte)num5;
					array2[13] = 144;
					array2[13] = 117;
					array2[14] = 13;
					num5 = 74 + 11;
					array2[14] = (byte)num5;
					num5 = 190 - 63;
					array2[14] = (byte)num5;
					num5 = 125 + 81;
					array2[14] = (byte)num5;
					num5 = 109 + 39;
					array2[15] = (byte)num5;
					array2[15] = 171;
					num5 = 137 - 45;
					array2[15] = (byte)num5;
					array2[15] = 154;
					array2[15] = 106;
					num5 = 163 - 54;
					array2[16] = (byte)num5;
					num5 = 174 - 58;
					array2[16] = (byte)num5;
					array2[16] = 110;
					num5 = 129 - 106;
					array2[16] = (byte)num5;
					num5 = 165 - 55;
					array2[17] = (byte)num5;
					array2[17] = 137;
					num5 = 125 + 36;
					array2[17] = (byte)num5;
					num5 = 64 + 32;
					array2[18] = (byte)num5;
					array2[18] = 124;
					array2[18] = 148;
					num5 = 193 - 64;
					array2[18] = (byte)num5;
					array2[18] = 137;
					num5 = 117 + 105;
					array2[18] = (byte)num5;
					array2[19] = 85;
					num5 = 149 - 49;
					array2[19] = (byte)num5;
					array2[19] = 0;
					array2[20] = 114;
					array2[20] = 86;
					array2[20] = 33;
					array2[21] = 71;
					array2[21] = 190;
					array2[21] = 60;
					num5 = 44 + 57;
					array2[21] = (byte)num5;
					array2[21] = 224;
					array2[22] = 126;
					array2[22] = 151;
					num5 = 64 + 56;
					array2[22] = (byte)num5;
					array2[22] = 39;
					array2[23] = 120;
					num5 = 181 - 60;
					array2[23] = (byte)num5;
					array2[23] = 24;
					num5 = 245 - 81;
					array2[24] = (byte)num5;
					num5 = 194 - 64;
					array2[24] = (byte)num5;
					num5 = 47 + 12;
					array2[24] = (byte)num5;
					array2[24] = 8;
					array2[25] = 166;
					array2[25] = 92;
					array2[25] = 117;
					num5 = 165 - 55;
					array2[25] = (byte)num5;
					array2[25] = 196;
					array2[26] = 148;
					array2[26] = 84;
					num5 = 59 + 107;
					array2[26] = (byte)num5;
					array2[26] = 134;
					array2[26] = 128;
					array2[26] = 17;
					array2[27] = 117;
					array2[27] = 100;
					array2[27] = 186;
					num5 = 110 + 84;
					array2[28] = (byte)num5;
					num5 = 205 - 68;
					array2[28] = (byte)num5;
					num5 = 151 - 50;
					array2[28] = (byte)num5;
					array2[28] = 237;
					array2[28] = 109;
					num5 = 82 + 119;
					array2[29] = (byte)num5;
					num5 = 44 + 73;
					array2[29] = (byte)num5;
					num5 = 45 + 83;
					array2[29] = (byte)num5;
					num5 = 163 - 54;
					array2[29] = (byte)num5;
					num5 = 57 + 11;
					array2[29] = (byte)num5;
					num5 = 131 - 12;
					array2[29] = (byte)num5;
					num5 = 176 - 58;
					array2[30] = (byte)num5;
					array2[30] = 194;
					num5 = 18 - 10;
					array2[30] = (byte)num5;
					array2[31] = 113;
					array2[31] = 185;
					num5 = 48 + 55;
					array2[31] = (byte)num5;
					num5 = 146 + 63;
					array2[31] = (byte)num5;
					byte[] rgbKey = array2;
					byte[] array3 = new byte[16];
					int num6 = 94 + 36;
					array3[0] = (byte)num6;
					array3[0] = 28;
					num6 = 138 - 46;
					array3[0] = (byte)num6;
					num6 = 3 + 57;
					array3[0] = (byte)num6;
					array3[0] = 85;
					num6 = 63 + 114;
					array3[1] = (byte)num6;
					array3[1] = 130;
					array3[1] = 61;
					int num7 = 133 - 44;
					array3[2] = (byte)num7;
					array3[2] = 114;
					array3[2] = 96;
					array3[3] = 96;
					array3[3] = 146;
					num7 = 28 + 9;
					array3[3] = (byte)num7;
					num7 = 185 - 61;
					array3[3] = (byte)num7;
					num7 = 105 + 84;
					array3[3] = (byte)num7;
					array3[4] = 130;
					num6 = 195 - 65;
					array3[4] = (byte)num6;
					num7 = 89 + 54;
					array3[4] = (byte)num7;
					num7 = 168 - 56;
					array3[5] = (byte)num7;
					num6 = 154 - 51;
					array3[5] = (byte)num6;
					num7 = 138 + 16;
					array3[5] = (byte)num7;
					array3[6] = 176;
					num6 = 155 - 51;
					array3[6] = (byte)num6;
					array3[6] = 184;
					array3[7] = 116;
					num6 = 181 - 60;
					array3[7] = (byte)num6;
					num6 = 93 - 87;
					array3[7] = (byte)num6;
					array3[8] = 123;
					num7 = 51 + 58;
					array3[8] = (byte)num7;
					num7 = 117 + 63;
					array3[8] = (byte)num7;
					num6 = 20 + 124;
					array3[8] = (byte)num6;
					num7 = 126 + 24;
					array3[8] = (byte)num7;
					array3[9] = 136;
					num6 = 182 - 60;
					array3[9] = (byte)num6;
					num7 = 106 + 19;
					array3[9] = (byte)num7;
					array3[9] = 227;
					array3[10] = 99;
					array3[10] = 112;
					array3[10] = 50;
					num7 = 53 + 86;
					array3[10] = (byte)num7;
					array3[11] = 88;
					array3[11] = 99;
					num6 = 200 - 66;
					array3[11] = (byte)num6;
					num6 = 219 - 73;
					array3[11] = (byte)num6;
					array3[11] = 60;
					array3[12] = 126;
					num6 = 16 + 89;
					array3[12] = (byte)num6;
					array3[12] = 111;
					num7 = 82 - 31;
					array3[12] = (byte)num7;
					num7 = 218 - 72;
					array3[13] = (byte)num7;
					num6 = 232 - 77;
					array3[13] = (byte)num6;
					num6 = 180 - 60;
					array3[13] = (byte)num6;
					array3[13] = 0;
					array3[14] = 115;
					array3[14] = 170;
					array3[14] = 84;
					num7 = 140 - 46;
					array3[14] = (byte)num7;
					array3[14] = 35;
					num7 = 88 + 65;
					array3[15] = (byte)num7;
					array3[15] = 103;
					num6 = 253 - 84;
					array3[15] = (byte)num6;
					num6 = 148 - 49;
					array3[15] = (byte)num6;
					array3[15] = 185;
					array3[15] = 244;
					byte[] array4 = array3;
					byte[] publicKeyToken = typeof(Decorator).Assembly.GetName().GetPublicKeyToken();
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
					SymmetricAlgorithm symmetricAlgorithm = AssetPage();
					symmetricAlgorithm.Mode = CipherMode.CBC;
					ICryptoTransform transform = symmetricAlgorithm.CreateDecryptor(rgbKey, array4);
					MemoryStream memoryStream = new MemoryStream();
					CryptoStream cryptoStream = new CryptoStream(memoryStream, transform, CryptoStreamMode.Write);
					cryptoStream.Write(array, 0, array.Length);
					cryptoStream.FlushFinalBlock();
					candidate = memoryStream.ToArray();
					memoryStream.Close();
					cryptoStream.Close();
					binaryReader.Close();
					goto case 0;
				}
				case 0:
				case 2:
					if (((Array)m_Service).Length != 0)
					{
						goto case 4;
					}
					goto case 6;
				default:
					num = 6;
					if (!CheckCandidate())
					{
						break;
					}
					goto case 7;
				case 7:
					try
					{
						num3 = BitConverter.ToInt32(new byte[4]
						{
							((byte[])candidate)[P_0],
							((byte[])candidate)[P_0 + 1],
							((byte[])candidate)[P_0 + 2],
							((byte[])candidate)[P_0 + 3]
						}, 0);
					}
					catch
					{
					}
					try
					{
						if (((byte[])m_Service)[num3] == 128)
						{
							FlushCandidate();
							int num4;
							if (!CheckCandidate())
							{
								num4 = 2;
								if (false)
								{
									goto IL_168a;
								}
							}
							else
							{
								num4 = 3;
							}
							switch (num4)
							{
							case 0:
							case 2:
								break;
							default:
								return result;
							}
							goto IL_168a;
						}
						goto end_IL_165a;
						IL_168a:
						return true;
						end_IL_165a:;
					}
					catch
					{
					}
					return false;
				}
				break;
			}
		}
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	static string OrderPage(int P_0)
	{
		int num = 298;
		if (false)
		{
			goto IL_0016;
		}
		goto IL_26c1;
		IL_0016:
		byte[] array = default(byte[]);
		array[12] = 116;
		num = 98;
		if (false)
		{
			goto IL_003a;
		}
		goto IL_26c1;
		IL_003a:
		byte[] array2 = default(byte[]);
		int num2 = default(int);
		array2[1] = (byte)num2;
		int num3 = 354;
		goto IL_26c5;
		IL_26c5:
		byte[] array6 = default(byte[]);
		int num31 = default(int);
		uint num35 = default(uint);
		int num8 = default(int);
		uint num27 = default(uint);
		BinaryReader binaryReader = default(BinaryReader);
		uint num28 = default(uint);
		int num23 = default(int);
		byte[] array3 = default(byte[]);
		int num5 = default(int);
		byte[] array4 = default(byte[]);
		byte[] publicKeyToken = default(byte[]);
		MemoryStream memoryStream = default(MemoryStream);
		ICryptoTransform transform = default(ICryptoTransform);
		byte[] array7 = default(byte[]);
		uint num30 = default(uint);
		int num38 = default(int);
		int num24 = default(int);
		int num33 = default(int);
		int num36 = default(int);
		int num34 = default(int);
		uint num39 = default(uint);
		int num32 = default(int);
		int num37 = default(int);
		uint num10 = default(uint);
		uint num29 = default(uint);
		int num25 = default(int);
		uint num26 = default(uint);
		while (true)
		{
			int num4;
			switch (num3)
			{
			case 301:
				break;
			case 136:
				goto IL_003a;
			case 236:
				num2 = 111 + 32;
				num = 27;
				if (false)
				{
					goto case 225;
				}
				goto IL_26c1;
			case 225:
				array6[num31 + 3] = (byte)((num35 & 0xFF000000u) >> 24);
				num = 407;
				if (!DestroyCandidate())
				{
					goto case 120;
				}
				goto IL_26c1;
			case 393:
				array2[13] = 115;
				num3 = 55;
				continue;
			case 325:
				array2[6] = (byte)num2;
				num4 = 302;
				goto IL_26bd;
			case 93:
				num8 = 212 - 107;
				num4 = 274;
				goto IL_26bd;
			case 354:
				num2 = 200 - 66;
				num = 64;
				if (PrepareCandidate())
				{
					goto case 73;
				}
				goto IL_26c1;
			case 73:
				num8 = 65 + 64;
				num = 56;
				goto IL_26c1;
			case 138:
				num8 = 42 + 108;
				num4 = 1;
				goto IL_26bd;
			case 347:
				num27 = 0u;
				num3 = 351;
				continue;
			case 357:
				binaryReader.Close();
				num3 = 242;
				continue;
			case 24:
				num8 = 20 + 101;
				num3 = 120;
				continue;
			case 92:
				array2[15] = (byte)num2;
				num = 223;
				if (1 == 0)
				{
					goto case 117;
				}
				goto IL_26c1;
			case 117:
				array[15] = 132;
				num3 = 205;
				continue;
			case 15:
				array2[13] = (byte)num2;
				num4 = 95;
				goto IL_26bd;
			case 27:
				array2[12] = (byte)num2;
				num4 = 174;
				goto IL_26bd;
			case 8:
				num28 <<= 8;
				num = 60;
				if (PrepareCandidate())
				{
					goto case 398;
				}
				goto IL_26c1;
			case 398:
				num8 = 165 - 60;
				num4 = 241;
				goto IL_26bd;
			case 331:
				array[12] = 41;
				num4 = 262;
				goto IL_26bd;
			case 291:
				num23 = array3.Length / 4;
				num3 = 347;
				continue;
			case 346:
				num8 = 153 - 51;
				num = 314;
				goto IL_26c1;
			case 195:
				_Attr = array6;
				num = 6;
				goto IL_26c1;
			case 239:
				array[18] = (byte)num8;
				num = 222;
				goto IL_26c1;
			case 175:
				num8 = 86 + 103;
				num = 208;
				goto IL_26c1;
			case 378:
				array2[0] = (byte)num2;
				num = 202;
				goto IL_26c1;
			case 270:
				num8 = 80 + 104;
				num3 = 94;
				continue;
			case 6:
				num5 = BitConverter.ToInt32((byte[])_Attr, P_0);
				num3 = 426;
				continue;
			case 125:
				array2[14] = (byte)num2;
				num = 402;
				if (!DestroyCandidate())
				{
					goto case 152;
				}
				goto IL_26c1;
			case 339:
				array2[8] = 45;
				num = 352;
				if (!DestroyCandidate())
				{
					goto case 366;
				}
				goto IL_26c1;
			case 366:
				num8 = 253 - 84;
				num = 253;
				if (false)
				{
					goto case 349;
				}
				goto IL_26c1;
			case 349:
				array2[11] = 116;
				num4 = 7;
				goto IL_26bd;
			case 353:
				array4[15] = publicKeyToken[7];
				num4 = 290;
				goto IL_26bd;
			case 62:
				array[1] = (byte)num8;
				num4 = 175;
				goto IL_26bd;
			case 395:
				array[8] = (byte)num8;
				num4 = 256;
				goto IL_26bd;
			case 79:
				array[27] = 210;
				num = 209;
				if (1 == 0)
				{
					goto case 295;
				}
				goto IL_26c1;
			case 295:
				num8 = 72 + 100;
				num3 = 168;
				continue;
			case 411:
				num2 = 13 + 9;
				num3 = 125;
				continue;
			case 316:
				num8 = 178 - 59;
				num = 414;
				goto IL_26c1;
			case 21:
			{
				CryptoStream cryptoStream = new CryptoStream(memoryStream, transform, CryptoStreamMode.Write);
				cryptoStream.Write(array7, 0, array7.Length);
				cryptoStream.FlushFinalBlock();
				_Attr = memoryStream.ToArray();
				memoryStream.Close();
				cryptoStream.Close();
				num4 = 357;
				goto IL_26bd;
			}
			case 335:
				array[27] = 96;
				num3 = 105;
				continue;
			case 162:
				num8 = 31 + 100;
				num = 323;
				if (false)
				{
					goto case 332;
				}
				goto IL_26c1;
			case 332:
				num30 = (uint)(num38 * 4);
				num4 = 235;
				goto IL_26bd;
			case 37:
				num8 = 216 - 72;
				num = 165;
				goto IL_26c1;
			case 159:
				num24++;
				num = 418;
				if (!PrepareCandidate())
				{
					goto IL_26c1;
				}
				goto case 142;
			case 312:
				num2 = 7 + 74;
				num3 = 293;
				continue;
			case 289:
				num8 = 6 + 99;
				num3 = 373;
				continue;
			case 268:
				array2[4] = (byte)num2;
				num = 237;
				if (false)
				{
					goto case 273;
				}
				goto IL_26c1;
			case 273:
				array[14] = (byte)num8;
				num = 12;
				if (false)
				{
					goto case 105;
				}
				goto IL_26c1;
			case 105:
				num8 = 104 + 95;
				num = 397;
				if (false)
				{
					goto case 86;
				}
				goto IL_26c1;
			case 86:
				array2[14] = 9;
				num3 = 83;
				continue;
			case 66:
				num8 = 126 - 42;
				num = 59;
				goto IL_26c1;
			case 212:
				array[20] = (byte)num8;
				num = 182;
				if (false)
				{
					goto case 20;
				}
				goto IL_26c1;
			case 20:
				array[14] = 107;
				num = 37;
				goto IL_26c1;
			case 168:
				array[9] = (byte)num8;
				num4 = 22;
				goto IL_26bd;
			case 144:
				num8 = 8 + 95;
				num3 = 350;
				continue;
			case 161:
				array[6] = (byte)num8;
				num3 = 118;
				continue;
			case 231:
				num8 = 229 + 10;
				num3 = 48;
				continue;
			case 278:
				num2 = 71 + 17;
				num4 = 36;
				goto IL_26bd;
			case 253:
				array[5] = (byte)num8;
				num4 = 401;
				goto IL_26bd;
			case 101:
				num8 = 214 - 71;
				num3 = 328;
				continue;
			case 69:
				num8 = 81 + 7;
				num4 = 377;
				goto IL_26bd;
			case 52:
				array[16] = (byte)num8;
				num3 = 87;
				continue;
			case 294:
				num33++;
				num = 245;
				if (!DestroyCandidate())
				{
					goto case 220;
				}
				goto IL_26c1;
			case 220:
				num8 = 239 - 79;
				num3 = 179;
				continue;
			case 227:
				num36++;
				num = 232;
				if (PrepareCandidate())
				{
					goto case 71;
				}
				goto IL_26c1;
			case 71:
				num8 = 31 + 93;
				num = 103;
				goto IL_26c1;
			case 254:
				array[11] = 153;
				num4 = 304;
				goto IL_26bd;
			case 187:
				num8 = 52 + 69;
				num = 52;
				if (false)
				{
					goto case 217;
				}
				goto IL_26c1;
			case 217:
				array[29] = (byte)num8;
				num = 142;
				if (PrepareCandidate())
				{
					goto case 185;
				}
				goto IL_26c1;
			case 61:
				num2 = 157 - 52;
				num3 = 126;
				continue;
			case 365:
				array4[5] = publicKeyToken[2];
				num = 272;
				if (!DestroyCandidate())
				{
					goto case 163;
				}
				goto IL_26c1;
			case 163:
				num2 = 92 + 116;
				num = 81;
				goto IL_26c1;
			case 10:
				array[23] = 155;
				num = 3;
				if (PrepareCandidate())
				{
					goto case 189;
				}
				goto IL_26c1;
			case 26:
				array[3] = (byte)num8;
				num3 = 172;
				continue;
			case 102:
				array[23] = (byte)num8;
				num4 = 316;
				goto IL_26bd;
			case 424:
				array[6] = 141;
				num4 = 130;
				goto IL_26bd;
			case 146:
				array2[2] = 209;
				num4 = 341;
				goto IL_26bd;
			case 409:
				num8 = 42 + 53;
				num = 343;
				if (!PrepareCandidate())
				{
					goto IL_26c1;
				}
				goto case 293;
			case 397:
				array[27] = (byte)num8;
				num3 = 238;
				continue;
			case 266:
				num34 = array7.Length % 4;
				num = 320;
				if (1 == 0)
				{
					goto case 169;
				}
				goto IL_26c1;
			case 169:
				array4[3] = publicKeyToken[1];
				num4 = 365;
				goto IL_26bd;
			case 423:
				array[21] = (byte)num8;
				num = 415;
				if (!DestroyCandidate())
				{
					goto case 83;
				}
				goto IL_26c1;
			case 83:
				num2 = 13 + 59;
				num3 = 18;
				continue;
			case 286:
				array[30] = (byte)num8;
				num4 = 280;
				goto IL_26bd;
			case 274:
				array[26] = (byte)num8;
				num4 = 73;
				goto IL_26bd;
			case 173:
				array[22] = 89;
				num = 425;
				if (PrepareCandidate())
				{
					goto case 166;
				}
				goto IL_26c1;
			case 401:
				array[5] = 211;
				num3 = 424;
				continue;
			case 246:
				num8 = 121 + 38;
				num = 286;
				if (1 == 0)
				{
					goto case 369;
				}
				goto IL_26c1;
			case 369:
				array[22] = 102;
				num = 10;
				if (false)
				{
					goto case 380;
				}
				goto IL_26c1;
			case 380:
				num2 = 215 - 71;
				num = 183;
				if (!PrepareCandidate())
				{
					goto IL_26c1;
				}
				goto case 192;
			case 132:
				array2[3] = (byte)num2;
				num4 = 277;
				goto IL_26bd;
			case 408:
				array2[3] = 116;
				num4 = 108;
				goto IL_26bd;
			case 280:
				array[30] = 73;
				num3 = 180;
				continue;
			case 299:
				array[0] = (byte)num8;
				num = 220;
				goto IL_26c1;
			case 308:
				num39 = 255u;
				num4 = 156;
				goto IL_26bd;
			case 53:
				array2[7] = (byte)num2;
				num4 = 40;
				goto IL_26bd;
			case 156:
				num32 = 0;
				num = 410;
				if (PrepareCandidate())
				{
					goto case 122;
				}
				goto IL_26c1;
			case 250:
				array2[8] = 153;
				num = 119;
				if (!DestroyCandidate())
				{
					goto case 98;
				}
				goto IL_26c1;
			case 98:
				array[12] = 136;
				num = 346;
				if (!DestroyCandidate())
				{
					goto case 403;
				}
				goto IL_26c1;
			case 403:
				array2[8] = (byte)num2;
				num3 = 313;
				continue;
			case 23:
				num8 = 97 + 57;
				num4 = 395;
				goto IL_26bd;
			case 323:
				array[12] = (byte)num8;
				num4 = 301;
				goto IL_26bd;
			case 421:
				array2[7] = (byte)num2;
				num = 333;
				if (!DestroyCandidate())
				{
					goto case 198;
				}
				goto IL_26c1;
			case 54:
				num2 = 52 + 69;
				num3 = 176;
				continue;
			case 166:
				num2 = 222 - 74;
				num3 = 321;
				continue;
			case 211:
				num2 = 216 - 72;
				num = 15;
				if (1 == 0)
				{
					goto case 302;
				}
				goto IL_26c1;
			case 302:
				num2 = 208 - 69;
				num4 = 207;
				goto IL_26bd;
			case 208:
				array[1] = (byte)num8;
				num = 65;
				if (false)
				{
					goto case 40;
				}
				goto IL_26c1;
			case 40:
				array2[8] = 191;
				num3 = 41;
				continue;
			case 259:
				num8 = 208 - 69;
				num4 = 157;
				goto IL_26bd;
			case 390:
				num2 = 173 + 49;
				num3 = 329;
				continue;
			case 272:
				array4[7] = publicKeyToken[3];
				num3 = 413;
				continue;
			case 383:
				array[11] = 136;
				num4 = 285;
				goto IL_26bd;
			case 361:
				array2[7] = (byte)num2;
				num3 = 297;
				continue;
			case 364:
				array[11] = (byte)num8;
				num3 = 292;
				continue;
			case 256:
				num8 = 28 + 39;
				num4 = 233;
				goto IL_26bd;
			case 177:
				array2[6] = 169;
				num3 = 184;
				continue;
			case 282:
				array[17] = (byte)num8;
				num = 371;
				if (PrepareCandidate())
				{
					goto case 182;
				}
				goto IL_26c1;
			case 182:
				array[20] = 17;
				num = 270;
				goto IL_26c1;
			case 121:
			case 134:
				array[16] = 191;
				num3 = 140;
				continue;
			case 28:
			case 232:
				if (num36 >= num34)
				{
					num = 75;
					if (DestroyCandidate())
					{
						goto IL_26c1;
					}
					goto case 293;
				}
				if (num36 <= 0)
				{
					goto case 63;
				}
				num4 = 310;
				goto IL_26bd;
			case 344:
				array2[9] = 166;
				num = 89;
				if (!DestroyCandidate())
				{
					goto case 406;
				}
				goto IL_26c1;
			case 152:
				array[9] = 126;
				num = 362;
				if (false)
				{
					goto case 249;
				}
				goto IL_26c1;
			case 249:
				num8 = 228 - 76;
				num4 = 212;
				goto IL_26bd;
			case 324:
				array3 = array;
				num = 422;
				if (DestroyCandidate())
				{
					goto IL_26c1;
				}
				goto case 311;
			case 417:
				array[3] = (byte)num8;
				num = 370;
				if (PrepareCandidate())
				{
					goto case 221;
				}
				goto IL_26c1;
			case 184:
				num2 = 157 + 1;
				num4 = 325;
				goto IL_26bd;
			case 218:
				array2[13] = 124;
				num3 = 211;
				continue;
			case 309:
				num8 = 45 + 122;
				num = 363;
				if (1 == 0)
				{
					goto case 318;
				}
				goto IL_26c1;
			case 318:
				num37 = 0;
				num = 327;
				if (1 == 0)
				{
					goto case 214;
				}
				goto IL_26c1;
			case 214:
				num8 = 94 + 65;
				num4 = 139;
				goto IL_26bd;
			case 33:
				array2[12] = (byte)num2;
				num3 = 218;
				continue;
			case 174:
				num2 = 143 + 40;
				num3 = 33;
				continue;
			case 41:
				num2 = 166 - 55;
				num = 403;
				goto IL_26c1;
			case 260:
				num8 = 240 - 80;
				num = 273;
				if (false)
				{
					goto case 0;
				}
				goto IL_26c1;
			case 0:
				array[29] = (byte)num8;
				num = 186;
				if (false)
				{
					goto case 247;
				}
				goto IL_26c1;
			case 247:
				array[31] = 112;
				num4 = 376;
				goto IL_26bd;
			case 48:
				array[10] = (byte)num8;
				num = 315;
				if (!DestroyCandidate())
				{
					goto case 90;
				}
				goto IL_26c1;
			case 269:
				array[8] = (byte)num8;
				num = 23;
				goto IL_26c1;
			case 341:
				array2[3] = 125;
				num = 163;
				if (!DestroyCandidate())
				{
					goto case 264;
				}
				goto IL_26c1;
			case 264:
				array[29] = (byte)num8;
				num3 = 113;
				continue;
			case 97:
				num8 = 157 - 52;
				num3 = 379;
				continue;
			case 234:
				array[20] = (byte)num8;
				num = 259;
				goto IL_26c1;
			case 363:
				array[10] = (byte)num8;
				num4 = 231;
				goto IL_26bd;
			case 271:
				array2[1] = 126;
				num4 = 49;
				goto IL_26bd;
			case 285:
				array[11] = 159;
				num3 = 254;
				continue;
			case 319:
				array[3] = 118;
				num3 = 131;
				continue;
			case 226:
				num2 = 11 + 36;
				num4 = 342;
				goto IL_26bd;
			case 188:
				array2[10] = (byte)num2;
				num3 = 191;
				continue;
			case 80:
				array[21] = (byte)num8;
				num = 416;
				goto IL_26c1;
			case 131:
				num8 = 8 + 30;
				num3 = 26;
				continue;
			case 382:
				array[20] = 116;
				num4 = 284;
				goto IL_26bd;
			case 181:
				array4 = array2;
				num4 = 148;
				goto IL_26bd;
			case 359:
				num2 = 137 - 45;
				num4 = 136;
				goto IL_26bd;
			case 251:
			case 327:
				if (num37 >= num34)
				{
					num = 221;
				}
				else
				{
					if (num37 <= 0)
					{
						goto case 60;
					}
					num = 8;
				}
				goto IL_26c1;
			case 198:
				array[4] = (byte)num8;
				num3 = 85;
				continue;
			case 158:
				array[25] = 139;
				num = 57;
				goto IL_26c1;
			case 74:
				array[21] = (byte)num8;
				num = 124;
				if (PrepareCandidate())
				{
					goto case 114;
				}
				goto IL_26c1;
			case 114:
				array[19] = (byte)num8;
				num = 71;
				goto IL_26c1;
			case 16:
				array[2] = 187;
				num4 = 319;
				goto IL_26bd;
			case 333:
				num2 = 28 + 39;
				num4 = 287;
				goto IL_26bd;
			case 145:
				array2[1] = 134;
				num4 = 271;
				goto IL_26bd;
			case 240:
				num36 = 0;
				num4 = 28;
				goto IL_26bd;
			case 72:
				array[2] = 126;
				num4 = 215;
				goto IL_26bd;
			case 373:
				array[18] = (byte)num8;
				num4 = 13;
				goto IL_26bd;
			case 205:
				array[15] = 136;
				num3 = 197;
				continue;
			case 201:
				num8 = 180 - 60;
				num3 = 374;
				continue;
			case 261:
				array[7] = 94;
				num4 = 44;
				goto IL_26bd;
			case 180:
				num8 = 102 - 88;
				num4 = 381;
				goto IL_26bd;
			case 194:
				array2[14] = 84;
				num4 = 86;
				goto IL_26bd;
			case 65:
				array[1] = 14;
				num = 127;
				if (!DestroyCandidate())
				{
					goto case 262;
				}
				goto IL_26c1;
			case 262:
				num8 = 194 + 40;
				num3 = 58;
				continue;
			case 94:
				array[21] = (byte)num8;
				num4 = 32;
				goto IL_26bd;
			case 297:
				num2 = 97 + 57;
				num = 421;
				goto IL_26c1;
			case 191:
				array2[10] = 110;
				num4 = 38;
				goto IL_26bd;
			case 242:
				array7 = (byte[])_Attr;
				num = 266;
				if (!DestroyCandidate())
				{
					goto case 313;
				}
				goto IL_26c1;
			case 313:
				num2 = 201 - 67;
				num4 = 122;
				goto IL_26bd;
			case 46:
				num27 = num10;
				num4 = 164;
				goto IL_26bd;
			case 50:
				num8 = 215 - 71;
				num = 269;
				goto IL_26c1;
			case 405:
				array2[2] = (byte)num2;
				num4 = 146;
				goto IL_26bd;
			case 154:
				array6 = new byte[array7.Length];
				num = 291;
				goto IL_26c1;
			case 155:
				if (num34 > 0)
				{
					num3 = 326;
					continue;
				}
				goto IL_0e8b;
			case 419:
				array[10] = (byte)num8;
				num = 309;
				goto IL_26c1;
			case 414:
				array[23] = (byte)num8;
				num4 = 276;
				goto IL_26bd;
			case 149:
				array2[15] = (byte)num2;
				num = 181;
				if (PrepareCandidate())
				{
					goto case 216;
				}
				goto IL_26c1;
			case 216:
				num8 = 181 - 60;
				num = 0;
				if (false)
				{
					goto case 183;
				}
				goto IL_26c1;
			case 183:
				array2[2] = (byte)num2;
				num = 305;
				if (1 == 0)
				{
					goto case 14;
				}
				goto IL_26c1;
			case 14:
				array2[5] = 169;
				num4 = 391;
				goto IL_26bd;
			case 352:
				array2[9] = 98;
				num4 = 82;
				goto IL_26bd;
			case 303:
				array[13] = (byte)num8;
				num4 = 348;
				goto IL_26bd;
			case 425:
				num8 = 206 - 68;
				num4 = 9;
				goto IL_26bd;
			case 221:
			case 257:
				num10 = num27;
				num4 = 30;
				goto IL_26bd;
			case 118:
				array[7] = 195;
				num3 = 261;
				continue;
			case 296:
				array[18] = (byte)num8;
				num3 = 409;
				continue;
			case 368:
				array4[13] = publicKeyToken[6];
				num = 353;
				if (PrepareCandidate())
				{
					goto case 170;
				}
				goto IL_26c1;
			case 170:
				num2 = 157 - 52;
				num4 = 268;
				goto IL_26bd;
			case 151:
				num2 = 1 + 14;
				num3 = 167;
				continue;
			case 56:
				array[27] = (byte)num8;
				num = 79;
				goto IL_26c1;
			case 238:
				num8 = 35 + 13;
				num = 2;
				if (false)
				{
					goto case 252;
				}
				goto IL_26c1;
			case 252:
				num8 = 25 + 73;
				num3 = 114;
				continue;
			case 340:
				num8 = 180 + 45;
				num4 = 279;
				goto IL_26bd;
			case 287:
				array2[7] = (byte)num2;
				num = 200;
				goto IL_26c1;
			case 5:
				array[29] = 94;
				num = 43;
				goto IL_26c1;
			case 45:
				num8 = 13 + 118;
				num = 299;
				goto IL_26c1;
			case 109:
				array[7] = 96;
				num3 = 190;
				continue;
			case 85:
				num8 = 2 + 31;
				num = 404;
				goto IL_26c1;
			case 84:
				array[28] = 162;
				num = 67;
				goto IL_26c1;
			case 9:
				array[22] = (byte)num8;
				num4 = 394;
				goto IL_26bd;
			case 237:
				num2 = 147 - 49;
				num4 = 115;
				goto IL_26bd;
			case 143:
				array6[num31 + 2] = (byte)((num35 & 0xFF0000) >> 16);
				num3 = 225;
				continue;
			case 306:
				num8 = 194 - 64;
				num4 = 135;
				goto IL_26bd;
			case 89:
				num2 = 89 + 100;
				num3 = 188;
				continue;
			case 150:
				array[26] = 122;
				num4 = 93;
				goto IL_26bd;
			case 281:
				if (num34 <= 0)
				{
					goto IL_0d49;
				}
				num4 = 123;
				goto IL_26bd;
			case 43:
				num8 = 196 - 65;
				num4 = 264;
				goto IL_26bd;
			case 348:
				array[13] = 230;
				num = 260;
				if (false)
				{
					goto case 200;
				}
				goto IL_26c1;
			case 200:
				num2 = 51 + 81;
				num4 = 53;
				goto IL_26bd;
			case 126:
				array2[6] = (byte)num2;
				num = 337;
				goto IL_26c1;
			case 115:
				array2[4] = (byte)num2;
				num4 = 389;
				goto IL_26bd;
			case 29:
				array6[num31 + 1] = (byte)((num35 & 0xFF00) >> 8);
				num = 143;
				goto IL_26c1;
			case 229:
				array4[11] = publicKeyToken[5];
				num = 368;
				if (1 == 0)
				{
					goto case 38;
				}
				goto IL_26c1;
			case 38:
				array2[10] = 183;
				num3 = 258;
				continue;
			case 244:
				num28 = (uint)((array7[num30 + 3] << 24) | (array7[num30 + 2] << 16) | (array7[num30 + 1] << 8) | array7[num30]);
				num4 = 257;
				goto IL_26bd;
			case 100:
				num8 = 136 - 45;
				num = 282;
				goto IL_26c1;
			case 233:
				array[8] = (byte)num8;
				num3 = 51;
				continue;
			case 362:
				array[9] = 45;
				num = 360;
				if (1 == 0)
				{
					goto case 367;
				}
				goto IL_26c1;
			case 367:
				array[28] = (byte)num8;
				num = 5;
				goto IL_26c1;
			case 321:
				array2[12] = (byte)num2;
				num4 = 255;
				goto IL_26bd;
			case 355:
				array[9] = (byte)num8;
				num4 = 295;
				goto IL_26bd;
			case 329:
				array2[1] = (byte)num2;
				num3 = 380;
				continue;
			case 64:
				array2[1] = (byte)num2;
				num3 = 145;
				continue;
			case 127:
				num8 = 215 - 71;
				DestroyCandidate();
				if (!PrepareCandidate())
				{
					num4 = 147;
					goto IL_26bd;
				}
				num3 = 134;
				continue;
			case 400:
				array[31] = 157;
				num4 = 247;
				goto IL_26bd;
			case 345:
				array6[num31] = (byte)(num35 & 0xFF);
				num4 = 29;
				goto IL_26bd;
			case 330:
				array2[5] = (byte)num2;
				num = 14;
				if (false)
				{
					goto case 58;
				}
				goto IL_26c1;
			case 58:
				array[12] = (byte)num8;
				num = 375;
				goto IL_26c1;
			case 176:
				array2[14] = (byte)num2;
				num4 = 194;
				goto IL_26bd;
			case 104:
				num8 = 165 - 115;
				num = 296;
				goto IL_26c1;
			case 358:
				num8 = 148 - 49;
				num3 = 399;
				continue;
			case 388:
				num2 = 229 - 76;
				num4 = 116;
				goto IL_26bd;
			case 67:
				num8 = 103 + 108;
				num3 = 367;
				continue;
			case 412:
				array[26] = 178;
				num = 150;
				if (PrepareCandidate())
				{
					goto case 353;
				}
				goto IL_26c1;
			case 379:
				array[6] = (byte)num8;
				num = 141;
				goto IL_26c1;
			case 219:
				array[31] = 131;
				num3 = 324;
				continue;
			case 36:
				array2[7] = (byte)num2;
				num3 = 311;
				continue;
			case 416:
				array[21] = 146;
				num = 171;
				if (1 == 0)
				{
					goto case 230;
				}
				goto IL_26c1;
			case 230:
				num8 = 120 + 45;
				num3 = 112;
				continue;
			case 392:
				if (num34 <= 0)
				{
					goto case 418;
				}
				num = 159;
				if (!DestroyCandidate())
				{
					goto case 398;
				}
				goto IL_26c1;
			case 81:
				array2[3] = (byte)num2;
				num3 = 275;
				continue;
			case 351:
				num29 = 0u;
				num = 111;
				if (1 == 0)
				{
					goto case 360;
				}
				goto IL_26c1;
			case 360:
				num8 = 201 - 67;
				num3 = 355;
				continue;
			case 68:
				num2 = 1 + 59;
				num4 = 405;
				goto IL_26bd;
			case 248:
				array[31] = 112;
				num3 = 192;
				continue;
			case 215:
				num8 = 59 + 50;
				num = 193;
				if (false)
				{
					goto case 4;
				}
				goto IL_26c1;
			case 4:
				array[0] = (byte)num8;
				num3 = 45;
				continue;
			case 284:
				num8 = 131 - 43;
				num4 = 234;
				goto IL_26bd;
			case 292:
				array[11] = 125;
				num = 162;
				if (false)
				{
					goto case 108;
				}
				goto IL_26c1;
			case 108:
				num2 = 123 + 8;
				num4 = 132;
				goto IL_26bd;
			case 406:
				num25 = 0;
				num3 = 90;
				continue;
			case 394:
				array[22] = 101;
				num4 = 369;
				goto IL_26bd;
			case 322:
				array[0] = 95;
				num = 267;
				goto IL_26c1;
			case 17:
				array2[6] = (byte)num2;
				num = 177;
				goto IL_26c1;
			case 122:
				array2[8] = (byte)num2;
				num = 250;
				if (!DestroyCandidate())
				{
					goto case 199;
				}
				goto IL_26c1;
			case 199:
				array[31] = (byte)num8;
				num4 = 400;
				goto IL_26bd;
			case 391:
				array2[5] = 166;
				num = 384;
				goto IL_26c1;
			case 328:
				array[1] = (byte)num8;
				num = 317;
				if (PrepareCandidate())
				{
					goto case 42;
				}
				goto IL_26c1;
			case 42:
				if (P_0 != -1)
				{
					goto case 266;
				}
				num = 387;
				if (1 == 0)
				{
					goto case 342;
				}
				goto IL_26c1;
			case 342:
				array2[11] = (byte)num2;
				num = 88;
				goto IL_26c1;
			case 18:
				array2[15] = (byte)num2;
				num3 = 70;
				continue;
			case 25:
			case 147:
				array[2] = (byte)num8;
				num = 72;
				goto IL_26c1;
			case 95:
				array2[13] = 144;
				num3 = 393;
				continue;
			case 314:
				array[12] = (byte)num8;
				num4 = 331;
				goto IL_26bd;
			case 1:
				array[0] = (byte)num8;
				num = 19;
				goto IL_26c1;
			case 290:
				num33 = 0;
				num = 185;
				if (1 == 0)
				{
					goto case 207;
				}
				goto IL_26c1;
			case 207:
				array2[7] = (byte)num2;
				num3 = 278;
				continue;
			case 228:
				num31 = num25 * 4;
				num = 332;
				goto IL_26c1;
			case 275:
				num2 = 50 + 8;
				num = 96;
				goto IL_26c1;
			case 49:
				num2 = 214 - 71;
				num3 = 396;
				continue;
			case 7:
				array2[11] = 90;
				num4 = 226;
				goto IL_26bd;
			case 171:
				num8 = 66 - 7;
				num = 423;
				if (false)
				{
					goto case 413;
				}
				goto IL_26c1;
			case 413:
				array4[9] = publicKeyToken[4];
				num = 229;
				if (false)
				{
					goto case 157;
				}
				goto IL_26c1;
			case 157:
				array[20] = (byte)num8;
				num = 336;
				if (PrepareCandidate())
				{
					goto case 78;
				}
				goto IL_26c1;
			case 78:
				num2 = 123 + 98;
				num3 = 149;
				continue;
			case 376:
				array[31] = 2;
				num3 = 219;
				continue;
			case 283:
				num30 = (uint)num31;
				num = 244;
				if (PrepareCandidate())
				{
					goto case 326;
				}
				goto IL_26c1;
			case 11:
				array[2] = 184;
				num = 16;
				if (1 == 0)
				{
					goto case 193;
				}
				goto IL_26c1;
			case 193:
				array[2] = (byte)num8;
				num4 = 11;
				goto IL_26bd;
			case 39:
				array[23] = (byte)num8;
				num3 = 214;
				continue;
			case 110:
				array[11] = (byte)num8;
				num = 383;
				goto IL_26c1;
			case 203:
				num2 = 224 - 74;
				num = 330;
				goto IL_26c1;
			case 370:
				num8 = 8 + 81;
				num4 = 198;
				goto IL_26bd;
			case 119:
				num2 = 7 + 57;
				num3 = 76;
				continue;
			case 298:
				if (((Array)_Attr).Length != 0)
				{
					goto case 6;
				}
				num4 = 372;
				goto IL_26bd;
			case 377:
				array[15] = (byte)num8;
				num3 = 117;
				continue;
			case 51:
				array[8] = 170;
				num3 = 152;
				continue;
			case 90:
			case 307:
				if (num25 < num24)
				{
					num38 = num25 % num23;
					num = 228;
					goto IL_26c1;
				}
				num4 = 195;
				goto IL_26bd;
			case 276:
				num8 = 181 + 59;
				num3 = 39;
				continue;
			case 336:
				array[20] = 85;
				num4 = 249;
				goto IL_26bd;
			case 47:
				array2[4] = (byte)num2;
				num = 203;
				if (false)
				{
					goto case 209;
				}
				goto IL_26c1;
			case 209:
				array[27] = 36;
				num = 335;
				if (!DestroyCandidate())
				{
					goto case 338;
				}
				goto IL_26c1;
			case 338:
				num27 += num29;
				num3 = 318;
				continue;
			case 326:
				num28 = 0u;
				num = 338;
				if (1 == 0)
				{
					goto case 31;
				}
				goto IL_26c1;
			case 31:
				num32 += 8;
				num3 = 63;
				continue;
			case 243:
				array[24] = 213;
				num = 300;
				goto IL_26c1;
			case 70:
				num2 = 136 - 45;
				num = 92;
				goto IL_26c1;
			case 87:
				num8 = 126 - 42;
				num = 34;
				if (PrepareCandidate())
				{
					goto case 133;
				}
				goto IL_26c1;
			case 133:
				array = new byte[32];
				num3 = 138;
				continue;
			case 179:
				array[0] = (byte)num8;
				num3 = 201;
				continue;
			case 384:
				array2[5] = 108;
				num3 = 386;
				continue;
			case 76:
				array2[8] = (byte)num2;
				num4 = 339;
				goto IL_26bd;
			case 418:
				num30 = 0u;
				num = 406;
				if (PrepareCandidate())
				{
					goto case 422;
				}
				goto IL_26c1;
			case 422:
				array2 = new byte[16];
				num3 = 224;
				continue;
			case 111:
				num28 = 0u;
				num = 392;
				if (!DestroyCandidate())
				{
					goto case 262;
				}
				goto IL_26c1;
			case 55:
				array2[13] = 142;
				num3 = 312;
				continue;
			case 389:
				num2 = 194 + 40;
				num4 = 47;
				goto IL_26bd;
			case 189:
				num37++;
				num4 = 251;
				goto IL_26bd;
			case 165:
				array[14] = (byte)num8;
				num3 = 356;
				continue;
			case 224:
				num2 = 169 - 56;
				num3 = 378;
				continue;
			case 141:
				num8 = 77 - 51;
				num3 = 161;
				continue;
			case 140:
				array[17] = 72;
				num = 100;
				if (1 == 0)
				{
					goto case 267;
				}
				goto IL_26c1;
			case 267:
				array[1] = 87;
				num = 101;
				if (1 == 0)
				{
					goto case 190;
				}
				goto IL_26c1;
			case 190:
				array[7] = 69;
				num3 = 50;
				continue;
			case 30:
				num27++;
				num = 129;
				goto IL_26c1;
			case 258:
				array2[10] = 186;
				num4 = 388;
				goto IL_26bd;
			case 263:
				if (publicKeyToken == null)
				{
					goto case 290;
				}
				num = 204;
				if (1 == 0)
				{
					goto case 396;
				}
				goto IL_26c1;
			case 396:
				array2[1] = (byte)num2;
				num = 390;
				if (!DestroyCandidate())
				{
					goto case 337;
				}
				goto IL_26c1;
			case 337:
				num2 = 51 + 87;
				num = 17;
				if (1 == 0)
				{
					goto case 372;
				}
				goto IL_26c1;
			case 372:
				binaryReader = new BinaryReader(typeof(Decorator).Assembly.GetManifestResourceStream("340f0de1-da6a-4652-a989-73fe059c84ad"));
				num = 160;
				goto IL_26c1;
			case 386:
				array2[5] = 136;
				num4 = 61;
				goto IL_26bd;
			case 96:
				array2[3] = (byte)num2;
				num = 408;
				goto IL_26c1;
			case 32:
				num8 = 161 - 53;
				num3 = 74;
				continue;
			case 172:
				num8 = 135 - 79;
				num3 = 417;
				continue;
			case 113:
				array[29] = 92;
				num = 216;
				goto IL_26c1;
			case 185:
			case 245:
				if (num33 < array4.Length)
				{
					array3[num33] ^= array4[num33];
					num = 294;
				}
				else
				{
					num = 42;
					if (PrepareCandidate())
					{
						goto case 310;
					}
				}
				goto IL_26c1;
			case 310:
				num39 <<= 8;
				num3 = 31;
				continue;
			case 99:
				array[4] = 236;
				num4 = 144;
				goto IL_26bd;
			case 223:
				array2[15] = 79;
				num3 = 78;
				continue;
			case 241:
				array[25] = (byte)num8;
				num = 412;
				if (1 == 0)
				{
					goto case 305;
				}
				goto IL_26c1;
			case 305:
				num2 = 47 + 45;
				num3 = 385;
				continue;
			case 410:
				if (num25 != num24 - 1)
				{
					goto IL_0e8b;
				}
				num4 = 155;
				goto IL_26bd;
			case 399:
				array[7] = (byte)num8;
				num3 = 109;
				continue;
			case 63:
				array6[num31 + num36] = (byte)((num26 & num39) >> num32);
				num3 = 227;
				continue;
			case 255:
				array2[12] = 93;
				num3 = 236;
				continue;
			case 128:
				num2 = 185 - 61;
				num = 35;
				if (1 == 0)
				{
					goto case 120;
				}
				goto IL_26c1;
			case 120:
				array[19] = (byte)num8;
				num = 340;
				if (1 == 0)
				{
					goto case 19;
				}
				goto IL_26c1;
			case 19:
				num8 = 93 + 1;
				num4 = 4;
				goto IL_26bd;
			case 186:
				num8 = 212 - 70;
				goto case 217;
			default:
				num3 = 217;
				continue;
			case 2:
				array[28] = (byte)num8;
				num4 = 84;
				goto IL_26bd;
			case 265:
				num8 = 54 + 76;
				num = 303;
				if (!PrepareCandidate())
				{
					goto IL_26c1;
				}
				goto case 13;
			case 13:
				num8 = 182 - 60;
				num = 239;
				goto IL_26c1;
			case 88:
				array2[11] = 118;
				num = 137;
				goto IL_26c1;
			case 213:
				array[22] = 43;
				num = 173;
				if (true)
				{
					goto IL_26c1;
				}
				goto case 315;
			case 315:
				num8 = 184 - 61;
				num = 110;
				goto IL_26c1;
			case 91:
				array[14] = 138;
				num = 20;
				if (!DestroyCandidate())
				{
					goto case 331;
				}
				goto IL_26c1;
			case 356:
				array[14] = 109;
				num4 = 230;
				goto IL_26bd;
			case 420:
				array[7] = (byte)num8;
				num = 358;
				if (true)
				{
					goto IL_26c1;
				}
				goto case 350;
			case 350:
				array[5] = (byte)num8;
				num = 366;
				if (DestroyCandidate())
				{
					goto IL_26c1;
				}
				goto case 334;
			case 334:
				array7 = binaryReader.ReadBytes((int)binaryReader.BaseStream.Length);
				num4 = 133;
				goto IL_26bd;
			case 277:
				array2[4] = 153;
				num3 = 170;
				continue;
			case 206:
				array2[0] = 123;
				num3 = 359;
				continue;
			case 135:
				array[24] = (byte)num8;
				num3 = 243;
				continue;
			case 139:
				array[24] = (byte)num8;
				num = 288;
				if (!PrepareCandidate())
				{
					goto IL_26c1;
				}
				goto case 112;
			case 112:
				array[15] = (byte)num8;
				num = 69;
				if (!PrepareCandidate())
				{
					goto IL_26c1;
				}
				goto case 91;
			case 106:
				array2[11] = (byte)num2;
				num = 166;
				goto IL_26c1;
			case 137:
				num2 = 127 + 38;
				num4 = 106;
				goto IL_26bd;
			case 197:
				array[15] = 166;
				num = 187;
				goto IL_26c1;
			case 371:
				array[17] = 192;
				num4 = 289;
				goto IL_26bd;
			case 374:
				array[0] = (byte)num8;
				num = 322;
				goto IL_26c1;
			case 12:
				array[14] = 124;
				num3 = 91;
				continue;
			case 164:
				if (num25 == num24 - 1)
				{
					num3 = 281;
					continue;
				}
				goto IL_0d49;
			case 124:
				num8 = 246 - 82;
				num = 80;
				goto IL_26c1;
			case 279:
				array[19] = (byte)num8;
				num3 = 382;
				continue;
			case 153:
				array[13] = (byte)num8;
				num = 265;
				goto IL_26c1;
			case 311:
				num2 = 34 + 86;
				num3 = 361;
				continue;
			case 235:
				num29 = (uint)((array3[num30 + 3] << 24) | (array3[num30 + 2] << 16) | (array3[num30 + 1] << 8) | array3[num30]);
				num4 = 308;
				goto IL_26bd;
			case 123:
				num26 = num27 ^ num28;
				num = 240;
				if (!PrepareCandidate())
				{
					goto IL_26c1;
				}
				goto case 59;
			case 59:
				array[19] = (byte)num8;
				num = 252;
				goto IL_26c1;
			case 60:
				num28 |= array7[^(1 + num37)];
				num4 = 189;
				goto IL_26bd;
			case 402:
				array2[14] = 85;
				num3 = 54;
				continue;
			case 304:
				num8 = 222 - 74;
				num4 = 364;
				goto IL_26bd;
			case 160:
				binaryReader.BaseStream.Position = 0L;
				num3 = 334;
				continue;
			case 222:
				array[18] = 46;
				num3 = 104;
				continue;
			case 75:
			case 407:
				num25++;
				num4 = 307;
				goto IL_26bd;
			case 35:
				array2[2] = (byte)num2;
				num3 = 68;
				continue;
			case 192:
				num8 = 109 + 30;
				num = 199;
				if (PrepareCandidate())
				{
					goto case 361;
				}
				goto IL_26c1;
			case 22:
				num8 = 132 - 44;
				num4 = 419;
				goto IL_26bd;
			case 82:
				array2[9] = 123;
				num4 = 344;
				goto IL_26bd;
			case 415:
				num8 = 254 - 84;
				num3 = 178;
				continue;
			case 300:
				array[24] = 154;
				num = 107;
				goto IL_26c1;
			case 320:
				num24 = array7.Length / 4;
				num = 154;
				if (0 == 0)
				{
					goto IL_26c1;
				}
				goto case 210;
			case 210:
				array4[1] = publicKeyToken[0];
				num = 169;
				if (0 == 0)
				{
					goto IL_26c1;
				}
				goto case 148;
			case 148:
				publicKeyToken = typeof(Decorator).Assembly.GetName().GetPublicKeyToken();
				num = 263;
				if (DestroyCandidate())
				{
					goto IL_26c1;
				}
				goto case 44;
			case 44:
				num8 = 249 - 83;
				num3 = 420;
				continue;
			case 77:
				array[4] = 98;
				num = 99;
				if (true)
				{
					goto IL_26c1;
				}
				goto case 178;
			case 178:
				array[22] = (byte)num8;
				num = 213;
				if (true)
				{
					goto IL_26c1;
				}
				goto case 107;
			case 107:
				array[24] = 131;
				num3 = 158;
				continue;
			case 288:
				array[24] = 155;
				num = 306;
				if (!PrepareCandidate())
				{
					goto IL_26c1;
				}
				goto case 204;
			case 204:
				if (publicKeyToken.Length == 0)
				{
					goto case 290;
				}
				num4 = 210;
				goto IL_26bd;
			case 317:
				num8 = 176 - 58;
				num3 = 62;
				continue;
			case 167:
				array2[0] = (byte)num2;
				num4 = 206;
				goto IL_26bd;
			case 202:
				array2[0] = 131;
				num4 = 151;
				goto IL_26bd;
			case 375:
				num8 = 184 - 61;
				num = 153;
				if (!DestroyCandidate())
				{
					goto case 281;
				}
				goto IL_26c1;
			case 130:
				array[6] = 134;
				num4 = 97;
				goto IL_26bd;
			case 293:
				array2[14] = (byte)num2;
				num = 411;
				if (true)
				{
					goto IL_26c1;
				}
				goto case 57;
			case 57:
				array[25] = 210;
				num4 = 398;
				goto IL_26bd;
			case 129:
			{
				uint num9 = num10;
				uint num11 = num10;
				uint num12 = 399522727u;
				uint num13 = 1175363962u;
				uint num14 = 656276816u;
				uint num15 = 297323369u;
				uint num16 = num11;
				uint num17 = 1356102888u;
				ulong num18 = num13 * 371293044;
				num18 |= 1;
				num15 = (uint)(num15 * num15 % num18);
				uint num19 = ((num14 >> 5) | (num14 << 27)) + num12;
				uint num20 = num19 & 0x55555555;
				num19 &= 0xAAAAAAAAu;
				num14 = (num19 >> 1) | (num20 << 1);
				if ((double)num12 == 0.0)
				{
					num12--;
				}
				uint num21 = (uint)(64079.0 / (double)num12 + (double)num12);
				num12 = (uint)((uint)((short)num15 + (ushort)num15 + (int)num21) + (short)num15);
				num13 += num15;
				ulong num22 = num15 * num15;
				if (num22 == 0)
				{
					num22--;
				}
				num17 = (uint)(num17 * num17 % num22);
				num16 ^= num16 << 9;
				num16 += num12;
				num16 ^= num16 >> 21;
				num16 += num13;
				num16 ^= num16 << 2;
				num16 += num17;
				num16 = (((num15 << 6) + num15) ^ num13) + num16;
				num10 = num9 + (uint)(double)num16;
				num = 46;
				if (0 == 0)
				{
					goto IL_26c1;
				}
				goto case 404;
			}
			case 404:
				array[4] = (byte)num8;
				num = 77;
				if (true)
				{
					goto IL_26c1;
				}
				goto case 116;
			case 116:
				array2[11] = (byte)num2;
				num = 349;
				if (true)
				{
					goto IL_26c1;
				}
				goto case 34;
			case 34:
				array[16] = (byte)num8;
				goto case 121;
			case 385:
				array2[2] = (byte)num2;
				num3 = 128;
				continue;
			case 142:
				array[29] = 34;
				num4 = 246;
				goto IL_26bd;
			case 381:
				array[30] = (byte)num8;
				num4 = 248;
				goto IL_26bd;
			case 343:
				array[19] = (byte)num8;
				num = 66;
				if (DestroyCandidate())
				{
					goto IL_26c1;
				}
				goto case 103;
			case 103:
				array[19] = (byte)num8;
				num = 24;
				goto IL_26c1;
			case 3:
				num8 = 172 - 57;
				num = 102;
				goto IL_26c1;
			case 426:
				try
				{
					byte[] array5 = new byte[num5];
					DestroyCandidate();
					int num7;
					if (!PrepareCandidate())
					{
						int num6 = 2;
						if (PrepareCandidate())
						{
							goto IL_37bf;
						}
						num7 = num6;
					}
					else
					{
						num7 = 3;
					}
					switch (num7)
					{
					case 0:
					case 2:
						Array.Copy((Array)_Attr, P_0 + 4, array5, 0, num5);
						break;
					}
					goto IL_37bf;
					IL_37bf:
					return Encoding.Unicode.GetString(array5, 0, array5.Length);
				}
				catch
				{
				}
				return "";
			case 387:
			{
				SymmetricAlgorithm symmetricAlgorithm = AssetPage();
				symmetricAlgorithm.Mode = CipherMode.CBC;
				transform = symmetricAlgorithm.CreateDecryptor(array3, array4);
				num4 = 196;
				goto IL_26bd;
			}
			case 196:
				{
					memoryStream = new MemoryStream();
					num = 21;
					if (PrepareCandidate())
					{
						goto case 5;
					}
					goto IL_26c1;
				}
				IL_0d49:
				num35 = num27 ^ num28;
				num3 = 345;
				continue;
				IL_0e8b:
				num27 += num29;
				num3 = 283;
				continue;
				IL_26bd:
				num = num4;
				goto IL_26c1;
			}
			break;
		}
		goto IL_0016;
		IL_26c1:
		num3 = num;
		goto IL_26c5;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static string AwakePage(object P_0)
	{
		byte[] array = Convert.FromBase64String((string)P_0);
		return Encoding.Unicode.GetString(array, 0, array.Length);
	}

	[DllImport("kernel32.dll", EntryPoint = "VirtualProtect")]
	private static extern int RatePage(nint P_0, int P_1, int P_2, ref int P_3);

	[MethodImpl(MethodImplOptions.NoInlining)]
	[ReaderRulesStatus(typeof(ReaderRulesStatus.SchemaSpecificationResolver<object>[]))]
	static void EnablePage()
	{
		int num = 93;
		uint num17 = default(uint);
		byte[] array = default(byte[]);
		byte[] array2 = default(byte[]);
		int num13 = default(int);
		int num16 = default(int);
		byte[] array3 = default(byte[]);
		byte[] publicKeyToken = default(byte[]);
		int num2 = default(int);
		int num14 = default(int);
		byte[] array6 = default(byte[]);
		uint num33 = default(uint);
		int num20 = default(int);
		int num21 = default(int);
		uint num28 = default(uint);
		byte[] array5 = default(byte[]);
		int num26 = default(int);
		uint num30 = default(uint);
		nint num31 = default(nint);
		int num10 = default(int);
		int num29 = default(int);
		BinaryReader binaryReader = default(BinaryReader);
		nint hINSTANCE = default(nint);
		int num32 = default(int);
		int num19 = default(int);
		uint num24 = default(uint);
		nint num12 = default(nint);
		int num35 = default(int);
		byte[] array4 = default(byte[]);
		uint num23 = default(uint);
		byte[] array7 = default(byte[]);
		int num22 = default(int);
		int num18 = default(int);
		int num25 = default(int);
		int num34 = default(int);
		uint num27 = default(uint);
		int num8 = default(int);
		int num9 = default(int);
		nint num6 = default(nint);
		int num7 = default(int);
		while (true)
		{
			int num3;
			int num15;
			nint zero;
			switch (num)
			{
			case 160:
				num17 <<= 8;
				num = 40;
				break;
			case 354:
				array[13] = 94;
				num = 313;
				break;
			case 372:
				array[23] = 46;
				num3 = 27;
				goto IL_1d80;
			case 305:
				array2[5] = (byte)num13;
				num15 = 165;
				goto IL_1d7c;
			case 388:
				array[14] = 144;
				num = 73;
				break;
			case 131:
			case 336:
				num16++;
				num3 = 246;
				if (1 == 0)
				{
					goto case 242;
				}
				goto IL_1d80;
			case 242:
				array3[7] = publicKeyToken[3];
				num3 = 22;
				goto IL_1d80;
			case 409:
				array[9] = (byte)num2;
				num3 = 170;
				if (!SetupObserver())
				{
					goto case 231;
				}
				goto IL_1d80;
			case 231:
				num13 = 7 - 3;
				num3 = 97;
				if (true)
				{
					goto IL_1d80;
				}
				goto case 353;
			case 161:
				num14 = 76 + 99;
				num3 = 149;
				if (false)
				{
					goto case 146;
				}
				goto IL_1d80;
			case 146:
				array[13] = (byte)num2;
				num15 = 354;
				goto IL_1d7c;
			case 29:
				array[13] = 94;
				num = 422;
				break;
			case 285:
				num17 = (uint)((array6[num33 + 3] << 24) | (array6[num33 + 2] << 16) | (array6[num33 + 1] << 8) | array6[num33]);
				num = 235;
				break;
			case 450:
				array[23] = 140;
				num3 = 373;
				if (ChangeObserver())
				{
					goto case 201;
				}
				goto IL_1d80;
			case 201:
				array[15] = 112;
				num3 = 337;
				goto IL_1d80;
			case 2:
				array[30] = 82;
				num = 92;
				break;
			case 153:
				num2 = 86 + 2;
				num15 = 195;
				goto IL_1d7c;
			case 28:
			case 329:
				if (num20 >= num21)
				{
					num15 = 131;
				}
				else
				{
					if (num20 <= 0)
					{
						goto case 414;
					}
					num15 = 110;
				}
				goto IL_1d7c;
			case 192:
				num14 = 118 + 55;
				num3 = 239;
				goto IL_1d80;
			case 80:
				array[9] = 96;
				num15 = 206;
				goto IL_1d7c;
			case 423:
				array[21] = 154;
				num = 257;
				break;
			case 127:
				num14 = 75 + 50;
				num = 389;
				break;
			case 315:
				array[7] = 58;
				num15 = 435;
				goto IL_1d7c;
			case 178:
				array[27] = (byte)num14;
				num3 = 416;
				if (false)
				{
					goto case 251;
				}
				goto IL_1d80;
			case 251:
				array[8] = 219;
				num15 = 252;
				goto IL_1d7c;
			case 302:
				array3[13] = publicKeyToken[6];
				num = 154;
				break;
			case 54:
				num28 = 255u;
				num3 = 228;
				if (1 == 0)
				{
					goto case 331;
				}
				goto IL_1d80;
			case 331:
				array[10] = 218;
				num = 159;
				break;
			case 376:
				array[15] = (byte)num2;
				num15 = 371;
				goto IL_1d7c;
			case 170:
				num14 = 229 - 76;
				num15 = 220;
				goto IL_1d7c;
			case 20:
				array2[2] = (byte)num13;
				num15 = 177;
				goto IL_1d7c;
			case 272:
				array[19] = 129;
				num = 369;
				break;
			case 97:
				array2[6] = (byte)num13;
				num15 = 397;
				goto IL_1d7c;
			case 111:
				array[6] = (byte)num2;
				num3 = 282;
				goto IL_1d80;
			case 91:
				array5[num26 + 3] = (byte)((num30 & 0xFF000000u) >> 24);
				num3 = 336;
				if (1 == 0)
				{
					goto case 398;
				}
				goto IL_1d80;
			case 398:
				num2 = 184 - 61;
				num3 = 98;
				goto IL_1d80;
			case 356:
				array[10] = 72;
				num15 = 209;
				goto IL_1d7c;
			case 258:
				array[29] = (byte)num14;
				num3 = 183;
				if (1 == 0)
				{
					goto case 322;
				}
				goto IL_1d80;
			case 322:
				array[31] = (byte)num14;
				num3 = 38;
				goto IL_1d80;
			case 292:
				num2 = 24 + 60;
				num15 = 415;
				goto IL_1d7c;
			case 101:
			case 368:
				array[11] = (byte)num2;
				num3 = 161;
				if (1 == 0)
				{
					goto case 419;
				}
				goto IL_1d80;
			case 419:
				if (num21 <= 0)
				{
					goto IL_02c8;
				}
				num3 = 250;
				goto IL_1d80;
			case 89:
				Array.Reverse(array3);
				num3 = 119;
				goto IL_1d80;
			case 278:
				RatePage(num31, 4, 4, ref num10);
				num3 = 353;
				if (false)
				{
					goto case 79;
				}
				goto IL_1d80;
			case 79:
				array3[5] = publicKeyToken[2];
				num3 = 242;
				goto IL_1d80;
			case 47:
				array[6] = 81;
				num15 = 286;
				goto IL_1d7c;
			case 45:
				num13 = 57 + 55;
				num15 = 317;
				goto IL_1d7c;
			case 126:
				array[8] = 166;
				num = 175;
				break;
			case 166:
				array[4] = 199;
				num3 = 345;
				if (1 == 0)
				{
					goto case 410;
				}
				goto IL_1d80;
			case 410:
				array[16] = 194;
				num3 = 13;
				if (false)
				{
					goto case 63;
				}
				goto IL_1d80;
			case 63:
				array2[15] = (byte)num13;
				num = 290;
				break;
			case 68:
				array[24] = 224;
				num15 = 249;
				goto IL_1d7c;
			case 271:
				array[14] = (byte)num2;
				num15 = 153;
				goto IL_1d7c;
			case 249:
				array[24] = 40;
				num3 = 3;
				if (!SetupObserver())
				{
					goto case 139;
				}
				goto IL_1d80;
			case 139:
				array[26] = 84;
				num3 = 433;
				if (ChangeObserver())
				{
					goto case 10;
				}
				goto IL_1d80;
			case 154:
				array3[15] = publicKeyToken[7];
				num15 = 428;
				goto IL_1d7c;
			case 364:
				array[25] = (byte)num2;
				num15 = 385;
				goto IL_1d7c;
			case 230:
				array[27] = 36;
				num3 = 0;
				goto IL_1d80;
			case 72:
				array[2] = (byte)num2;
				num = 94;
				break;
			case 85:
			case 150:
				RatePage(num31, 4, num10, ref num10);
				num3 = 277;
				if (1 == 0)
				{
					goto case 332;
				}
				goto IL_1d80;
			case 332:
				array[4] = (byte)num2;
				num3 = 308;
				if (false)
				{
					goto case 88;
				}
				goto IL_1d80;
			case 88:
				array[23] = 106;
				num = 450;
				break;
			case 57:
				num14 = 5 + 5;
				num15 = 283;
				goto IL_1d7c;
			case 32:
				array[31] = (byte)num2;
				num15 = 392;
				goto IL_1d7c;
			case 362:
				array2[6] = 128;
				num3 = 231;
				if (!SetupObserver())
				{
					goto case 399;
				}
				goto IL_1d80;
			case 399:
				array[5] = (byte)num14;
				num15 = 48;
				goto IL_1d7c;
			case 326:
				array[28] = 90;
				num3 = 193;
				if (1 == 0)
				{
					goto case 121;
				}
				goto IL_1d80;
			case 121:
				array[1] = 109;
				num = 66;
				break;
			case 238:
				num13 = 130 + 33;
				num3 = 328;
				if (false)
				{
					goto case 3;
				}
				goto IL_1d80;
			case 3:
				array[24] = 130;
				num = 135;
				break;
			case 375:
				array[21] = 158;
				num3 = 423;
				goto IL_1d80;
			case 301:
				array[26] = (byte)num14;
				num3 = 87;
				if (1 == 0)
				{
					goto case 5;
				}
				goto IL_1d80;
			case 5:
				array2[9] = (byte)num13;
				num3 = 241;
				if (false)
				{
					goto case 442;
				}
				goto IL_1d80;
			case 442:
				num29 += 8;
				num = 414;
				break;
			case 397:
				array2[7] = 125;
				num3 = 259;
				if (ChangeObserver())
				{
					goto case 138;
				}
				goto IL_1d80;
			case 67:
				array[29] = 48;
				num15 = 226;
				goto IL_1d7c;
			case 298:
				array[29] = (byte)num2;
				num3 = 134;
				if (false)
				{
					goto case 106;
				}
				goto IL_1d80;
			case 106:
				array[9] = (byte)num2;
				num = 425;
				break;
			case 27:
				array[23] = 164;
				num3 = 88;
				if (false)
				{
					goto case 403;
				}
				goto IL_1d80;
			case 403:
				array2[1] = 199;
				num = 288;
				break;
			case 199:
				num2 = 85 + 61;
				num = 72;
				break;
			case 264:
				num14 = 18 + 69;
				num15 = 122;
				goto IL_1d7c;
			case 366:
				array2[8] = (byte)num13;
				num = 82;
				break;
			case 16:
				array[16] = 194;
				num15 = 303;
				goto IL_1d7c;
			case 296:
				array2[0] = (byte)num13;
				num3 = 311;
				if (ChangeObserver())
				{
					goto case 21;
				}
				goto IL_1d80;
			case 452:
				array[3] = 133;
				num3 = 319;
				goto IL_1d80;
			case 156:
				array[3] = (byte)num2;
				num = 452;
				break;
			case 446:
				array2[0] = 88;
				num15 = 8;
				goto IL_1d7c;
			case 257:
				num2 = 73 + 104;
				goto case 182;
			case 335:
				binaryReader.BaseStream.Position = 0L;
				num15 = 391;
				goto IL_1d7c;
			case 94:
				array[2] = 110;
				num15 = 321;
				goto IL_1d7c;
			case 445:
				array[12] = 63;
				num15 = 404;
				goto IL_1d7c;
			case 42:
				num2 = 229 - 76;
				num3 = 409;
				goto IL_1d80;
			case 420:
				array[11] = (byte)num2;
				num = 240;
				break;
			case 369:
				array[19] = 124;
				num = 254;
				break;
			case 109:
				num13 = 246 - 82;
				num = 296;
				break;
			case 115:
				num21 = array6.Length % 4;
				num = 9;
				break;
			case 53:
				array2[5] = 108;
				num3 = 402;
				if (1 == 0)
				{
					goto case 116;
				}
				goto IL_1d80;
			case 116:
				_Adapter = ((IntPtr)hINSTANCE).ToInt64();
				num = 217;
				break;
			case 110:
				num28 <<= 8;
				num3 = 442;
				if (false)
				{
					goto case 102;
				}
				goto IL_1d80;
			case 102:
				array[30] = 116;
				num3 = 75;
				goto IL_1d80;
			case 197:
				array[27] = 36;
				num3 = 304;
				if (ChangeObserver())
				{
					goto case 10;
				}
				goto IL_1d80;
			case 10:
				num14 = 194 - 64;
				num = 65;
				break;
			case 124:
				array[2] = (byte)num14;
				num15 = 293;
				goto IL_1d7c;
			case 17:
				num32++;
				num3 = 323;
				if (!SetupObserver())
				{
					goto case 84;
				}
				goto IL_1d80;
			case 84:
				num19++;
				num15 = 280;
				goto IL_1d7c;
			case 429:
				num13 = 204 - 68;
				num = 382;
				break;
			case 138:
				array[13] = (byte)num14;
				num = 360;
				break;
			case 345:
				num14 = 253 - 84;
				num = 39;
				break;
			case 303:
				array[17] = 125;
				num3 = 10;
				if (ChangeObserver())
				{
					goto case 104;
				}
				goto IL_1d80;
			case 104:
			{
				uint num36 = num24;
				uint num37 = num24;
				uint num38 = 399522727u;
				uint num39 = 1175363962u;
				uint num40 = 656276816u;
				uint num41 = 297323369u;
				uint num42 = num37;
				uint num43 = 1356102888u;
				ulong num44 = num39 * 371293044;
				num44 |= 1;
				num41 = (uint)(num41 * num41 % num44);
				uint num45 = ((num40 >> 5) | (num40 << 27)) + num38;
				uint num46 = num45 & 0x55555555;
				num45 &= 0xAAAAAAAAu;
				num40 = (num45 >> 1) | (num46 << 1);
				if ((double)num38 == 0.0)
				{
					num38--;
				}
				uint num47 = (uint)(64079.0 / (double)num38 + (double)num38);
				num38 = (uint)((uint)((short)num41 + (ushort)num41 + (int)num47) + (short)num41);
				num39 += num41;
				ulong num48 = num41 * num41;
				if (num48 == 0)
				{
					num48--;
				}
				num43 = (uint)(num43 * num43 % num48);
				num42 ^= num42 << 9;
				num42 += num38;
				num42 ^= num42 >> 21;
				num42 += num39;
				num42 ^= num42 << 2;
				num42 += num43;
				num42 = (((num41 << 6) + num41) ^ num39) + num42;
				num24 = num36 + (uint)(double)num42;
				num3 = 437;
				if (!SetupObserver())
				{
					goto case 378;
				}
				goto IL_1d80;
			}
			case 378:
				num2 = 60 + 95;
				num3 = 172;
				if (ChangeObserver())
				{
					goto case 104;
				}
				goto IL_1d80;
			case 218:
				array[8] = (byte)num14;
				num = 126;
				break;
			case 221:
				array2[3] = 135;
				num = 30;
				break;
			case 227:
				array[18] = 100;
				num = 367;
				break;
			case 9:
				num32 = array6.Length / 4;
				num15 = 355;
				goto IL_1d7c;
			case 350:
				array2[4] = 9;
				num3 = 370;
				if (SetupObserver())
				{
					goto IL_1d80;
				}
				goto case 136;
			case 325:
				array2[15] = (byte)num13;
				num15 = 374;
				goto IL_1d7c;
			case 77:
				array[15] = 15;
				num3 = 107;
				if (!SetupObserver())
				{
					goto case 243;
				}
				goto IL_1d80;
			case 118:
				array[4] = (byte)num2;
				num3 = 401;
				if (false)
				{
					goto case 383;
				}
				goto IL_1d80;
			case 383:
				num2 = 74 + 79;
				num3 = 420;
				if (false)
				{
					goto case 222;
				}
				goto IL_1d80;
			case 222:
				array[5] = (byte)num14;
				num3 = 342;
				goto IL_1d80;
			case 93:
				if (!_Expression)
				{
					num3 = 381;
					if (1 == 0)
					{
						goto case 290;
					}
					goto IL_1d80;
				}
				return;
			case 290:
				num13 = 100 + 61;
				num3 = 327;
				if (!SetupObserver())
				{
					goto case 21;
				}
				goto IL_1d80;
			case 21:
				num12 = IntPtr.Zero;
				num = 14;
				break;
			case 239:
				array[10] = (byte)num14;
				num3 = 266;
				if (false)
				{
					goto case 75;
				}
				goto IL_1d80;
			case 75:
				array[30] = 226;
				num3 = 346;
				if (ChangeObserver())
				{
					goto case 265;
				}
				goto IL_1d80;
			case 265:
				array2[11] = (byte)num13;
				num3 = 339;
				if (ChangeObserver())
				{
					goto case 38;
				}
				goto IL_1d80;
			case 38:
				num2 = 179 - 59;
				num3 = 32;
				if (1 == 0)
				{
					goto case 190;
				}
				goto IL_1d80;
			case 190:
				num14 = 137 - 45;
				num = 261;
				break;
			case 185:
				array2[13] = (byte)num13;
				num = 90;
				break;
			case 266:
				array[10] = 121;
				num3 = 275;
				goto IL_1d80;
			case 210:
				num14 = 211 - 70;
				num3 = 431;
				if (ChangeObserver())
				{
					goto case 343;
				}
				goto IL_1d80;
			case 343:
				array[19] = (byte)num14;
				num = 276;
				break;
			case 96:
				num13 = 99 + 84;
				num = 20;
				break;
			case 69:
				array2[7] = (byte)num13;
				num = 289;
				break;
			case 287:
				num35 = array4.Length / 4;
				num = 300;
				break;
			case 418:
				array[20] = (byte)num14;
				num3 = 171;
				if (!SetupObserver())
				{
					goto case 66;
				}
				goto IL_1d80;
			case 66:
				array[1] = 127;
				num15 = 411;
				goto IL_1d7c;
			case 390:
				num14 = 219 + 0;
				num = 244;
				break;
			case 289:
				num13 = 34 + 124;
				num3 = 155;
				if (1 == 0)
				{
					goto case 379;
				}
				goto IL_1d80;
			case 379:
				array[25] = 112;
				num = 173;
				break;
			case 74:
				num14 = 223 - 74;
				num3 = 138;
				if (ChangeObserver())
				{
					goto case 125;
				}
				goto IL_1d80;
			case 125:
				array2[4] = 131;
				num = 314;
				break;
			case 443:
				num24 += num23;
				num15 = 285;
				goto IL_1d7c;
			case 374:
				num13 = 59 + 20;
				num3 = 63;
				if (!SetupObserver())
				{
					goto case 12;
				}
				goto IL_1d80;
			case 12:
				array[7] = 84;
				num15 = 315;
				goto IL_1d7c;
			case 260:
				array[22] = 77;
				num3 = 194;
				if (1 == 0)
				{
					goto case 408;
				}
				goto IL_1d80;
			case 408:
				num19 = 0;
				num = 181;
				break;
			case 229:
				array[5] = 85;
				num15 = 210;
				goto IL_1d7c;
			case 206:
				array[9] = 92;
				num3 = 424;
				if (!SetupObserver())
				{
					goto case 134;
				}
				goto IL_1d80;
			case 134:
				num14 = 6 + 92;
				num3 = 258;
				goto IL_1d80;
			case 194:
				array[22] = 150;
				num = 128;
				break;
			case 337:
				num2 = 132 - 44;
				num3 = 376;
				goto IL_1d80;
			case 122:
				array[26] = (byte)num14;
				num3 = 139;
				goto IL_1d80;
			case 444:
				num14 = 168 - 56;
				num = 200;
				break;
			case 387:
				array2[3] = 167;
				num3 = 46;
				goto IL_1d80;
			case 304:
				num14 = 112 + 36;
				num3 = 178;
				if (false)
				{
					goto case 184;
				}
				goto IL_1d80;
			case 184:
				array3[3] = publicKeyToken[1];
				num3 = 79;
				if (false)
				{
					goto case 349;
				}
				goto IL_1d80;
			case 349:
				array[2] = 254;
				num15 = 199;
				goto IL_1d7c;
			case 214:
				array[23] = 46;
				num = 299;
				break;
			case 226:
				num14 = 73 + 101;
				num3 = 421;
				goto IL_1d80;
			case 95:
				array6 = array7;
				num15 = 115;
				goto IL_1d7c;
			case 377:
				num2 = 217 - 72;
				num = 268;
				break;
			case 323:
				num33 = 0u;
				num = 359;
				break;
			case 114:
				array[22] = 120;
				num = 223;
				break;
			case 225:
				array2[5] = (byte)num13;
				num = 86;
				break;
			case 18:
				num2 = 218 - 72;
				num = 332;
				break;
			case 317:
				array2[10] = (byte)num13;
				num15 = 180;
				goto IL_1d7c;
			case 4:
				array[20] = 97;
				num15 = 274;
				goto IL_1d7c;
			case 86:
				array2[5] = 250;
				num15 = 451;
				goto IL_1d7c;
			case 348:
				num13 = 156 - 52;
				num = 163;
				break;
			case 147:
				array2[2] = (byte)num13;
				num3 = 429;
				if (SetupObserver())
				{
					goto IL_1d80;
				}
				goto case 90;
			case 346:
				num2 = 95 + 16;
				num3 = 306;
				if (false)
				{
					goto case 25;
				}
				goto IL_1d80;
			case 25:
				num13 = 56 + 108;
				num15 = 281;
				goto IL_1d7c;
			case 41:
				array[31] = 132;
				num15 = 174;
				goto IL_1d7c;
			case 413:
				array2[11] = (byte)num13;
				num3 = 320;
				goto IL_1d80;
			case 87:
				array[26] = 206;
				num3 = 197;
				goto IL_1d80;
			case 240:
				num2 = 74 + 51;
				_ = 1;
				if (ChangeObserver())
				{
					num15 = 208;
					goto IL_1d7c;
				}
				num3 = 368;
				if (!SetupObserver())
				{
					goto case 34;
				}
				goto IL_1d80;
			case 34:
				array[1] = (byte)num2;
				num15 = 444;
				goto IL_1d7c;
			case 164:
				array[10] = (byte)num2;
				num3 = 331;
				if (ChangeObserver())
				{
					goto case 318;
				}
				goto IL_1d80;
			case 318:
				num14 = 38 + 124;
				num3 = 418;
				if (ChangeObserver())
				{
					goto case 9;
				}
				goto IL_1d80;
			case 187:
				array2[9] = (byte)num13;
				num = 426;
				break;
			case 342:
				array[5] = 141;
				num15 = 307;
				goto IL_1d7c;
			case 357:
				array2[10] = (byte)num13;
				num3 = 427;
				goto IL_1d80;
			case 78:
				array2[8] = (byte)num13;
				num = 120;
				break;
			case 360:
				array[13] = 166;
				num15 = 309;
				goto IL_1d7c;
			case 437:
				if (num16 == num32 - 1)
				{
					num = 419;
					break;
				}
				goto IL_02c8;
			case 56:
				array[20] = (byte)num14;
				num3 = 212;
				goto IL_1d80;
			case 275:
				num2 = 245 - 81;
				num = 164;
				break;
			case 449:
				array2[14] = 102;
				num = 238;
				break;
			case 43:
				array[20] = (byte)num14;
				num15 = 15;
				goto IL_1d7c;
			case 120:
				num13 = 200 - 66;
				num3 = 5;
				if (ChangeObserver())
				{
					goto case 20;
				}
				goto IL_1d80;
			case 215:
				num13 = 53 + 27;
				num3 = 225;
				if (false)
				{
					goto case 189;
				}
				goto IL_1d80;
			case 189:
				num14 = 93 + 106;
				num3 = 19;
				if (false)
				{
					goto case 157;
				}
				goto IL_1d80;
			case 157:
				num2 = 97 + 64;
				num15 = 156;
				goto IL_1d7c;
			case 171:
				num14 = 110 + 53;
				num = 43;
				break;
			case 279:
				array[2] = 132;
				num15 = 52;
				goto IL_1d7c;
			case 135:
				array[24] = 208;
				num3 = 430;
				if (false)
				{
					goto case 213;
				}
				goto IL_1d80;
			case 213:
				array[14] = 239;
				num3 = 77;
				if (ChangeObserver())
				{
					goto case 70;
				}
				goto IL_1d80;
			case 205:
				if (num21 <= 0)
				{
					goto IL_0bcc;
				}
				num15 = 198;
				goto IL_1d7c;
			case 217:
				zero = IntPtr.Zero;
				num3 = 256;
				if (false)
				{
					goto case 0;
				}
				goto IL_1d80;
			case 0:
				array[28] = 180;
				num3 = 234;
				if (1 == 0)
				{
					goto case 422;
				}
				goto IL_1d80;
			case 422:
				num14 = 225 - 75;
				num15 = 447;
				goto IL_1d7c;
			case 92:
				array[31] = 25;
				num15 = 216;
				goto IL_1d7c;
			case 281:
				array2[13] = (byte)num13;
				num3 = 60;
				if (1 == 0)
				{
					goto case 297;
				}
				goto IL_1d80;
			case 297:
				array[30] = (byte)num2;
				num15 = 292;
				goto IL_1d7c;
			case 243:
				array2[3] = (byte)num13;
				num3 = 221;
				if (1 == 0)
				{
					goto case 107;
				}
				goto IL_1d80;
			case 107:
				array[15] = 89;
				num = 248;
				break;
			case 133:
				array[23] = (byte)num2;
				num3 = 214;
				if (ChangeObserver())
				{
					goto case 204;
				}
				goto IL_1d80;
			case 204:
				num23 = (uint)((array4[num33 + 3] << 24) | (array4[num33 + 2] << 16) | (array4[num33 + 1] << 8) | array4[num33]);
				num15 = 54;
				goto IL_1d7c;
			case 394:
				num13 = 146 - 48;
				num3 = 441;
				goto IL_1d80;
			case 295:
				num13 = 87 - 51;
				num15 = 265;
				goto IL_1d7c;
			case 70:
			case 255:
				if (num22 >= num18)
				{
					num = 455;
					break;
				}
				num31 = new IntPtr(_Adapter + binaryReader.ReadInt32());
				num15 = 278;
				goto IL_1d7c;
			case 98:
				array[28] = (byte)num2;
				num15 = 326;
				goto IL_1d7c;
			case 451:
				num13 = 54 + 18;
				num3 = 273;
				if (ChangeObserver())
				{
					goto case 347;
				}
				goto IL_1d80;
			case 347:
				array2 = new byte[16];
				num3 = 11;
				if (ChangeObserver())
				{
					goto case 252;
				}
				goto IL_1d80;
			case 252:
				num14 = 214 - 71;
				num3 = 218;
				if (1 == 0)
				{
					goto case 330;
				}
				goto IL_1d80;
			case 330:
				array[17] = 125;
				num15 = 51;
				goto IL_1d7c;
			case 391:
				array7 = binaryReader.ReadBytes((int)binaryReader.BaseStream.Length);
				num15 = 312;
				goto IL_1d7c;
			case 355:
				array5 = new byte[array6.Length];
				num3 = 287;
				goto IL_1d80;
			case 13:
				array[16] = 80;
				num3 = 127;
				if (!ChangeObserver())
				{
					goto IL_1d80;
				}
				goto case 44;
			case 220:
				array[9] = (byte)num14;
				num15 = 80;
				goto IL_1d7c;
			case 236:
				array[20] = (byte)num14;
				num = 57;
				break;
			case 149:
				array[11] = (byte)num14;
				num3 = 33;
				if (!SetupObserver())
				{
					goto case 352;
				}
				goto IL_1d80;
			case 352:
				array2[9] = (byte)num13;
				num = 432;
				break;
			case 277:
				num22++;
				num3 = 255;
				goto IL_1d80;
			case 179:
				array2[0] = (byte)num13;
				num3 = 446;
				goto IL_1d80;
			case 361:
				array[26] = (byte)num14;
				num3 = 264;
				if (!SetupObserver())
				{
					goto case 191;
				}
				goto IL_1d80;
			case 191:
				array2[13] = 196;
				num15 = 407;
				goto IL_1d7c;
			case 188:
				num14 = 149 - 68;
				num3 = 6;
				if (false)
				{
					goto case 427;
				}
				goto IL_1d80;
			case 427:
				num13 = 22 + 29;
				num3 = 413;
				if (1 == 0)
				{
					goto case 83;
				}
				goto IL_1d80;
			case 83:
				array2[12] = (byte)num13;
				num = 25;
				break;
			case 81:
				num13 = 78 + 44;
				num3 = 366;
				if (1 == 0)
				{
					goto case 412;
				}
				goto IL_1d80;
			case 412:
				array2[13] = 147;
				num15 = 191;
				goto IL_1d7c;
			case 46:
				array2[4] = 124;
				num15 = 24;
				goto IL_1d7c;
			case 320:
				array2[11] = 153;
				num15 = 295;
				goto IL_1d7c;
			case 7:
				array3 = array2;
				num3 = 89;
				if (1 == 0)
				{
					goto case 314;
				}
				goto IL_1d80;
			case 314:
				array2[4] = 132;
				num = 350;
				break;
			case 439:
				num2 = 101 - 38;
				num3 = 176;
				goto IL_1d80;
			case 237:
				array[4] = 102;
				num15 = 18;
				goto IL_1d7c;
			case 405:
				num20 = 0;
				num = 329;
				break;
			case 169:
				array2[10] = (byte)num13;
				num3 = 23;
				if (!SetupObserver())
				{
					goto case 241;
				}
				goto IL_1d80;
			case 241:
				num13 = 238 - 79;
				num = 352;
				break;
			case 234:
				array[28] = 102;
				goto case 398;
			default:
				num15 = 398;
				goto IL_1d7c;
			case 288:
				num13 = 33 + 115;
				num3 = 162;
				if (true)
				{
					goto IL_1d80;
				}
				goto case 428;
			case 428:
				Array.Clear(publicKeyToken, 0, publicKeyToken.Length);
				num = 408;
				break;
			case 293:
				array[3] = 155;
				num = 157;
				break;
			case 267:
				num13 = 238 + 13;
				num = 232;
				break;
			case 14:
			{
				Assembly assembly = Type.GetTypeFromHandle(AuthenticationClientContainer.e53w34m968awCm9P85taUZe(33554616)).Assembly;
				num12 = PostPage(56u, 1, (uint)Process.GetCurrentProcess().Id);
				hINSTANCE = Marshal.GetHINSTANCE(assembly.GetModules()[0]);
				num15 = 116;
				goto IL_1d7c;
			}
			case 312:
				array = new byte[32];
				num3 = 103;
				goto IL_1d80;
			case 37:
				array[29] = (byte)num14;
				num = 233;
				break;
			case 203:
				array[1] = 136;
				num3 = 61;
				if (true)
				{
					goto IL_1d80;
				}
				goto case 454;
			case 454:
				num2 = 64 + 71;
				num15 = 297;
				goto IL_1d7c;
			case 438:
				array[22] = 77;
				num15 = 372;
				goto IL_1d7c;
			case 212:
				array[21] = 177;
				num = 375;
				break;
			case 358:
				array2[3] = (byte)num13;
				num3 = 387;
				if (SetupObserver())
				{
					goto IL_1d80;
				}
				goto case 6;
			case 6:
				array[6] = (byte)num14;
				num3 = 12;
				if (ChangeObserver())
				{
					goto case 10;
				}
				goto IL_1d80;
			case 440:
				array[18] = 136;
				num3 = 227;
				if (!SetupObserver())
				{
					goto case 160;
				}
				goto IL_1d80;
			case 167:
				array[12] = 101;
				num3 = 439;
				goto IL_1d80;
			case 155:
				array2[7] = (byte)num13;
				num15 = 140;
				goto IL_1d7c;
			case 341:
				array[6] = 149;
				num3 = 188;
				goto IL_1d80;
			case 108:
				array[9] = 35;
				num3 = 42;
				goto IL_1d80;
			case 76:
				num25 = 0;
				num3 = 453;
				goto IL_1d80;
			case 15:
				array[20] = 72;
				num15 = 386;
				goto IL_1d7c;
			case 136:
				array[11] = 202;
				num3 = 445;
				if (0 == 0)
				{
					goto IL_1d80;
				}
				goto case 232;
			case 232:
				array2[2] = (byte)num13;
				num3 = 145;
				goto IL_1d80;
			case 31:
				array4 = array;
				num3 = 347;
				if (0 == 0)
				{
					goto IL_1d80;
				}
				goto case 382;
			case 382:
				array2[2] = (byte)num13;
				num15 = 267;
				goto IL_1d7c;
			case 365:
				array[0] = (byte)num2;
				num = 100;
				break;
			case 90:
				array2[13] = 104;
				num15 = 412;
				goto IL_1d7c;
			case 140:
				num13 = 22 + 45;
				num3 = 130;
				if (true)
				{
					goto IL_1d80;
				}
				goto case 211;
			case 211:
				num13 = 119 + 66;
				num = 243;
				break;
			case 168:
			case 246:
				if (num16 >= num32)
				{
					num15 = 50;
					goto IL_1d7c;
				}
				num34 = num16 % num35;
				num3 = 284;
				goto IL_1d80;
			case 235:
			case 247:
				num24 = num24;
				num3 = 104;
				goto IL_1d80;
			case 62:
				num2 = 177 - 59;
				num = 148;
				break;
			case 200:
				array[1] = (byte)num14;
				num15 = 203;
				goto IL_1d7c;
			case 334:
				array[2] = (byte)num2;
				num15 = 324;
				goto IL_1d7c;
			case 274:
				num14 = 180 - 60;
				num3 = 236;
				if (0 == 0)
				{
					goto IL_1d80;
				}
				goto case 415;
			case 415:
				array[30] = (byte)num2;
				num3 = 2;
				if (SetupObserver())
				{
					goto IL_1d80;
				}
				goto case 404;
			case 404:
				array[12] = 167;
				num3 = 167;
				if (true)
				{
					goto IL_1d80;
				}
				goto case 259;
			case 259:
				num13 = 89 + 69;
				num15 = 69;
				goto IL_1d7c;
			case 370:
				num13 = 89 + 57;
				num = 305;
				break;
			case 344:
				num33 = (uint)(num34 * 4);
				num3 = 204;
				goto IL_1d80;
			case 158:
				array[14] = (byte)num2;
				num = 388;
				break;
			case 165:
				array2[5] = 142;
				num3 = 53;
				goto IL_1d80;
			case 433:
				num14 = 195 - 65;
				num3 = 301;
				if (0 == 0)
				{
					goto IL_1d80;
				}
				goto case 291;
			case 291:
				num13 = 249 - 83;
				num3 = 224;
				goto IL_1d80;
			case 36:
				if (publicKeyToken == null)
				{
					goto case 408;
				}
				num3 = 49;
				if (true)
				{
					goto IL_1d80;
				}
				goto case 117;
			case 117:
				num25++;
				num3 = 316;
				if (true)
				{
					goto IL_1d80;
				}
				goto case 319;
			case 319:
				num2 = 148 - 49;
				num3 = 363;
				goto IL_1d80;
			case 447:
				array[13] = (byte)num14;
				num3 = 62;
				if (0 == 0)
				{
					goto IL_1d80;
				}
				goto case 64;
			case 64:
				array2[2] = 164;
				num15 = 96;
				goto IL_1d7c;
			case 172:
				array[3] = (byte)num2;
				num = 166;
				break;
			case 196:
				num20++;
				num15 = 28;
				goto IL_1d7c;
			case 402:
				array2[5] = 108;
				num = 215;
				break;
			case 103:
				array[0] = 184;
				num3 = 380;
				if (!SetupObserver())
				{
					goto case 239;
				}
				goto IL_1d80;
			case 82:
				num13 = 162 - 70;
				num3 = 78;
				if (!ChangeObserver())
				{
					goto IL_1d80;
				}
				goto case 448;
			case 269:
				num13 = 75 + 66;
				num = 325;
				break;
			case 340:
				num2 = 219 - 73;
				num15 = 298;
				goto IL_1d7c;
			case 144:
				num2 = 14 + 115;
				num = 158;
				break;
			case 416:
				num2 = 109 + 25;
				num = 396;
				break;
			case 129:
				num17 = 0u;
				num3 = 35;
				if (SetupObserver())
				{
					goto IL_1d80;
				}
				goto case 128;
			case 8:
				array2[0] = 192;
				num = 348;
				break;
			case 441:
				array2[15] = (byte)num13;
				num = 269;
				break;
			case 434:
				num2 = 106 - 22;
				num = 99;
				break;
			case 33:
				array[11] = 114;
				num3 = 136;
				if (true)
				{
					goto IL_1d80;
				}
				goto case 162;
			case 162:
				array2[1] = (byte)num13;
				num3 = 123;
				if (true)
				{
					goto IL_1d80;
				}
				goto case 24;
			case 24:
				array2[4] = 80;
				num3 = 125;
				goto IL_1d80;
			case 128:
				array[22] = 99;
				num15 = 114;
				goto IL_1d7c;
			case 228:
				num29 = 0;
				num = 219;
				break;
			case 60:
				num13 = 86 + 108;
				num15 = 185;
				goto IL_1d7c;
			case 193:
				array[28] = 149;
				num3 = 310;
				if (0 == 0)
				{
					goto IL_1d80;
				}
				goto case 143;
			case 143:
				binaryReader = new BinaryReader(Type.GetTypeFromHandle(AuthenticationClientContainer.e53w34m968awCm9P85taUZe(33554616)).Assembly.GetManifestResourceStream("4d5b1420-4b1d-40b7-bc18-bd6dc94be7a6"));
				num = 335;
				break;
			case 393:
				array[26] = 206;
				num15 = 351;
				goto IL_1d7c;
			case 313:
				array[14] = 239;
				num = 144;
				break;
			case 328:
				array2[14] = (byte)num13;
				num15 = 394;
				goto IL_1d7c;
			case 35:
				if (num21 <= 0)
				{
					goto case 323;
				}
				num15 = 17;
				goto IL_1d7c;
			case 59:
				array[30] = 82;
				num3 = 102;
				if (0 == 0)
				{
					goto IL_1d80;
				}
				goto case 299;
			case 299:
				array[24] = 208;
				num = 68;
				break;
			case 311:
				num13 = 164 - 54;
				num3 = 179;
				if (SetupObserver())
				{
					goto IL_1d80;
				}
				goto case 180;
			case 180:
				num13 = 10 + 93;
				num = 169;
				break;
			case 73:
				num2 = 11 + 124;
				num3 = 271;
				goto IL_1d80;
			case 256:
				num10 = 0;
				num15 = 262;
				goto IL_1d7c;
			case 159:
				array[11] = 202;
				num = 383;
				break;
			case 71:
				array[19] = (byte)num2;
				num3 = 272;
				if (!ChangeObserver())
				{
					goto IL_1d80;
				}
				goto case 406;
			case 406:
				num2 = 187 - 62;
				num = 71;
				break;
			case 23:
				num13 = 198 - 106;
				num3 = 357;
				goto IL_1d80;
			case 52:
				num14 = 205 + 49;
				num3 = 124;
				goto IL_1d80;
			case 198:
				num24 += num23;
				num = 142;
				break;
			case 284:
				num26 = num16 * 4;
				num3 = 344;
				if (SetupObserver())
				{
					goto IL_1d80;
				}
				goto case 176;
			case 176:
				array[12] = (byte)num2;
				num15 = 29;
				goto IL_1d7c;
			case 421:
				array[29] = (byte)num14;
				num3 = 340;
				if (0 == 0)
				{
					goto IL_1d80;
				}
				goto case 381;
			case 381:
				_Expression = true;
				num3 = 143;
				if (0 == 0)
				{
					goto IL_1d80;
				}
				goto case 385;
			case 385:
				array[25] = 139;
				num = 338;
				break;
			case 219:
				if (num16 == num32 - 1)
				{
					num = 205;
					break;
				}
				goto IL_0bcc;
			case 371:
				array[15] = 15;
				num3 = 410;
				if (0 == 0)
				{
					goto IL_1d80;
				}
				goto case 11;
			case 11:
				array2[0] = 71;
				num = 109;
				break;
			case 58:
				array[19] = 229;
				num3 = 406;
				goto IL_1d80;
			case 363:
				array[3] = (byte)num2;
				num15 = 378;
				goto IL_1d7c;
			case 148:
				array[13] = (byte)num2;
				num15 = 74;
				goto IL_1d7c;
			case 250:
				num27 = num24 ^ num17;
				num = 405;
				break;
			case 414:
				array5[num26 + num20] = (byte)((num27 & num28) >> num29);
				num3 = 196;
				goto IL_1d80;
			case 182:
			case 208:
				array[21] = (byte)num2;
				num = 260;
				break;
			case 195:
				array[14] = (byte)num2;
				num3 = 213;
				if (!SetupObserver())
				{
					goto case 437;
				}
				goto IL_1d80;
			case 99:
				array[7] = (byte)num2;
				num = 251;
				break;
			case 431:
				array[5] = (byte)num14;
				num = 400;
				break;
			case 202:
				array[22] = (byte)num2;
				num3 = 438;
				if (!ChangeObserver())
				{
					goto IL_1d80;
				}
				goto case 407;
			case 407:
				num13 = 127 - 42;
				num15 = 1;
				goto IL_1d7c;
			case 123:
				array2[1] = 68;
				num15 = 64;
				goto IL_1d7c;
			case 137:
				ResetPage(num12, num31, BitConverter.GetBytes(binaryReader.ReadInt32()), 4u, out zero);
				num15 = 150;
				goto IL_1d7c;
			case 436:
				array5[num26 + 2] = (byte)((num30 & 0xFF0000) >> 16);
				num3 = 91;
				goto IL_1d80;
			case 174:
				num14 = 179 - 59;
				num3 = 322;
				if (0 == 0)
				{
					goto IL_1d80;
				}
				goto case 248;
			case 248:
				array[15] = 113;
				num = 201;
				break;
			case 396:
				array[27] = (byte)num2;
				num15 = 230;
				goto IL_1d7c;
			case 261:
				array[31] = (byte)num14;
				num15 = 41;
				goto IL_1d7c;
			case 276:
				array[19] = 35;
				num3 = 207;
				if (!SetupObserver())
				{
					goto case 57;
				}
				goto IL_1d80;
			case 333:
				binaryReader.ReadInt32();
				num15 = 417;
				goto IL_1d7c;
			case 254:
				num14 = 170 - 56;
				num3 = 343;
				goto IL_1d80;
			case 263:
				num2 = 68 + 116;
				num3 = 365;
				goto IL_1d80;
			case 338:
				array[25] = 108;
				num3 = 393;
				if (SetupObserver())
				{
					goto IL_1d80;
				}
				goto case 324;
			case 324:
				array[2] = 102;
				num = 279;
				break;
			case 48:
				num2 = 76 + 66;
				num3 = 270;
				if (true)
				{
					goto IL_1d80;
				}
				goto case 177;
			case 177:
				num13 = 63 + 93;
				num3 = 147;
				goto IL_1d80;
			case 270:
				array[5] = (byte)num2;
				num15 = 132;
				goto IL_1d7c;
			case 400:
				num14 = 23 + 21;
				num3 = 222;
				if (SetupObserver())
				{
					goto IL_1d80;
				}
				goto case 373;
			case 373:
				array[23] = 164;
				num3 = 151;
				goto IL_1d80;
			case 132:
				array[5] = 85;
				num15 = 47;
				goto IL_1d7c;
			case 65:
				array[17] = (byte)num14;
				num3 = 448;
				goto IL_1d80;
			case 163:
				array2[1] = (byte)num13;
				num15 = 403;
				goto IL_1d7c;
			case 55:
				array5[num26] = (byte)(num30 & 0xFF);
				num15 = 44;
				goto IL_1d7c;
			case 50:
			{
				byte[] buffer = array5;
				Array.Clear(array3, 0, array3.Length);
				binaryReader.Close();
				binaryReader = new BinaryReader(new MemoryStream(buffer));
				num = 26;
				break;
			}
			case 327:
				array2[15] = (byte)num13;
				num = 7;
				break;
			case 183:
				num14 = 166 - 55;
				num = 37;
				break;
			case 310:
				array[28] = 108;
				num15 = 112;
				goto IL_1d7c;
			case 224:
				array2[12] = (byte)num13;
				num15 = 141;
				goto IL_1d7c;
			case 430:
				array[25] = 108;
				num3 = 379;
				if (SetupObserver())
				{
					goto IL_1d80;
				}
				goto case 173;
			case 173:
				num2 = 52 + 122;
				num3 = 364;
				goto IL_1d80;
			case 105:
				array[28] = (byte)num2;
				num = 67;
				break;
			case 253:
				array[18] = 152;
				num15 = 377;
				goto IL_1d7c;
			case 425:
				array[10] = 218;
				num3 = 356;
				if (0 == 0)
				{
					goto IL_1d80;
				}
				goto case 268;
			case 268:
				array[18] = (byte)num2;
				num = 186;
				break;
			case 401:
				array[4] = 135;
				num = 189;
				break;
			case 145:
				array2[3] = 151;
				num = 211;
				break;
			case 316:
			case 453:
				if (num25 < num21)
				{
					if (num25 <= 0)
					{
						goto case 40;
					}
					num3 = 160;
					if (!ChangeObserver())
					{
						goto IL_1d80;
					}
					goto case 113;
				}
				num = 247;
				break;
			case 426:
				array2[10] = 152;
				num15 = 45;
				goto IL_1d7c;
			case 300:
				num24 = 0u;
				num3 = 245;
				goto IL_1d80;
			case 308:
				num2 = 175 - 58;
				num3 = 118;
				goto IL_1d80;
			case 307:
				num14 = 0 + 10;
				num15 = 399;
				goto IL_1d7c;
			case 435:
				array[7] = 138;
				num3 = 434;
				goto IL_1d80;
			case 100:
				array[1] = 194;
				num = 121;
				break;
			case 411:
				num2 = 143 - 47;
				num3 = 34;
				goto IL_1d80;
			case 245:
				num23 = 0u;
				num3 = 129;
				if (true)
				{
					goto IL_1d80;
				}
				goto case 61;
			case 61:
				array[1] = 194;
				num3 = 349;
				goto IL_1d80;
			case 233:
				array[29] = 48;
				num = 59;
				break;
			case 22:
				array3[9] = publicKeyToken[4];
				num = 294;
				break;
			case 51:
				array[18] = 231;
				num15 = 440;
				goto IL_1d7c;
			case 417:
				num22 = 0;
				num3 = 70;
				goto IL_1d80;
			case 49:
				if (publicKeyToken.Length == 0)
				{
					goto case 408;
				}
				num15 = 152;
				goto IL_1d7c;
			case 151:
				num2 = 155 - 51;
				num = 133;
				break;
			case 309:
				num2 = 121 + 84;
				num = 146;
				break;
			case 432:
				num13 = 170 - 82;
				num15 = 187;
				goto IL_1d7c;
			case 44:
				array5[num26 + 1] = (byte)((num30 & 0xFF00) >> 8);
				num3 = 436;
				if (ChangeObserver())
				{
					goto case 249;
				}
				goto IL_1d80;
			case 175:
				array[8] = 148;
				num = 390;
				break;
			case 1:
				array2[14] = (byte)num13;
				num = 449;
				break;
			case 282:
				array[6] = 158;
				num = 341;
				break;
			case 39:
				array[4] = (byte)num14;
				num15 = 237;
				goto IL_1d7c;
			case 273:
				array2[6] = (byte)num13;
				num3 = 362;
				if (0 == 0)
				{
					goto IL_1d80;
				}
				goto case 152;
			case 152:
				array3[1] = publicKeyToken[0];
				num = 184;
				break;
			case 223:
				array[22] = 188;
				num3 = 384;
				goto IL_1d80;
			case 209:
				array[10] = 85;
				num3 = 192;
				goto IL_1d80;
			case 286:
				num2 = 222 - 74;
				num3 = 111;
				if (SetupObserver())
				{
					goto IL_1d80;
				}
				goto case 130;
			case 181:
			case 280:
				if (num19 >= array3.Length)
				{
					num3 = 95;
					if (0 == 0)
					{
						goto IL_1d80;
					}
					goto case 244;
				}
				array4[num19] ^= array3[num19];
				num15 = 84;
				goto IL_1d7c;
			case 244:
				array[8] = (byte)num14;
				num3 = 108;
				if (SetupObserver())
				{
					goto IL_1d80;
				}
				goto case 19;
			case 19:
				array[4] = (byte)num14;
				num3 = 229;
				if (SetupObserver())
				{
					goto IL_1d80;
				}
				goto case 40;
			case 40:
				num17 |= array6[^(1 + num25)];
				num = 117;
				break;
			case 262:
				num18 = binaryReader.ReadInt32();
				num = 333;
				break;
			case 142:
				num17 = 0u;
				num = 76;
				break;
			case 395:
				array[0] = 110;
				num15 = 263;
				goto IL_1d7c;
			case 424:
				num2 = 62 - 27;
				num15 = 106;
				goto IL_1d7c;
			case 141:
				num13 = 157 - 49;
				num15 = 83;
				goto IL_1d7c;
			case 321:
				num2 = 217 - 72;
				num3 = 334;
				if (true)
				{
					goto IL_1d80;
				}
				goto case 351;
			case 351:
				num14 = 59 + 111;
				num3 = 361;
				if (ChangeObserver())
				{
					goto case 27;
				}
				goto IL_1d80;
			case 119:
				publicKeyToken = Type.GetTypeFromHandle(AuthenticationClientContainer.e53w34m968awCm9P85taUZe(33554616)).Assembly.GetName().GetPublicKeyToken();
				num3 = 36;
				if (true)
				{
					goto IL_1d80;
				}
				goto case 283;
			case 283:
				array[20] = (byte)num14;
				num3 = 318;
				goto IL_1d80;
			case 392:
				array[31] = 25;
				num = 31;
				break;
			case 216:
				array[31] = 85;
				num = 190;
				break;
			case 367:
				array[18] = 119;
				num3 = 253;
				if (true)
				{
					goto IL_1d80;
				}
				goto case 294;
			case 294:
				array3[11] = publicKeyToken[5];
				num3 = 302;
				if (SetupObserver())
				{
					goto IL_1d80;
				}
				goto case 306;
			case 306:
				array[30] = (byte)num2;
				num3 = 454;
				if (0 == 0)
				{
					goto IL_1d80;
				}
				goto case 207;
			case 207:
				array[19] = 229;
				num = 4;
				break;
			case 339:
				array2[12] = 153;
				num3 = 291;
				goto IL_1d80;
			case 389:
				array[16] = (byte)num14;
				num = 16;
				break;
			case 359:
				num16 = 0;
				num3 = 168;
				if (SetupObserver())
				{
					goto IL_1d80;
				}
				goto case 386;
			case 386:
				num14 = 155 - 58;
				num = 56;
				break;
			case 448:
				array[17] = 129;
				num = 330;
				break;
			case 26:
				binaryReader.BaseStream.Position = 0L;
				num3 = 21;
				goto IL_1d80;
			case 113:
				array[18] = (byte)num14;
				num15 = 58;
				goto IL_1d7c;
			case 130:
				array2[8] = (byte)num13;
				num3 = 81;
				if (!ChangeObserver())
				{
					goto IL_1d80;
				}
				goto case 112;
			case 112:
				num2 = 124 + 56;
				num15 = 105;
				goto IL_1d7c;
			case 186:
				num14 = 147 + 84;
				num15 = 113;
				goto IL_1d7c;
			case 380:
				array[0] = 102;
				num = 395;
				break;
			case 30:
				num13 = 244 - 81;
				num3 = 358;
				goto IL_1d80;
			case 384:
				num2 = 115 + 98;
				num3 = 202;
				if (0 == 0)
				{
					goto IL_1d80;
				}
				goto case 455;
			case 455:
				try
				{
					while (binaryReader.BaseStream.Position < binaryReader.BaseStream.Length - 1)
					{
						int num4 = 9;
						while (true)
						{
							IL_3c0d:
							int num5 = num4;
							while (true)
							{
								int num11;
								switch (num5)
								{
								case 11:
									break;
								case 6:
									goto IL_3b5b;
								case 5:
								case 10:
									if (num8 >= num9)
									{
										num4 = 6;
										if (0 == 0)
										{
											goto IL_3c0d;
										}
										goto case 8;
									}
									Marshal.WriteInt32(new IntPtr(((IntPtr)num6).ToInt64() + num8 * 4), binaryReader.ReadInt32());
									num11 = 7;
									goto IL_3c09;
								case 8:
									num9 = binaryReader.ReadInt32();
									_ = 0;
									if (SetupObserver())
									{
										num5 = 1;
										continue;
									}
									num11 = 0;
									goto IL_3c09;
								case 1:
								case 3:
									RatePage(num6, num9 * 4, 4, ref num10);
									goto case 0;
								case 0:
								case 4:
									num8 = 0;
									goto case 5;
								default:
									num5 = 10;
									continue;
								case 9:
									num7 = binaryReader.ReadInt32();
									num5 = 2;
									continue;
								case 7:
									num8++;
									num4 = 5;
									goto IL_3c0d;
								case 2:
									{
										num6 = new IntPtr(_Adapter + num7);
										num4 = 8;
										goto IL_3c0d;
									}
									IL_3c09:
									num4 = num11;
									goto IL_3c0d;
								}
								break;
								IL_3b5b:
								RatePage(num6, num9 * 4, num10, ref num10);
								num4 = 11;
								goto IL_3c0d;
							}
							break;
						}
					}
					DisablePage(num12);
					return;
				}
				catch
				{
					return;
				}
			case 353:
				{
					if (IntPtr.Size == 4)
					{
						num3 = 137;
						if (!ChangeObserver())
						{
							goto IL_1d80;
						}
						goto case 454;
					}
					ResetPage(num12, num31, BitConverter.GetBytes(binaryReader.ReadInt32()), 4u, out zero);
					num = 85;
					break;
				}
				IL_1d7c:
				num3 = num15;
				goto IL_1d80;
				IL_1d80:
				num = num3;
				break;
				IL_0bcc:
				num33 = (uint)num26;
				num15 = 443;
				goto IL_1d7c;
				IL_02c8:
				num30 = num24 ^ num17;
				num3 = 55;
				goto IL_1d80;
			}
		}
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static object GetPage(object P_0)
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
	private static extern int ResetPage(nint P_0, nint P_1, [In][Out] byte[] P_2, uint P_3, out nint P_4);

	[DllImport("kernel32.dll", EntryPoint = "ReadProcessMemory")]
	private static extern int ConcatPage(nint P_0, nint P_1, [In][Out] byte[] P_2, uint P_3, out nint P_4);

	[DllImport("kernel32.dll", EntryPoint = "OpenProcess")]
	private static extern nint PostPage(uint P_0, int P_1, uint P_2);

	[DllImport("kernel32.dll", EntryPoint = "CloseHandle")]
	private static extern int DisablePage(nint P_0);

	[MethodImpl(MethodImplOptions.NoInlining)]
	private static byte[] CollectPage(object P_0)
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
	private static byte[] SearchPage(object P_0)
	{
		MemoryStream memoryStream = new MemoryStream();
		SymmetricAlgorithm symmetricAlgorithm = AssetPage();
		symmetricAlgorithm.Key = new byte[32]
		{
			124, 23, 14, 157, 124, 31, 120, 118, 141, 184,
			59, 137, 27, 2, 81, 150, 187, 111, 184, 91,
			200, 211, 199, 190, 205, 133, 243, 41, 142, 201,
			39, 226
		};
		symmetricAlgorithm.IV = new byte[16]
		{
			66, 7, 16, 222, 129, 179, 100, 37, 224, 181,
			117, 5, 183, 171, 212, 87
		};
		CryptoStream cryptoStream = new CryptoStream(memoryStream, symmetricAlgorithm.CreateDecryptor(), CryptoStreamMode.Write);
		cryptoStream.Write((byte[])P_0, 0, ((Array)P_0).Length);
		cryptoStream.Close();
		return memoryStream.ToArray();
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private byte[] CalculatePage()
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private byte[] LoginPage()
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private byte[] LogoutPage()
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private byte[] DeletePage()
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private byte[] RemovePage()
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private byte[] CountPage()
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal byte[] SortPage()
	{
		_ = "{11111-22222-40001-00001}".Length;
		_ = 0;
		return new byte[2] { 1, 2 };
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal byte[] CreatePage()
	{
		_ = "{11111-22222-40001-00002}".Length;
		_ = 0;
		return new byte[2] { 1, 2 };
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal byte[] RegisterPage()
	{
		_ = "{11111-22222-50001-00001}".Length;
		_ = 0;
		return new byte[2] { 1, 2 };
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal byte[] InvokePage()
	{
		_ = "{11111-22222-50001-00002}".Length;
		_ = 0;
		return new byte[2] { 1, 2 };
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal byte[] ForgotPage()
	{
		_ = "{11111-22222-60001-00001}".Length;
		_ = 0;
		return new byte[2] { 1, 2 };
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal byte[] FillPage()
	{
		_ = "{11111-22222-60001-00002}".Length;
		_ = 0;
		return new byte[2] { 1, 2 };
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static string CalcPage(object P_0, object P_1)
	{
		byte[] bytes = Encoding.Unicode.GetBytes((string)P_0);
		byte[] key = new byte[32]
		{
			82, 102, 104, 110, 32, 77, 24, 34, 118, 181,
			51, 17, 18, 51, 12, 109, 10, 32, 77, 24,
			34, 158, 161, 41, 97, 28, 118, 181, 5, 25,
			1, 88
		};
		byte[] iV = ExcludePage(Encoding.Unicode.GetBytes((string)P_1));
		MemoryStream memoryStream = new MemoryStream();
		SymmetricAlgorithm symmetricAlgorithm = AssetPage();
		symmetricAlgorithm.Key = key;
		symmetricAlgorithm.IV = iV;
		CryptoStream cryptoStream = new CryptoStream(memoryStream, symmetricAlgorithm.CreateEncryptor(), CryptoStreamMode.Write);
		cryptoStream.Write(bytes, 0, bytes.Length);
		cryptoStream.Close();
		return Convert.ToBase64String(memoryStream.ToArray());
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public Decorator()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool DestroyCandidate()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool PrepareCandidate()
	{
		return false;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool FlushCandidate()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool CheckCandidate()
	{
		return false;
	}

	internal static bool SetupObserver()
	{
		return true;
	}

	internal static bool ChangeObserver()
	{
		return false;
	}
}
