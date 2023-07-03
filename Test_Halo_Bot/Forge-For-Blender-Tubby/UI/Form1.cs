using System.Numerics;
using System.Runtime.CompilerServices;
using System.Windows.Forms.VisualStyles;
using System.Xml;
using System.Xml.Linq;
using Bond;
using Bond.IO.Unsafe;
using Bond.Protocols;
using Bond.Tag;
using BondReader;
using BondReader.Schemas;
using BondReader.Schemas.Generic;
using BondReader.Schemas.Items;
using ForgeTools;
using ForgeTools.Core;
using InfiniteForgeConstants;
using InfiniteForgeConstants.MapSettings;
using InfiniteForgeConstants.ObjectSettings;
using InfiniteForgePacker.XML;
using Microsoft.VisualBasic.CompilerServices;
using Newtonsoft.Json;
using Serilog;
using InputBuffer = Bond.IO.Safe.InputBuffer;
using OutputBuffer = Bond.IO.Safe.OutputBuffer;
using Vector3 = System.Numerics.Vector3;

namespace DerriksForgeTools;

public partial class Form1 : Form
{
    private Dictionary<Button, string> fileButtons = new Dictionary<Button, string>();
    private string fullMvarSavePath;
    private string _mvarName;
    private string _exportDir = Program.EXEPath;



    public Form1()
    {

        InitializeComponent();

        textBox_MvarName.Text = "Test";
    }



    private void UpdateExportPath()
    {
        fullMvarSavePath = $"{_exportDir}/{_mvarName}.mvar";

        label_ExportPath.Text = fullMvarSavePath;
    }
    private void OnFileButtonClick(object? sender, EventArgs e)
    {
        var path = fileButtons[(Button)sender];
    }


    private void DisplayMapData(string xmlPath)
    {
        // ADD Displaying of map data here. mostly for testing
        Log.Debug("display map data method {XMLPath}", xmlPath);
    }







    private void Form1_Load(object sender, EventArgs e)
    {

        // DCMap.LoadMap(XDocument.Load(Program.EXEPath + "/DefaultStaticPrimitiveCube Variant 16x16x16.mvar.xml"));


        // var bonded = InfiniteForgePacker.XML.  Bonded<BondSchema>

        // var Bond = BondHelper.ProcessFile<IBonded<BondSchema>>(Program.EXEPath +
        //"/testmap.mvar"); // new BondSchema(MapId.BEHEMOTH);

        //var passThroughTest = BondHelper.ProcessFile<BondSchema>(Program.EXEPath + "/Guardian_Blockedout.mvar");
        // IBonded<MvarSchema> testCast = new Bonded<MvarSchema>(new MvarSchema());

        //BondHelper.WriteBond(testCast,Program.EXEPath + "/OUTPUTTEST.mvar");
        /*
                var reader =
                    new CompactBinaryReader<InputBuffer>(
                        new InputBuffer(File.ReadAllBytes(Program.EXEPath + "/Guardian_Blockedout.mvar")), version: 2);
                IBonded<MvarSchema> ibond = new Bonded<MvarSchema, CompactBinaryReader<InputBuffer>>(reader);




                var xmlstream = new System.IO.MemoryStream();
                var xmlwriter = new SimpleXmlWriter(xmlstream);

                //var t = ibond.Deserialize();
        */
        //ibond.Serialize();
        // StructDef def = new StructDef();
        //  CompactBinaryReader<InputBuffer> read;
        //read.ReadFieldBegin();
        // SchemaDef sd = new SchemaDef();
        //RuntimeSchema rs = new RuntimeSchema(ibond)
        /*
                t.MapIdContainer.Deserialize().MapId.Int = 5555;
                var b = t.MapIdContainer.Deserialize();
                b.MapId.Int = 2222;

                var output = new OutputBuffer();
                var writer = new CompactBinaryWriter<OutputBuffer>(output, 2);

               // Transcode.FromTo(reader,xmlwriter);
                //ibond.Serialize(writer);
                Serialize.To(writer, ibond);
                File.WriteAllBytes(Program.EXEPath + "/OUTPUTTEST.mvar", output.Data.ToArray());
        */

        //var test = BondHelper.ProcessFile<IBonded<BondSchema>>(Program.EXEPath + "/Guardian_Blockedout.mvar");
        //var serializer = new Serializer<CompactBinaryWriter<OutputStream>>(typeof(MvarSchema));
        //var deserializer = new Deserializer(,typeof(MvarSchema));

        // .Deserialize()
        // var bondedField = BondHelper.ProcessFile<IBonded<MvarSchema>>(Program.EXEPath + "/Guardian_Blockedout.mvar");
        // var t2 = deserializer.Deserialize(bondedField);
        // (new CompactBinaryReader<InputBuffer>(
        //    new InputBuffer(File.ReadAllBytes(Program.EXEPath + "/Guardian_Blockedout.mvar")),version:2));
        // bondedField.Deserialize().MapIdContainer.MapId.Int = 321321;
        // bondedField.MapIdContainer.Serialize(writer);

        //Serialize.To(writer, t2);

        //output.Flush();
        //fileStream.Flush();


        // b.MapIdContainer.Deserialize();

        //  var test = Deserialize<IBonded<BondSchema>>.From<InputBuffer>(input);

        // Bonded<MvarSchema> t = new Bonded<MvarSchema>(new MvarSchema());

        //var input = new Bond.IO.Unsafe.InputBuffer(output.Data);
        // var reader = new CompactBinaryReader<InputBuffer>(input, 2);
        // var obj = Deserialize<BondSchema>.From(reader);

        // var schema = Schema.GetRuntimeSchema(typeof(SchemaDef));
        //var runtime = new RuntimeSchema(schema);
        //BondHelper.WriteBond(schema,Program.EXEPath+"/schemaDefTest");

        //var fieldSchema = new RuntimeSchema(schema.StructDef);

        // var map = new MvarSchema();
        // BondSchema m = new BondSchema();

        /*
                var random = new Random();
                for (int i = 0; i < 1200; i++)
                {
                    var randonPos = new Vector3(
                        (-1389 + (random.Next(-25, 25))) / 10f,
                        (709 + (random.Next(-25, 25))) / 10f,
                        (100 + 250 + (random.Next(0, 25))) / 10f
                    );

                    var randomRot = new Vector3(random.Next(-180, 180), random.Next(-180, 180), random.Next(-180, 180));

                    Transform transform = new Transform(randonPos, randomRot);

                    transform.PhysicsType = PhysicsType.NORMAL;
                    var go = new GameObject(transform: transform);

                    go.ObjectSettings ??= new AdditionalObjectSettings(-1847613636);


                    ObjectId[] sphereVariants = new[]
                    {
                        ObjectId.FUSION_COIL_PLASMA, ObjectId.FUSION_COIL_SHOCK, ObjectId.FUSION_COIL_KINETIC
                    }; //{ 329774963, -1868408199, 11784207, -192867617 };
                    var randonVariant = random.Next(0, 3);


                    go.Transform.IsStatic = false;
                    go.ObjectId = ObjectId.FUSION_COIL_PLASMA;
                    go.ObjectId = sphereVariants[randonVariant];


                    ItemSchema itemSchema = new ItemSchema(go);

                    itemSchema.SettingsContainer.Scale.RemoveFirst();
                    // map.Items.AddLast(itemSchema);
                }

                //  map.MapIdContainer.MapId.Int = (int)InfiniteForgeConstants.MapSettings.MapId.BEHEMOTH;
                // BondHelper.WriteBond(map, Program.EXEPath + "/testmapSaved22222222.mvar");
                BondHelper.WriteBond(map, "C:/Halo Infinite Insider/__cms__/rtx-new/variants/Test.mvar");

                */
    }

    private void button2_Click(object sender, EventArgs e)
    {
        OpenFileDialog fileDialog = new OpenFileDialog();
        fileDialog.InitialDirectory = Program.Settings.LastUsedPath;
        fileDialog.Filter = "Blender Export files (*.DCjson)|*.DCjson";

        if (fileDialog.ShowDialog() == DialogResult.OK)
        {
            //BlenderData.ProcessAndSave(fileDialog.FileName, "C:/Halo Infinite Insider/__cms__/rtx-new/variants/");


        }
    }

    private void flowLayoutPanel1_Paint(object sender, PaintEventArgs e)
    {
    }

    private void button_LoadBlenderJson_Click(object sender, EventArgs e)
    {
        OpenFileDialog fileDialog = new OpenFileDialog();
        fileDialog.InitialDirectory = Program.Settings.LastUsedPath;
        fileDialog.Filter = "Blender Export files (*.DCjson)|*.DCjson";
        fileDialog.Title = "Select Exported Blender Map Data";
        if (fileDialog.ShowDialog() == DialogResult.OK)
        {
            BlenderData.ProcessAndSave(fileDialog.FileName, _exportDir, _mvarName);
        }
    }

    private void label1_Click(object sender, EventArgs e)
    {

    }

    private void button1_Click(object sender, EventArgs e) // set save location
    {
        FolderBrowserDialog fileDialog = new FolderBrowserDialog();
        fileDialog.InitialDirectory = Program.Settings.LastUsedPath; //todo pretty sure this is broken


        if (fileDialog.ShowDialog() == DialogResult.OK)
        {
            _exportDir = fileDialog.SelectedPath;
            UpdateExportPath();
        }
    }

    private void textBox_MvarName_TextChanged(object sender, EventArgs e)
    {
        _mvarName = textBox_MvarName.Text;
        UpdateExportPath();
    }

    AboutForm about = new AboutForm();
    private void button2_Click_1(object sender, EventArgs e)
    {
        if (about.IsDisposed)
        {
            about = new AboutForm();
        }
        about.ShowDialog();

    }

    private void button3_Click(object sender, EventArgs e)
    {

    }

    DevForm dev = new DevForm();
    private void button_dev_Click(object sender, EventArgs e)
    {
        if (dev.IsDisposed)
        {
            dev = new DevForm();
        }
        dev.ShowDialog();
    }
}