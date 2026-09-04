using System;
using System.Collections;
using System.IO;
using System.Reflection;
using System.Runtime.CompilerServices;
using System.Security.Cryptography;
using System.Text;
using System.Threading;
using Onyx.Common;
using Onyx.Writers;

namespace Onyx.Containers;

internal class ConfigRepository
{
	private static object _ReaderRepository;

	private static bool _PageRepository;

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static void lLHifFIsCLsZtjvFfN0i()
	{
		StopExpression();
		int num;
		if (ConcatExpression())
		{
			num = 1;
			goto IL_0071;
		}
		int num2 = 3;
		if (1 == 0)
		{
			return;
		}
		goto IL_006d;
		IL_006d:
		num = num2;
		goto IL_0071;
		IL_0071:
		while (true)
		{
			switch (num)
			{
			default:
				goto IL_0021;
			case 0:
			case 1:
				break;
			case 4:
				_PageRepository = true;
				goto IL_0021;
			case 5:
				return;
			}
			break;
			IL_0021:
			AppDomain.CurrentDomain.AssemblyResolve += VisitClass;
			num = 5;
		}
		if (!_PageRepository)
		{
			num2 = 4;
			goto IL_006d;
		}
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private static Assembly VisitClass(object P_0, object P_1)
	{
		_ = 1;
		int num = (StopExpression() ? 2 : 3);
		Hashtable readerRepository = default(Hashtable);
		bool lockTaken = default(bool);
		while (true)
		{
			switch (num)
			{
			case 0:
			case 3:
				readerRepository = (Hashtable)_ReaderRepository;
				goto case 1;
			case 1:
			case 2:
				lockTaken = false;
				break;
			default:
				goto IL_0060;
			case 4:
				break;
			}
			break;
			IL_0060:
			num = 4;
		}
		try
		{
			Monitor.Enter(readerRepository, ref lockTaken);
			string text = ((ResolveEventArgs)P_1).Name.Trim();
			object obj = ((Hashtable)_ReaderRepository)[(object)text];
			if (obj == null)
			{
				try
				{
					RSACryptoServiceProvider.UseMachineKeyStore = true;
					string text2 = TestClass(text);
					byte[] bytes = Encoding.Unicode.GetBytes(text2);
					string text3 = ThreadIndexerContainer.FindClass(269690) + Convert.ToBase64String(ThreadIndexerContainer.CalculateClass(bytes));
					Stream manifestResourceStream = Type.GetTypeFromHandle(ProcessRepository.e53w34m968awCm9P85taUZe(33554747)).Assembly.GetManifestResourceStream(text3);
					if (manifestResourceStream != null)
					{
						try
						{
							BinaryReader binaryReader = new BinaryReader(manifestResourceStream);
							binaryReader.BaseStream.Position = 0L;
							byte[] array = new byte[manifestResourceStream.Length];
							binaryReader.Read(array, 0, array.Length);
							binaryReader.Close();
							bool flag = false;
							Assembly assembly = null;
							try
							{
								assembly = Assembly.Load(array);
							}
							catch (FileLoadException)
							{
								flag = true;
							}
							catch (BadImageFormatException)
							{
								flag = true;
							}
							if (flag)
							{
								string path = Path.Combine(Path.Combine(Path.GetTempPath(), text3), text2 + ThreadIndexerContainer.FindClass(269722));
								if (!File.Exists(path))
								{
									Directory.CreateDirectory(Path.GetDirectoryName(path));
									FileStream fileStream = new FileStream(path, FileMode.Create, FileAccess.Write);
									fileStream.Write(array, 0, array.Length);
									fileStream.Close();
								}
								assembly = Assembly.LoadFile(path);
								((Hashtable)_ReaderRepository).Add((object)text, (object?)assembly);
							}
							else
							{
								((Hashtable)_ReaderRepository).Add((object)text, (object?)assembly);
							}
							return assembly;
						}
						catch
						{
						}
					}
				}
				catch
				{
				}
				return null;
			}
			return (Assembly)obj;
		}
		finally
		{
			if (lockTaken)
			{
				Monitor.Exit(readerRepository);
			}
		}
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private static string TestClass(object P_0)
	{
		_ = 1;
		int num = (StopExpression() ? 2 : 3);
		string text = default(string);
		int num2 = default(int);
		while (true)
		{
			switch (num)
			{
			case 0:
			case 3:
				text = ((string)P_0).Trim();
				goto case 1;
			case 4:
				text = text.Substring(0, num2);
				num = 6;
				continue;
			case 5:
				if (num2 < 0)
				{
					break;
				}
				goto case 4;
			default:
				num = 4;
				continue;
			case 1:
			case 2:
				do
				{
					num2 = text.IndexOf(',');
					num = 5;
				}
				while (!ConcatExpression());
				continue;
			case 6:
				break;
			}
			break;
		}
		return text;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public ConfigRepository()
	{
		ProducerCustomerWriter.SLV0fFIsptsZtjvFft17();
		base._002Ector();
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	static ConfigRepository()
	{
		ThreadIndexerContainer.IncludeClass();
		_ = 0;
		int num;
		if (ConcatExpression())
		{
			num = 3;
			goto IL_0047;
		}
		int num2 = 4;
		if (false)
		{
			return;
		}
		goto IL_0043;
		IL_0043:
		num = num2;
		goto IL_0047;
		IL_0047:
		while (true)
		{
			switch (num)
			{
			case 2:
				goto IL_001b;
			case 1:
			case 4:
				_ReaderRepository = new Hashtable();
				goto IL_001b;
			default:
				num2 = 2;
				if (true)
				{
					break;
				}
				goto case 0;
			case 0:
			case 3:
				ProducerCustomerWriter.SLV0fFIsptsZtjvFft17();
				goto case 1;
			case 5:
				return;
			}
			break;
			IL_001b:
			_PageRepository = false;
			num = 5;
		}
		goto IL_0043;
	}

	internal static bool ConcatExpression()
	{
		return true;
	}

	internal static bool StopExpression()
	{
		return false;
	}
}
