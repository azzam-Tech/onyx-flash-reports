using System.Collections;
using System.IO;
using System.Reflection;
using System.Runtime.CompilerServices;
using System.Security.Cryptography;
using System.Text;
using System.Threading;
using Onyx.Distribution.Services.Filter;
using Onyx.Distribution.Services.Instances;

namespace System.Writers;

internal class ServerWatcherWriter
{
	private static object reponseWatcher;

	private static bool m_StrategyWatcher;

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static void lLHifFIsCLsZtjvFfN0i()
	{
		_ = 0;
		int num;
		if (AssetAdapter())
		{
			num = 3;
			goto IL_0052;
		}
		int num2 = 1;
		if (0 == 0)
		{
			goto IL_004e;
		}
		goto IL_0084;
		IL_004e:
		num = num2;
		goto IL_0052;
		IL_0084:
		AppDomain.CurrentDomain.AssemblyResolve += DeleteUtils;
		num = 5;
		goto IL_0052;
		IL_0052:
		switch (num)
		{
		case 0:
		case 3:
			if (!m_StrategyWatcher)
			{
				num2 = 4;
				if (CallAdapter())
				{
					goto case 4;
				}
				goto IL_004e;
			}
			return;
		case 4:
			m_StrategyWatcher = true;
			break;
		case 5:
			return;
		}
		goto IL_0084;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private static Assembly DeleteUtils(object P_0, object P_1)
	{
		_ = 1;
		int num;
		if (!CallAdapter())
		{
			num = 2;
			goto IL_002d;
		}
		int num2 = 3;
		goto IL_0031;
		IL_0031:
		bool lockTaken = default(bool);
		Hashtable obj = default(Hashtable);
		switch (num2)
		{
		case 1:
		case 3:
			lockTaken = false;
			goto case 4;
		case 0:
		case 2:
			obj = (Hashtable)reponseWatcher;
			goto case 1;
		case 4:
			try
			{
				Monitor.Enter(obj, ref lockTaken);
				string text = ((ResolveEventArgs)P_1).Name.Trim();
				object obj2 = ((Hashtable)reponseWatcher)[(object)text];
				if (obj2 == null)
				{
					try
					{
						RSACryptoServiceProvider.UseMachineKeyStore = true;
						string text2 = PatchUtils(text);
						byte[] bytes = Encoding.Unicode.GetBytes(text2);
						string text3 = IssuerWatcherWriter.ReadUtils(289194) + Convert.ToBase64String(IssuerWatcherWriter.RegisterUtils(bytes));
						Stream manifestResourceStream = Type.GetTypeFromHandle(QueueDefinitionFilter.e53w34m968awCm9P85taUZe(33554656)).Assembly.GetManifestResourceStream(text3);
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
									string path = Path.Combine(Path.Combine(Path.GetTempPath(), text3), text2 + IssuerWatcherWriter.ReadUtils(289226));
									if (!File.Exists(path))
									{
										Directory.CreateDirectory(Path.GetDirectoryName(path));
										FileStream fileStream = new FileStream(path, FileMode.Create, FileAccess.Write);
										fileStream.Write(array, 0, array.Length);
										fileStream.Close();
									}
									assembly = Assembly.LoadFile(path);
									((Hashtable)reponseWatcher).Add((object)text, (object?)assembly);
								}
								else
								{
									((Hashtable)reponseWatcher).Add((object)text, (object?)assembly);
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
				return (Assembly)obj2;
			}
			finally
			{
				if (lockTaken)
				{
					Monitor.Exit(obj);
				}
			}
		}
		num = 4;
		goto IL_002d;
		IL_002d:
		num2 = num;
		goto IL_0031;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private static string PatchUtils(object P_0)
	{
		int num = 5;
		string text = default(string);
		int num3 = default(int);
		while (true)
		{
			int num2 = num;
			while (true)
			{
				switch (num2)
				{
				case 3:
					text = text.Substring(0, num3);
					num2 = 6;
					continue;
				case 2:
				case 4:
					if (num3 < 0)
					{
						break;
					}
					goto case 3;
				default:
					num = 3;
					if (AssetAdapter())
					{
						goto end_IL_0041;
					}
					goto case 2;
				case 5:
					text = ((string)P_0).Trim();
					_ = 1;
					num2 = (CallAdapter() ? 4 : 0);
					continue;
				case 0:
				case 1:
					num3 = text.IndexOf(',');
					goto case 2;
				case 6:
					break;
				}
				return text;
				continue;
				end_IL_0041:
				break;
			}
		}
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public ServerWatcherWriter()
	{
		InvocationWatcher.SLV0fFIsptsZtjvFft17();
		base._002Ector();
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	static ServerWatcherWriter()
	{
		IssuerWatcherWriter.CustomizeUtils();
		CallAdapter();
		int num;
		if (AssetAdapter())
		{
			num = 4;
			if (CallAdapter())
			{
				goto IL_0028;
			}
		}
		else
		{
			num = 3;
			if (false)
			{
				return;
			}
		}
		goto IL_0040;
		IL_0040:
		while (true)
		{
			switch (num)
			{
			case 1:
			case 3:
				break;
			default:
				num = 2;
				continue;
			case 2:
				goto IL_006f;
			case 0:
			case 4:
				InvocationWatcher.SLV0fFIsptsZtjvFft17();
				break;
			case 5:
				return;
			}
			break;
		}
		goto IL_0028;
		IL_006f:
		m_StrategyWatcher = false;
		num = 5;
		goto IL_0040;
		IL_0028:
		reponseWatcher = new Hashtable();
		goto IL_006f;
	}

	internal static bool AssetAdapter()
	{
		return true;
	}

	internal static bool CallAdapter()
	{
		return false;
	}
}
