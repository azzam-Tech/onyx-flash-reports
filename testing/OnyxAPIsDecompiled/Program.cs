using System;
using System.Runtime.CompilerServices;
using System.States;
using Microsoft.AspNetCore.Authentication;
using Microsoft.AspNetCore.Authentication.JwtBearer;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Cors.Infrastructure;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Onyx.Distribution.APIs.Filter;
using Onyx.Distribution.Models.DTOs;
using Onyx.Distribution.Models.MainDTOs;
using Onyx.Distribution.Services.DependencyInjection;
using Onyx.IX.Distribution.Track.Models.DTOs;
using OnyxIX.ESS.APIs;
using Swashbuckle.AspNetCore.Swagger;
using Swashbuckle.AspNetCore.SwaggerGen;
using Swashbuckle.AspNetCore.SwaggerUI;

[CompilerGenerated]
internal class Program
{
	[Serializable]
	[CompilerGenerated]
	private sealed class Specification
	{
		public static readonly Specification _003C_003E9;

		public static Action<MvcNewtonsoftJsonOptions> _003C_003E9__0_0;

		public static Action<SwaggerGenOptions> _003C_003E9__0_1;

		public static Action<AuthenticationOptions> _003C_003E9__0_2;

		public static Action<CorsPolicyBuilder> _003C_003E9__0_7;

		public static Action<CorsOptions> _003C_003E9__0_4;

		public static Action<SwaggerOptions> _003C_003E9__0_5;

		public static Action<SwaggerUIOptions> _003C_003E9__0_6;

		[MethodImpl(MethodImplOptions.NoInlining)]
		static Specification()
		{
			Decorator.EnablePage();
			RegRulesStatus.SLV0fFIsptsZtjvFft17();
			_003C_003E9 = new Specification();
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		public Specification()
		{
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal void ResolvePage(MvcNewtonsoftJsonOptions x)
		{
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal void DefinePage(SwaggerGenOptions c)
		{
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal void TestPage(AuthenticationOptions options)
		{
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal void ChangePage(CorsOptions options)
		{
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal void MapPage(CorsPolicyBuilder builder)
		{
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal void PopPage(SwaggerOptions c)
		{
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal void RestartPage(SwaggerUIOptions c)
		{
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool IncludeCandidate()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool DeleteCandidate()
		{
			return true;
		}
	}

	[CompilerGenerated]
	private sealed class ConnectionDispatcherWriter
	{
		public string clientId;

		public string key;

		[MethodImpl(MethodImplOptions.NoInlining)]
		public ConnectionDispatcherWriter()
		{
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal void PreparePage(JwtBearerOptions options)
		{
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool PostCandidate()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool AwakeCandidate()
		{
			return true;
		}

		static ConnectionDispatcherWriter()
		{
			Decorator.EnablePage();
		}
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private static void Main(string[] args)
	{
		int num = 1;
		WebApplicationBuilder webApplicationBuilder = default(WebApplicationBuilder);
		ConfigurationManager configuration = default(ConfigurationManager);
		WebApplication webApplication = default(WebApplication);
		ConnectionDispatcherWriter connectionDispatcherWriter = default(ConnectionDispatcherWriter);
		DependencyInjection dependencyInjection = default(DependencyInjection);
		while (true)
		{
			int num2 = num;
			while (true)
			{
				int num3;
				switch (num2)
				{
				case 3:
					webApplicationBuilder.Services.Configure<ApiConfig>(configuration.GetSection(Decorator.OrderPage(838)));
					num2 = 22;
					continue;
				case 18:
					webApplication.UseStaticFiles();
					num3 = 13;
					goto IL_02fa;
				case 27:
					NewtonsoftJsonMvcBuilderExtensions.AddNewtonsoftJson(webApplicationBuilder.Services.AddControllers(), (Action<MvcNewtonsoftJsonOptions>)([MethodImpl(MethodImplOptions.NoInlining)] (MvcNewtonsoftJsonOptions x) =>
					{
					}));
					num3 = 28;
					goto IL_02fa;
				case 9:
				case 15:
					webApplication.UseCors(Decorator.OrderPage(888));
					num = 11;
					if (true)
					{
						break;
					}
					goto case 19;
				case 19:
					webApplication.Run();
					num3 = 33;
					goto IL_02fa;
				case 14:
					SwaggerGenServiceCollectionExtensions.AddSwaggerGen(webApplicationBuilder.Services, (Action<SwaggerGenOptions>)([MethodImpl(MethodImplOptions.NoInlining)] (SwaggerGenOptions c) =>
					{
					}));
					num3 = 3;
					goto IL_02fa;
				case 0:
					SwaggerBuilderExtensions.UseSwagger((IApplicationBuilder)webApplication, (Action<SwaggerOptions>)([MethodImpl(MethodImplOptions.NoInlining)] (SwaggerOptions c) =>
					{
					}));
					num = 20;
					if (0 == 0)
					{
						break;
					}
					goto case 10;
				case 10:
					webApplicationBuilder.Services.AddCors([MethodImpl(MethodImplOptions.NoInlining)] (CorsOptions options) =>
					{
					});
					num3 = 12;
					goto IL_02fa;
				case 26:
					webApplication.UseAuthentication();
					num2 = 16;
					continue;
				case 1:
					if (Decorator.StopPage(0))
					{
						num = 5;
						if (VerifyCandidate())
						{
							break;
						}
						goto case 3;
					}
					return;
				case 16:
					webApplication.UseAuthorization();
					num3 = 31;
					goto IL_02fa;
				case 22:
					webApplicationBuilder.Services.Configure<TokenSetting>(configuration.GetSection(Decorator.OrderPage(860)));
					num3 = 4;
					goto IL_02fa;
				case 25:
					webApplication.UseDeveloperExceptionPage();
					num3 = 15;
					goto IL_02fa;
				case 13:
					webApplication.UseMiddleware<RequestBodyReaderMiddleware>(Array.Empty<object>());
					num = 0;
					if (0 == 0)
					{
						break;
					}
					goto case 29;
				case 29:
					webApplicationBuilder.Services.AddOptions();
					num3 = 14;
					goto IL_02fa;
				case 20:
					SwaggerUIBuilderExtensions.UseSwaggerUI((IApplicationBuilder)webApplication, (Action<SwaggerUIOptions>)([MethodImpl(MethodImplOptions.NoInlining)] (SwaggerUIOptions c) =>
					{
					}));
					num2 = 26;
					continue;
				case 11:
					webApplication.UseRouting();
					num3 = 18;
					goto IL_02fa;
				case 4:
					JwtBearerExtensions.AddJwtBearer(webApplicationBuilder.Services.AddAuthentication([MethodImpl(MethodImplOptions.NoInlining)] (AuthenticationOptions options) =>
					{
					}), (Action<JwtBearerOptions>)connectionDispatcherWriter.PreparePage);
					num2 = 10;
					continue;
				case 7:
					connectionDispatcherWriter.key = Decorator.OrderPage(136);
					num = 27;
					break;
				case 24:
					dependencyInjection.InjectDependencies(webApplicationBuilder.Services);
					goto case 21;
				default:
					num = 21;
					if (!PopCandidate())
					{
						break;
					}
					goto case 9;
				case 32:
					webApplication.UseStatusCodePages();
					num = 19;
					break;
				case 6:
					configuration = webApplicationBuilder.Configuration;
					num = 30;
					if (0 == 0)
					{
						break;
					}
					goto case 12;
				case 12:
					dependencyInjection = new DependencyInjection(configuration);
					num = 24;
					if (VerifyCandidate())
					{
						break;
					}
					goto case 5;
				case 5:
					connectionDispatcherWriter = new ConnectionDispatcherWriter();
					VerifyCandidate();
					if (!PopCandidate())
					{
						num = 23;
						if (!PopCandidate())
						{
							break;
						}
						goto case 31;
					}
					num3 = 8;
					goto IL_02fa;
				case 31:
					webApplication.MapControllers();
					num2 = 32;
					continue;
				case 21:
					webApplication = webApplicationBuilder.Build();
					goto case 8;
				case 2:
				case 23:
					webApplicationBuilder = WebApplication.CreateBuilder(args);
					num3 = 6;
					goto IL_02fa;
				case 8:
				case 17:
					if (!webApplication.Environment.IsDevelopment())
					{
						webApplication.UseMiddleware<ExceptionHandlingMiddleware>(Array.Empty<object>());
						num3 = 9;
						goto IL_02fa;
					}
					num = 25;
					break;
				case 30:
					connectionDispatcherWriter.clientId = Decorator.OrderPage(108);
					num3 = 7;
					goto IL_02fa;
				case 28:
					webApplicationBuilder.Services.AddEndpointsApiExplorer();
					num = 29;
					break;
				case 33:
					return;
					IL_02fa:
					num = num3;
					break;
				}
				break;
			}
		}
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public Program()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool VerifyCandidate()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool PopCandidate()
	{
		return true;
	}

	static Program()
	{
		Decorator.EnablePage();
	}
}
