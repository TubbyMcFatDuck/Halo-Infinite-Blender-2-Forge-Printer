using ForgeTools;
using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Microsoft.VisualBasic.Logging;
using static ForgeTools.ForgeObjectDataReader;
using Log = Serilog.Log;

namespace DerriksForgeTools
{
    public partial class DevForm : Form
    {
        public DevForm()
        {
            InitializeComponent();
        }

        private void button_gatherItemData_Click(object sender, EventArgs e)
        {
            string folderPath;
            if (Utils.SelectFolderDialog(out folderPath))
            {
                string[] files = System.IO.Directory.GetFiles(folderPath, "*.forgeobjectdata");

                List<ForgeModelData> data = new List<ForgeModelData>();
                foreach (var item in files)
                {
                    var obj = ReadForgeObjectFile(item);

                    if (obj != null)
                    {
                        data.Add(obj);
                        
                    }

                    
                    
                }

                string json = JsonConvert.SerializeObject(data);

                File.WriteAllText(folderPath + "/ItemData.json", json);
            }
        }
    }
}