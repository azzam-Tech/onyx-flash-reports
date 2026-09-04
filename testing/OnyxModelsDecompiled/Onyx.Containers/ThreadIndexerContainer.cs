using System;
using System.Diagnostics;
using System.IO;
using System.Reflection;
using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;
using System.Security.Cryptography;
using System.Text;
using Onyx.Common;

namespace Onyx.Containers;

internal class ThreadIndexerContainer
{
	internal class DatabaseDecoratorConsumer : Attribute
	{
		internal class StubRepository<T>
		{
			[MethodImpl(MethodImplOptions.NoInlining)]
			public StubRepository()
			{
			}

			[MethodImpl(MethodImplOptions.NoInlining)]
			internal static bool CollectExpression()
			{
				return true;
			}

			[MethodImpl(MethodImplOptions.NoInlining)]
			internal static bool LogoutExpression()
			{
				return true;
			}

			static StubRepository()
			{
				ThreadIndexerContainer.IncludeClass();
			}
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		[DatabaseDecoratorConsumer(typeof(StubRepository<object>[]))]
		public DatabaseDecoratorConsumer(object P_0)
		{
		}

		static DatabaseDecoratorConsumer()
		{
			ThreadIndexerContainer.IncludeClass();
		}
	}

	[Flags]
	private enum QueueOptions
	{

	}

	private static object dispatcherRepository;

	private static object advisorRepository;

	private static nint _ExceptionRepository;

	private static object _WatcherRepository;

	private static int m_StrategyRepository;

	private static int refRepository;

	private static bool producerRepository;

	private static object m_SystemRepository;

	private static object _ContextRepository;

	private static object _AuthenticationRepository;

	private static bool m_AccountRepository;

	private static nint m_FilterRepository;

	private static long _TestsRepository;

	private static bool _FieldRepository;

	private static object predicateRepository;

	[MethodImpl(MethodImplOptions.NoInlining)]
	static ThreadIndexerContainer()
	{
		dispatcherRepository = new uint[64]
		{
			3614090360u, 3905402710u, 606105819u, 3250441966u, 4118548399u, 1200080426u, 2821735955u, 4249261313u, 1770035416u, 2336552879u,
			4294925233u, 2304563134u, 1804603682u, 4254626195u, 2792965006u, 1236535329u, 4129170786u, 3225465664u, 643717713u, 3921069994u,
			3593408605u, 38016083u, 3634488961u, 3889429448u, 568446438u, 3275163606u, 4107603335u, 1163531501u, 2850285829u, 4243563512u,
			1735328473u, 2368359562u, 4294588738u, 2272392833u, 1839030562u, 4259657740u, 2763975236u, 1272893353u, 4139469664u, 3200236656u,
			681279174u, 3936430074u, 3572445317u, 76029189u, 3654602809u, 3873151461u, 530742520u, 3299628645u, 4096336452u, 1126891415u,
			2878612391u, 4237533241u, 1700485571u, 2399980690u, 4293915773u, 2240044497u, 1873313359u, 4264355552u, 2734768916u, 1309151649u,
			4149444226u, 3174756917u, 718787259u, 3951481745u
		};
		_FieldRepository = false;
		m_AccountRepository = false;
		predicateRepository = new byte[0];
		_ContextRepository = new byte[0];
		advisorRepository = new byte[0];
		_AuthenticationRepository = new byte[0];
		m_FilterRepository = IntPtr.Zero;
		_ExceptionRepository = IntPtr.Zero;
		m_SystemRepository = new string[0];
		_WatcherRepository = new int[0];
		m_StrategyRepository = 1;
		_TestsRepository = 0L;
		refRepository = 0;
		producerRepository = false;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private void leHifFIJCLsZtKEFfM1i()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static byte[] AwakeClass(object P_0)
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
			CalcClass(ref num6, num7, num8, num9, 0u, 7, 1u, array);
			CalcClass(ref num9, num6, num7, num8, 1u, 12, 2u, array);
			CalcClass(ref num8, num9, num6, num7, 2u, 17, 3u, array);
			CalcClass(ref num7, num8, num9, num6, 3u, 22, 4u, array);
			CalcClass(ref num6, num7, num8, num9, 4u, 7, 5u, array);
			CalcClass(ref num9, num6, num7, num8, 5u, 12, 6u, array);
			CalcClass(ref num8, num9, num6, num7, 6u, 17, 7u, array);
			CalcClass(ref num7, num8, num9, num6, 7u, 22, 8u, array);
			CalcClass(ref num6, num7, num8, num9, 8u, 7, 9u, array);
			CalcClass(ref num9, num6, num7, num8, 9u, 12, 10u, array);
			CalcClass(ref num8, num9, num6, num7, 10u, 17, 11u, array);
			CalcClass(ref num7, num8, num9, num6, 11u, 22, 12u, array);
			CalcClass(ref num6, num7, num8, num9, 12u, 7, 13u, array);
			CalcClass(ref num9, num6, num7, num8, 13u, 12, 14u, array);
			CalcClass(ref num8, num9, num6, num7, 14u, 17, 15u, array);
			CalcClass(ref num7, num8, num9, num6, 15u, 22, 16u, array);
			OrderClass(ref num6, num7, num8, num9, 1u, 5, 17u, array);
			OrderClass(ref num9, num6, num7, num8, 6u, 9, 18u, array);
			OrderClass(ref num8, num9, num6, num7, 11u, 14, 19u, array);
			OrderClass(ref num7, num8, num9, num6, 0u, 20, 20u, array);
			OrderClass(ref num6, num7, num8, num9, 5u, 5, 21u, array);
			OrderClass(ref num9, num6, num7, num8, 10u, 9, 22u, array);
			OrderClass(ref num8, num9, num6, num7, 15u, 14, 23u, array);
			OrderClass(ref num7, num8, num9, num6, 4u, 20, 24u, array);
			OrderClass(ref num6, num7, num8, num9, 9u, 5, 25u, array);
			OrderClass(ref num9, num6, num7, num8, 14u, 9, 26u, array);
			OrderClass(ref num8, num9, num6, num7, 3u, 14, 27u, array);
			OrderClass(ref num7, num8, num9, num6, 8u, 20, 28u, array);
			OrderClass(ref num6, num7, num8, num9, 13u, 5, 29u, array);
			OrderClass(ref num9, num6, num7, num8, 2u, 9, 30u, array);
			OrderClass(ref num8, num9, num6, num7, 7u, 14, 31u, array);
			OrderClass(ref num7, num8, num9, num6, 12u, 20, 32u, array);
			CreateClass(ref num6, num7, num8, num9, 5u, 4, 33u, array);
			CreateClass(ref num9, num6, num7, num8, 8u, 11, 34u, array);
			CreateClass(ref num8, num9, num6, num7, 11u, 16, 35u, array);
			CreateClass(ref num7, num8, num9, num6, 14u, 23, 36u, array);
			CreateClass(ref num6, num7, num8, num9, 1u, 4, 37u, array);
			CreateClass(ref num9, num6, num7, num8, 4u, 11, 38u, array);
			CreateClass(ref num8, num9, num6, num7, 7u, 16, 39u, array);
			CreateClass(ref num7, num8, num9, num6, 10u, 23, 40u, array);
			CreateClass(ref num6, num7, num8, num9, 13u, 4, 41u, array);
			CreateClass(ref num9, num6, num7, num8, 0u, 11, 42u, array);
			CreateClass(ref num8, num9, num6, num7, 3u, 16, 43u, array);
			CreateClass(ref num7, num8, num9, num6, 6u, 23, 44u, array);
			CreateClass(ref num6, num7, num8, num9, 9u, 4, 45u, array);
			CreateClass(ref num9, num6, num7, num8, 12u, 11, 46u, array);
			CreateClass(ref num8, num9, num6, num7, 15u, 16, 47u, array);
			CreateClass(ref num7, num8, num9, num6, 2u, 23, 48u, array);
			ValidateClass(ref num6, num7, num8, num9, 0u, 6, 49u, array);
			ValidateClass(ref num9, num6, num7, num8, 7u, 10, 50u, array);
			ValidateClass(ref num8, num9, num6, num7, 14u, 15, 51u, array);
			ValidateClass(ref num7, num8, num9, num6, 5u, 21, 52u, array);
			ValidateClass(ref num6, num7, num8, num9, 12u, 6, 53u, array);
			ValidateClass(ref num9, num6, num7, num8, 3u, 10, 54u, array);
			ValidateClass(ref num8, num9, num6, num7, 10u, 15, 55u, array);
			ValidateClass(ref num7, num8, num9, num6, 1u, 21, 56u, array);
			ValidateClass(ref num6, num7, num8, num9, 8u, 6, 57u, array);
			ValidateClass(ref num9, num6, num7, num8, 15u, 10, 58u, array);
			ValidateClass(ref num8, num9, num6, num7, 6u, 15, 59u, array);
			ValidateClass(ref num7, num8, num9, num6, 13u, 21, 60u, array);
			ValidateClass(ref num6, num7, num8, num9, 4u, 6, 61u, array);
			ValidateClass(ref num9, num6, num7, num8, 11u, 10, 62u, array);
			ValidateClass(ref num8, num9, num6, num7, 2u, 15, 63u, array);
			ValidateClass(ref num7, num8, num9, num6, 9u, 21, 64u, array);
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
	private static void CalcClass(ref uint P_0, uint P_1, uint P_2, uint P_3, uint P_4, ushort P_5, uint P_6, object P_7)
	{
		P_0 = P_1 + ExcludeClass(P_0 + ((P_1 & P_2) | (~P_1 & P_3)) + ((uint[])P_7)[P_4] + ((uint[])dispatcherRepository)[P_6 - 1], P_5);
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private static void OrderClass(ref uint P_0, uint P_1, uint P_2, uint P_3, uint P_4, ushort P_5, uint P_6, object P_7)
	{
		P_0 = P_1 + ExcludeClass(P_0 + ((P_1 & P_3) | (P_2 & ~P_3)) + ((uint[])P_7)[P_4] + ((uint[])dispatcherRepository)[P_6 - 1], P_5);
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private static void CreateClass(ref uint P_0, uint P_1, uint P_2, uint P_3, uint P_4, ushort P_5, uint P_6, object P_7)
	{
		P_0 = P_1 + ExcludeClass(P_0 + (P_1 ^ P_2 ^ P_3) + ((uint[])P_7)[P_4] + ((uint[])dispatcherRepository)[P_6 - 1], P_5);
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private static void ValidateClass(ref uint P_0, uint P_1, uint P_2, uint P_3, uint P_4, ushort P_5, uint P_6, object P_7)
	{
		P_0 = P_1 + ExcludeClass(P_0 + (P_2 ^ (P_1 | ~P_3)) + ((uint[])P_7)[P_4] + ((uint[])dispatcherRepository)[P_6 - 1], P_5);
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private static uint ExcludeClass(uint P_0, ushort P_1)
	{
		return (P_0 >> 32 - P_1) | (P_0 << (int)P_1);
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool ConnectClass()
	{
		if (!_FieldRepository)
		{
			SortClass();
			_FieldRepository = true;
		}
		return m_AccountRepository;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static void SortClass()
	{
		try
		{
			new MD5CryptoServiceProvider();
		}
		catch
		{
			m_AccountRepository = true;
			return;
		}
		try
		{
			m_AccountRepository = (bool)Type.GetTypeFromHandle(ProcessRepository.e53w34m968awCm9P85taUZe(16777411)).Assembly.GetType("System.Security.Cryptography.CryptoConfig", throwOnError: false).GetMethod("get_AllowOnlyFipsAlgorithms", BindingFlags.Static | BindingFlags.Public).Invoke(null, new object[0]);
		}
		catch
		{
		}
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static SymmetricAlgorithm WriteClass()
	{
		SymmetricAlgorithm symmetricAlgorithm = null;
		if (ConnectClass())
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
	internal static byte[] CalculateClass(object P_0)
	{
		if (!ConnectClass())
		{
			return new MD5CryptoServiceProvider().ComputeHash((byte[])P_0);
		}
		return AwakeClass(P_0);
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	static bool DestroyClass(int P_0)
	{
		int num = 5;
		if (IncludeObserver())
		{
			goto IL_001a;
		}
		goto IL_1784;
		IL_001a:
		if (((Array)_ContextRepository).Length != 0)
		{
			goto IL_176b;
		}
		_ = 1;
		if (!IncludeObserver())
		{
			num = 4;
		}
		else
		{
			num = 6;
			if (!ExcludeObserver())
			{
				goto IL_176b;
			}
		}
		goto IL_1784;
		IL_17b7:
		predicateRepository = SetupClass(ConcatClass(typeof(ThreadIndexerContainer).Assembly).ToString());
		int num2 = 3;
		goto IL_1788;
		IL_176b:
		if (((Array)predicateRepository).Length == 0)
		{
			goto IL_17b7;
		}
		goto IL_17e4;
		IL_17e4:
		int num3 = 0;
		num = 7;
		if (ExcludeObserver())
		{
			goto IL_1784;
		}
		goto IL_17b7;
		IL_1784:
		num2 = num;
		goto IL_1788;
		IL_1788:
		bool result = default(bool);
		while (true)
		{
			switch (num2)
			{
			case 5:
				break;
			case 1:
			case 4:
			{
				BinaryReader binaryReader = new BinaryReader(typeof(ThreadIndexerContainer).Assembly.GetManifestResourceStream("56bd827b-5b5e-4d84-acd3-02144d8f6654"));
				binaryReader.BaseStream.Position = 0L;
				byte[] array = binaryReader.ReadBytes((int)binaryReader.BaseStream.Length);
				byte[] array2 = new byte[32];
				array2[0] = 146;
				array2[0] = 94;
				int num6 = 47 + 116;
				array2[0] = (byte)num6;
				num6 = 117 - 116;
				array2[0] = (byte)num6;
				array2[1] = 52;
				num6 = 125 - 41;
				array2[1] = (byte)num6;
				array2[1] = 83;
				num6 = 9 + 117;
				array2[1] = (byte)num6;
				array2[2] = 168;
				num6 = 164 - 54;
				array2[2] = (byte)num6;
				array2[2] = 217;
				num6 = 170 - 56;
				array2[3] = (byte)num6;
				num6 = 144 - 48;
				array2[3] = (byte)num6;
				array2[3] = 125;
				array2[3] = 155;
				array2[3] = 159;
				array2[4] = 168;
				num6 = 16 + 13;
				array2[4] = (byte)num6;
				num6 = 228 - 76;
				array2[4] = (byte)num6;
				array2[4] = 125;
				array2[4] = 44;
				array2[5] = 133;
				array2[5] = 90;
				num6 = 132 + 48;
				array2[5] = (byte)num6;
				array2[6] = 156;
				array2[6] = 114;
				array2[6] = 125;
				array2[6] = 73;
				array2[6] = 158;
				array2[6] = 98;
				array2[7] = 103;
				array2[7] = 125;
				num6 = 38 + 85;
				array2[7] = (byte)num6;
				array2[7] = 140;
				num6 = 172 + 20;
				array2[7] = (byte)num6;
				array2[8] = 108;
				array2[8] = 127;
				num6 = 123 + 17;
				array2[8] = (byte)num6;
				array2[9] = 162;
				array2[9] = 176;
				num6 = 113 + 47;
				array2[9] = (byte)num6;
				array2[9] = 102;
				array2[9] = 185;
				num6 = 35 + 8;
				array2[10] = (byte)num6;
				num6 = 109 + 17;
				array2[10] = (byte)num6;
				num6 = 190 - 103;
				array2[10] = (byte)num6;
				array2[11] = 23;
				num6 = 175 - 58;
				array2[11] = (byte)num6;
				array2[11] = 132;
				num6 = 26 + 99;
				array2[11] = (byte)num6;
				num6 = 91 + 61;
				array2[11] = (byte)num6;
				array2[12] = 159;
				array2[12] = 154;
				num6 = 78 - 53;
				array2[12] = (byte)num6;
				num6 = 22 + 43;
				array2[13] = (byte)num6;
				array2[13] = 108;
				array2[13] = 143;
				array2[13] = 99;
				array2[13] = 37;
				array2[13] = 35;
				num6 = 47 + 69;
				array2[14] = (byte)num6;
				num6 = 82 + 22;
				array2[14] = (byte)num6;
				array2[14] = 121;
				array2[14] = 95;
				array2[14] = 80;
				num6 = 95 + 121;
				array2[15] = (byte)num6;
				num6 = 154 - 51;
				array2[15] = (byte)num6;
				array2[15] = 109;
				num6 = 110 + 91;
				array2[15] = (byte)num6;
				num6 = 205 - 68;
				array2[15] = (byte)num6;
				num6 = 187 + 4;
				array2[15] = (byte)num6;
				num6 = 6 + 0;
				array2[16] = (byte)num6;
				num6 = 90 + 109;
				array2[16] = (byte)num6;
				num6 = 74 + 25;
				array2[16] = (byte)num6;
				array2[16] = 112;
				array2[16] = 35;
				num6 = 143 + 39;
				array2[16] = (byte)num6;
				array2[17] = 154;
				array2[17] = 99;
				array2[17] = 152;
				num6 = 122 + 111;
				array2[17] = (byte)num6;
				array2[17] = 105;
				num6 = 92 + 24;
				array2[18] = (byte)num6;
				num6 = 187 - 62;
				array2[18] = (byte)num6;
				array2[18] = 124;
				array2[18] = 130;
				num6 = 11 + 15;
				array2[19] = (byte)num6;
				num6 = 121 + 109;
				array2[19] = (byte)num6;
				num6 = 171 - 57;
				array2[19] = (byte)num6;
				num6 = 125 + 2;
				array2[19] = (byte)num6;
				array2[20] = 179;
				array2[20] = 100;
				num6 = 151 - 50;
				array2[20] = (byte)num6;
				array2[20] = 154;
				array2[20] = 232;
				num6 = 170 - 86;
				array2[20] = (byte)num6;
				num6 = 180 - 60;
				array2[21] = (byte)num6;
				array2[21] = 132;
				array2[21] = 94;
				array2[21] = 90;
				num6 = 222 + 2;
				array2[21] = (byte)num6;
				num6 = 119 + 72;
				array2[22] = (byte)num6;
				array2[22] = 95;
				num6 = 181 - 103;
				array2[22] = (byte)num6;
				num6 = 126 - 42;
				array2[23] = (byte)num6;
				array2[23] = 118;
				array2[23] = 178;
				array2[24] = 69;
				array2[24] = 88;
				num6 = 51 + 121;
				array2[24] = (byte)num6;
				num6 = 175 - 94;
				array2[24] = (byte)num6;
				array2[25] = 162;
				num6 = 110 + 93;
				array2[25] = (byte)num6;
				array2[25] = 105;
				num6 = 11 + 81;
				array2[25] = (byte)num6;
				num6 = 132 + 12;
				array2[25] = (byte)num6;
				num6 = 199 - 66;
				array2[26] = (byte)num6;
				num6 = 156 - 52;
				array2[26] = (byte)num6;
				array2[26] = 134;
				num6 = 134 - 44;
				array2[26] = (byte)num6;
				array2[26] = 80;
				num6 = 188 + 36;
				array2[26] = (byte)num6;
				array2[27] = 102;
				num6 = 22 + 62;
				array2[27] = (byte)num6;
				num6 = 213 - 71;
				array2[27] = (byte)num6;
				num6 = 111 + 94;
				array2[27] = (byte)num6;
				num6 = 122 - 21;
				array2[27] = (byte)num6;
				array2[28] = 113;
				num6 = 199 - 66;
				array2[28] = (byte)num6;
				num6 = 8 + 95;
				array2[28] = (byte)num6;
				num6 = 55 + 120;
				array2[28] = (byte)num6;
				num6 = 158 - 45;
				array2[28] = (byte)num6;
				num6 = 20 + 79;
				array2[29] = (byte)num6;
				array2[29] = 128;
				num6 = 57 + 30;
				array2[29] = (byte)num6;
				array2[29] = 248;
				num6 = 224 - 74;
				array2[30] = (byte)num6;
				array2[30] = 159;
				num6 = 96 + 121;
				array2[30] = (byte)num6;
				array2[30] = 92;
				array2[30] = 241;
				num6 = 195 - 65;
				array2[31] = (byte)num6;
				array2[31] = 146;
				num6 = 160 - 53;
				array2[31] = (byte)num6;
				num6 = 85 + 101;
				array2[31] = (byte)num6;
				num6 = 67 + 102;
				array2[31] = (byte)num6;
				num6 = 121 + 107;
				array2[31] = (byte)num6;
				byte[] rgbKey = array2;
				byte[] array3 = new byte[16]
				{
					72, 0, 0, 0, 0, 0, 0, 0, 0, 0,
					0, 0, 0, 0, 0, 0
				};
				int num7 = 48 + 4;
				array3[0] = (byte)num7;
				array3[0] = 161;
				int num8 = 13 + 27;
				array3[0] = (byte)num8;
				num7 = 249 - 83;
				array3[0] = (byte)num7;
				array3[0] = 221;
				array3[1] = 81;
				array3[1] = 122;
				array3[1] = 117;
				array3[1] = 105;
				num8 = 30 + 77;
				array3[1] = (byte)num8;
				array3[1] = 254;
				num8 = 161 - 53;
				array3[2] = (byte)num8;
				num8 = 162 - 54;
				array3[2] = (byte)num8;
				array3[2] = 126;
				num7 = 136 - 98;
				array3[2] = (byte)num7;
				num7 = 50 + 121;
				array3[3] = (byte)num7;
				num7 = 167 - 55;
				array3[3] = (byte)num7;
				num7 = 254 - 84;
				array3[3] = (byte)num7;
				array3[3] = 220;
				array3[4] = 94;
				num7 = 100 + 61;
				array3[4] = (byte)num7;
				num8 = 84 + 80;
				array3[4] = (byte)num8;
				num7 = 122 + 83;
				array3[4] = (byte)num7;
				num7 = 207 - 69;
				array3[5] = (byte)num7;
				num8 = 251 - 83;
				array3[5] = (byte)num8;
				num8 = 26 + 104;
				array3[5] = (byte)num8;
				num7 = 38 - 8;
				array3[5] = (byte)num7;
				array3[6] = 59;
				num8 = 1 + 71;
				array3[6] = (byte)num8;
				num7 = 140 - 46;
				array3[6] = (byte)num7;
				array3[6] = 169;
				array3[6] = 49;
				num8 = 86 - 23;
				array3[6] = (byte)num8;
				array3[7] = 152;
				array3[7] = 122;
				num8 = 195 - 65;
				array3[7] = (byte)num8;
				array3[7] = 126;
				num8 = 27 + 3;
				array3[7] = (byte)num8;
				array3[7] = 6;
				num7 = 179 - 59;
				array3[8] = (byte)num7;
				num7 = 118 + 63;
				array3[8] = (byte)num7;
				num7 = 49 + 103;
				array3[8] = (byte)num7;
				array3[8] = 115;
				num7 = 64 + 1;
				array3[9] = (byte)num7;
				num7 = 54 + 30;
				array3[9] = (byte)num7;
				array3[9] = 120;
				array3[9] = 237;
				num8 = 169 + 72;
				array3[9] = (byte)num8;
				array3[10] = 129;
				num8 = 103 + 11;
				array3[10] = (byte)num8;
				array3[10] = 62;
				array3[11] = 144;
				num7 = 135 - 45;
				array3[11] = (byte)num7;
				array3[11] = 92;
				array3[11] = 170;
				num8 = 149 - 68;
				array3[11] = (byte)num8;
				array3[12] = 97;
				array3[12] = 188;
				num8 = 22 + 24;
				array3[12] = (byte)num8;
				num8 = 93 + 24;
				array3[12] = (byte)num8;
				array3[12] = 111;
				array3[13] = 101;
				num8 = 128 - 42;
				array3[13] = (byte)num8;
				array3[13] = 130;
				array3[13] = 232;
				num7 = 222 - 74;
				array3[14] = (byte)num7;
				array3[14] = 162;
				array3[14] = 78;
				array3[14] = 95;
				num8 = 236 - 78;
				array3[14] = (byte)num8;
				num7 = 52 - 28;
				array3[14] = (byte)num7;
				num7 = 240 - 80;
				array3[15] = (byte)num7;
				array3[15] = 156;
				array3[15] = 146;
				array3[15] = 94;
				num7 = 112 + 111;
				array3[15] = (byte)num7;
				array3[15] = 68;
				byte[] array4 = array3;
				byte[] publicKeyToken = typeof(ThreadIndexerContainer).Assembly.GetName().GetPublicKeyToken();
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
				SymmetricAlgorithm symmetricAlgorithm = WriteClass();
				symmetricAlgorithm.Mode = CipherMode.CBC;
				ICryptoTransform transform = symmetricAlgorithm.CreateDecryptor(rgbKey, array4);
				MemoryStream memoryStream = new MemoryStream();
				CryptoStream cryptoStream = new CryptoStream(memoryStream, transform, CryptoStreamMode.Write);
				cryptoStream.Write(array, 0, array.Length);
				cryptoStream.FlushFinalBlock();
				_ContextRepository = memoryStream.ToArray();
				memoryStream.Close();
				cryptoStream.Close();
				binaryReader.Close();
				goto IL_176b;
			}
			case 2:
			case 6:
				goto IL_176b;
			default:
				num2 = 0;
				continue;
			case 0:
				goto IL_17b7;
			case 3:
				goto IL_17e4;
			case 7:
				try
				{
					num3 = BitConverter.ToInt32(new byte[4]
					{
						((byte[])_ContextRepository)[P_0],
						((byte[])_ContextRepository)[P_0 + 1],
						((byte[])_ContextRepository)[P_0 + 2],
						((byte[])_ContextRepository)[P_0 + 3]
					}, 0);
				}
				catch
				{
				}
				try
				{
					if (((byte[])predicateRepository)[num3] == 128)
					{
						_ = 0;
						int num5;
						if (ExcludeObserver())
						{
							int num4 = 2;
							num5 = num4;
						}
						else
						{
							num5 = 3;
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
		goto IL_001a;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	static string FindClass(int P_0)
	{
		int num = 3;
		if (false)
		{
			goto IL_0016;
		}
		goto IL_1768;
		IL_0016:
		BinaryReader binaryReader = default(BinaryReader);
		binaryReader.Close();
		int num2 = 110;
		goto IL_176c;
		IL_176c:
		int num8 = default(int);
		int num7 = default(int);
		byte[] array3 = default(byte[]);
		int num3 = default(int);
		byte[] array4 = default(byte[]);
		byte[] array2 = default(byte[]);
		byte[] publicKeyToken = default(byte[]);
		int num18 = default(int);
		int num14 = default(int);
		int num25 = default(int);
		uint num19 = default(uint);
		uint num26 = default(uint);
		byte[] array6 = default(byte[]);
		int num10 = default(int);
		uint num11 = default(uint);
		uint num27 = default(uint);
		int num23 = default(int);
		int num12 = default(int);
		int num21 = default(int);
		byte[] array = default(byte[]);
		uint num16 = default(uint);
		int num13 = default(int);
		uint num15 = default(uint);
		int num22 = default(int);
		byte[] array7 = default(byte[]);
		int num17 = default(int);
		uint num20 = default(uint);
		uint num24 = default(uint);
		MemoryStream memoryStream = default(MemoryStream);
		ICryptoTransform transform = default(ICryptoTransform);
		int num4 = default(int);
		while (true)
		{
			int num9;
			switch (num2)
			{
			case 411:
				break;
			case 311:
				goto IL_0026;
			case 363:
				num8 = 139 - 53;
				num9 = 66;
				goto IL_1764;
			case 398:
				num7 = 67 + 91;
				num = 368;
				goto IL_1768;
			case 91:
				array3[4] = (byte)num7;
				num2 = 341;
				continue;
			case 409:
				array3[19] = 50;
				num2 = 200;
				continue;
			case 107:
				num3 = 226 - 75;
				num2 = 217;
				continue;
			case 132:
				array3[13] = 120;
				num9 = 395;
				goto IL_1764;
			case 15:
				array4[10] = 137;
				num2 = 190;
				continue;
			case 308:
				array3[2] = 128;
				num = 94;
				if (1 == 0)
				{
					goto case 45;
				}
				goto IL_1768;
			case 45:
				array3[27] = (byte)num7;
				num = 111;
				goto IL_1768;
			case 141:
				array4[8] = 158;
				num9 = 399;
				goto IL_1764;
			case 390:
				num3 = 27 + 89;
				num2 = 326;
				continue;
			case 167:
				array2[1] = publicKeyToken[0];
				num = 346;
				if (1 == 0)
				{
					goto case 26;
				}
				goto IL_1768;
			case 26:
				num7 = 109 + 46;
				num = 90;
				goto IL_1768;
			case 345:
				array3[31] = (byte)num7;
				num = 76;
				if (false)
				{
					goto case 242;
				}
				goto IL_1768;
			case 242:
				array4[3] = 104;
				num = 175;
				if (ResolveObserver())
				{
					goto case 14;
				}
				goto IL_1768;
			case 253:
				num18++;
				num = 279;
				goto IL_1768;
			case 7:
				num7 = 41 + 39;
				num9 = 55;
				goto IL_1764;
			case 254:
				array3[17] = (byte)num7;
				num9 = 350;
				goto IL_1764;
			case 391:
				array3[23] = 191;
				num9 = 178;
				goto IL_1764;
			case 207:
				array3[25] = 129;
				num9 = 154;
				goto IL_1764;
			case 187:
				num7 = 6 + 86;
				num2 = 413;
				continue;
			case 81:
				array4[2] = 55;
				num2 = 74;
				continue;
			case 387:
				array4[11] = (byte)num3;
				num = 35;
				goto IL_1768;
			case 96:
				num7 = 193 + 42;
				num = 255;
				if (ResolveObserver())
				{
					goto case 145;
				}
				goto IL_1768;
			case 145:
				num3 = 216 - 72;
				num = 137;
				if (CalcObserver())
				{
					goto IL_1768;
				}
				goto case 12;
			case 190:
				num3 = 93 + 22;
				num2 = 410;
				continue;
			case 382:
				num8 = 194 - 97;
				num2 = 140;
				continue;
			case 239:
				num8 = 113 + 38;
				num2 = 199;
				continue;
			case 199:
				array4[4] = (byte)num8;
				num = 206;
				if (false)
				{
					goto case 116;
				}
				goto IL_1768;
			case 116:
				array3[28] = 109;
				num = 28;
				if (!ResolveObserver())
				{
					goto IL_1768;
				}
				goto case 12;
			case 78:
				array3[22] = 167;
				num9 = 383;
				goto IL_1764;
			case 122:
				array3[15] = 230;
				num2 = 325;
				continue;
			case 184:
				array4[13] = (byte)num8;
				num2 = 67;
				continue;
			case 222:
				array4[9] = 98;
				num2 = 344;
				continue;
			case 109:
				num14++;
				num9 = 108;
				goto IL_1764;
			case 153:
				array3[5] = (byte)num7;
				num9 = 263;
				goto IL_1764;
			case 235:
				num25 = 0;
				num9 = 280;
				goto IL_1764;
			case 287:
				array3[7] = 129;
				num = 340;
				if (!CalcObserver())
				{
					goto case 60;
				}
				goto IL_1768;
			case 133:
				array2[9] = publicKeyToken[4];
				num9 = 0;
				goto IL_1764;
			case 147:
				array3[5] = 132;
				num = 324;
				if (1 == 0)
				{
					goto case 212;
				}
				goto IL_1768;
			case 212:
				array3[2] = (byte)num7;
				num = 106;
				if (false)
				{
					goto case 251;
				}
				goto IL_1768;
			case 251:
			case 313:
				num3 = 25 + 10;
				num2 = 104;
				continue;
			case 414:
				array3[10] = (byte)num7;
				num2 = 241;
				continue;
			case 47:
				array3[24] = 111;
				num9 = 83;
				goto IL_1764;
			case 401:
				array3[12] = (byte)num7;
				num2 = 398;
				continue;
			case 381:
				array3[15] = 84;
				num = 165;
				if (!CalcObserver())
				{
					goto case 77;
				}
				goto IL_1768;
			case 234:
				array3[21] = 107;
				num2 = 360;
				continue;
			case 0:
				array2[11] = publicKeyToken[5];
				num = 278;
				goto IL_1768;
			case 126:
				array4[6] = 113;
				num = 221;
				if (!CalcObserver())
				{
					goto case 395;
				}
				goto IL_1768;
			case 404:
				array4[13] = 123;
				num = 306;
				goto IL_1768;
			case 164:
				num7 = 147 - 49;
				num = 305;
				goto IL_1768;
			case 103:
				num7 = 4 + 41;
				num = 31;
				if (ResolveObserver())
				{
					goto case 78;
				}
				goto IL_1768;
			case 369:
				array3[23] = 86;
				num9 = 47;
				goto IL_1764;
			case 142:
				num19 += num26;
				num9 = 193;
				goto IL_1764;
			case 23:
				array3[20] = (byte)num7;
				num2 = 2;
				continue;
			case 407:
				num7 = 253 - 84;
				num2 = 162;
				continue;
			case 347:
				array3[12] = 111;
				num2 = 166;
				continue;
			case 327:
				num3 = 125 - 41;
				num2 = 205;
				continue;
			case 114:
				num7 = 89 + 110;
				num2 = 374;
				continue;
			case 371:
				array6[num10 + 1] = (byte)((num11 & 0xFF00) >> 8);
				num = 117;
				goto IL_1768;
			case 213:
				num7 = 108 + 69;
				num = 64;
				goto IL_1768;
			case 380:
			{
				uint num28 = num27;
				uint num29 = num27;
				uint num30 = 399522727u;
				uint num31 = 1175363962u;
				uint num32 = 656276816u;
				uint num33 = 297323369u;
				uint num34 = num29;
				uint num35 = 1356102888u;
				ulong num36 = num31 * 371293044;
				num36 |= 1;
				num33 = (uint)(num33 * num33 % num36);
				uint num37 = ((num32 >> 5) | (num32 << 27)) + num30;
				uint num38 = num37 & 0x55555555;
				num37 &= 0xAAAAAAAAu;
				num32 = (num37 >> 1) | (num38 << 1);
				if ((double)num30 == 0.0)
				{
					num30--;
				}
				uint num39 = (uint)(64079.0 / (double)num30 + (double)num30);
				num30 = (uint)((uint)((short)num33 + (ushort)num33 + (int)num39) + (short)num33);
				num31 += num33;
				ulong num40 = num33 * num33;
				if (num40 == 0)
				{
					num40--;
				}
				num35 = (uint)(num35 * num35 % num40);
				num34 ^= num34 << 9;
				num34 += num30;
				num34 ^= num34 >> 21;
				num34 += num31;
				num34 ^= num34 << 2;
				num34 += num35;
				num34 = (((num33 << 6) + num33) ^ num31) + num34;
				num27 = num28 + (uint)(double)num34;
				num2 = 163;
				continue;
			}
			case 274:
				num23++;
				num = 12;
				goto IL_1768;
			case 34:
				array3[3] = (byte)num7;
				num = 96;
				if (!CalcObserver())
				{
					goto case 164;
				}
				goto IL_1768;
			case 339:
				array3[25] = 123;
				num9 = 11;
				goto IL_1764;
			case 232:
				num7 = 48 + 48;
				num = 72;
				if (1 == 0)
				{
					goto case 64;
				}
				goto IL_1768;
			case 64:
				array3[6] = (byte)num7;
				num9 = 7;
				goto IL_1764;
			case 341:
				array3[4] = 161;
				num = 276;
				if (1 == 0)
				{
					goto case 298;
				}
				goto IL_1768;
			case 298:
				array3[5] = 158;
				num = 173;
				if (1 == 0)
				{
					goto case 335;
				}
				goto IL_1768;
			case 335:
				array3[31] = 96;
				num = 54;
				if (1 == 0)
				{
					goto case 295;
				}
				goto IL_1768;
			case 295:
				array4[6] = 57;
				num = 126;
				if (ResolveObserver())
				{
					goto case 124;
				}
				goto IL_1768;
			case 124:
				array3[26] = (byte)num7;
				num2 = 86;
				continue;
			case 395:
				num7 = 190 - 63;
				num = 290;
				if (ResolveObserver())
				{
					goto case 356;
				}
				goto IL_1768;
			case 356:
				array3[6] = 91;
				num = 53;
				if (1 == 0)
				{
					goto case 240;
				}
				goto IL_1768;
			case 240:
				num7 = 53 + 19;
				num9 = 264;
				goto IL_1764;
			case 185:
				array3[29] = 129;
				num2 = 151;
				continue;
			case 325:
				num7 = 122 + 113;
				num9 = 176;
				goto IL_1764;
			case 79:
				num7 = 130 - 43;
				num2 = 412;
				continue;
			case 40:
			case 275:
				if (num12 >= num21)
				{
					num = 58;
					if (false)
					{
						goto case 165;
					}
					goto IL_1768;
				}
				if (num12 > 0)
				{
					num2 = 268;
					continue;
				}
				goto case 282;
			case 165:
				array3[15] = 164;
				num9 = 27;
				goto IL_1764;
			case 60:
				array3[24] = 168;
				num9 = 8;
				goto IL_1764;
			case 328:
				num26 = (uint)((array[num16 + 3] << 24) | (array[num16 + 2] << 16) | (array[num16 + 1] << 8) | array[num16]);
				num2 = 285;
				continue;
			case 353:
				num13 = 0;
				num = 14;
				if (!ResolveObserver())
				{
					goto IL_1768;
				}
				goto case 112;
			case 65:
				array3[7] = (byte)num7;
				num2 = 299;
				continue;
			case 157:
				array2[5] = publicKeyToken[2];
				num2 = 230;
				continue;
			case 135:
				num7 = 175 + 9;
				num = 389;
				goto IL_1768;
			case 83:
				array3[24] = 140;
				num2 = 60;
				continue;
			case 30:
				num7 = 68 + 47;
				num9 = 16;
				goto IL_1764;
			case 4:
				num3 = 161 - 53;
				num = 171;
				goto IL_1768;
			case 221:
				num3 = 196 - 116;
				num = 265;
				goto IL_1768;
			case 340:
				num7 = 76 + 75;
				num9 = 65;
				goto IL_1764;
			case 71:
				array3[1] = 108;
				num9 = 24;
				goto IL_1764;
			case 406:
				array3[18] = (byte)num7;
				num9 = 338;
				goto IL_1764;
			case 55:
				array3[6] = (byte)num7;
				num = 356;
				goto IL_1768;
			case 104:
				array4[2] = (byte)num3;
				num = 81;
				if (false)
				{
					goto case 224;
				}
				goto IL_1768;
			case 224:
				num7 = 107 + 53;
				num9 = 23;
				goto IL_1764;
			case 231:
				num7 = 224 - 74;
				num9 = 45;
				goto IL_1764;
			case 140:
				array4[15] = (byte)num8;
				num9 = 48;
				goto IL_1764;
			case 77:
				num7 = 93 + 28;
				num = 134;
				if (1 == 0)
				{
					goto case 46;
				}
				goto IL_1768;
			case 46:
				array3[7] = (byte)num7;
				num = 287;
				goto IL_1768;
			case 19:
				array3[21] = (byte)num7;
				num9 = 349;
				goto IL_1764;
			case 300:
				array4[1] = (byte)num8;
				num9 = 57;
				goto IL_1764;
			case 139:
				array3[25] = (byte)num7;
				num = 207;
				if (1 == 0)
				{
					goto case 8;
				}
				goto IL_1768;
			case 8:
				num7 = 13 + 25;
				num9 = 304;
				goto IL_1764;
			case 95:
				num7 = 7 + 39;
				num9 = 93;
				goto IL_1764;
			case 323:
				array3[9] = (byte)num7;
				num9 = 244;
				goto IL_1764;
			case 39:
				array3[20] = (byte)num7;
				num9 = 224;
				goto IL_1764;
			case 99:
				num8 = 144 + 84;
				num = 333;
				if (false)
				{
					goto case 405;
				}
				goto IL_1768;
			case 405:
				array3[3] = (byte)num7;
				num2 = 215;
				continue;
			case 35:
				array4[11] = 146;
				num9 = 214;
				goto IL_1764;
			case 280:
				if (num13 != num14 - 1)
				{
					goto IL_120d;
				}
				num = 17;
				if (ResolveObserver())
				{
					goto case 308;
				}
				goto IL_1768;
			case 412:
				array3[0] = (byte)num7;
				num9 = 201;
				goto IL_1764;
			case 90:
				array3[16] = (byte)num7;
				num = 105;
				if (ResolveObserver())
				{
					goto case 132;
				}
				goto IL_1768;
			case 17:
				if (num21 <= 0)
				{
					goto IL_120d;
				}
				num = 181;
				goto IL_1768;
			case 125:
				num8 = 114 - 46;
				num = 36;
				goto IL_1768;
			case 215:
				num7 = 26 + 121;
				num = 34;
				if (ResolveObserver())
				{
					goto case 181;
				}
				goto IL_1768;
			case 181:
				num15 = 0u;
				num = 142;
				goto IL_1768;
			case 156:
				array3[18] = 130;
				num9 = 87;
				goto IL_1764;
			case 307:
				num22 = array.Length / 4;
				num9 = 42;
				goto IL_1764;
			case 183:
				num7 = 223 - 74;
				num2 = 323;
				continue;
			case 238:
				array3[23] = (byte)num7;
				num2 = 59;
				continue;
			case 373:
				array4[14] = (byte)num8;
				num = 149;
				if (!CalcObserver())
				{
					goto case 388;
				}
				goto IL_1768;
			case 196:
				array3[26] = (byte)num7;
				num = 270;
				goto IL_1768;
			case 163:
				num19 = num27;
				num2 = 294;
				continue;
			case 197:
				array3[29] = 91;
				num2 = 354;
				continue;
			case 12:
			case 227:
				if (num23 >= num21)
				{
					num = 378;
					if (false)
					{
						goto case 2;
					}
				}
				else
				{
					if (num23 <= 0)
					{
						goto case 21;
					}
					num = 296;
				}
				goto IL_1768;
			case 2:
				array3[21] = 94;
				num2 = 218;
				continue;
			case 5:
				array6 = new byte[array7.Length];
				num9 = 307;
				goto IL_1764;
			case 62:
				num8 = 84 + 47;
				num9 = 373;
				goto IL_1764;
			case 110:
				array7 = (byte[])advisorRepository;
				num = 6;
				if (!CalcObserver())
				{
					goto case 103;
				}
				goto IL_1768;
			case 182:
				array4[10] = 114;
				num = 195;
				if (ResolveObserver())
				{
					goto case 244;
				}
				goto IL_1768;
			case 244:
				num7 = 98 + 121;
				num = 119;
				if (1 == 0)
				{
					goto case 69;
				}
				goto IL_1768;
			case 69:
				num7 = 253 - 84;
				num2 = 220;
				continue;
			case 70:
				array3[5] = (byte)num7;
				num9 = 147;
				goto IL_1764;
			case 180:
				num7 = 2 + 81;
				num9 = 118;
				goto IL_1764;
			case 173:
				num7 = 4 + 1;
				num = 70;
				if (1 == 0)
				{
					goto case 44;
				}
				goto IL_1768;
			case 44:
				array7 = binaryReader.ReadBytes((int)binaryReader.BaseStream.Length);
				num = 136;
				goto IL_1768;
			case 329:
				array3[17] = 94;
				num2 = 209;
				continue;
			case 209:
				num7 = 101 + 103;
				num2 = 254;
				continue;
			case 105:
				num7 = 8 + 86;
				num = 127;
				if (false)
				{
					goto case 246;
				}
				goto IL_1768;
			case 246:
				publicKeyToken = typeof(ThreadIndexerContainer).Assembly.GetName().GetPublicKeyToken();
				num = 237;
				if (1 == 0)
				{
					goto case 217;
				}
				goto IL_1768;
			case 217:
				array4[0] = (byte)num3;
				num2 = 331;
				continue;
			case 172:
				array3[22] = (byte)num7;
				num = 358;
				if (true)
				{
					goto IL_1768;
				}
				goto case 58;
			case 220:
				array3[30] = (byte)num7;
				num = 161;
				goto IL_1768;
			case 129:
				num14 = array7.Length / 4;
				num9 = 5;
				goto IL_1764;
			case 54:
				array = array3;
				num2 = 236;
				continue;
			case 385:
				num7 = 210 - 70;
				num = 158;
				goto IL_1768;
			case 14:
			case 20:
				if (num13 < num14)
				{
					num17 = num13 % num22;
					num9 = 144;
				}
				else
				{
					num9 = 98;
				}
				goto IL_1764;
			case 362:
				array4[2] = (byte)num8;
				num = 315;
				if (!CalcObserver())
				{
					goto case 366;
				}
				goto IL_1768;
			case 366:
				array3[8] = (byte)num7;
				num9 = 164;
				goto IL_1764;
			case 32:
				array4[2] = (byte)num3;
				num = 343;
				if (ResolveObserver())
				{
					goto case 110;
				}
				goto IL_1768;
			case 285:
				num20 = 255u;
				num = 235;
				if (!ResolveObserver())
				{
					goto IL_1768;
				}
				goto case 111;
			case 336:
				num7 = 181 - 60;
				num2 = 345;
				continue;
			case 403:
				num7 = 128 - 42;
				num2 = 297;
				continue;
			case 43:
				array3[22] = (byte)num7;
				num = 78;
				if (CalcObserver())
				{
					goto IL_1768;
				}
				goto case 257;
			case 93:
				array3[16] = (byte)num7;
				num2 = 103;
				continue;
			case 155:
				array3[15] = 214;
				num2 = 381;
				continue;
			case 177:
				array2[15] = publicKeyToken[7];
				num = 131;
				goto IL_1768;
			case 63:
				array3[14] = 86;
				num = 114;
				if (false)
				{
					goto case 267;
				}
				goto IL_1768;
			case 267:
				array3[10] = (byte)num7;
				num = 348;
				if (false)
				{
					goto case 138;
				}
				goto IL_1768;
			case 138:
				num8 = 82 - 75;
				num9 = 179;
				goto IL_1764;
			case 376:
				array4[14] = 106;
				num = 363;
				if (ResolveObserver())
				{
					goto case 12;
				}
				goto IL_1768;
			case 1:
				num26 = 0u;
				num9 = 123;
				goto IL_1764;
			case 342:
			case 378:
				num13++;
				num = 20;
				if (CalcObserver())
				{
					goto IL_1768;
				}
				goto case 291;
			case 152:
				array3[28] = 158;
				num2 = 38;
				continue;
			case 162:
				array3[12] = (byte)num7;
				num2 = 347;
				continue;
			case 61:
				array3[6] = 84;
				num = 291;
				if (false)
				{
					goto case 211;
				}
				goto IL_1768;
			case 211:
				array4[1] = 138;
				num9 = 330;
				goto IL_1764;
			case 388:
				array3[11] = (byte)num7;
				num = 407;
				if (ResolveObserver())
				{
					goto case 191;
				}
				goto IL_1768;
			case 191:
				array3[14] = (byte)num7;
				num = 155;
				goto IL_1768;
			case 101:
				array4[3] = 62;
				num = 239;
				if (ResolveObserver())
				{
					goto case 320;
				}
				goto IL_1768;
			case 320:
				array4[10] = 176;
				num2 = 332;
				continue;
			case 146:
				array3[7] = 6;
				num = 334;
				if (ResolveObserver())
				{
					goto case 175;
				}
				goto IL_1768;
			case 175:
				num3 = 20 + 103;
				num2 = 288;
				continue;
			case 202:
				array3[15] = (byte)num7;
				num = 240;
				goto IL_1768;
			case 397:
				num8 = 108 + 36;
				num = 300;
				if (false)
				{
					goto case 168;
				}
				goto IL_1768;
			case 168:
				num3 = 146 - 48;
				num9 = 82;
				goto IL_1764;
			case 85:
				array3[9] = 80;
				num2 = 183;
				continue;
			case 282:
				num15 |= array7[^(1 + num12)];
				num = 121;
				if (1 == 0)
				{
					goto case 72;
				}
				goto IL_1768;
			case 72:
				array3[19] = (byte)num7;
				num = 409;
				if (ResolveObserver())
				{
					goto case 113;
				}
				goto IL_1768;
			case 113:
				array4[4] = (byte)num3;
				num = 372;
				if (false)
				{
					goto case 73;
				}
				goto IL_1768;
			case 73:
				num7 = 160 - 53;
				num2 = 406;
				continue;
			case 302:
				num25 += 8;
				num = 21;
				if (false)
				{
					goto case 131;
				}
				goto IL_1768;
			case 131:
				num18 = 0;
				num9 = 293;
				goto IL_1764;
			case 273:
				binaryReader = new BinaryReader(typeof(ThreadIndexerContainer).Assembly.GetManifestResourceStream("ef6cda30-8fbf-4df7-802f-b0604668c7e0"));
				num2 = 50;
				continue;
			case 350:
				num7 = 154 - 51;
				num2 = 375;
				continue;
			case 355:
				array3[16] = (byte)num7;
				num9 = 26;
				goto IL_1764;
			case 359:
				array6[num10] = (byte)(num11 & 0xFF);
				num = 371;
				goto IL_1768;
			case 358:
				num7 = 170 - 56;
				num = 238;
				if (!CalcObserver())
				{
					goto case 38;
				}
				goto IL_1768;
			case 38:
				array3[28] = 46;
				goto case 361;
			default:
				num2 = 361;
				continue;
			case 36:
				array4[7] = (byte)num8;
				num = 309;
				if (0 == 0)
				{
					goto IL_1768;
				}
				goto case 100;
			case 100:
				array3[1] = (byte)num7;
				num9 = 52;
				goto IL_1764;
			case 318:
				num19++;
				num = 380;
				goto IL_1768;
			case 402:
				num7 = 76 + 77;
				num2 = 196;
				continue;
			case 52:
				array3[1] = 130;
				num = 71;
				if (CalcObserver())
				{
					goto IL_1768;
				}
				goto case 229;
			case 174:
				array3[27] = 149;
				num9 = 231;
				goto IL_1764;
			case 270:
				array3[26] = 158;
				num = 75;
				if (CalcObserver())
				{
					goto IL_1768;
				}
				goto case 25;
			case 25:
				array4[5] = 158;
				num9 = 292;
				goto IL_1764;
			case 66:
				array4[14] = (byte)num8;
				num = 112;
				goto IL_1768;
			case 154:
				num7 = 93 + 41;
				num9 = 311;
				goto IL_1764;
			case 304:
				array3[24] = (byte)num7;
				num9 = 187;
				goto IL_1764;
			case 317:
				array3[8] = 87;
				num9 = 322;
				goto IL_1764;
			case 3:
				if (((Array)advisorRepository).Length == 0)
				{
					num2 = 273;
					continue;
				}
				goto case 337;
			case 233:
				array3[19] = (byte)num7;
				num = 92;
				if (0 == 0)
				{
					goto IL_1768;
				}
				goto case 410;
			case 410:
				array4[10] = (byte)num3;
				num = 390;
				if (!ResolveObserver())
				{
					goto IL_1768;
				}
				goto case 384;
			case 372:
				num8 = 67 + 81;
				num2 = 29;
				continue;
			case 218:
				array3[21] = 106;
				num9 = 234;
				goto IL_1764;
			case 143:
				array4[1] = 225;
				num9 = 365;
				goto IL_1764;
			case 148:
				array3[4] = (byte)num7;
				num = 384;
				goto IL_1768;
			case 290:
				array3[14] = (byte)num7;
				num = 63;
				goto IL_1768;
			case 351:
				num7 = 196 - 65;
				num9 = 248;
				goto IL_1764;
			case 257:
				array3[8] = (byte)num7;
				num = 317;
				if (true)
				{
					goto IL_1768;
				}
				goto case 368;
			case 368:
				array3[13] = (byte)num7;
				num9 = 159;
				goto IL_1764;
			case 281:
				array4[13] = (byte)num3;
				num2 = 319;
				continue;
			case 75:
				array3[26] = 198;
				num2 = 357;
				continue;
			case 74:
				num3 = 103 + 73;
				num9 = 316;
				goto IL_1764;
			case 86:
				array3[27] = 130;
				num9 = 174;
				goto IL_1764;
			case 112:
				num8 = 193 - 64;
				num9 = 392;
				goto IL_1764;
			case 102:
				array4[9] = 124;
				num = 222;
				goto IL_1768;
			case 87:
				array3[18] = 84;
				num = 314;
				if (0 == 0)
				{
					goto IL_1768;
				}
				goto case 393;
			case 393:
				if (num21 <= 0)
				{
					goto IL_2784;
				}
				goto case 377;
			case 268:
				num15 <<= 8;
				num9 = 282;
				goto IL_1764;
			case 277:
				array3[28] = (byte)num7;
				num2 = 116;
				continue;
			case 161:
				array3[30] = 185;
				num = 180;
				if (!CalcObserver())
				{
					goto case 12;
				}
				goto IL_1768;
			case 315:
				array4[3] = 94;
				num2 = 242;
				continue;
			case 226:
				if (num21 > 0)
				{
					num9 = 109;
					goto IL_1764;
				}
				goto case 108;
			case 158:
				array3[23] = (byte)num7;
				num2 = 369;
				continue;
			case 228:
				array3[5] = 132;
				num9 = 77;
				goto IL_1764;
			case 37:
				array3[9] = 160;
				num9 = 85;
				goto IL_1764;
			case 98:
				advisorRepository = array6;
				num9 = 337;
				goto IL_1764;
			case 136:
				array3 = new byte[32];
				num2 = 79;
				continue;
			case 24:
				array3[1] = 38;
				num = 249;
				if (!ResolveObserver())
				{
					goto IL_1768;
				}
				goto case 94;
			case 94:
				num7 = 116 + 49;
				num = 212;
				if (ResolveObserver())
				{
					goto case 221;
				}
				goto IL_1768;
			case 49:
				array4[7] = 133;
				num2 = 22;
				continue;
			case 361:
				num7 = 85 + 56;
				num = 277;
				goto IL_1768;
			case 286:
				num23 = 0;
				num = 227;
				if (!ResolveObserver())
				{
					goto IL_1768;
				}
				goto case 108;
			case 108:
				num16 = 0u;
				num = 353;
				goto IL_1768;
			case 386:
				array3[17] = 112;
				num2 = 271;
				continue;
			case 11:
				num7 = 249 - 83;
				num = 139;
				goto IL_1768;
			case 229:
				array4[14] = (byte)num3;
				num9 = 376;
				goto IL_1764;
			case 130:
				num7 = 148 - 49;
				num9 = 148;
				goto IL_1764;
			case 375:
				array3[17] = (byte)num7;
				num = 386;
				if (0 == 0)
				{
					goto IL_1768;
				}
				goto case 58;
			case 58:
			case 128:
				num27 = num19;
				num = 318;
				goto IL_1768;
			case 68:
				if (publicKeyToken.Length == 0)
				{
					goto case 131;
				}
				num = 167;
				goto IL_1768;
			case 170:
				num7 = 158 + 33;
				num = 172;
				goto IL_1768;
			case 160:
				array3[22] = 140;
				num = 170;
				if (true)
				{
					goto IL_1768;
				}
				goto case 120;
			case 120:
				num7 = 165 - 55;
				num2 = 100;
				continue;
			case 134:
				array3[5] = (byte)num7;
				num = 298;
				if (!ResolveObserver())
				{
					goto IL_1768;
				}
				goto case 106;
			case 201:
				array3[0] = 214;
				num9 = 88;
				goto IL_1764;
			case 333:
				array4[5] = (byte)num8;
				num9 = 295;
				goto IL_1764;
			case 316:
				array4[2] = (byte)num3;
				num = 80;
				if (CalcObserver())
				{
					goto IL_1768;
				}
				goto case 149;
			case 149:
				num3 = 4 + 16;
				num = 229;
				if (true)
				{
					goto IL_1768;
				}
				goto case 374;
			case 374:
				array3[14] = (byte)num7;
				num2 = 188;
				continue;
			case 48:
				array2 = array4;
				num = 246;
				if (0 == 0)
				{
					goto IL_1768;
				}
				goto case 159;
			case 159:
				array3[13] = 106;
				num = 245;
				if (0 == 0)
				{
					goto IL_1768;
				}
				goto case 208;
			case 208:
				array4[13] = 126;
				num2 = 41;
				continue;
			case 338:
				num7 = 176 - 58;
				num = 89;
				if (0 == 0)
				{
					goto IL_1768;
				}
				goto case 115;
			case 115:
				if (P_0 == -1)
				{
					num2 = 252;
					continue;
				}
				goto case 6;
			case 264:
				array3[15] = (byte)num7;
				num9 = 122;
				goto IL_1764;
			case 392:
				array4[15] = (byte)num8;
				num9 = 219;
				goto IL_1764;
			case 349:
				num7 = 217 - 72;
				num9 = 43;
				goto IL_1764;
			case 322:
				array3[8] = 134;
				num = 259;
				goto IL_1768;
			case 171:
				array4[15] = (byte)num3;
				num9 = 382;
				goto IL_1764;
			case 265:
				array4[6] = (byte)num3;
				num9 = 261;
				goto IL_1764;
			case 301:
				num7 = 164 - 54;
				num = 414;
				if (CalcObserver())
				{
					goto IL_1768;
				}
				goto case 80;
			case 80:
				num8 = 109 + 99;
				num9 = 362;
				goto IL_1764;
			case 364:
				num7 = 49 + 122;
				num9 = 289;
				goto IL_1764;
			case 31:
				array3[16] = (byte)num7;
				num = 266;
				if (true)
				{
					goto IL_1768;
				}
				goto case 203;
			case 203:
				array3[25] = (byte)num7;
				num = 339;
				if (CalcObserver())
				{
					goto IL_1768;
				}
				goto case 189;
			case 189:
				array4[13] = (byte)num3;
				num9 = 208;
				goto IL_1764;
			case 255:
				array3[3] = (byte)num7;
				num = 130;
				if (0 == 0)
				{
					goto IL_1768;
				}
				goto case 332;
			case 332:
				num3 = 28 + 45;
				num = 387;
				if (ResolveObserver())
				{
					goto case 172;
				}
				goto IL_1768;
			case 261:
				array4[7] = 82;
				num = 49;
				if (ResolveObserver())
				{
					goto case 342;
				}
				goto IL_1768;
			case 82:
				array4[12] = (byte)num3;
				num = 400;
				goto IL_1768;
			case 314:
				num7 = 175 - 58;
				num = 233;
				goto IL_1768;
			case 67:
				array4[14] = 137;
				num = 62;
				if (true)
				{
					goto IL_1768;
				}
				goto case 259;
			case 259:
				num7 = 100 + 88;
				num = 366;
				goto IL_1768;
			case 319:
				num3 = 157 - 52;
				num = 189;
				if (true)
				{
					goto IL_1768;
				}
				goto case 334;
			case 334:
				num7 = 30 + 119;
				num9 = 257;
				goto IL_1764;
			case 352:
				array3[22] = (byte)num7;
				num9 = 198;
				goto IL_1764;
			case 106:
				array3[2] = 212;
				num = 169;
				if (true)
				{
					goto IL_1768;
				}
				goto case 288;
			case 288:
				array4[3] = (byte)num3;
				num9 = 408;
				goto IL_1764;
			case 367:
				num7 = 81 - 10;
				num2 = 388;
				continue;
			case 28:
				array3[28] = 34;
				num = 185;
				goto IL_1768;
			case 84:
				array3[29] = 150;
				num9 = 351;
				goto IL_1764;
			case 263:
				array3[6] = 90;
				num = 61;
				if (!CalcObserver())
				{
					goto case 380;
				}
				goto IL_1768;
			case 377:
			case 396:
				num24 = num19 ^ num15;
				num = 286;
				goto IL_1768;
			case 188:
				num7 = 77 - 11;
				num9 = 191;
				goto IL_1764;
			case 309:
				array4[8] = 160;
				num2 = 141;
				continue;
			case 192:
				array3[10] = 136;
				num9 = 364;
				goto IL_1764;
			case 27:
				num7 = 158 - 52;
				num9 = 202;
				goto IL_1764;
			case 245:
				array3[13] = 168;
				num9 = 132;
				goto IL_1764;
			case 9:
				array3[30] = 156;
				num9 = 69;
				goto IL_1764;
			case 21:
				array6[num10 + num23] = (byte)((num24 & num20) >> num25);
				num2 = 274;
				continue;
			case 223:
				num3 = 103 + 46;
				num9 = 312;
				goto IL_1764;
			case 354:
				array3[29] = 127;
				num9 = 9;
				goto IL_1764;
			case 200:
				num7 = 207 - 69;
				num = 33;
				if (!ResolveObserver())
				{
					goto IL_1768;
				}
				goto case 144;
			case 326:
				array4[10] = (byte)num3;
				num2 = 320;
				continue;
			case 291:
				num7 = 165 - 55;
				num9 = 260;
				goto IL_1764;
			case 258:
				num7 = 11 + 87;
				num2 = 39;
				continue;
			case 346:
				array2[3] = publicKeyToken[1];
				num2 = 157;
				continue;
			case 127:
				array3[17] = (byte)num7;
				num2 = 329;
				continue;
			case 249:
				num7 = 184 - 61;
				num9 = 394;
				goto IL_1764;
			case 289:
				array3[10] = (byte)num7;
				num = 301;
				goto IL_1768;
			case 343:
				array4[2] = 105;
				_ = 1;
				if (ResolveObserver())
				{
					num = 377;
					if (!ResolveObserver())
					{
						goto IL_1768;
					}
					goto case 150;
				}
				num9 = 313;
				goto IL_1764;
			case 384:
				num7 = 77 + 31;
				num2 = 91;
				continue;
			case 117:
				array6[num10 + 2] = (byte)((num11 & 0xFF0000) >> 16);
				num2 = 97;
				continue;
			case 204:
				num7 = 189 - 68;
				num2 = 124;
				continue;
			case 321:
				num15 = (uint)((array7[num16 + 3] << 24) | (array7[num16 + 2] << 16) | (array7[num16 + 1] << 8) | array7[num16]);
				num = 128;
				if (0 == 0)
				{
					goto IL_1768;
				}
				goto case 50;
			case 50:
				binaryReader.BaseStream.Position = 0L;
				num9 = 44;
				goto IL_1764;
			case 312:
				array4[0] = (byte)num3;
				num2 = 262;
				continue;
			case 413:
				array3[24] = (byte)num7;
				num9 = 283;
				goto IL_1764;
			case 247:
				num3 = 163 - 54;
				num9 = 186;
				goto IL_1764;
			case 278:
				array2[13] = publicKeyToken[6];
				num2 = 177;
				continue;
			case 194:
				array4[15] = 104;
				num = 4;
				goto IL_1768;
			case 41:
				num8 = 106 + 111;
				num = 184;
				goto IL_1768;
			case 331:
				array4[0] = 87;
				num9 = 397;
				goto IL_1764;
			case 306:
				num3 = 251 - 83;
				num = 281;
				if (!ResolveObserver())
				{
					goto IL_1768;
				}
				goto case 57;
			case 56:
				array3[28] = 89;
				num = 152;
				if (0 == 0)
				{
					goto IL_1768;
				}
				goto case 186;
			case 186:
				array4[0] = (byte)num3;
				num9 = 107;
				goto IL_1764;
			case 179:
				array4[9] = (byte)num8;
				num = 182;
				if (0 == 0)
				{
					goto IL_1768;
				}
				goto case 330;
			case 330:
				array4[1] = 24;
				num9 = 327;
				goto IL_1764;
			case 296:
				num20 <<= 8;
				num2 = 302;
				continue;
			case 119:
				array3[9] = (byte)num7;
				num = 192;
				if (CalcObserver())
				{
					goto IL_1768;
				}
				goto case 310;
			case 310:
			{
				CryptoStream cryptoStream = new CryptoStream(memoryStream, transform, CryptoStreamMode.Write);
				cryptoStream.Write(array7, 0, array7.Length);
				cryptoStream.FlushFinalBlock();
				advisorRepository = memoryStream.ToArray();
				memoryStream.Close();
				cryptoStream.Close();
				num = 411;
				goto IL_1768;
			}
			case 365:
				num3 = 200 - 66;
				num2 = 32;
				continue;
			case 248:
				array3[29] = (byte)num7;
				num2 = 197;
				continue;
			case 297:
				array3[11] = (byte)num7;
				num9 = 367;
				goto IL_1764;
			case 6:
				num21 = array7.Length % 4;
				num = 129;
				if (true)
				{
					goto IL_1768;
				}
				goto case 137;
			case 137:
				array4[4] = (byte)num3;
				num = 216;
				goto IL_1768;
			case 389:
				array3[27] = (byte)num7;
				num = 56;
				if (ResolveObserver())
				{
					goto case 71;
				}
				goto IL_1768;
			case 262:
				array4[0] = 131;
				num = 247;
				if (!CalcObserver())
				{
					goto case 353;
				}
				goto IL_1768;
			case 394:
				array3[1] = (byte)num7;
				num = 51;
				if (!CalcObserver())
				{
					goto case 58;
				}
				goto IL_1768;
			case 276:
				array3[4] = 211;
				num2 = 228;
				continue;
			case 89:
				array3[18] = (byte)num7;
				num = 156;
				goto IL_1768;
			case 383:
				num7 = 199 - 66;
				num = 352;
				if (true)
				{
					goto IL_1768;
				}
				goto case 337;
			case 337:
				num4 = BitConverter.ToInt32((byte[])advisorRepository, P_0);
				num9 = 415;
				goto IL_1764;
			case 51:
				array3[1] = 254;
				num = 308;
				if (true)
				{
					goto IL_1768;
				}
				goto case 195;
			case 195:
				array4[10] = 147;
				num2 = 15;
				continue;
			case 348:
				array3[11] = 141;
				num = 403;
				goto IL_1768;
			case 303:
				array4[9] = (byte)num3;
				num2 = 102;
				continue;
			case 198:
				array3[22] = 161;
				num = 160;
				if (CalcObserver())
				{
					goto IL_1768;
				}
				goto case 176;
			case 176:
				array3[16] = (byte)num7;
				num = 269;
				if (!CalcObserver())
				{
					goto case 355;
				}
				goto IL_1768;
			case 237:
				if (publicKeyToken != null)
				{
					num2 = 68;
					continue;
				}
				goto case 131;
			case 357:
				array3[26] = 131;
				num9 = 204;
				goto IL_1764;
			case 370:
				array4[12] = (byte)num3;
				num9 = 404;
				goto IL_1764;
			case 22:
				array4[7] = 103;
				num2 = 125;
				continue;
			case 88:
				array3[0] = 9;
				num2 = 120;
				continue;
			case 42:
				num19 = 0u;
				num9 = 1;
				goto IL_1764;
			case 279:
			case 293:
				if (num18 < array2.Length)
				{
					array[num18] ^= array2[num18];
					num = 253;
					if (CalcObserver())
					{
						goto IL_1768;
					}
					goto case 48;
				}
				num2 = 115;
				continue;
			case 169:
				num7 = 21 + 21;
				num2 = 405;
				continue;
			case 205:
				array4[1] = (byte)num3;
				num2 = 143;
				continue;
			case 59:
				array3[23] = 117;
				num = 391;
				if (!ResolveObserver())
				{
					goto IL_1768;
				}
				goto case 292;
			case 292:
				array4[5] = 126;
				num = 99;
				if (CalcObserver())
				{
					goto IL_1768;
				}
				goto case 148;
			case 53:
				array3[7] = 164;
				num2 = 18;
				continue;
			case 256:
				num16 = (uint)(num17 * 4);
				num = 328;
				if (CalcObserver())
				{
					goto IL_1768;
				}
				goto case 193;
			case 193:
				num12 = 0;
				num2 = 275;
				continue;
			case 272:
				array3[20] = (byte)num7;
				num9 = 258;
				goto IL_1764;
			case 299:
				array3[7] = 134;
				num9 = 146;
				goto IL_1764;
			case 144:
				num10 = num13 * 4;
				num2 = 256;
				continue;
			case 271:
				array3[17] = 175;
				num = 30;
				goto IL_1768;
			case 16:
				array3[18] = (byte)num7;
				num2 = 73;
				continue;
			case 57:
				num3 = 207 - 69;
				num9 = 210;
				goto IL_1764;
			case 210:
				array4[1] = (byte)num3;
				num = 211;
				if (!ResolveObserver())
				{
					goto IL_1768;
				}
				goto case 225;
			case 166:
				num7 = 120 - 1;
				num9 = 401;
				goto IL_1764;
			case 400:
				array4[12] = 157;
				num2 = 379;
				continue;
			case 29:
				array4[4] = (byte)num8;
				num2 = 25;
				continue;
			case 214:
				array4[11] = 205;
				num9 = 168;
				goto IL_1764;
			case 13:
				num16 = (uint)num10;
				num = 321;
				if (true)
				{
					goto IL_1768;
				}
				goto case 92;
			case 92:
				array3[19] = 142;
				num = 232;
				goto IL_1768;
			case 230:
				array2[7] = publicKeyToken[3];
				num = 133;
				if (0 == 0)
				{
					goto IL_1768;
				}
				goto case 305;
			case 305:
				array3[9] = (byte)num7;
				num = 37;
				if (true)
				{
					goto IL_1768;
				}
				goto case 324;
			case 324:
				num7 = 152 - 91;
				num = 153;
				if (CalcObserver())
				{
					goto IL_1768;
				}
				goto case 206;
			case 206:
				array4[4] = 120;
				num9 = 145;
				goto IL_1764;
			case 241:
				num7 = 150 + 69;
				num9 = 267;
				goto IL_1764;
			case 111:
				array3[27] = 127;
				num = 135;
				if (0 == 0)
				{
					goto IL_1768;
				}
				goto case 269;
			case 269:
				array3[16] = 95;
				num9 = 95;
				goto IL_1764;
			case 10:
				num3 = 145 - 48;
				num = 303;
				goto IL_1768;
			case 283:
				array3[24] = 252;
				num = 250;
				goto IL_1768;
			case 219:
				num8 = 210 - 70;
				num9 = 243;
				goto IL_1764;
			case 18:
				num7 = 78 + 117;
				num = 46;
				if (CalcObserver())
				{
					goto IL_1768;
				}
				goto case 245;
			case 266:
				num7 = 208 - 69;
				num = 355;
				goto IL_1768;
			case 250:
				num7 = 103 + 82;
				num = 203;
				goto IL_1768;
			case 236:
				array4 = new byte[16];
				num9 = 223;
				goto IL_1764;
			case 123:
				num15 = 0u;
				num2 = 226;
				continue;
			case 178:
				array3[23] = 220;
				num2 = 385;
				continue;
			case 151:
				array3[29] = 145;
				num9 = 84;
				goto IL_1764;
			case 399:
				array4[8] = 23;
				num2 = 10;
				continue;
			case 225:
				num7 = 71 + 13;
				num = 272;
				if (true)
				{
					goto IL_1768;
				}
				goto case 260;
			case 260:
				array3[6] = (byte)num7;
				num = 213;
				if (!CalcObserver())
				{
					goto case 156;
				}
				goto IL_1768;
			case 408:
				array4[3] = 119;
				num9 = 101;
				goto IL_1764;
			case 294:
				if (num13 != num14 - 1)
				{
					goto IL_2784;
				}
				num = 393;
				if (!ResolveObserver())
				{
					goto IL_1768;
				}
				goto case 179;
			case 33:
				array3[20] = (byte)num7;
				num2 = 225;
				continue;
			case 76:
				array3[31] = 66;
				num2 = 284;
				continue;
			case 121:
				num12++;
				num9 = 40;
				goto IL_1764;
			case 97:
				array6[num10 + 3] = (byte)((num11 & 0xFF000000u) >> 24);
				num2 = 342;
				continue;
			case 118:
				array3[31] = (byte)num7;
				num9 = 336;
				goto IL_1764;
			case 379:
				num3 = 139 + 14;
				num2 = 370;
				continue;
			case 243:
				array4[15] = (byte)num8;
				num = 194;
				if (0 == 0)
				{
					goto IL_1768;
				}
				goto case 360;
			case 360:
				num7 = 135 - 66;
				num9 = 19;
				goto IL_1764;
			case 284:
				array3[31] = 80;
				num = 335;
				if (0 == 0)
				{
					goto IL_1768;
				}
				goto case 216;
			case 216:
				num3 = 142 - 47;
				num = 113;
				if (true)
				{
					goto IL_1768;
				}
				goto case 344;
			case 344:
				array4[9] = 98;
				num = 138;
				if (CalcObserver())
				{
					goto IL_1768;
				}
				goto case 415;
			case 415:
				try
				{
					byte[] array5 = new byte[num4];
					ResolveObserver();
					int num5;
					if (CalcObserver())
					{
						num5 = 2;
					}
					else
					{
						int num6 = 3;
						if (!CalcObserver())
						{
							goto IL_3744;
						}
						num5 = num6;
					}
					switch (num5)
					{
					case 0:
					case 2:
						Array.Copy((Array)advisorRepository, P_0 + 4, array5, 0, num4);
						break;
					}
					goto IL_3744;
					IL_3744:
					return Encoding.Unicode.GetString(array5, 0, array5.Length);
				}
				catch
				{
				}
				return "";
			case 150:
				memoryStream = new MemoryStream();
				num2 = 310;
				continue;
			case 252:
				{
					SymmetricAlgorithm symmetricAlgorithm = WriteClass();
					symmetricAlgorithm.Mode = CipherMode.CBC;
					transform = symmetricAlgorithm.CreateDecryptor(array, array2);
					num2 = 150;
					continue;
				}
				IL_2784:
				num11 = num19 ^ num15;
				num = 359;
				goto IL_1768;
				IL_1764:
				num = num9;
				goto IL_1768;
				IL_120d:
				num19 += num26;
				num = 13;
				if (1 == 0)
				{
					goto case 220;
				}
				goto IL_1768;
			}
			break;
			IL_0026:
			array3[26] = (byte)num7;
			num = 402;
			goto IL_1768;
		}
		goto IL_0016;
		IL_1768:
		num2 = num;
		goto IL_176c;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static string ManageClass(object P_0)
	{
		byte[] array = Convert.FromBase64String((string)P_0);
		return Encoding.Unicode.GetString(array, 0, array.Length);
	}

	[DllImport("kernel32.dll", EntryPoint = "VirtualProtect")]
	private static extern int PushClass(nint P_0, int P_1, int P_2, ref int P_3);

	[MethodImpl(MethodImplOptions.NoInlining)]
	[DatabaseDecoratorConsumer(typeof(DatabaseDecoratorConsumer.StubRepository<object>[]))]
	static void IncludeClass()
	{
		int num = 312;
		byte[] array = default(byte[]);
		int num6 = default(int);
		int num16 = default(int);
		int num15 = default(int);
		byte[] array5 = default(byte[]);
		byte[] array4 = default(byte[]);
		int num34 = default(int);
		int num28 = default(int);
		int num49 = default(int);
		int num25 = default(int);
		uint num19 = default(uint);
		int num17 = default(int);
		int num29 = default(int);
		byte[] publicKeyToken = default(byte[]);
		uint num20 = default(uint);
		nint num3 = default(nint);
		nint num4 = default(nint);
		BinaryReader binaryReader = default(BinaryReader);
		uint num27 = default(uint);
		uint num30 = default(uint);
		uint num26 = default(uint);
		nint hINSTANCE = default(nint);
		int num12 = default(int);
		byte[] array2 = default(byte[]);
		int num21 = default(int);
		uint num22 = default(uint);
		int num35 = default(int);
		int num23 = default(int);
		byte[] array7 = default(byte[]);
		int num32 = default(int);
		int num24 = default(int);
		int num33 = default(int);
		byte[] array6 = default(byte[]);
		int num31 = default(int);
		byte[] array3 = default(byte[]);
		uint num18 = default(uint);
		int num11 = default(int);
		int num14 = default(int);
		nint num10 = default(nint);
		int num9 = default(int);
		while (true)
		{
			int num2;
			int num5;
			nint zero;
			switch (num)
			{
			case 174:
				array[7] = (byte)num6;
				num = 354;
				break;
			case 256:
				array[3] = (byte)num16;
				num2 = 82;
				goto IL_098d;
			case 234:
				array[29] = 131;
				num5 = 252;
				goto IL_0991;
			case 448:
				num15 = 62 + 47;
				num = 185;
				break;
			case 447:
				array5 = array4;
				num5 = 402;
				if (ReflectService())
				{
					goto IL_0991;
				}
				goto case 61;
			case 67:
				array[23] = 188;
				num5 = 284;
				if (!ReflectService())
				{
					goto case 272;
				}
				goto IL_0991;
			case 272:
			case 380:
				if (num34 >= num28)
				{
					num5 = 28;
					goto IL_0991;
				}
				num49 = num34 % num25;
				num = 397;
				break;
			case 438:
				array[9] = (byte)num6;
				num = 212;
				break;
			case 270:
				array4[6] = 153;
				num5 = 231;
				if (ReflectService())
				{
					goto IL_0991;
				}
				goto case 119;
			case 104:
				num15 = 38 + 107;
				num5 = 3;
				goto IL_0991;
			case 118:
			case 423:
				num19 = num19;
				num = 269;
				break;
			case 403:
				array[9] = (byte)num6;
				num = 441;
				break;
			case 315:
				num17 = 78 + 52;
				num2 = 171;
				goto IL_098d;
			case 6:
				array[7] = (byte)num16;
				num = 90;
				break;
			case 351:
				array[6] = (byte)num6;
				num2 = 56;
				goto IL_098d;
			case 407:
				num17 = 104 + 74;
				num5 = 117;
				if (ReflectService())
				{
					goto IL_0991;
				}
				goto case 378;
			case 273:
				array4[15] = (byte)num15;
				num = 104;
				break;
			case 200:
				producerRepository = true;
				num2 = 324;
				goto IL_098d;
			case 168:
				num6 = 178 - 59;
				num5 = 95;
				goto IL_0991;
			case 362:
				array[4] = (byte)num6;
				num5 = 410;
				if (1 == 0)
				{
					goto case 144;
				}
				goto IL_0991;
			case 144:
				array[17] = 113;
				num = 321;
				break;
			case 365:
				num29 = 0;
				num2 = 156;
				goto IL_098d;
			case 147:
				array[15] = 71;
				num2 = 31;
				goto IL_098d;
			case 424:
				array[22] = 239;
				num5 = 305;
				goto IL_0991;
			case 267:
				array[24] = 164;
				num5 = 20;
				goto IL_0991;
			case 408:
				num6 = 93 + 31;
				num2 = 183;
				goto IL_098d;
			case 21:
				num16 = 9 + 41;
				num2 = 255;
				goto IL_098d;
			case 134:
				array4[3] = (byte)num17;
				num = 348;
				break;
			case 165:
				array[13] = 209;
				num2 = 393;
				goto IL_098d;
			case 146:
				array[1] = (byte)num6;
				num5 = 153;
				goto IL_0991;
			case 281:
				array[21] = (byte)num6;
				num5 = 333;
				if (1 == 0)
				{
					goto case 230;
				}
				goto IL_0991;
			case 230:
				array[15] = (byte)num6;
				num2 = 384;
				goto IL_098d;
			case 372:
				if (publicKeyToken != null)
				{
					num2 = 236;
					goto IL_098d;
				}
				goto case 86;
			case 113:
				array[3] = 88;
				num5 = 379;
				if (false)
				{
					goto case 337;
				}
				goto IL_0991;
			case 337:
				num6 = 188 - 62;
				num = 125;
				break;
			case 293:
				array[3] = (byte)num6;
				num = 414;
				break;
			case 185:
				array4[7] = (byte)num15;
				num5 = 7;
				if (!ReflectService())
				{
					goto case 394;
				}
				goto IL_0991;
			case 394:
				array[29] = 150;
				num = 411;
				break;
			case 254:
				num6 = 237 - 79;
				num = 146;
				break;
			case 84:
				array[26] = (byte)num6;
				num = 326;
				break;
			case 257:
				array[9] = 86;
				num5 = 240;
				if (!CustomizeService())
				{
					goto IL_0991;
				}
				goto case 278;
			case 149:
				num20 <<= 8;
				num = 335;
				break;
			case 116:
				array4[7] = (byte)num15;
				num = 75;
				break;
			case 405:
				num6 = 108 + 28;
				num5 = 320;
				if (ReflectService())
				{
					goto IL_0991;
				}
				goto case 338;
			case 136:
				num6 = 238 + 1;
				num2 = 289;
				goto IL_098d;
			case 109:
				num16 = 156 - 52;
				num5 = 12;
				goto IL_0991;
			case 444:
				array[10] = (byte)num16;
				num5 = 261;
				if (!ReflectService())
				{
					goto case 432;
				}
				goto IL_0991;
			case 432:
				array4[3] = 116;
				_ = 1;
				if (!CustomizeService())
				{
					num = 304;
					break;
				}
				num5 = 369;
				goto IL_0991;
			case 266:
				num34 = 0;
				num = 380;
				break;
			case 95:
				array[2] = (byte)num6;
				num2 = 64;
				goto IL_098d;
			case 318:
				array[10] = (byte)num6;
				num = 327;
				break;
			case 172:
				array[8] = (byte)num16;
				num5 = 375;
				goto IL_0991;
			case 42:
				array4[13] = (byte)num17;
				num2 = 331;
				goto IL_098d;
			case 3:
				array4[15] = (byte)num15;
				num2 = 155;
				goto IL_098d;
			case 409:
				array[7] = 149;
				num5 = 385;
				goto IL_0991;
			case 75:
				array4[7] = 124;
				num2 = 145;
				goto IL_098d;
			case 253:
				array[24] = 134;
				num5 = 215;
				if (1 == 0)
				{
					goto case 379;
				}
				goto IL_0991;
			case 379:
				num6 = 129 - 43;
				num5 = 293;
				goto IL_0991;
			case 350:
				array[27] = 95;
				num = 337;
				break;
			case 135:
				RunClass(num3, num4, BitConverter.GetBytes(binaryReader.ReadInt32()), 4u, out zero);
				num = 119;
				break;
			case 34:
				num27 = (uint)(num49 * 4);
				num2 = 132;
				goto IL_098d;
			case 43:
				array4[4] = (byte)num15;
				num5 = 206;
				if (false)
				{
					goto case 26;
				}
				goto IL_0991;
			case 26:
				array[26] = 168;
				num2 = 295;
				goto IL_098d;
			case 58:
				num6 = 161 - 53;
				num2 = 263;
				goto IL_098d;
			case 49:
				num30 <<= 8;
				num2 = 286;
				goto IL_098d;
			case 321:
				array[17] = 41;
				num2 = 307;
				goto IL_098d;
			case 197:
				num16 = 26 + 102;
				num = 169;
				break;
			case 190:
				array4[6] = (byte)num17;
				num = 270;
				break;
			case 228:
				num6 = 158 - 123;
				num = 396;
				break;
			case 354:
				num16 = 223 - 74;
				num2 = 389;
				goto IL_098d;
			case 51:
				array[6] = 159;
				num = 409;
				break;
			case 225:
				array4[0] = 142;
				num5 = 154;
				goto IL_0991;
			case 371:
				num26 = 0u;
				num = 436;
				break;
			case 446:
				array[28] = 240;
				num = 191;
				break;
			case 358:
				array[16] = 157;
				num = 381;
				break;
			case 212:
				array[10] = 47;
				num = 303;
				break;
			case 341:
				array[12] = 19;
				num2 = 165;
				goto IL_098d;
			case 46:
				array4[0] = 248;
				num2 = 370;
				goto IL_098d;
			case 9:
				array[26] = 168;
				num = 26;
				break;
			case 63:
				array[0] = (byte)num16;
				num5 = 415;
				if (false)
				{
					goto case 70;
				}
				goto IL_0991;
			case 70:
				num15 = 162 - 39;
				num5 = 133;
				goto IL_0991;
			case 396:
				array[20] = (byte)num6;
				num2 = 313;
				goto IL_098d;
			case 336:
				array[20] = (byte)num6;
				num5 = 192;
				if (CustomizeService())
				{
					goto case 47;
				}
				goto IL_0991;
			case 47:
				array[8] = (byte)num16;
				num = 227;
				break;
			case 383:
				num6 = 201 + 14;
				goto case 332;
			default:
				num5 = 332;
				if (true)
				{
					goto IL_0991;
				}
				goto case 194;
			case 194:
				array4[11] = (byte)num17;
				num = 102;
				break;
			case 0:
				array4[5] = 102;
				num5 = 44;
				goto IL_0991;
			case 427:
				array[31] = (byte)num16;
				num = 296;
				break;
			case 64:
				array[2] = 105;
				num = 251;
				break;
			case 198:
				num6 = 58 + 64;
				num = 245;
				break;
			case 349:
				array4[15] = (byte)num17;
				num5 = 299;
				if (0 == 0)
				{
					goto IL_0991;
				}
				goto case 417;
			case 417:
				num29++;
				num5 = 226;
				goto IL_0991;
			case 139:
				array5[13] = publicKeyToken[6];
				num2 = 355;
				goto IL_098d;
			case 404:
				array4[4] = 92;
				num5 = 48;
				if (true)
				{
					goto IL_0991;
				}
				goto case 218;
			case 218:
				array4[8] = (byte)num17;
				num2 = 283;
				goto IL_098d;
			case 291:
				num6 = 167 - 55;
				num2 = 433;
				goto IL_098d;
			case 377:
				num19 = 0u;
				num2 = 371;
				goto IL_098d;
			case 215:
				num6 = 246 - 82;
				num2 = 340;
				goto IL_098d;
			case 239:
				array4[14] = (byte)num15;
				num5 = 70;
				if (true)
				{
					goto IL_0991;
				}
				goto case 353;
			case 353:
				array[5] = (byte)num6;
				num2 = 359;
				goto IL_098d;
			case 240:
				array[9] = 142;
				num2 = 292;
				goto IL_098d;
			case 334:
			case 343:
				num34++;
				num5 = 272;
				if (!CustomizeService())
				{
					goto IL_0991;
				}
				goto case 311;
			case 311:
				array[30] = (byte)num6;
				num = 347;
				break;
			case 10:
				array[1] = (byte)num6;
				num2 = 418;
				goto IL_098d;
			case 433:
				array[29] = (byte)num6;
				num2 = 394;
				goto IL_098d;
			case 359:
				array[6] = 159;
				num5 = 247;
				if (true)
				{
					goto IL_0991;
				}
				goto case 72;
			case 72:
				array[11] = 221;
				num2 = 406;
				goto IL_098d;
			case 429:
				num16 = 123 + 19;
				num2 = 178;
				goto IL_098d;
			case 415:
				array[1] = 105;
				num5 = 346;
				if (ReflectService())
				{
					goto IL_0991;
				}
				goto case 180;
			case 180:
			{
				Assembly assembly = Type.GetTypeFromHandle(ProcessRepository.e53w34m968awCm9P85taUZe(33554741)).Assembly;
				num3 = InvokeClass(56u, 1, (uint)Process.GetCurrentProcess().Id);
				hINSTANCE = Marshal.GetHINSTANCE(assembly.GetModules()[0]);
				num2 = 111;
				goto IL_098d;
			}
			case 259:
				array4[8] = (byte)num15;
				num = 440;
				break;
			case 94:
				num6 = 70 + 13;
				num5 = 152;
				if (true)
				{
					goto IL_0991;
				}
				goto case 37;
			case 37:
				num16 = 7 + 13;
				num2 = 172;
				goto IL_098d;
			case 331:
				array4[13] = 180;
				num5 = 60;
				if (true)
				{
					goto IL_0991;
				}
				goto case 287;
			case 287:
				Array.Clear(publicKeyToken, 0, publicKeyToken.Length);
				num5 = 86;
				goto IL_0991;
			case 29:
				num17 = 99 + 105;
				num2 = 194;
				goto IL_098d;
			case 431:
				array4[9] = (byte)num17;
				num5 = 407;
				if (true)
				{
					goto IL_0991;
				}
				goto case 23;
			case 23:
				num16 = 225 - 75;
				num2 = 374;
				goto IL_098d;
			case 78:
				num15 = 60 + 19;
				num2 = 301;
				goto IL_098d;
			case 243:
				num16 = 232 - 77;
				num5 = 47;
				if (true)
				{
					goto IL_0991;
				}
				goto case 119;
			case 119:
			case 425:
				PushClass(num4, 4, num12, ref num12);
				num = 15;
				break;
			case 98:
				num27 = 0u;
				num = 266;
				break;
			case 402:
				Array.Reverse(array5);
				num2 = 308;
				goto IL_098d;
			case 155:
				num17 = 136 - 45;
				num = 349;
				break;
			case 434:
				array2[num21 + 1] = (byte)((num22 & 0xFF00) >> 8);
				num2 = 214;
				goto IL_098d;
			case 61:
				num17 = 148 - 49;
				num = 96;
				break;
			case 173:
				num6 = 133 - 44;
				num2 = 281;
				goto IL_098d;
			case 114:
				array4[6] = 136;
				num5 = 207;
				if (0 == 0)
				{
					goto IL_0991;
				}
				goto case 428;
			case 428:
				num35 = 0;
				num = 157;
				break;
			case 178:
				array[16] = (byte)num16;
				num = 408;
				break;
			case 4:
				array = new byte[32];
				num5 = 223;
				goto IL_0991;
			case 211:
				array[23] = 163;
				num5 = 123;
				goto IL_0991;
			case 406:
				array[11] = 16;
				num2 = 189;
				goto IL_098d;
			case 346:
				array[1] = 96;
				num5 = 254;
				if (ReflectService())
				{
					goto IL_0991;
				}
				goto case 229;
			case 344:
				array5[7] = publicKeyToken[3];
				num5 = 430;
				if (0 == 0)
				{
					goto IL_0991;
				}
				goto case 222;
			case 222:
				num6 = 183 - 61;
				num5 = 52;
				if (0 == 0)
				{
					goto IL_0991;
				}
				goto case 1;
			case 1:
				array[25] = 137;
				num = 268;
				break;
			case 41:
				array2[num21] = (byte)(num22 & 0xFF);
				num5 = 434;
				if (!CustomizeService())
				{
					goto IL_0991;
				}
				goto case 236;
			case 236:
				if (publicKeyToken.Length != 0)
				{
					num2 = 213;
					goto IL_098d;
				}
				goto case 86;
			case 183:
				array[16] = (byte)num6;
				num5 = 358;
				if (0 == 0)
				{
					goto IL_0991;
				}
				goto case 333;
			case 333:
				num16 = 91 - 26;
				num5 = 126;
				goto IL_0991;
			case 5:
				array[28] = 240;
				num = 234;
				break;
			case 133:
				array4[14] = (byte)num15;
				num2 = 110;
				goto IL_098d;
			case 235:
				array[23] = 117;
				num5 = 300;
				goto IL_0991;
			case 385:
				num6 = 221 - 73;
				num5 = 174;
				if (!CustomizeService())
				{
					goto IL_0991;
				}
				goto case 393;
			case 393:
				array[13] = 106;
				num2 = 53;
				goto IL_098d;
			case 264:
				array4[8] = (byte)num17;
				goto case 316;
			case 316:
			case 369:
				num17 = 225 - 75;
				num5 = 431;
				if (true)
				{
					goto IL_0991;
				}
				goto case 414;
			case 414:
				array[3] = 163;
				num5 = 420;
				if (!CustomizeService())
				{
					goto IL_0991;
				}
				goto case 384;
			case 38:
				num15 = 181 - 60;
				num2 = 273;
				goto IL_098d;
			case 152:
				array[0] = (byte)num6;
				num2 = 450;
				goto IL_098d;
			case 368:
				array[29] = (byte)num6;
				num5 = 291;
				if (ReflectService())
				{
					goto IL_0991;
				}
				goto case 220;
			case 220:
				array[23] = 49;
				num5 = 211;
				if (CustomizeService())
				{
					goto case 135;
				}
				goto IL_0991;
			case 329:
				num3 = IntPtr.Zero;
				num5 = 180;
				goto IL_0991;
			case 157:
			case 158:
				if (num35 >= num23)
				{
					num5 = 451;
					goto IL_0991;
				}
				num4 = new IntPtr(_TestsRepository + binaryReader.ReadInt32());
				num = 258;
				break;
			case 160:
				array[18] = 220;
				num5 = 378;
				goto IL_0991;
			case 105:
				num16 = 115 + 30;
				num = 427;
				break;
			case 83:
				array7 = binaryReader.ReadBytes((int)binaryReader.BaseStream.Length);
				num = 4;
				break;
			case 439:
				array4[12] = (byte)num15;
				num5 = 275;
				if (0 == 0)
				{
					goto IL_0991;
				}
				goto case 93;
			case 93:
				array4[12] = 93;
				num2 = 17;
				goto IL_098d;
			case 62:
				array4[2] = 64;
				num5 = 432;
				goto IL_0991;
			case 416:
				array4[12] = 164;
				num5 = 91;
				if (ReflectService())
				{
					goto IL_0991;
				}
				goto case 108;
			case 108:
				array[8] = (byte)num16;
				num2 = 37;
				goto IL_098d;
			case 120:
				array5[3] = publicKeyToken[1];
				num5 = 376;
				goto IL_0991;
			case 247:
				num6 = 20 + 115;
				num5 = 351;
				goto IL_0991;
			case 131:
				num6 = 20 + 37;
				num5 = 403;
				goto IL_0991;
			case 314:
				num15 = 230 - 76;
				num5 = 265;
				if (!CustomizeService())
				{
					goto IL_0991;
				}
				goto case 263;
			case 298:
				array[4] = (byte)num16;
				num2 = 140;
				goto IL_098d;
			case 397:
				num21 = num34 * 4;
				num5 = 34;
				goto IL_0991;
			case 378:
				array[19] = 97;
				num5 = 219;
				goto IL_0991;
			case 261:
				num16 = 80 + 21;
				num = 181;
				break;
			case 392:
				array4[4] = 144;
				num = 435;
				break;
			case 87:
				if (num34 == num28 - 1)
				{
					num5 = 382;
					if (true)
					{
						goto IL_0991;
					}
					goto case 297;
				}
				goto IL_2b39;
			case 297:
				num6 = 16 + 7;
				num5 = 422;
				goto IL_0991;
			case 32:
				array[26] = 56;
				num = 9;
				break;
			case 231:
				array4[6] = 172;
				num = 448;
				break;
			case 280:
				num6 = 151 - 50;
				num = 336;
				break;
			case 219:
				array[19] = 147;
				num5 = 309;
				if (!CustomizeService())
				{
					goto IL_0991;
				}
				goto case 93;
			case 56:
				array[6] = 117;
				num5 = 51;
				goto IL_0991;
			case 101:
				array[27] = 215;
				num5 = 350;
				if (!CustomizeService())
				{
					goto IL_0991;
				}
				goto case 386;
			case 386:
				array[25] = 146;
				num = 297;
				break;
			case 275:
				array4[12] = 112;
				num5 = 416;
				if (!CustomizeService())
				{
					goto IL_0991;
				}
				goto case 140;
			case 443:
				array[22] = 100;
				num5 = 136;
				if (true)
				{
					goto IL_0991;
				}
				goto case 182;
			case 182:
				num17 = 163 + 90;
				num2 = 134;
				goto IL_098d;
			case 186:
				array[30] = 1;
				num5 = 142;
				if (true)
				{
					goto IL_0991;
				}
				goto case 436;
			case 436:
				num20 = 0u;
				num5 = 88;
				if (ReflectService())
				{
					goto IL_0991;
				}
				goto case 221;
			case 204:
				num12 = 0;
				num5 = 193;
				goto IL_0991;
			case 441:
				num6 = 222 - 74;
				num5 = 277;
				if (!CustomizeService())
				{
					goto IL_0991;
				}
				goto case 244;
			case 245:
				array[12] = (byte)num6;
				num5 = 76;
				goto IL_0991;
			case 323:
				num17 = 184 - 61;
				num5 = 42;
				if (!ReflectService())
				{
					goto case 341;
				}
				goto IL_0991;
			case 145:
				array4[7] = 139;
				num = 106;
				break;
			case 357:
				num6 = 9 + 35;
				num5 = 19;
				goto IL_0991;
			case 53:
				array[13] = 112;
				num5 = 196;
				goto IL_0991;
			case 213:
				array5[1] = publicKeyToken[0];
				num5 = 120;
				goto IL_0991;
			case 25:
				num32++;
				num2 = 449;
				goto IL_098d;
			case 88:
				if (num24 > 0)
				{
					num = 195;
					break;
				}
				goto case 98;
			case 399:
				array[14] = 116;
				num2 = 167;
				goto IL_098d;
			case 128:
				num6 = 186 - 62;
				num5 = 367;
				if (!CustomizeService())
				{
					goto IL_0991;
				}
				goto case 121;
			case 121:
				array[25] = 137;
				num5 = 58;
				if (!CustomizeService())
				{
					goto IL_0991;
				}
				goto case 450;
			case 195:
				num28++;
				num5 = 98;
				if (!CustomizeService())
				{
					goto IL_0991;
				}
				goto case 8;
			case 8:
				array[28] = 150;
				num5 = 210;
				goto IL_0991;
			case 303:
				num6 = 43 + 57;
				num5 = 318;
				if (!CustomizeService())
				{
					goto IL_0991;
				}
				goto case 387;
			case 387:
				num6 = 86 - 15;
				num5 = 16;
				if (true)
				{
					goto IL_0991;
				}
				goto case 249;
			case 249:
				num17 = 104 + 45;
				num = 356;
				break;
			case 90:
				array[7] = 149;
				num2 = 288;
				goto IL_098d;
			case 366:
				array4[6] = (byte)num17;
				num = 114;
				break;
			case 269:
			{
				uint num36 = num19;
				uint num37 = num19;
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
				num19 = num36 + (uint)(double)num42;
				num5 = 87;
				goto IL_0991;
			}
			case 167:
				num6 = 109 + 51;
				num5 = 413;
				if (!CustomizeService())
				{
					goto IL_0991;
				}
				goto case 308;
			case 68:
				array[16] = 74;
				num2 = 429;
				goto IL_098d;
			case 162:
				array4[0] = 104;
				num2 = 177;
				goto IL_098d;
			case 418:
				array[2] = 232;
				num5 = 168;
				goto IL_0991;
			case 92:
				array4[1] = (byte)num15;
				num5 = 442;
				if (true)
				{
					goto IL_0991;
				}
				goto case 17;
			case 17:
				num15 = 57 + 123;
				num = 439;
				break;
			case 246:
				array4[9] = 119;
				num5 = 419;
				if (ReflectService())
				{
					goto IL_0991;
				}
				goto case 171;
			case 300:
				array[23] = 110;
				num2 = 220;
				goto IL_098d;
			case 292:
				array[9] = 65;
				num = 127;
				break;
			case 97:
			case 421:
				if (num33 < array5.Length)
				{
					array6[num33] ^= array5[num33];
					num = 124;
					break;
				}
				num5 = 282;
				if (!CustomizeService())
				{
					goto IL_0991;
				}
				goto case 218;
			case 221:
				num16 = 119 + 57;
				num = 241;
				break;
			case 179:
				array4[15] = (byte)num17;
				num5 = 38;
				if (true)
				{
					goto IL_0991;
				}
				goto case 143;
			case 143:
				array4[2] = 219;
				num2 = 61;
				goto IL_098d;
			case 313:
				array[21] = 65;
				num5 = 363;
				if (true)
				{
					goto IL_0991;
				}
				goto case 125;
			case 125:
				array[27] = (byte)num6;
				num5 = 383;
				goto IL_0991;
			case 100:
				num6 = 81 + 57;
				num2 = 353;
				goto IL_098d;
			case 241:
				array[5] = (byte)num16;
				num5 = 202;
				goto IL_0991;
			case 151:
				num17 = 89 - 54;
				num5 = 89;
				goto IL_0991;
			case 309:
				num16 = 203 - 67;
				num = 271;
				break;
			case 419:
				array4[9] = 98;
				num2 = 13;
				goto IL_098d;
			case 161:
				if (num24 <= 0)
				{
					goto IL_0173;
				}
				num5 = 360;
				goto IL_0991;
			case 66:
				array[24] = 183;
				num = 253;
				break;
			case 301:
				array4[14] = (byte)num15;
				num = 345;
				break;
			case 340:
				array[24] = (byte)num6;
				num2 = 267;
				goto IL_098d;
			case 276:
				array[18] = 195;
				num = 197;
				break;
			case 255:
				array[1] = (byte)num16;
				num = 59;
				break;
			case 15:
				num35++;
				num5 = 158;
				if (ReflectService())
				{
					goto IL_0991;
				}
				goto case 181;
			case 141:
				if (num34 != num28 - 1)
				{
					goto IL_0173;
				}
				num5 = 161;
				if (true)
				{
					goto IL_0991;
				}
				goto case 129;
			case 129:
				array[30] = (byte)num6;
				num5 = 199;
				if (true)
				{
					goto IL_0991;
				}
				goto case 286;
			case 286:
				num31 += 8;
				num = 150;
				break;
			case 170:
				array[0] = (byte)num16;
				num2 = 224;
				goto IL_098d;
			case 324:
				binaryReader = new BinaryReader(Type.GetTypeFromHandle(ProcessRepository.e53w34m968awCm9P85taUZe(33554741)).Assembly.GetManifestResourceStream("d6918adf-2c1b-429c-ba87-c0d5d39f857c"));
				num2 = 36;
				goto IL_098d;
			case 250:
				zero = IntPtr.Zero;
				num2 = 204;
				goto IL_098d;
			case 132:
				num26 = (uint)((array6[num27 + 3] << 24) | (array6[num27 + 2] << 16) | (array6[num27 + 1] << 8) | array6[num27]);
				num = 364;
				break;
			case 102:
				array4[11] = 104;
				num = 151;
				break;
			case 364:
				num30 = 255u;
				num2 = 390;
				goto IL_098d;
			case 391:
				array[12] = 85;
				num5 = 57;
				if (!CustomizeService())
				{
					goto IL_0991;
				}
				goto case 285;
			case 11:
				array[4] = 113;
				num5 = 80;
				goto IL_0991;
			case 124:
				num33++;
				num2 = 421;
				goto IL_098d;
			case 375:
				array[8] = 141;
				num2 = 243;
				goto IL_098d;
			case 40:
				array[24] = 123;
				num5 = 395;
				if (!CustomizeService())
				{
					goto IL_0991;
				}
				goto case 71;
			case 71:
				num16 = 106 + 117;
				num5 = 6;
				goto IL_0991;
			case 352:
				array[31] = (byte)num16;
				num = 306;
				break;
			case 81:
				array[11] = 217;
				num2 = 401;
				goto IL_098d;
			case 209:
				array[12] = (byte)num16;
				num5 = 391;
				goto IL_0991;
			case 206:
				array4[4] = 84;
				num = 404;
				break;
			case 412:
				array4[15] = (byte)num17;
				num = 447;
				break;
			case 142:
				num16 = 146 - 48;
				num2 = 27;
				goto IL_098d;
			case 401:
				array[11] = 161;
				num5 = 262;
				if (ReflectService())
				{
					goto IL_0991;
				}
				goto case 216;
			case 216:
				num16 = 143 - 47;
				num5 = 373;
				goto IL_0991;
			case 69:
				array[28] = (byte)num16;
				num2 = 5;
				goto IL_098d;
			case 73:
				array2[num21 + 3] = (byte)((num22 & 0xFF000000u) >> 24);
				num5 = 334;
				if (0 == 0)
				{
					goto IL_0991;
				}
				goto case 242;
			case 242:
				num17 = 239 - 79;
				num5 = 218;
				if (0 == 0)
				{
					goto IL_0991;
				}
				goto case 335;
			case 335:
				num20 |= array3[^(1 + num32)];
				num2 = 25;
				goto IL_098d;
			case 140:
				num6 = 136 + 19;
				num5 = 362;
				goto IL_0991;
			case 166:
				array4[10] = (byte)num15;
				num = 184;
				break;
			case 111:
				_TestsRepository = ((IntPtr)hINSTANCE).ToInt64();
				num2 = 250;
				goto IL_098d;
			case 258:
				PushClass(num4, 4, 4, ref num12);
				num = 14;
				break;
			case 77:
				array[18] = (byte)num16;
				num = 238;
				break;
			case 35:
				num6 = 197 - 111;
				num5 = 438;
				if (ReflectService())
				{
					goto IL_0991;
				}
				goto case 106;
			case 260:
				array4[6] = (byte)num15;
				num5 = 99;
				goto IL_0991;
			case 164:
				array[14] = 225;
				num5 = 399;
				if (CustomizeService())
				{
					goto case 97;
				}
				goto IL_0991;
			case 79:
			case 449:
				if (num32 < num24)
				{
					if (num32 > 0)
					{
						num5 = 149;
						if (1 == 0)
						{
							goto case 438;
						}
						goto IL_0991;
					}
					goto case 335;
				}
				num2 = 423;
				goto IL_098d;
			case 2:
				num32 = 0;
				num5 = 79;
				if (0 == 0)
				{
					goto IL_0991;
				}
				goto case 299;
			case 299:
				num17 = 141 - 106;
				num5 = 412;
				if (!CustomizeService())
				{
					goto IL_0991;
				}
				goto case 366;
			case 374:
				array[15] = (byte)num16;
				num5 = 137;
				goto IL_0991;
			case 284:
				array[23] = 110;
				num = 235;
				break;
			case 238:
				array[18] = 136;
				num = 276;
				break;
			case 302:
				array[20] = (byte)num6;
				num2 = 228;
				goto IL_098d;
			case 54:
				array[17] = 41;
				num5 = 357;
				if (true)
				{
					goto IL_0991;
				}
				goto case 39;
			case 39:
				array[20] = 101;
				num = 280;
				break;
			case 390:
				num31 = 0;
				num2 = 141;
				goto IL_098d;
			case 150:
				array2[num21 + num29] = (byte)((num18 & num30) >> num31);
				num = 417;
				break;
			case 262:
				array[11] = 221;
				num5 = 208;
				goto IL_0991;
			case 294:
				num15 = 57 - 23;
				num = 92;
				break;
			case 278:
			case 304:
				array4[3] = 28;
				num5 = 314;
				goto IL_0991;
			case 326:
				array[26] = 105;
				num5 = 101;
				goto IL_0991;
			case 282:
				array3 = array7;
				num5 = 339;
				if (!CustomizeService())
				{
					goto IL_0991;
				}
				goto case 280;
			case 320:
				array[7] = (byte)num6;
				num5 = 71;
				if (true)
				{
					goto IL_0991;
				}
				goto case 279;
			case 279:
				array[17] = 163;
				num2 = 144;
				goto IL_098d;
			case 48:
				array4[5] = 92;
				num = 317;
				break;
			case 191:
				array[28] = 129;
				num5 = 8;
				goto IL_0991;
			case 16:
				array[15] = (byte)num6;
				num5 = 68;
				if (0 == 0)
				{
					goto IL_0991;
				}
				goto case 360;
			case 360:
				num19 += num26;
				num5 = 163;
				if (0 == 0)
				{
					goto IL_0991;
				}
				goto case 229;
			case 229:
				array5[11] = publicKeyToken[5];
				num = 139;
				break;
			case 327:
				array[10] = 164;
				num2 = 437;
				goto IL_098d;
			case 347:
				array[30] = 1;
				num5 = 50;
				if (!CustomizeService())
				{
					goto IL_0991;
				}
				goto case 76;
			case 76:
				num16 = 48 + 26;
				num5 = 209;
				if (true)
				{
					goto IL_0991;
				}
				goto case 156;
			case 156:
			case 226:
				if (num29 < num24)
				{
					if (num29 <= 0)
					{
						goto case 150;
					}
					num5 = 49;
				}
				else
				{
					num5 = 343;
					if (!ReflectService())
					{
						goto case 282;
					}
				}
				goto IL_0991;
			case 388:
				array[25] = (byte)num16;
				num2 = 386;
				goto IL_098d;
			case 271:
				array[19] = (byte)num16;
				num2 = 74;
				goto IL_098d;
			case 252:
				num6 = 231 - 77;
				num = 368;
				break;
			case 80:
				array[4] = 142;
				num5 = 216;
				if (!CustomizeService())
				{
					goto IL_0991;
				}
				goto case 132;
			case 325:
				num6 = 41 + 49;
				num2 = 129;
				goto IL_098d;
			case 65:
				binaryReader.ReadInt32();
				num = 428;
				break;
			case 115:
				num28 = array3.Length / 4;
				num = 55;
				break;
			case 265:
				array4[3] = (byte)num15;
				num = 182;
				break;
			case 201:
				num16 = 171 - 57;
				num5 = 77;
				if (0 == 0)
				{
					goto IL_0991;
				}
				goto case 248;
			case 248:
				array[12] = (byte)num16;
				num2 = 341;
				goto IL_098d;
			case 199:
				num6 = 14 + 31;
				num5 = 311;
				goto IL_0991;
			case 437:
				num16 = 115 + 45;
				num5 = 444;
				if (!CustomizeService())
				{
					goto IL_0991;
				}
				goto case 284;
			case 426:
				num20 = (uint)((array3[num27 + 3] << 24) | (array3[num27 + 2] << 16) | (array3[num27 + 1] << 8) | array3[num27]);
				num5 = 118;
				if (!CustomizeService())
				{
					goto IL_0991;
				}
				goto case 268;
			case 268:
				array[26] = 105;
				num = 32;
				break;
			case 445:
				array[13] = (byte)num6;
				num5 = 244;
				if (true)
				{
					goto IL_0991;
				}
				goto case 440;
			case 440:
				num15 = 177 - 59;
				num5 = 85;
				if (CustomizeService())
				{
					goto case 84;
				}
				goto IL_0991;
			case 389:
				array[7] = (byte)num16;
				num5 = 405;
				goto IL_0991;
			case 288:
				array[8] = 98;
				num = 159;
				break;
			case 24:
				array[24] = (byte)num6;
				num = 40;
				break;
			case 422:
				array[25] = (byte)num6;
				num5 = 1;
				if (0 == 0)
				{
					goto IL_0991;
				}
				goto case 290;
			case 290:
				array[23] = (byte)num6;
				num5 = 66;
				if (0 == 0)
				{
					goto IL_0991;
				}
				goto case 338;
			case 338:
				num16 = 82 + 91;
				num5 = 108;
				goto IL_0991;
			case 283:
				num17 = 96 - 47;
				num5 = 264;
				goto IL_0991;
			case 22:
				binaryReader.BaseStream.Position = 0L;
				num = 329;
				break;
			case 355:
				array5[15] = publicKeyToken[7];
				num5 = 287;
				if (true)
				{
					goto IL_0991;
				}
				goto case 137;
			case 137:
				num6 = 218 - 72;
				num5 = 230;
				if (CustomizeService())
				{
					goto case 147;
				}
				goto IL_0991;
			case 310:
				array[15] = 121;
				num = 387;
				break;
			case 181:
				array[10] = (byte)num16;
				num2 = 175;
				goto IL_098d;
			case 59:
				num6 = 211 - 106;
				num2 = 10;
				goto IL_098d;
			case 435:
				num15 = 64 + 47;
				num2 = 43;
				goto IL_098d;
			case 177:
				num15 = 204 - 68;
				num5 = 322;
				if (0 == 0)
				{
					goto IL_0991;
				}
				goto case 348;
			case 348:
				array4[4] = 146;
				num5 = 392;
				if (true)
				{
					goto IL_0991;
				}
				goto case 31;
			case 31:
				array[15] = 126;
				num = 23;
				break;
			case 356:
				array4[0] = (byte)num17;
				num5 = 162;
				if (0 == 0)
				{
					goto IL_0991;
				}
				goto case 27;
			case 27:
				array[30] = (byte)num16;
				num5 = 325;
				if (!CustomizeService())
				{
					goto IL_0991;
				}
				goto case 50;
			case 50:
				array[31] = 166;
				num2 = 103;
				goto IL_098d;
			case 175:
				array[10] = 62;
				num = 130;
				break;
			case 169:
				array[18] = (byte)num16;
				num2 = 160;
				goto IL_098d;
			case 33:
				array[10] = (byte)num16;
				num5 = 72;
				goto IL_0991;
			case 153:
				array[1] = 117;
				num2 = 21;
				goto IL_098d;
			case 317:
				array4[5] = 90;
				num = 0;
				break;
			case 112:
				num15 = 28 + 0;
				num2 = 259;
				goto IL_098d;
			case 274:
				num6 = 212 - 70;
				num = 84;
				break;
			case 203:
				num16 = 239 - 79;
				num2 = 388;
				goto IL_098d;
			case 196:
				num6 = 130 - 43;
				num2 = 445;
				goto IL_098d;
			case 36:
				binaryReader.BaseStream.Position = 0L;
				num5 = 83;
				if (0 == 0)
				{
					goto IL_0991;
				}
				goto case 159;
			case 159:
				array[8] = 168;
				num5 = 338;
				goto IL_0991;
			case 384:
				array[15] = 189;
				num5 = 310;
				goto IL_0991;
			case 163:
				num20 = 0u;
				num2 = 2;
				goto IL_098d;
			case 89:
				array4[11] = (byte)num17;
				num2 = 93;
				goto IL_098d;
			case 138:
				num15 = 254 - 84;
				num = 205;
				break;
			case 244:
				num6 = 134 + 75;
				num2 = 232;
				goto IL_098d;
			case 263:
				array[25] = (byte)num6;
				num5 = 203;
				goto IL_0991;
			case 207:
				num15 = 16 + 16;
				num5 = 260;
				if (ReflectService())
				{
					goto IL_0991;
				}
				goto case 198;
			case 82:
				array[4] = 155;
				num5 = 11;
				goto IL_0991;
			case 398:
				array[14] = 225;
				num5 = 147;
				goto IL_0991;
			case 328:
				num15 = 56 + 98;
				num = 166;
				break;
			case 187:
				array4[14] = 44;
				num5 = 78;
				if (!CustomizeService())
				{
					goto IL_0991;
				}
				goto case 77;
			case 345:
				num15 = 252 - 84;
				num2 = 239;
				goto IL_098d;
			case 342:
				num19 += num26;
				num5 = 426;
				if (ReflectService())
				{
					goto IL_0991;
				}
				goto case 123;
			case 123:
				num6 = 68 + 120;
				num2 = 290;
				goto IL_098d;
			case 295:
				array[26] = 92;
				num5 = 274;
				if (0 == 0)
				{
					goto IL_0991;
				}
				goto case 12;
			case 12:
				array[3] = (byte)num16;
				num = 113;
				break;
			case 322:
				array4[0] = (byte)num15;
				num5 = 225;
				goto IL_0991;
			case 361:
				array[22] = (byte)num6;
				num5 = 443;
				if (!ReflectService())
				{
					goto case 230;
				}
				goto IL_0991;
			case 205:
				array4[1] = (byte)num15;
				num5 = 294;
				if (!CustomizeService())
				{
					goto IL_0991;
				}
				goto case 330;
			case 330:
				num25 = array6.Length / 4;
				num5 = 377;
				if (true)
				{
					goto IL_0991;
				}
				goto case 296;
			case 296:
				num16 = 120 + 46;
				num5 = 352;
				goto IL_0991;
			case 192:
				num6 = 107 + 64;
				num2 = 302;
				goto IL_098d;
			case 312:
				if (!producerRepository)
				{
					num5 = 200;
					goto IL_0991;
				}
				return;
			case 18:
				array4 = new byte[16];
				num = 249;
				break;
			case 184:
				array4[10] = 126;
				num2 = 217;
				goto IL_098d;
			case 285:
				array[3] = 147;
				num5 = 109;
				goto IL_0991;
			case 382:
				if (num24 > 0)
				{
					num = 107;
					break;
				}
				goto IL_2b39;
			case 20:
				num6 = 235 - 78;
				num = 24;
				break;
			case 96:
				array4[2] = (byte)num17;
				num2 = 62;
				goto IL_098d;
			case 237:
				num16 = 236 - 78;
				num2 = 170;
				goto IL_098d;
			case 233:
				array[29] = (byte)num6;
				num = 186;
				break;
			case 19:
				array[17] = (byte)num6;
				num5 = 279;
				if (true)
				{
					goto IL_0991;
				}
				goto case 400;
			case 400:
				num16 = 4 + 51;
				num5 = 298;
				if (0 == 0)
				{
					goto IL_0991;
				}
				goto case 208;
			case 208:
				array[12] = 19;
				num = 198;
				break;
			case 381:
				array[16] = 74;
				num5 = 54;
				goto IL_0991;
			case 74:
				array[19] = 97;
				num5 = 122;
				if (true)
				{
					goto IL_0991;
				}
				goto case 395;
			case 395:
				array[24] = 183;
				num5 = 121;
				if (ReflectService())
				{
					goto IL_0991;
				}
				goto case 420;
			case 420:
				num16 = 186 + 30;
				num2 = 256;
				goto IL_098d;
			case 117:
				array4[9] = (byte)num17;
				num5 = 246;
				if (true)
				{
					goto IL_0991;
				}
				goto case 227;
			case 227:
				array[8] = 98;
				num5 = 257;
				goto IL_0991;
			case 176:
				array[3] = 216;
				num5 = 285;
				if (0 == 0)
				{
					goto IL_0991;
				}
				goto case 126;
			case 126:
				array[21] = (byte)num16;
				num2 = 424;
				goto IL_098d;
			case 148:
				array4[15] = (byte)num17;
				num5 = 45;
				if (true)
				{
					goto IL_0991;
				}
				goto case 7;
			case 7:
				num15 = 155 - 51;
				num5 = 116;
				if (ReflectService())
				{
					goto IL_0991;
				}
				goto case 339;
			case 339:
				num24 = array3.Length % 4;
				num = 115;
				break;
			case 85:
				array4[8] = (byte)num15;
				num5 = 242;
				if (0 == 0)
				{
					goto IL_0991;
				}
				goto case 106;
			case 106:
				array4[8] = 112;
				num5 = 112;
				if (0 == 0)
				{
					goto IL_0991;
				}
				goto case 289;
			case 289:
				array[22] = (byte)num6;
				num5 = 67;
				if (0 == 0)
				{
					goto IL_0991;
				}
				goto case 367;
			case 367:
				array[11] = (byte)num6;
				num = 81;
				break;
			case 450:
				array[0] = 124;
				num = 237;
				break;
			case 232:
				array[13] = (byte)num6;
				num = 164;
				break;
			case 13:
				array4[9] = 193;
				num5 = 328;
				if (!CustomizeService())
				{
					goto IL_0991;
				}
				goto case 127;
			case 442:
				array4[2] = 92;
				num5 = 315;
				if (ReflectService())
				{
					goto IL_0991;
				}
				goto case 274;
			case 30:
				num16 = 150 - 50;
				num5 = 69;
				goto IL_0991;
			case 154:
				array4[0] = 156;
				num2 = 46;
				goto IL_098d;
			case 307:
				array[18] = 220;
				num5 = 201;
				goto IL_0991;
			case 57:
				num16 = 249 - 83;
				num5 = 248;
				if (0 == 0)
				{
					goto IL_0991;
				}
				goto case 44;
			case 44:
				num17 = 197 - 65;
				num5 = 366;
				goto IL_0991;
			case 45:
				num17 = 212 - 70;
				num5 = 179;
				if (!CustomizeService())
				{
					goto IL_0991;
				}
				goto case 138;
			case 91:
				array4[13] = 170;
				num = 323;
				break;
			case 370:
				array4[1] = 133;
				num2 = 138;
				goto IL_098d;
			case 130:
				num16 = 168 - 121;
				num5 = 33;
				if (0 == 0)
				{
					goto IL_0991;
				}
				goto case 308;
			case 308:
				publicKeyToken = Type.GetTypeFromHandle(ProcessRepository.e53w34m968awCm9P85taUZe(33554741)).Assembly.GetName().GetPublicKeyToken();
				num2 = 372;
				goto IL_098d;
			case 430:
				array5[9] = publicKeyToken[4];
				num5 = 229;
				goto IL_0991;
			case 99:
				num17 = 215 - 71;
				num5 = 190;
				if (true)
				{
					goto IL_0991;
				}
				goto case 103;
			case 103:
				array[31] = 56;
				num2 = 105;
				goto IL_098d;
			case 193:
				num23 = binaryReader.ReadInt32();
				num5 = 65;
				if (!ReflectService())
				{
					goto case 351;
				}
				goto IL_0991;
			case 319:
				array4[11] = (byte)num15;
				num5 = 29;
				goto IL_0991;
			case 122:
				array[20] = 35;
				num2 = 39;
				goto IL_098d;
			case 223:
				array[0] = 48;
				num = 94;
				break;
			case 363:
				array[21] = 144;
				num2 = 173;
				goto IL_098d;
			case 214:
				array2[num21 + 2] = (byte)((num22 & 0xFF0000) >> 16);
				num5 = 73;
				if (0 == 0)
				{
					goto IL_0991;
				}
				goto case 52;
			case 52:
				array[5] = (byte)num6;
				num5 = 221;
				if (ReflectService())
				{
					goto IL_0991;
				}
				goto case 205;
			case 202:
				array[5] = 96;
				num = 100;
				break;
			case 189:
				array[11] = 96;
				num5 = 128;
				if (0 == 0)
				{
					goto IL_0991;
				}
				goto case 305;
			case 305:
				num6 = 64 + 82;
				num2 = 361;
				goto IL_098d;
			case 373:
				array[4] = (byte)num16;
				num2 = 400;
				goto IL_098d;
			case 251:
				array[2] = 232;
				num5 = 176;
				if (CustomizeService())
				{
					goto case 394;
				}
				goto IL_0991;
			case 86:
				num33 = 0;
				num2 = 97;
				goto IL_098d;
			case 28:
			{
				byte[] buffer = array2;
				Array.Clear(array5, 0, array5.Length);
				binaryReader.Close();
				binaryReader = new BinaryReader(new MemoryStream(buffer));
				num2 = 22;
				goto IL_098d;
			}
			case 127:
				array[9] = 116;
				num5 = 131;
				if (0 == 0)
				{
					goto IL_0991;
				}
				goto case 410;
			case 410:
				array[5] = 138;
				num2 = 222;
				goto IL_098d;
			case 413:
				array[14] = (byte)num6;
				num5 = 398;
				if (ReflectService())
				{
					goto IL_0991;
				}
				goto case 107;
			case 107:
				num18 = num19 ^ num20;
				num = 365;
				break;
			case 210:
				array[28] = 92;
				num5 = 30;
				goto IL_0991;
			case 376:
				array5[5] = publicKeyToken[2];
				num5 = 344;
				if (!CustomizeService())
				{
					goto IL_0991;
				}
				goto case 97;
			case 171:
				array4[2] = (byte)num17;
				num = 143;
				break;
			case 110:
				num17 = 88 + 68;
				num2 = 148;
				goto IL_098d;
			case 60:
				array4[14] = 156;
				num5 = 187;
				goto IL_0991;
			case 224:
				num16 = 101 - 53;
				num = 63;
				break;
			case 277:
				array[9] = (byte)num6;
				num2 = 35;
				goto IL_098d;
			case 188:
				num15 = 38 + 77;
				num5 = 319;
				goto IL_0991;
			case 217:
				array4[10] = 152;
				num2 = 188;
				goto IL_098d;
			case 411:
				num6 = 48 + 83;
				num5 = 233;
				goto IL_0991;
			case 332:
				array[27] = (byte)num6;
				num5 = 446;
				if (ReflectService())
				{
					goto IL_0991;
				}
				goto case 306;
			case 306:
				array6 = array;
				num2 = 18;
				goto IL_098d;
			case 55:
				array2 = new byte[array3.Length];
				num = 330;
				break;
			case 451:
				try
				{
					while (binaryReader.BaseStream.Position < binaryReader.BaseStream.Length - 1)
					{
						CustomizeService();
						int num7;
						if (ReflectService())
						{
							num7 = 5;
							goto IL_3ba0;
						}
						int num8 = 8;
						goto IL_3b9c;
						IL_3ba0:
						while (true)
						{
							int num13;
							switch (num7)
							{
							case 11:
								break;
							case 7:
								num11 = binaryReader.ReadInt32();
								num13 = 10;
								goto IL_3b98;
							case 9:
								num14++;
								num13 = 3;
								goto IL_3b98;
							case 4:
								num14 = 0;
								goto case 3;
							default:
								num13 = 6;
								goto IL_3b98;
							case 10:
								PushClass(num10, num11 * 4, 4, ref num12);
								num7 = 4;
								continue;
							case 3:
							case 6:
								if (num14 < num11)
								{
									Marshal.WriteInt32(new IntPtr(((IntPtr)num10).ToInt64() + num14 * 4), binaryReader.ReadInt32());
									num7 = 9;
									continue;
								}
								num13 = 2;
								goto IL_3b98;
							case 2:
								PushClass(num10, num11 * 4, num12, ref num12);
								num8 = 11;
								goto IL_3b9c;
							case 1:
							case 8:
								num10 = new IntPtr(_TestsRepository + num9);
								num7 = 7;
								continue;
							case 0:
							case 5:
								{
									num9 = binaryReader.ReadInt32();
									goto case 1;
								}
								IL_3b98:
								num8 = num13;
								goto IL_3b9c;
							}
							break;
						}
						continue;
						IL_3b9c:
						num7 = num8;
						goto IL_3ba0;
					}
					RemoveClass(num3);
					return;
				}
				catch
				{
					return;
				}
			case 14:
				{
					if (IntPtr.Size == 4)
					{
						num2 = 135;
						goto IL_098d;
					}
					RunClass(num3, num4, BitConverter.GetBytes(binaryReader.ReadInt32()), 4u, out zero);
					num5 = 425;
					goto IL_0991;
				}
				IL_0173:
				num27 = (uint)num21;
				num5 = 342;
				goto IL_0991;
				IL_0991:
				num = num5;
				break;
				IL_2b39:
				num22 = num19 ^ num20;
				num2 = 41;
				goto IL_098d;
				IL_098d:
				num5 = num2;
				goto IL_0991;
			}
		}
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static object ConcatClass(object P_0)
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
	private static extern int RunClass(nint P_0, nint P_1, [In][Out] byte[] P_2, uint P_3, out nint P_4);

	[DllImport("kernel32.dll", EntryPoint = "ReadProcessMemory")]
	private static extern int DefineClass(nint P_0, nint P_1, [In][Out] byte[] P_2, uint P_3, out nint P_4);

	[DllImport("kernel32.dll", EntryPoint = "OpenProcess")]
	private static extern nint InvokeClass(uint P_0, int P_1, uint P_2);

	[DllImport("kernel32.dll", EntryPoint = "CloseHandle")]
	private static extern int RemoveClass(nint P_0);

	[MethodImpl(MethodImplOptions.NoInlining)]
	private static byte[] SetupClass(object P_0)
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
	private static byte[] ViewClass(object P_0)
	{
		MemoryStream memoryStream = new MemoryStream();
		SymmetricAlgorithm symmetricAlgorithm = WriteClass();
		symmetricAlgorithm.Key = new byte[32]
		{
			93, 201, 148, 13, 219, 93, 175, 238, 126, 50,
			141, 188, 84, 101, 132, 43, 102, 252, 147, 85,
			156, 52, 123, 148, 147, 54, 152, 62, 130, 2,
			99, 58
		};
		symmetricAlgorithm.IV = new byte[16]
		{
			71, 199, 9, 149, 32, 54, 52, 28, 220, 71,
			58, 69, 179, 226, 128, 140
		};
		CryptoStream cryptoStream = new CryptoStream(memoryStream, symmetricAlgorithm.CreateDecryptor(), CryptoStreamMode.Write);
		cryptoStream.Write((byte[])P_0, 0, ((Array)P_0).Length);
		cryptoStream.Close();
		return memoryStream.ToArray();
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private byte[] ResetClass()
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private byte[] CustomizeClass()
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private byte[] CompareClass()
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private byte[] PrintClass()
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private byte[] VerifyClass()
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private byte[] MapClass()
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal byte[] NewClass()
	{
		_ = "{11111-22222-40001-00001}".Length;
		_ = 0;
		return new byte[2] { 1, 2 };
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal byte[] InstantiateClass()
	{
		_ = "{11111-22222-40001-00002}".Length;
		_ = 0;
		return new byte[2] { 1, 2 };
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal byte[] EnableClass()
	{
		_ = "{11111-22222-50001-00001}".Length;
		_ = 0;
		return new byte[2] { 1, 2 };
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal byte[] SelectClass()
	{
		_ = "{11111-22222-50001-00002}".Length;
		_ = 0;
		return new byte[2] { 1, 2 };
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal byte[] FlushClass()
	{
		_ = "{11111-22222-60001-00001}".Length;
		_ = 0;
		return new byte[2] { 1, 2 };
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal byte[] PrepareClass()
	{
		_ = "{11111-22222-60001-00002}".Length;
		_ = 0;
		return new byte[2] { 1, 2 };
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static string StartClass(object P_0, object P_1)
	{
		byte[] bytes = Encoding.Unicode.GetBytes((string)P_0);
		byte[] key = new byte[32]
		{
			82, 102, 104, 110, 32, 77, 24, 34, 118, 181,
			51, 17, 18, 51, 12, 109, 10, 32, 77, 24,
			34, 158, 161, 41, 97, 28, 118, 181, 5, 25,
			1, 88
		};
		byte[] iV = CalculateClass(Encoding.Unicode.GetBytes((string)P_1));
		MemoryStream memoryStream = new MemoryStream();
		SymmetricAlgorithm symmetricAlgorithm = WriteClass();
		symmetricAlgorithm.Key = key;
		symmetricAlgorithm.IV = iV;
		CryptoStream cryptoStream = new CryptoStream(memoryStream, symmetricAlgorithm.CreateEncryptor(), CryptoStreamMode.Write);
		cryptoStream.Write(bytes, 0, bytes.Length);
		cryptoStream.Close();
		return Convert.ToBase64String(memoryStream.ToArray());
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public ThreadIndexerContainer()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool CalcObserver()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool ResolveObserver()
	{
		return false;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool ExcludeObserver()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool IncludeObserver()
	{
		return false;
	}

	internal static bool ReflectService()
	{
		return true;
	}

	internal static bool CustomizeService()
	{
		return false;
	}
}
