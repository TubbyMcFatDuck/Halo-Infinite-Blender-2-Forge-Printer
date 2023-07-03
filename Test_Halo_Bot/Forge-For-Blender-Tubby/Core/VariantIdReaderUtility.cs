using System.Windows.Forms;
using System.Windows.Forms.VisualStyles;
using BondReader;
using BondReader.Schemas;
using Serilog;

namespace ForgeTools.Core;

public class VariantIdReaderUtility
{
    public static FileSystemWatcher? watcher;

    public static void StartWatcher(string path)
    {
        watcher?.Dispose();

        Log.Debug("Starting file watcher at {Path}", path);
        watcher = new FileSystemWatcher(@path);

        watcher.NotifyFilter = NotifyFilters.Attributes
                               | NotifyFilters.CreationTime
                               | NotifyFilters.DirectoryName
                               | NotifyFilters.FileName
                               | NotifyFilters.LastAccess
                               | NotifyFilters.LastWrite
                               | NotifyFilters.Security
                               | NotifyFilters.Size;

        watcher.Changed += OnChanged;
        watcher.Created += OnCreated;
        watcher.Deleted += OnDeleted;
        watcher.Renamed += OnRenamed;
        watcher.Error += OnError;
        // watcher.Created += OnCreated;


        watcher.Filter = "*.*";
        watcher.IncludeSubdirectories = true;
        watcher.EnableRaisingEvents = true;
    }

    private static void OnError(object sender, ErrorEventArgs e)
    {
        Log.Debug("Error: {EventArgs}", e);
    }

    private static void OnRenamed(object sender, RenamedEventArgs e)
    {
        Log.Debug("File renamed: {EventArgs}", e);
    }

    private static void OnDeleted(object sender, FileSystemEventArgs e)
    {
        Log.Debug("File deleted: {EventArgs}", e);
    }

    private static void OnCreated(object sender, FileSystemEventArgs e)
    {
        Log.Debug("File created: {EventArgs}", e);
    }

    private static void OnChanged(object sender, FileSystemEventArgs e)
    {
        Thread.Sleep(1000);
        if (File.Exists(e.FullPath))
        {
            var mvar = BondHelper.ProcessFile<BondSchema>(e.FullPath);
            try
            {
                int variantId = mvar.Items.First().SettingsContainer.VariantSettings.First().VaraintIdContainer
                    .ItemVaraintId;

                Log.Debug("Variant Id {VariantId}", variantId);

                Thread thread = new Thread(() => Clipboard.SetText(variantId.ToString()));
                thread.SetApartmentState(ApartmentState.STA); //Set the thread to STA
                thread.Start();
                thread.Join(); //Wait for the thread to end
            }
            catch (Exception exception)
            {
                Log.Error("{exception}", exception);
            }
        }
        else
        {
            Log.Debug("file at {FilePath} does not exist", e.FullPath);
        }
    }
}