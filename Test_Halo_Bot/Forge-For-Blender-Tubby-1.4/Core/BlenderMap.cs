using Newtonsoft.Json;

namespace ForgeTools.Core;

public class BlenderMap
{
    [JsonProperty("mapId")] 
    public int MapId { get; set; }
   [JsonProperty("itemList")] 
    public List<BlenderItem> ItemList { get; set; }
}