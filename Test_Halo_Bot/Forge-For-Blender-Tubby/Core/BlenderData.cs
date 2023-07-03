using System.Numerics;
using BondReader;
using BondReader.Schemas;
using BondReader.Schemas.Generic;
using BondReader.Schemas.Items;
using InfiniteForgeConstants;
using InfiniteForgeConstants.MapSettings;
using InfiniteForgeConstants.ObjectSettings;
using Newtonsoft.Json;
using Serilog;
using Vector3 = System.Numerics.Vector3;

namespace ForgeTools.Core;

public static class BlenderData
{
    public static void ProcessAndSave(string dataPath, string outputPath, string fileName)
    {
        Log.Information("Saving Mvar to {OutputPath}", outputPath);

        var jsonString = File.ReadAllText(dataPath);
        var blenderMap = JsonConvert.DeserializeObject<BlenderMap>(jsonString);

        var mapObject = new Map((MapId)blenderMap.MapId); //todo read map id from blender
        BondSchema map = new BondSchema(mapObject);
        var fileInfo = new FileInfo(dataPath);
        // var map = new Map();


        //var mapShell = XDocument.Load(Program.EXEPath + "/ExampleMap.xml");
        string[] items = File.ReadAllText(fileInfo.FullName).Split("}", StringSplitOptions.RemoveEmptyEntries);
        foreach (var item in blenderMap.ItemList)
        {
            NewFunction(item, mapObject, 0, new Vector3(item.RotationX, item.RotationY, item.RotationZ));
        }

        void NewFunction(BlenderItem blenderItem, Map o, float offset, Vector3 rotation)
        {
            //forward = new Vector3(blenderItem.ForwardX, blenderItem.ForwardY, blenderItem.ForwardZ);
            var up = new Vector3(blenderItem.UpX, blenderItem.UpY, blenderItem.UpZ);
            rotation = Vector3.Normalize(-rotation);
            //var rotation = new Vector3(blenderItem.RotationZ, blenderItem.RotationX, blenderItem.RotationY);
            //rotation = Vector3.Normalize(rotation);
            //rotation *= -1;


            Transform t = new Transform(Vector3.Zero, rotation);
            GameObject go = new GameObject(transform: t);


            go.Transform.Rotation = Quaternion.CreateFromYawPitchRoll(rotation.X, rotation.Y, rotation.Z);
            go.Transform.Position.X = (blenderItem.PositionX);// / 10f;
            go.Transform.Position.Y = (blenderItem.PositionY);// / 10f;
            go.Transform.Position.Z = (blenderItem.PositionZ + offset); /// 10f;

            go.Transform.Scale.X = blenderItem.ScaleX; /// 4f;
            go.Transform.Scale.Y = blenderItem.ScaleY; /// 4f;
            go.Transform.Scale.Z = blenderItem.ScaleZ; // / 4f;
            go.Transform.IsStatic = true;


            go.ObjectId = (ObjectId)blenderItem.ItemId;


            ItemSchema itemSchema = new ItemSchema(go);
            itemSchema.Forward =
                new BondReader.Schemas.Generic.Vector3(blenderItem.ForwardX, blenderItem.ForwardY, blenderItem.ForwardZ);
            itemSchema.Up = new BondReader.Schemas.Generic.Vector3(blenderItem.UpX, blenderItem.UpY, blenderItem.UpZ);

            map.Items.AddLast(itemSchema);
            //  XMLHelper.AddObject(mapShell, mapItem.GameObject);
        }


        BondHelper.WriteBond(map, outputPath + $"/{fileName}.mvar");
        //mapShell.WriteTo(XmlWriter.Create(Program.EXEPath + "/Test.xml"));
    }
}