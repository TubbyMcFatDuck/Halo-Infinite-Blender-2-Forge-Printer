using Serilog;
using System.Runtime.InteropServices;

namespace ForgeTools;

public class ForgeObjectDataReader
{
    
    //TODO the file Z:\Halo\ForgeObjectData\assault_rifle_longshot.forgeobjectdata string data is offset by 16/15 bytes. might have something to do with the header alignment or off by 1 or an edge case for this object. ids in the header and see if the object is special in any way
    public static ForgeModelData? ReadForgeObjectFile(string filePath,
            string rootGamePath = "Z:/Halo/HaloData/__chore/gen__/")
        //basic prim block id 1759788903  //for prim block -340615357
    {
        //variant ids
        //68684793
        //-64454579
        //-359788102
        //603400642
        //787299103

        if (!File.Exists(filePath))
        {
            Log.Error("Selected File does not exist");
            return null;
        }


        var fileName = Path.GetFileName(filePath);
        //var path = "C:/Users/Derrik/Documents/";


        var bytes = File.ReadAllBytes(filePath);
        var stream = File.Open(filePath, FileMode.Open);
        BinaryReader reader = new BinaryReader(stream);

        var header = FromBinaryReader<UcsHeader>(reader);

        var tagList = new List<UCSTagDependecyList>();
        //tagList.Add(FromBinaryReader<UCSTagDependecyList>(reader));
        for (int i = 0; i < header.tag_dependency_count; i++)
        {
            tagList.Add(FromBinaryReader<UCSTagDependecyList>(reader));
        }


        var Nuggets = new List<UCSNugget>();
        for (int i = 0; i < header.nugget_count; i++)
        {
            Nuggets.Add(FromBinaryReader<UCSNugget>(reader));
        }


        var tag_block_instances = new List<TagBlockData>();

        for (int i = 0; i < header.tag_block_count; i++)
        {
            tag_block_instances.Add(FromBinaryReader<TagBlockData>(reader));
        }

        var tag_data_instances = new List<DataReferenceList>();

        for (int i = 0; i < header.data_reference_count; i++)
        {
            tag_data_instances.Add(FromBinaryReader<DataReferenceList>(reader));
        }

        var tag_reference = new List<TagReferenceList>();
        for (int i = 0; i < header.tag_reference_count; i++)
        {
            tag_reference.Add(FromBinaryReader<TagReferenceList>(reader));
        }

        //reader.ReadBytes(Marshal.SizeOf(typeof(TagReferenceList)) * (int)header.tag_reference_count);
        //byte stringTable = reader.ReadByte();

        //var pos = reader.BaseStream.Position;

        var string_table_position = reader.BaseStream.Position;
        var string_table = new string(reader.ReadChars((int)header.string_table_size));
        string static_model_path;
        List<char> staticObjChars = new List<char>();
        for (int i = 0; i < string_table.Length; i++)
        {
            if (string_table[i] == 0)
            {
                break;
            }


            staticObjChars.Add(string_table[i]);
        }

        static_model_path = new string(staticObjChars.ToArray());

        if (static_model_path == "")
        {
            Log.Error("Item {filePath} does not have a render model returning", filePath);
           // return null;
        }

        string[] parts = static_model_path.Split("\\");
        parts[parts.Length - 1] = "";
        static_model_path = string.Join("/", parts);
        //var staticObjectFilePath = staticObj.Contains(

        long zoneset_start = reader.BaseStream.Position;
        byte[] zoneset_data = reader.ReadBytes((int)header.zoneset_data_size);

        var extraDataSize = Math.Abs((int)header.data_size - (int)reader.BaseStream.Position);


        byte[] extra_data = reader.ReadBytes(extraDataSize);


        byte[] tag_data = reader.ReadBytes((int)bytes.Length - (int)reader.BaseStream.Position);

        byte[] objid = new byte[4];


        Array.Copy(bytes, zoneset_start + header.zoneset_data_size - 8, objid, 0, 4);

        int objectID = BitConverter.ToInt32(objid, 0);


        stream.Close();


        ForgeModelData forgeModelData = new ForgeModelData();
        forgeModelData.filePath = static_model_path;
        forgeModelData.ItemId = objectID;

        //var renderModels = Directory.GetFiles(rootGamePath + static_model_path, "*.render_model");
        //if (renderModels.Length != 1)
        {
            //throw new Exception($"This is {renderModels.Length} render models when 1 is expected");
        }

       // forgeModelData.RenderModelPath = renderModels[0];

        return forgeModelData;
    }


    private static T FromBinaryReader<T>(BinaryReader reader)
    {
        // Read in a byte array
        byte[] bytes = reader.ReadBytes(Marshal.SizeOf(typeof(T)));

        // Pin the managed memory while, copy it out the data, then unpin it
        GCHandle handle = GCHandle.Alloc(bytes, GCHandleType.Pinned);
        T theStructure = (T)Marshal.PtrToStructure(handle.AddrOfPinnedObject(), typeof(T));
        handle.Free();

        return theStructure;
    }

    public class ForgeModelData
    {
        public int ItemId;
        public string filePath;
        public string RenderModelPath;
    }

    [StructLayout(LayoutKind.Sequential)]
    public struct UcsHeader
    {
        //https://github.com/ChimpsAtSea/Blam-Creation-Suite/blob/29dbb93f72063eb31bad9e6583f841fa178352cb/Tags/MandrillLib/CacheInterface/infinite/infinite_ucs_reader.h#L3


        public int magic; // 'hscu' (UCSH = "Universal Cache Storage Header" ? )
        public int version; // 27 (0x1B)
        public ulong unknown8;

        public ulong
            asset_checksum; // Murmur3_x64_128 hash of(what appears to be) the original file that this file was built from.This is not always the same thing as the file stored in the module.

        public readonly uint tag_dependency_count; // Number of tag dependencies
        public uint nugget_count; // Number of data blocks
        public uint tag_block_count; // Number of tag structs
        public uint data_reference_count; // Number of data references
        public uint tag_reference_count; // Number of tag references
        public uint string_table_size; // String table size in bytes
        public uint zoneset_data_size; // Zoneset data size in bytes
        public int unknown19;
        public uint header_size; // Header size in bytes
        public uint data_size; // Tag data size in bytes
        public uint resource_data_size; // Resource data size in bytes
        public int unknown18;

        public byte
            header_alignment; // Power of 2 to align the header buffer to(e.g. 4 = align to a multiple of 16 bytes).

        public byte tag_data_alignment; // Power of 2 to align the tag data buffer to.
        public byte resource_data; // Alignment	Power of 2 to align the resource data buffer to.
        public byte unknown4B;

        public int unknown4C;
        /*
        public int Magic { get; set; }
        public int Version { get; set; }

        public ulong Unknown8 { get; set; }
        public ulong AssetChecksum { get; set; }

        public uint TagDependecyCount { get; set; }
        public uint NuggetCount { get; set; }
        public uint TagBlockCount { get; set; }
        public uint DataReferenceCount { get; set; }
        public uint TagReferenceCount { get; set; }
        public uint StringTableSize { get; set; }
        public uint ZonesetDataSize { get; set; }

        public int unknown19 { get; set; }
        public uint HeaderSize { get; set; }
        public uint DataSize { get; set; }
        public uint ResourceDataSize { get; set; }

        public int Unknown18 { get; set; }

        public byte HeaderAlignment { get; set; }
        public byte TagDataAlignment { get; set; }
        public byte ResourceData { get; set; }
        public byte Unknow4B { get; set; }
        public int Unknown4C { get; set; }
        */
    }

    public struct UCSTagDependecyList
    {
        public int GroupTagB1 { get; set; }
        public int GroupTagB2 { get; set; }
        public int GroupTagB3 { get; set; }
        public int GroupTagB4 { get; set; }

        public uint NameOffset { get; set; }
        public ulong AssetId { get; set; }
        public int GlobalId { get; set; }
        public int Unknown14 { get; set; }
    }

    public struct UCSNugget
    {
        public uint Size { get; set; }
        public short Unknow4 { get; set; }
        public short section { get; set; }

        public ulong _offset { get; set; }
        //public ulong offset { get { return _offset; } set { _offset = value ^ 0x1000000000000; } }
    }

    struct TagBlockData
    {
        public uint IdentifierPart0 { get; set; }
        public uint IdentifierPart1 { get; set; }
        public uint IdentifierPart2 { get; set; }
        public uint IdentifierPart3 { get; set; }

        public short Type { get; set; }
        public short unknown12 { get; set; }
        public int NuggetIndex { get; set; }
        public int OwnerBlockIndex { get; set; }
        public int OwnerBlockOffset { get; set; }
    }

    struct DataReferenceList
    {
        public int ParentTagBlockIndex;
        public int Unknown4;
        public int NuggetIndex;
        public int OwnerBlockIndex;
        public uint OwnerBlockOffset;
    }

    struct TagReferenceList
    {
        public int FieldBlock;
        public uint FieldOffset;
        public uint nameOffset;
        public int DependencyIndex;
    }
    

    // You can define other methods, fields, classes and namespaces here
}




