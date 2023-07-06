using System.Numerics;
using System.Runtime.CompilerServices;
using System.Xml.Linq;
using System.Xml.XPath;
using InfiniteForgeConstants;
using InfiniteForgeConstants.MapSettings;
using InfiniteForgeConstants.ObjectSettings;
using InfiniteForgePacker.XML;
using Serilog;

namespace ForgeTools;

public class MapLoading
{
    public static Map LoadMap(XDocument xml)
    {
        var map = new Map();

        //Get Map ID
        map.MapId = (MapId)int.Parse(xml.XPathSelectElement("/struct/struct[@id='1']/struct[@id='0']/int32").Value);

        var itemElements = xml.XPathSelectElement("/struct/list");


        foreach (var item in itemElements.Elements())
        {
            var go = new GameObject();


            
            
            //  go.ObjectId =
            //      (ObjectId)int.Parse(item.XPathSelectElement("/struct/list/struct/struct[@id='2']/int32").Value);


            // This is pretty messy. I need to see if all vectors are stored with the same hierarchy
            // if they are then this is very easy to make a method but for now this works
            // Gets forward vector
            // Forward X

            /*var currentElement = item.XPathSelectElement(
                "/struct/list/struct/struct[@id='4']/float[@id='0']");
            float forwardX =
                float.Parse(currentElement == null ? "0" : currentElement.Value);

            // Forward Y
            currentElement = item.XPathSelectElement(
                "/struct/list/struct/struct[@id='4']/float[@id='1']");
            float forwardY =
                float.Parse(currentElement == null ? "0" : currentElement.Value);

            // Forward Z
            currentElement = item.XPathSelectElement(
                "/struct/list/struct/struct[@id='4']/float[@id='2']");
            float forwardZ =
                float.Parse(currentElement == null ? "0" : currentElement.Value);
            // Stores forward for later assignment 
            var forward = new Vector3(forwardX, forwardY, forwardZ);

*/


            /*
            // Gets Up vector
            // Up X
            currentElement = item.XPathSelectElement(
                "/struct/list/struct/struct[@id='4']/float[@id='0']");
            var upX =
                float.Parse(currentElement == null ? "0" : currentElement.Value);

            // Up Y
            currentElement = item.XPathSelectElement(
                "/struct/list/struct/struct[@id='4']/float[@id='1']");
            var upY =
                float.Parse(currentElement == null ? "0" : currentElement.Value);

            // UP Z
            currentElement = item.XPathSelectElement(
                "/struct/list/struct/struct[@id='4']/float[@id='2']");
            var upZ =
                float.Parse(currentElement == null ? "0" : currentElement.Value);

            var up = new Vector3(upX, upY, upZ);

            go.Transform.EulerRotation = Transform.DirectionToEuler(forward, up).Degrees;


*/
            go.ObjectId = (ObjectId)XMLObject.ReadObjectId(item);
            go.Transform.EulerRotation = XMLObject.ReadObjectRotation(item).Degrees;
            go.Transform.Position = XMLObject.ReadObjectPosition(item);
            
            
            


            var isStaticInt = int.Parse(item
                .XPathSelectElement("/struct/list/struct/struct[@id='8']/list[@id='24']/struct/int32[@id='0']").Value);

            go.Transform.IsStatic = isStaticInt switch
            {
                1 => false,
                2 => true,
                _ => go.Transform.IsStatic
            };

            
            Log.Information("Loading Object with id : {ObjectID} ", go.ObjectId);
            map.GameObjects.Add(go);
        }

        return map;
    }
}