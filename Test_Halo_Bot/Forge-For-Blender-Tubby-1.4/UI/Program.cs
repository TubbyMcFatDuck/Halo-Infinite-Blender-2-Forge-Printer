using System.Numerics;
using System.Reflection;
using ForgeTools;
using Newtonsoft.Json;
using Serilog;
using Serilog.Formatting.Compact;

namespace DerriksForgeTools;

using System.Runtime.InteropServices;

static class Program
{
    public static Settings Settings;

    public static readonly string EXEPath =
        Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location);

    public static readonly string SettingsPath =
        Path.GetDirectoryName(EXEPath + "/Settings/");


    /// <summary>
    ///  The main entry point for the application.
    /// </summary>
    [STAThread]
    static void Main()
    {
        AllocConsole();
        Log.Logger = new LoggerConfiguration()
            .Enrich.WithMachineName()
            .Enrich.WithThreadId()
            .Enrich.WithProcessId()
            .Enrich.WithProcessName()
            .MinimumLevel.Verbose()
            .WriteTo.Console()
            .WriteTo.Debug()
            .WriteTo.File(new CompactJsonFormatter(),
                "Logs/log.json",
                rollingInterval: RollingInterval.Day)
            .CreateLogger();


        Log.Information("Loading Settings...");
        var jsonPath = SettingsPath + "Settings.json";
        var file = new FileInfo(jsonPath);
        file.Directory.Create(); // should only create dir if it doesnt exist
        if (File.Exists(jsonPath) == true)
        {
            Settings? deserializeObject = null;
            try
            {
                deserializeObject = JsonConvert.DeserializeObject<Settings>(file.ToString());
            }
            catch (Exception e)
            {
                Console.WriteLine(e);
                Log.Error("Caught exception while trying to parse settings {Exception}", e);
            }

            if (deserializeObject == null)
            {
                Log.Warning("Could not load settings. Creating new settings object and saving");
                Settings = new Settings();
                File.WriteAllText(file.ToString(), JsonConvert.SerializeObject(Settings, Formatting.Indented));
            }
        }
        else
        {
            File.Create(file.ToString()).Dispose();
            Settings = new Settings();
            File.WriteAllText(file.ToString(), JsonConvert.SerializeObject(Settings, Formatting.Indented));
        }

        Log.Information("Starting App...");
        // To customize application configuration such as set high DPI settings or default font,
        // see https://aka.ms/applicationconfiguration.
        ApplicationConfiguration.Initialize();
        Application.Run(new Form1());


        File.WriteAllText(file.FullName, JsonConvert.SerializeObject(Settings));

        var data = ForgeObjectDataReader.ReadForgeObjectFile("Z:/Halo/HaloData/globals/forge/palettes/gameplay.forgepalettedefinition");
    }


    [DllImport("kernel32.dll", SetLastError = true)]
    [return: MarshalAs(UnmanagedType.Bool)]
    static extern bool AllocConsole();
}